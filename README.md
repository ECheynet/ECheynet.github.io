# Academic website of Etienne Cheynet

This repository contains the source for [echeynet.github.io](https://echeynet.github.io/).

The site presents research themes, projects, PhD and MSc supervision, publications, teaching, open software, datasets, and a downloadable CV. It is built with the [al-folio](https://github.com/alshedivat/al-folio) Jekyll starter and deployed through GitHub Pages.

## Updating the site

- Edit the Markdown files in `_pages/` for main page content.
- Add or update project files in `_projects/`.
- Add dated research updates in `_news/`; they appear on the home page, the news archive and its Atom feed.
- Update the BibTeX files in `_bibliography/` to maintain the publication list.
- Set each entry's `preview` to a matching image filename in `assets/img/publication_preview/`, or to `placeholder.svg` when a cover is not available. Reuse one thumbnail for papers from the same venue.
- Publication thumbnails are representative venue artwork. Most were supplied by the site owner; the [Solar Energy](https://ars.els-cdn.com/content/image/S0038092X.jpg), [Renewable Energy](https://ars.els-cdn.com/content/image/X09601481.jpg), [Marine Policy](https://ars.els-cdn.com/content/image/S0308597X.jpg) and [IMAC 2017](https://link.springer.com/book/10.1007/978-3-319-54777-0) covers came from their publishers.
- Keep the HTML summary in `_pages/cv.md` and the accompanying LaTeX-generated PDF in sync. If the PDF filename changes, update the links in `_pages/cv.md`.
- Edit `_data/repositories.yml` to update the selected software links. The list is rendered locally so it does not depend on a badge service.
- The source for the site's social preview is `docs/social-preview.svg`. Regenerate the PNG with `inkscape docs/social-preview.svg --export-filename=assets/img/social-preview.png` after editing it.

Changes pushed to `main` are built and published automatically by the deployment workflow.

Use British English for original website copy and sentence case with an initial capital for page and section headings. Preserve the published spelling of publication titles.

See [CONTENT_GAPS.md](CONTENT_GAPS.md) for the prioritised content backlog.
