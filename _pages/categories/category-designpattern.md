---
title: "디자인 패턴 실험실"
layout: single
permalink: categories/designpattern
author_profile: true
sidebar:                  
    nav: "sidebar-category"
---

{% assign posts = site.categories.designpattern %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

