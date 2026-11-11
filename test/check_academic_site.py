"""Read-only integration checks for this academic site, not al-folio's demo posts."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import json
import re
import sys
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.images = []
        self.ids = set()
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag in ("a", "link") and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag in ("img", "script", "source") and attrs.get("src"):
            self.links.append(attrs["src"])
        if tag == "img":
            self.images.append(attrs.get("src", ""))


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    failures = []
    pages = {}
    html = {}
    for path in root.rglob("*.html"):
        html[path] = path.read_text(encoding="utf-8")
        pages[path] = Page(html[path])
    if not pages:
        raise SystemExit(f"No built HTML found in {root}")

    def require(relative, *markers):
        path = root / relative
        content = html.get(path, "")
        if not content:
            failures.append(f"Missing or empty page: {relative}")
        for marker in markers:
            if marker not in content:
                failures.append(f"{relative}: missing {marker!r}")
        return content

    require("index.html", "Etienne", "Cheynet", "ninja-keys", "light-toggle")
    require("cv/index.html", "al-folio-cv.css", "Contact Information", "Experience",
            "Education", "CV_Cheynet_2026.pdf")
    require("software/index.html", "/repositories/", "/zenodo/", "software-grid", "Cite archived release")
    require("repositories/index.html", "ECheynet", "/api/pin/", "Repository links")
    require("zenodo/index.html", "Software archives", "Publication copies", "Presentations")
    require("projects/index.html", "projects")
    require("publications/index.html", "publication-covers.css", "altmetric-embed",
            "__dimensions_badge_embed__", "scholar.google.com")
    require("supervision/index.html", "completed-msc-supervision", "nva.sikt.no/registration/")
    require("news/index.html", "Mathilde", "Zuhir", "European Academy of Wind Energy")

    # The catalogue is a reviewed local snapshot: builds never depend on Zenodo HTTP calls.
    catalogue = json.loads(Path("_data/zenodo.json").read_text(encoding="utf-8"))
    record_ids = set()
    concepts = set()
    bibliography = "\n".join(p.read_text(encoding="utf-8") for p in Path("_bibliography").glob("*.bib")).lower()
    if not catalogue.get("records"):
        failures.append("Zenodo catalogue is empty")
    for record in catalogue["records"]:
        record_id = record["record_id"]
        if record_id in record_ids:
            failures.append(f"Duplicate Zenodo record: {record_id}")
        record_ids.add(record_id)
        if record["url"] != f"https://zenodo.org/records/{record_id}":
            failures.append(f"Unexpected Zenodo record URL: {record_id}")
        if record["type"] not in ("dataset", "software", "publication", "presentation"):
            failures.append(f"Unknown Zenodo resource type: {record_id}")
        require("zenodo/index.html", f'href="{record["url"]}"', f'https://doi.org/{record["doi"]}')
        if record["type"] in ("dataset", "software"):
            if record.get("concept_doi") in concepts:
                failures.append(f"Multiple versions of the same Zenodo resource: {record_id}")
            concepts.add(record.get("concept_doi"))
            if record["doi"] != f"10.5281/zenodo.{record_id}":
                failures.append(f"Version DOI does not match Zenodo record: {record_id}")
        if record["type"] == "dataset":
            require("software/index.html", f'id="zenodo-{record_id}"', f'https://doi.org/{record["doi"]}')
            if record.get("group") not in catalogue["dataset_groups"] or not record.get("summary"):
                failures.append(f"Dataset is missing a group or description: {record_id}")
        if record["type"] == "publication" and record["doi"].lower() not in bibliography:
            failures.append(f"Zenodo publication is not represented in the bibliography: {record_id}")
        if record["type"] == "publication" and not record["doi"].startswith("10.5281/zenodo."):
            require("publications/index.html", f'href="{record["url"]}"')

    for source in Path("_projects").glob("*.md"):
        require(f"projects/{source.stem}/index.html", "post-title")
        image = re.search(r"^img:\s*(\S+)\s*$", source.read_text(encoding="utf-8"), re.MULTILINE)
        if image:
            image_path = image.group(1)
            require("projects/index.html", image_path)
            if not (root / image_path).is_file():
                failures.append(f"{source}: missing project illustration {image_path}")
    for name in ("cv/index.html", "index.html"):
        if "Albert Einstein" in html.get(root / name, ""):
            failures.append(f"Template identity leaked into {name}")

    # Test local destinations from every rendered page without external HTTP calls.
    for path, page in pages.items():
        relative = path.relative_to(root).as_posix()
        page_url = "/" + relative
        if relative.endswith("index.html"):
            page_url = page_url[:-10]
        for link in page.links:
            target = urlsplit(urljoin("https://echeynet.github.io" + page_url, link))
            if target.scheme not in ("http", "https") or target.netloc != "echeynet.github.io":
                continue
            destination = (root / unquote(target.path).lstrip("/")).resolve()
            if not destination.is_relative_to(root):
                failures.append(f"{relative}: local link escapes build: {link}")
                continue
            if destination.is_dir():
                destination = destination / "index.html"
            if not destination.is_file():
                failures.append(f"{relative}: missing local destination {link}")
                continue
            # Fragment-only links generated by interactive controls are not page anchors.
            if target.fragment and not target.fragment.startswith(("/", "search=")):
                if destination in pages and unquote(target.fragment) not in pages[destination].ids:
                    failures.append(f"{relative}: missing anchor {link}")

    feed = root / "feed.xml"
    if not feed.is_file():
        failures.append("Missing Atom feed")
    else:
        try:
            ns = {"a": "http://www.w3.org/2005/Atom"}
            entries = ET.parse(feed).findall("a:entry", ns)
            if not entries:
                failures.append("Atom feed has no entries")
        except ET.ParseError as error:
            failures.append(f"Invalid Atom XML: {error}")

    for item in ("CONTENT_GAPS.html", "assets/json/resume.json",
                 "assets/rendercv/rendercv_output/Albert_Einstein_CV.pdf"):
        if (root / item).exists():
            failures.append(f"Unwanted demo/internal file is published: {item}")
    if failures:
        raise SystemExit("\n".join(sorted(set(failures))))
    print(f"Academic-site integration checks passed ({len(pages)} HTML pages).")


if __name__ == "__main__":
    main()
