from django.contrib import admin
from routines.models import Exerciser, Routine


@admin.register(Exerciser)
class ExerciserAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "created_at"]
    list_display_links = ["author"]
    list_filter = ["author", "created_at"]
    search_fields = ["author"]
    list_per_page = 25


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "title", "created_at"]
    list_display_links = ["title"]
    list_filter = ["author", "created_at"]
    search_fields = ["author", "title"]
    list_per_page = 25
