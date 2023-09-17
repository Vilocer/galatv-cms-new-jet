# -*- coding: utf-8 -*-

from slugify import slugify


def get_upload_info_image_path(instance, default_name):
    """ Возвращает путь для сохранение InfoImage """
    string  = f'info/{ str(instance.date)[:10] }/{ slugify( str(instance.title) )[:10] }.jpg'

    return string