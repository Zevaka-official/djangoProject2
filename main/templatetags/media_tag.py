from django import template
from django.templatetags.static import static


register = template.Library()


@register.filter(name="mediapath")
def mediapath(value):
    if value:
        return value.url
    else:
        return static("image/123.jpg")