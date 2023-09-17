# -*- coding: utf-8 -*-

from django.conf import settings
from django.db.models import Q

from .models import GalleryImage


def get_all_gallery_images():
    """ Возвращает все Фото из Галереи сортируя их по дате добавления """
    gallery_images = GalleryImage.objects.all().order_by('-date_and_time')

    return gallery_images

def get_last_gallery_images():
    """ Возвращает последние фото из Галереи сортируя их по дате добавления """
    gallery_images = get_all_gallery_images()[:settings.GALLERY_IMAGES_ON_MAIN_PAGE_COUNT]

    return gallery_images

def get_gallery_images_by_q(request):
    """ Возвращает Фото галереи c учётом поиска """

    q = request.GET.get('q')

    if q:
        gallery_images = GalleryImage.objects.filter(
            Q(title__icontains=q)
        ).order_by('-date_and_time')

    else:
        gallery_images = None

    return gallery_images