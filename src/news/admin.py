from django.contrib import admin

from .models import Dislike, Like, News, Tag, View


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("title",)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ("title", "text", "tags__title")


@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    search_fields = ("news__title", "news__tags__title")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    search_fields = ("news__title", "news__tags__title")


@admin.register(Dislike)
class DislikeAdmin(admin.ModelAdmin):
    search_fields = ("news__title", "news__tags__title")
