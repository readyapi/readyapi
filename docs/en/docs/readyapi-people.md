---
hide:
  - navigation
---

# ReadyAPI People

ReadyAPI has an amazing community that welcomes people from all backgrounds.

## Creator

Hey! 👋

This is me:

<div class="user-list user-list-center">
{% for user in people.maintainers %}

<div class="user"><a href="{{ contributors.khulnasoft.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ contributors.khulnasoft.avatarUrl }}"/></div><div class="title">@{{ contributors.khulnasoft.login }}</div></a> <div class="count">Answers: {{ user.answers }}</div><div class="count">Pull Requests: {{ contributors.khulnasoft.count }}</div></div>
{% endfor %}

</div>

I'm the creator of **ReadyAPI**. You can read more about that in [Help ReadyAPI - Get Help - Connect with the author](help-readyapi.md#connect-with-the-author){.internal-link target=_blank}.

...But here I want to show you the community.

---

**ReadyAPI** receives a lot of support from the community. And I want to highlight their contributions.

These are the people that:

* [Help others with questions in GitHub](help-readyapi.md#help-others-with-questions-in-github){.internal-link target=_blank}.
* [Create Pull Requests](help-readyapi.md#create-a-pull-request){.internal-link target=_blank}.
* Review Pull Requests, [especially important for translations](contributing.md#translations){.internal-link target=_blank}.
* Help [manage the repository](management-tasks.md){.internal-link target=_blank} (team members).

All these tasks help maintain the repository.

A round of applause to them. 👏 🙇

## Team

This is the current list of team members. 😎

They have different levels of involvement and permissions, they can perform [repository management tasks](./management-tasks.md){.internal-link target=_blank} and together we  [manage the ReadyAPI repository](./management.md){.internal-link target=_blank}.

<div class="user-list user-list-center">
{% for user in members["members"] %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatar_url }}"/></div><div class="title">@{{ user.login }}</div></a></div>
{% endfor %}

</div>

Although the team members have the permissions to perform privileged tasks, all the [help from others maintaining ReadyAPI](./help-readyapi.md#help-maintain-readyapi){.internal-link target=_blank} is very much appreciated! 🙇‍♂️

## ReadyAPI Experts

These are the users that have been [helping others the most with questions in GitHub](help-readyapi.md#help-others-with-questions-in-github){.internal-link target=_blank}. 🙇

They have proven to be **ReadyAPI Experts** by helping many others. ✨

/// tip

You could become an official ReadyAPI Expert too!

Just [help others with questions in GitHub](help-readyapi.md#help-others-with-questions-in-github){.internal-link target=_blank}. 🤓

///

You can see the **ReadyAPI Experts** for:

* [Last Month](#readyapi-experts-last-month) 🤓
* [3 Months](#readyapi-experts-3-months) 😎
* [6 Months](#readyapi-experts-6-months) 🧐
* [1 Year](#readyapi-experts-1-year) 🧑‍🔬
* [**All Time**](#readyapi-experts-all-time) 🧙

### ReadyAPI Experts - Last Month

These are the users that have been [helping others the most with questions in GitHub](help-readyapi.md#help-others-with-questions-in-github){.internal-link target=_blank} during the last month. 🤓

<div class="user-list user-list-center">
{% for user in people.last_month_experts[:10] %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a> <div class="count">Questions replied: {{ user.count }}</div></div>
{% endfor %}

</div>

### ReadyAPI Experts - 3 Months

These are the users that have been [helping others the most with questions in GitHub](help-readyapi.md#help-others-with-questions-in-github){.internal-link target=_blank} during the last 3 months. 😎

<div class="user-list user-list-center">
{% for user in people.three_months_experts[:10] %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a> <div class="count">Questions replied: {{ user.count }}</div></div>
{% endfor %}

</div>

### ReadyAPI Experts - 6 Months

These are the users that have been [helping others the most with questions in GitHub](help-readyapi.md#help-others-with-questions-in-github){.internal-link target=_blank} during the last 6 months. 🧐

<div class="user-list user-list-center">
{% for user in people.six_months_experts[:10] %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a> <div class="count">Questions replied: {{ user.count }}</div></div>
{% endfor %}

</div>

### ReadyAPI Experts - 1 Year

These are the users that have been [helping others the most with questions in GitHub](help-readyapi.md#help-others-with-questions-in-github){.internal-link target=_blank} during the last year. 🧑‍🔬

<div class="user-list user-list-center">
{% for user in people.one_year_experts[:20] %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a> <div class="count">Questions replied: {{ user.count }}</div></div>
{% endfor %}

</div>

### ReadyAPI Experts - All Time

Here are the all time **ReadyAPI Experts**. 🤓🤯

These are the users that have [helped others the most with questions in GitHub](help-readyapi.md#help-others-with-questions-in-github){.internal-link target=_blank} through *all time*. 🧙

<div class="user-list user-list-center">
{% for user in people.experts[:50] %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a> <div class="count">Questions replied: {{ user.count }}</div></div>
{% endfor %}

</div>

## Top Contributors

Here are the **Top Contributors**. 👷

These users have [created the most Pull Requests](help-readyapi.md#create-a-pull-request){.internal-link target=_blank} that have been *merged*.

They have contributed source code, documentation, etc. 📦

<div class="user-list user-list-center">
{% for user in (contributors.values() | list)[:50] %}

{% if user.login not in skip_users %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a> <div class="count">Pull Requests: {{ user.count }}</div></div>

{% endif %}

{% endfor %}

</div>

There are hundreds of other contributors, you can see them all in the <a href="https://github.com/readyapi/readyapi/graphs/contributors" class="external-link" target="_blank">ReadyAPI GitHub Contributors page</a>. 👷

## Top Translators

These are the **Top Translators**. 🌐

These users have created the most Pull Requests with [translations to other languages](contributing.md#translations){.internal-link target=_blank} that have been *merged*.

<div class="user-list user-list-center">

{% for user in (translators.values() | list)[:50] %}

{% if user.login not in skip_users %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a> <div class="count">Translations: {{ user.count }}</div></div>

{% endif %}

{% endfor %}

</div>

## Top Translation Reviewers

These users are the **Top Translation Reviewers**. 🕵️

I only speak a few languages (and not very well 😅). So, the reviewers are the ones that have the [**power to approve translations**](contributing.md#translations){.internal-link target=_blank} of the documentation. Without them, there wouldn't be documentation in several other languages.

<div class="user-list user-list-center">
{% for user in (translation_reviewers.values() | list)[:50] %}

{% if user.login not in skip_users %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a> <div class="count">Reviews: {{ user.count }}</div></div>

{% endif %}

{% endfor %}

</div>

## Sponsors

These are the **Sponsors**. 😎

They are supporting my work with **ReadyAPI** (and others), mainly through <a href="https://github.com/sponsors/khulnasoft" class="external-link" target="_blank">GitHub Sponsors</a>.

{% if sponsors %}

{% if sponsors.gold %}

### Gold Sponsors

{% for sponsor in sponsors.gold -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor %}
{% endif %}

{% if sponsors.silver %}

### Silver Sponsors

{% for sponsor in sponsors.silver -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor %}
{% endif %}

{% if sponsors.bronze %}

### Bronze Sponsors

{% for sponsor in sponsors.bronze -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor %}
{% endif %}

{% endif %}

### Individual Sponsors

{% if github_sponsors %}
{% for group in github_sponsors.sponsors %}

<div class="user-list user-list-center">

{% for user in group %}
{% if user.login not in sponsors_badge.logins %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a></div>

{% endif %}
{% endfor %}

</div>

{% endfor %}
{% endif %}

## About the data - technical details

The main intention of this page is to highlight the effort of the community to help others.

Especially including efforts that are normally less visible, and in many cases more arduous, like helping others with questions and reviewing Pull Requests with translations.

The data is calculated each month, you can read the <a href="https://github.com/readyapi/readyapi/blob/master/scripts/" class="external-link" target="_blank">source code here</a>.

Here I'm also highlighting contributions from sponsors.

I also reserve the right to update the algorithm, sections, thresholds, etc (just in case 🤷).
