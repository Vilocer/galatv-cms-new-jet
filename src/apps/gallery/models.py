# -*- coding: utf-8 -*-

from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from . import models_services


class GalleryImage(models.Model):
    """ Модель представления Фотографии галереи """

    title = models.CharField('Название к фото', max_length=250, help_text='Короткое описание фото')
    date_and_time = models.DateTimeField('Дата и время', auto_now_add=True)

    image = ThumbnailerImageField('Изображение', upload_to=models_services.get_upload_gallery_image_path,
        resize_source={ 'quality': 70, 'size': (1600, 1600), 'crop': 'smart' }
    )

    def __str__(self):
        return f'{ self.title } | { str(self.date_and_time) }'

    class Meta:
        verbose_name = 'Изображение в галерее'
        verbose_name_plural = 'Изображения в галерее'