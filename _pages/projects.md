---
layout: page
title: Projects
permalink: /projects/
description: Selected national, international, and industry-connected research projects.
nav: true
nav_order: 2
display_categories: [ongoing, completed]
horizontal: true
_styles: |
  .projects .card-img { width: 100%; height: 160px; object-fit: cover; }
---

Grey panels reserve space for future project illustrations.

<div class="projects">
{% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}"><h2 class="category">{{ category | capitalize }}</h2></a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
{% endfor %}
</div>
