# -*- coding: utf-8 -*-

from slugify import slugify
from django.conf import settings


def get_upload_page_image_path(instance, image):
    """ Возвращает пусть для сохранения изображени Новости """

    string  = f'pages/{ str(instance.date_and_time)[:10] }/{ slugify( str(instance.title) )[:10] }.jpg'
    return string

def get_default_page_image_path():
    return settings.PAGE_DEFAULT_IMAGE_PATH