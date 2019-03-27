import re

from django import template
from kdl_wagtail.core.templatetags.kdl_wagtail_core_tags import \
    get_block_title as kdl_get_block_title

register = template.Library()


@register.simple_tag()
def get_block_title(block):
    if not block:
        return

    if block.block_type == 'map_block':
        if block.value.get('caption'):
            return block.value.get('caption')

        return 'Map'

    if block.block_type == 'modal_block':
        return block.value.get('title')

    if block.block_type == 'timeline_block':
        return block.value.get('title')

    if block.block_type == 'timeline_stream_block':
        return 'Timeline'

    return kdl_get_block_title(block).capitalize()


@register.simple_tag()
def get_filter_value(category, value):
    if not category or not value:
        return

    return '{}_{}'.format(category.lower(), re.sub(r'\W', '_', value.lower()))
