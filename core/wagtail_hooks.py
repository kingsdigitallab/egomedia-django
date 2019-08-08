from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register
)
from wagtail.core import hooks

from .models import Facet, FacetType


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('css/facets.css')
    )


class FacetAdmin(ModelAdmin):
    model = Facet

    menu_icon = 'tag'
    list_display = ['facet_type', 'title']
    list_filter = ['facet_type']
    search_fields = list_display


class FacetTypeAdmin(ModelAdmin):
    model = FacetType

    menu_icon = 'title'
    list_display = ['title']


class FacetGroup(ModelAdminGroup):
    menu_label = 'Facets'
    menu_icon = 'tag'
    items = [FacetTypeAdmin, FacetAdmin]


modeladmin_register(FacetGroup)


@hooks.register('register_rich_text_features')
def register_core_features(features):
    features.default_features.append('superscript')
    features.default_features.append('subscript')
    features.default_features.append('strikethrough')
    features.default_features.append('blockquote')
