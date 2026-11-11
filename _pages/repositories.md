---
layout: page
title: Repositories
permalink: /repositories/
description: Open research software on GitHub.
nav: false
_styles: |
  .repositories { display: flex; flex-wrap: wrap; gap: 0.75rem; }
  .repositories .repo { flex: 1 1 340px; max-width: 100%; }
  .repositories img { height: auto; }
---

[← Software & Data]({% link _pages/software.md %})

[Zenodo archives and citation DOIs]({% link _pages/zenodo.md %}) preserve citable snapshots of released software, separately from the current GitHub development versions.

## GitHub profile

<div class="repositories">
  {% include repository/repo_user.liquid username="ECheynet" %}
</div>

## Selected repositories

<div class="repositories">
  {% for repo in site.data.repositories.selected %}
    {% include repository/repo.liquid repository=repo.path %}
  {% endfor %}
</div>

## Repository links

The cards above use an external statistics service. These direct links remain available if that service is temporarily unavailable.

<ul>
  {% for repo in site.data.repositories.selected %}
    <li><a href="https://github.com/{{ repo.path }}">{{ repo.path | split: '/' | last }}</a> — {{ repo.description | escape }}</li>
  {% endfor %}
</ul>
