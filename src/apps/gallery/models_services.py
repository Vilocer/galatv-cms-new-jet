# -*- coding: utf-8 -*-

from slugify import slugify


def get_upload_gallery_image_path(instance, default_name):
    """ Возвращает путь для сохранение GalleryImage.image """
    string  = f'gallery/{ str(instance.date_and_time)[:10] }/{ slugify( str(instance.title) )[:10] }.jpg'
    
    return string