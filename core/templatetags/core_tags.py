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

    return kdl_get_block_title(block)


@register.simple_tag()
def get_filter_value(category, value):
    if not category or not value:
        return

    return '{}_{}'.format(
        re.sub(r'\W', '_', category.lower()),
        re.sub(r'\W', '_', value.lower())
    )


@register.filter
def get_filter_level(value, arg):
    if isinstance(arg, int):
        return range(5 * (arg - 4))

    return []


@register.simple_tag(takes_context=True)
def sort_endnotes(context, endnotes, field):
    request = context.get('request')

    # django modelcluster doesn't support __ clauses in order_by
    # and it causes the preview to fail
    if getattr(request, 'is_preview') and '__' in field:
        return endnotes

    return endnotes.order_by(field)


@register.simple_tag(takes_context=True)
def get_site_root(context):
    """Returns the site root Page, not the implementation-specific model used.
    Object-comparison to self will return false as objects would differ.

    :rtype: `wagtail.wagtailcore.models.Page`
    """
    return context['request'].site.root_page


@register.inclusion_tag('core/tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context, root, current_page):
    """Returns the pages that are part of the breadcrumb trail of the current
    page, up to the root page."""
    pages = current_page.get_ancestors(
        inclusive=True).descendant_of(root).filter(live=True)

    return {'request': context['request'], 'root': root,
            'current_page': current_page, 'pages': pages}
