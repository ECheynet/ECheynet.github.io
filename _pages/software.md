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
  .software-grid h3 { margin-top: 0; font-size: 1.15rem; }
---

I release research software and datasets through GitHub, Zenodo and MATLAB File Exchange. The resources below support wind engineering, atmospheric measurements and structural dynamics.

- [Browse all GitHub repositories](https://github.com/ECheynet?tab=repositories)
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
    </section>
  {% endfor %}
</div>

## Open datasets

- [LOLLEX vertical line-of-sight lidar velocities](https://doi.org/10.5281/zenodo.20929085) and [ship-based wind-speed profiles](https://doi.org/10.5281/zenodo.20811676) — data for the offshore wind-farm lidar campaign.
- [Tall wind-profile validation data](https://doi.org/10.5281/zenodo.14848924) — the dataset behind the figures comparing ERA5, NORA3 and NEWA with lidar observations.

## Research software themes

- **Turbulence simulation:** multivariate wind-field generation, non-Gaussian turbulence, and Mann-model implementations.
- **Operational modal analysis:** automated frequency, damping, and mode-shape identification from ambient vibration data.
- **Wind and metocean data:** tools for NORA3, ERA5, lidar observations, and turbulence statistics.
- **Structural response:** frequency- and time-domain models for wind-sensitive structures.
- **Teaching resources:** transparent examples used in courses on offshore wind energy and atmospheric turbulence.
