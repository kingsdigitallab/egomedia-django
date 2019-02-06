from wagtail.contrib.modeladmin.options import (ModelAdmin, ModelAdminGroup,
                                                modeladmin_register)

from .models import Discipline, Focus, Keyword, Method


class FacetAdmin(ModelAdmin):
    menu_icon = 'list-ul'
    list_display = ['title']
    list_filter = list_display
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
