# Harici Bağlantılar ve Makaleler

**ReadyAPI** sürekli büyüyen harika bir topluluğa sahiptir.

**ReadyAPI** ile alakalı birçok yazı, makale, araç ve proje bulunmaktadır.

Bunlardan bazılarının tamamlanmamış bir listesi aşağıda bulunmaktadır.

!!! tip "İpucu"
    Eğer **ReadyAPI** ile alakalı henüz burada listelenmemiş bir makale, proje, araç veya başka bir şeyiniz varsa, bunu eklediğiniz bir <a href="https://github.com/khulnasoft/readyapi/edit/master/docs/en/data/external_links.yml" class="external-link" target="_blank">Pull Request</a> oluşturabilirsiniz.

{% for section_name, section_content in external_links.items() %}

## {{ section_name }}

{% for lang_name, lang_content in section_content.items() %}

### {{ lang_name }}

{% for item in lang_content %}

* <a href="{{ item.link }}" class="external-link" target="_blank">{{ item.title }}</a> by <a href="{{ item.author_link }}" class="external-link" target="_blank">{{ item.author }}</a>.

{% endfor %}
{% endfor %}
{% endfor %}

## Projeler

`readyapi` konulu en son GitHub projeleri:

<div class="github-topic-projects">
</div>
