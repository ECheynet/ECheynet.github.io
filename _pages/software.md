---
layout: page
permalink: /software/
title: Software & Data
description: Open tools and datasets for wind engineering, atmospheric turbulence, and structural dynamics.
nav: true
nav_order: 5
---

I release research software and datasets through GitHub, Zenodo and MATLAB File Exchange. The resources below support wind engineering, atmospheric measurements and structural dynamics.

- [Browse all GitHub repositories](https://github.com/ECheynet?tab=repositories)
- [MATLAB File Exchange profile](https://www.mathworks.com/matlabcentral/fileexchange/?q=profileid%3A4608373)
- [ORCID research record](https://orcid.org/0000-0002-4854-1469)

## Selected repositories

<ul>
  {% for repo in site.data.repositories.selected %}
    <li><a href="https://github.com/{{ repo.path }}">{{ repo.path | split: '/' | last }}</a> — {{ repo.description | escape }}</li>
  {% endfor %}
</ul>

## Open datasets

- [LOLLEX vertical line-of-sight lidar velocities](https://doi.org/10.5281/zenodo.20929085) and [ship-based wind-speed profiles](https://doi.org/10.5281/zenodo.20811676) — data for the offshore wind-farm lidar campaign.
- [Tall wind-profile validation data](https://doi.org/10.5281/zenodo.14848924) — the dataset behind the figures comparing ERA5, NORA3 and NEWA with lidar observations.

## Research software themes

- **Turbulence simulation:** multivariate wind-field generation, non-Gaussian turbulence, and Mann-model implementations.
- **Operational modal analysis:** automated frequency, damping, and mode-shape identification from ambient vibration data.
- **Wind and metocean data:** tools for NORA3, ERA5, lidar observations, and turbulence statistics.
- **Structural response:** frequency- and time-domain models for wind-sensitive structures.
- **Teaching resources:** transparent examples used in courses on offshore wind energy and atmospheric turbulence.
