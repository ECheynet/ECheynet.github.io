---
layout: page
permalink: /software/
title: Software & Data
description: Open tools and datasets for wind engineering, atmospheric turbulence, and structural dynamics.
nav: true
nav_order: 5
_styles: |
  .software-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); gap: 1rem; margin-block: 1.5rem; }
  .software-grid .card { padding: 1.25rem; }
  .software-grid h3, .software-grid h4 { margin-top: 0; font-size: 1.15rem; }
  .software-grid .resource-meta { font-size: 0.85rem; color: var(--global-text-color-light); }
  .software-grid .resource-links { margin-bottom: 0; }
  .software-grid .resource-links a { display: inline-block; margin: 0 0.75rem 0.4rem 0; overflow-wrap: anywhere; }
---

I release research software and datasets through GitHub, Zenodo and MATLAB File Exchange. The resources below support wind engineering, atmospheric measurements and structural dynamics.

- [Browse all GitHub repositories](https://github.com/ECheynet?tab=repositories)
- [Browse the Zenodo archive catalogue]({% link _pages/zenodo.md %})
- [MATLAB File Exchange profile](https://www.mathworks.com/matlabcentral/fileexchange/?q=profileid%3A4608373)
- [ORCID research record](https://orcid.org/0000-0002-4854-1469)

## Selected repositories

<p><a href="{% link _pages/repositories.md %}">Explore GitHub profile and repository statistics →</a></p>

<div class="software-grid">
  {% for repo in site.data.repositories.selected %}
    <section class="card">
      <h3><a href="https://github.com/{{ repo.path }}">{{ repo.path | split: '/' | last }}</a></h3>
      <p>{{ repo.description | escape }}</p>
      <a href="https://github.com/{{ repo.path }}">View repository →</a>
      {% assign archive = site.data.zenodo.records | where: "type", "software" | where: "github", repo.path | first %}
      {% if archive %}
        <p class="resource-links"><a href="https://doi.org/{{ archive.doi }}">Cite archived release{% if archive.version %} ({{ archive.version | escape }}){% endif %}</a></p>
      {% endif %}
    </section>
  {% endfor %}
</div>

## Open datasets

These datasets include individual and collaborative research outputs. The linked Zenodo records provide the full creator lists, files and citation details; check each record for licensing conditions. Please cite the version used in your work.

{% assign datasets = site.data.zenodo.records | where: "type", "dataset" %}
{% for group in site.data.zenodo.dataset_groups %}

  <h3>{{ group | escape }}</h3>
  <div class="software-grid">
    {% assign grouped_datasets = datasets | where: "group", group %}
    {% for dataset in grouped_datasets %}
      <section class="card" id="zenodo-{{ dataset.record_id }}">
        <h4><a href="{{ dataset.url }}">{{ dataset.display_title | escape }}</a></h4>
        <p>{{ dataset.summary | escape }}</p>
        <p class="resource-meta">Published {{ dataset.date | date: '%-d %B %Y' }}{% if dataset.version %} · Version {{ dataset.version | escape }}{% endif %}</p>
        <p class="resource-links">
          <a href="https://doi.org/{{ dataset.doi }}">Dataset DOI</a>
          {% if dataset.concept_doi %}<a href="https://doi.org/{{ dataset.concept_doi }}">All versions</a>{% endif %}
          {% if dataset.github %}<a href="https://github.com/{{ dataset.github }}">Code and examples</a>{% endif %}
          {% for relation in dataset.relations %}
            {% if relation.scheme == "doi" and relation.resource_type contains "publication" %}
              <a href="https://doi.org/{{ relation.identifier }}">Related {% if relation.resource_type contains "preprint" %}preprint{% else %}paper{% endif %}</a>
            {% endif %}
          {% endfor %}
        </p>
      </section>
    {% endfor %}
  </div>
{% endfor %}

Dataset links last checked on {{ site.data.zenodo.reviewed_on | date: '%-d %B %Y' }}. For archived software, publication copies and presentations, see the [full Zenodo catalogue]({% link _pages/zenodo.md %}).

## Research software themes

- **Turbulence simulation:** multivariate wind-field generation, non-Gaussian turbulence, and Mann-model implementations.
- **Operational modal analysis:** automated frequency, damping, and mode-shape identification from ambient vibration data.
- **Wind and metocean data:** tools for NORA3, ERA5, lidar observations, and turbulence statistics.
- **Structural response:** frequency- and time-domain models for wind-sensitive structures.
- **Teaching resources:** transparent examples used in courses on offshore wind energy and atmospheric turbulence.
