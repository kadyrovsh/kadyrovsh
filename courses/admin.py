from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

@admin.register(Ustoz)
class UstozAdmin(ModelAdmin):
    search_fields = ("id", "ism")
    list_display = ("id", "ism", "familiya", "malumot")
    list_display_links = ("ism",)
    list_editable = ("malumot",)
    # list_filter = ()

@admin.register(Yonalish)
class YonalishAdmin(ModelAdmin):
    search_fields = ("id", "name")
    list_display = ("id", "name", "start_date",)
    list_display_links = ("name",)
    list_editable = ("start_date",)
    list_filter = ("is_active",)

@admin.register(Fan)
class FanAdmin(ModelAdmin):
    search_fields = ("id", "nom")
    list_display = ("id", "nom", "yonalish",)
    list_display_links = ("nom",)
    list_editable = ("yonalish",)
    list_filter = ("yonalish",)
