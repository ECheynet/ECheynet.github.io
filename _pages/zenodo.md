---
layout: page
title: Zenodo archives
permalink: /zenodo/
description: Citable datasets, software releases and other research outputs.
nav: false
_styles: |
  .zenodo-catalogue .table-wrap { overflow-x: auto; margin-bottom: 2rem; }
  .zenodo-catalogue table { width: 100%; border-collapse: collapse; }
  .zenodo-catalogue th, .zenodo-catalogue td { padding: 0.75rem; text-align: left; vertical-align: top; border-bottom: 1px solid var(--global-divider-color); overflow-wrap: anywhere; }
  .zenodo-catalogue th:first-child { width: 65%; }
  .zenodo-catalogue .archive-note { margin: 0.35rem 0 0; font-size: 0.85rem; color: var(--global-text-color-light); }
---

[← Software & Data]({% link _pages/software.md %}) · [GitHub repositories]({% link _pages/repositories.md %})

Zenodo preserves citable versions of research outputs that I have authored or co-authored. GitHub links point to the source repositories; a Zenodo DOI identifies an archived release and may differ from the current development version.

{% assign datasets = site.data.zenodo.records | where: "type", "dataset" %}
{% assign software = site.data.zenodo.records | where: "type", "software" | sort: "github" %}
{% assign publications = site.data.zenodo.records | where: "type", "publication" %}
{% assign presentations = site.data.zenodo.records | where: "type", "presentation" %}

This catalogue contains **{{ datasets.size }} datasets**, **{{ software.size }} software archives**, **{{ publications.size }} publications**, and **{{ presentations.size }} presentation deposits**, checked on {{ site.data.zenodo.reviewed_on | date: '%-d %B %Y' }}. It combines the [exact-name search]({{ site.data.zenodo.source_search }}) with verified name variants such as “E. Cheynet”; unrelated creators are excluded.

[Datasets](#datasets) · [Software archives](#software-archives) · [Publication copies](#publication-copies) · [Presentations](#presentations)

<div class="zenodo-catalogue">

<h2 id="datasets">Datasets</h2>

<p>See <a href="{% link _pages/software.md %}#open-datasets">Software & Data</a> for descriptions grouped by research area. These links identify the reviewed versions; each Zenodo record also links to its version history. Files remain hosted by Zenodo, not this website.</p>

<div class="table-wrap">
  <table>
    <caption class="sr-only">Research datasets and their version-specific DOIs</caption>
    <thead><tr><th scope="col">Dataset</th><th scope="col">DOI</th></tr></thead>
    <tbody>
    {% for record in datasets %}
      <tr>
        <td><a href="{{ record.url }}">{{ record.display_title | escape }}</a><p class="archive-note">{{ record.date | date: '%-d %B %Y' }}</p></td>
        <td><a href="https://doi.org/{{ record.doi }}">{{ record.doi }}</a></td>
      </tr>
    {% endfor %}
    </tbody>
  </table>
</div>

<h2 id="software-archives">Software archives</h2>

<p>Each project appears once, using its latest archived release found at the review date. Cite the release actually used for reproducibility. “All versions” links to the project's version-independent DOI. Resource types follow Zenodo's metadata; some software archives also include example datasets.</p>

<div class="table-wrap">
  <table>
    <caption class="sr-only">Software projects, source repositories and archived releases</caption>
    <thead><tr><th scope="col">Software</th><th scope="col">Archived release</th></tr></thead>
    <tbody>
    {% for record in software %}
      <tr id="zenodo-{{ record.record_id }}">
        <td>
          <a href="{{ record.url }}">{{ record.title | escape }}</a>
          <p class="archive-note">{% if record.github %}<a href="https://github.com/{{ record.github }}">{{ record.github }}</a> · {% endif %}{{ record.date | date: '%-d %B %Y' }}</p>
        </td>
        <td>
          <a href="https://doi.org/{{ record.doi }}">{% if record.version %}{{ record.version | escape }}{% else %}Archived release{% endif %}</a>
          <p class="archive-note">{{ record.doi }}</p>
          {% if record.concept_doi %}<a href="https://doi.org/{{ record.concept_doi }}">All versions</a>{% endif %}
        </td>
      </tr>
    {% endfor %}
    </tbody>
  </table>
</div>

<h2 id="publication-copies">Publication copies</h2>

<p>These are archived copies of papers and reports, not additional publications. Their bibliographic entries are listed on the <a href="{% link _pages/publications.md %}">Publications page</a>. A publisher DOI may be shared by the journal version and its deposited copy.</p>

<ul>
  {% for record in publications %}
    <li><a href="{{ record.url }}">{{ record.title | escape }}</a> · Zenodo record date: {{ record.date | date: '%-d %B %Y' }} · <a href="https://doi.org/{{ record.doi }}">Publication DOI</a></li>
  {% endfor %}
</ul>

<h2 id="presentations">Presentations</h2>

<p>Zenodo contains two separate SAMURAI presentation deposits with the same title and date. Both records are linked here without treating them as separate research articles.</p>

<ul>
  {% for record in presentations %}
    <li><a href="{{ record.url }}">{{ record.title | escape }}</a> — {{ record.date | date: '%-d %B %Y' }} · <a href="https://doi.org/{{ record.doi }}">DOI {{ record.doi }}</a></li>
  {% endfor %}
</ul>

</div>
