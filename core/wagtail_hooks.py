from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register
)
from wagtail.core import hooks

from .models import Discipline, Focus, Keyword, Method


class FacetAdmin(ModelAdmin):
    menu_icon = 'list-ul'
    list_display = ['title']
    search_fields = list_display


class DisciplineAdmin(FacetAdmin):
    model = Discipline


class FocusAdmin(FacetAdmin):
    model = Focus


class KeywordAdmin(FacetAdmin):
    model = Keyword


class MethodAdmin(FacetAdmin):
    model = Method


class FacetGroup(ModelAdminGroup):
    menu_label = 'Facets'
    menu_icon = 'folder-open-inverse'
    items = [DisciplineAdmin, FocusAdmin, KeywordAdmin, MethodAdmin]


modeladmin_register(FacetGroup)


@hooks.register('register_rich_text_features')
def register_core_features(features):
    features.default_features.append('superscript')
    features.default_features.append('subscript')
    features.default_features.append('strikethrough')
    features.default_features.append('blockquote')
