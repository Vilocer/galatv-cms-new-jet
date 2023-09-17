# -*- coding: utf-8 -*-

from slugify import slugify

def get_upload_vacancy_image_path(instance, default_name):
    """ Возвращает пусть сохранения Изображения вакансии в /media """

    path = f'vacancies/{ str(instance.date_and_time)[:10] }/{ slugify( str(instance.title) )[:10] }.jpg'
    return path