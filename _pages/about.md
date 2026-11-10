---
layout: about
title: About
permalink: /
subtitle: Associate Professor · Geophysical Institute · University of Bergen

profile:
  align: right
  image: profile.png
  image_circular: false
  more_info: >
    <p><a href="https://www4.uib.no/en/find-employees/etienne.cheynet">University of Bergen</a></p>
    <p><a href="https://www4.uib.no/en/forskning/forskningssentre/bergen-offshore-wind-centre-bow">Bergen Offshore Wind Centre</a></p>
    <p>Allégaten 55, Bergen, Norway</p>

social: true

announcements:
  limit: 3

latest_posts:
  enabled: false

_styles: |
  .lead-copy {
    font-size: 1.08rem;
    line-height: 1.75;
  }
  .metric-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(135px, 1fr));
    gap: 0.8rem;
    margin: 1.75rem 0 2rem;
  }
  .metric-card {
    border: 1px solid var(--global-divider-color);
    border-radius: 0.6rem;
    padding: 1rem;
    text-align: center;
  }
  .metric-card strong {
    color: var(--global-theme-color);
    display: block;
    font-size: 1.15rem;
    line-height: 1.25;
    margin-bottom: 0.25rem;
  }
  .focus-list li {
    margin-bottom: 0.6rem;
  }
---

<div class="lead-copy" markdown="1">
I study **atmospheric turbulence, wind engineering, and experimental meteorology**, with applications in offshore wind energy, bridge aerodynamics, and atmospheric measurement techniques. My work combines field observations, remote sensing, numerical methods, and structural dynamics to connect atmospheric science with engineering practice.
</div>

I lead and contribute to interdisciplinary research at the [Geophysical Institute](https://www.uib.no/en/gfi) and the [Bergen Offshore Wind Centre](https://www4.uib.no/en/forskning/forskningssentre/bergen-offshore-wind-centre-bow). I place particular emphasis on reproducible research, open data, reusable software, and the practical value of scientific results.

<div class="metric-grid" aria-label="Academic profile at a glance">
  <div class="metric-card"><strong><a href="{{ '/publications/' | relative_url }}">Publications</a></strong>Papers, proceedings and reports</div>
  <div class="metric-card"><strong><a href="{{ '/projects/' | relative_url }}">Projects</a></strong>Current and completed research</div>
  <div class="metric-card"><strong><a href="{{ '/supervision/' | relative_url }}">Supervision</a></strong>PhD and MSc research</div>
  <div class="metric-card"><strong><a href="{{ '/software/' | relative_url }}">Software and data</a></strong>Open research resources</div>
</div>

## Research focus

<ul class="focus-list">
  <li><strong>Atmospheric turbulence:</strong> structure, coherence, spectra, and non-neutral boundary layers.</li>
  <li><strong>Wind energy:</strong> offshore wind resources, metocean conditions, wakes, and turbine loading.</li>
  <li><strong>Measurement science:</strong> scanning Doppler lidar, sonic anemometry, and drone-based sensing.</li>
  <li><strong>Structural dynamics:</strong> full-scale monitoring, system identification, and bridge aerodynamics.</li>
</ul>

[Explore the research themes →]({% link _pages/research.md %})

## News

{% include news.liquid limit=true %}

[All research updates]({% link _pages/news.md %})

## Selected publications

{% include selected_papers.liquid %}

[Browse all publications]({% link _pages/publications.md %})
