# -*- coding: utf-8 -*-

from slugify import slugify

def get_service_image_upload_path(instance, default_name):
    """ Возвращает путь для сохранение Service.image """
    string  = f'services/{ str(instance.date)[:10] }/{ slugify( str(instance.title) )[:10] }.jpg'

    return string