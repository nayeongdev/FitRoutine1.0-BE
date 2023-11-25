from django.contrib import admin
from accounts.models import CustomUser


@admin.register(CustomUser)
class PostAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "date_joined"]
    list_display_links = ["username", "email"]
    list_filter = ["date_joined"]
    search_fields = ["email"]
    list_per_page = 25
