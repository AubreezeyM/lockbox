import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

# Originally borrowed from: https://realpython.com/django-markdown/
@register.filter
@stringfilter
def render_markdown(v):
    md = markdown.Markdown(extensions=["fenced_code"])
    return mark_safe(md.convert(v))