# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    """ Представление Фото Галереи в админ-панели """

    fields = ['title', 'image']
    list_display = ['title', 'image', 'date_and_time']