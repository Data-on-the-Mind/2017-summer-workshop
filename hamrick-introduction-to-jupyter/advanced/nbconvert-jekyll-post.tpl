{# Based on: http://mcwitt.github.io/2015/04/29/jekyll_blogging_with_ipython3/ #}
{%- extends 'markdown.tpl' -%}
{%- block header -%}
---
title: "{{resources['metadata']['title']}}"
layout: post
comments: true
date: {{resources['metadata']['date']}}
permalink: {{resources['metadata']['permalink']}}
{%- if resources['metadata']['categories'] %}
categories:
{%- for category in resources['metadata']['categories'] %}
  - {{category}}
{%- endfor -%}
{%- endif -%}
{%- if resources['metadata']['tags'] %}
tags:
{%- for tag in resources['metadata']['tags'] %}
  - {{tag}}
{%- endfor -%}
{%- endif %}
---
{% endblock header %}

{% block any_cell scoped %}
{{ super () }}
{% endblock any_cell %}

{%- block input -%}
{{ '{% highlight python %}' }}
{{ cell.source }}
{{ '{% endhighlight %}' }}
{%- endblock input -%}