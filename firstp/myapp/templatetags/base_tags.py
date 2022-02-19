from django import template
from ..models import Category

register = template.Library()

   
@register.inclusion_tag('category_nav.html')
def category_tag():
    return { "category": Category.objects.filter(status=True)}