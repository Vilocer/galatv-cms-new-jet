# -*- coding: utf-8 -*-

from django_summernote.admin import SummernoteModelAdmin

from django.contrib import admin
from django.conf import settings
from .models import News, NewsComment


class NewsCommentInline(admin.TabularInline):
    model = NewsComment

@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    """ Предствление модели Нвоости в админ-панели """

    fields = ['title', 'content', 'image', 'views_count']
    list_display = ['title', 'image', 'date_and_time', 'views_count']
    inlines = [ NewsCommentInline ]
    sort_by = ['-date_and_time']

if settings.NEWS_ALLOW_COMMENTS:
    @admin.register(NewsComment)
    class NewsCommentAdmin(admin.ModelAdmin):
        """ Предстваление модели комментария к Новости в админ-панели """

        fields = ['news', 'author_name', 'author_email', 'content']
        list_display = ['news', 'author_name', 'author_email', 'date_and_time']
        list_filter = ['news', 'author_email']
        sort_by = ['-date_and_time']