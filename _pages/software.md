---
layout: page
permalink: /software/
title: software & data
description: Open tools and datasets for wind engineering, atmospheric turbulence, and structural dynamics.
nav: true
nav_order: 5
---

Open and reproducible research is central to my work. I have released more than 55 datasets, software packages, and related research outputs through GitHub and Zenodo, alongside 60 MATLAB File Exchange contributions with more than 53,600 downloads.

- [Browse all GitHub repositories](https://github.com/ECheynet?tab=repositories)
- [MATLAB File Exchange profile](https://se.mathworks.com/matlabcentral/fileexchange/?q=profileid%3A4608373)
- [ORCID research record](https://orcid.org/0000-0002-4854-1469)

## selected repositories

{% if site.data.repositories.github_repos %}

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.liquid repository=repo %}
  {% endfor %}
</div>
{% endif %}

## research software themes

- **Turbulence simulation:** multivariate wind-field generation, non-Gaussian turbulence, and Mann-model implementations.
- **Operational modal analysis:** automated frequency, damping, and mode-shape identification from ambient vibration data.
- **Wind and metocean data:** tools for NORA3, ERA5, lidar observations, and turbulence statistics.
- **Structural response:** frequency- and time-domain models for wind-sensitive structures.
- **Teaching resources:** transparent examples used in courses on offshore wind energy and atmospheric turbulence.
