from django.contrib import admin
from .models import Tag, News, View


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("title", )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ("title", "text", "tags__title")


@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    search_fields = ("news__title", "news__tags__title")
