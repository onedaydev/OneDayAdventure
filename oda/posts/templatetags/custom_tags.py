from django import template

register = template.Library()

@register.filter
def get_item_index(page_obj, index):
    return page_obj.start_index() + index
