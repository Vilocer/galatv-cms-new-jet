# -*- coding: utf-8 -*-

from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from djangocms_text_ckeditor.fields import HTMLField
from django_ckeditor_5.fields import CKEditor5Field

from . import models_services


class News(models.Model):
    """ Модель Новости на сайте """

    title = models.CharField('Название', max_length=250)
    content = models.TextField('Содержание')
    date_and_time = models.DateTimeField('Дата Создания', auto_now_add=True)
    
    image = ThumbnailerImageField('Изображение', upload_to=models_services.get_upload_news_image_path,
        resize_source={ 'quality': 70, 'size': (1240, 835), 'crop': 'smart', 'upscale': True },
        default=models_services.get_default_news_image_path
    )

    views_count = models.PositiveIntegerField('Количество просмотров', default=0)

    def __str__(self):
        return self.title + ' - ' + str(self.date_and_time)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

class NewsComment(models.Model):
    """ Модель Комментария в Новости """
    
    news = models.ForeignKey(News, verbose_name="Новость", on_delete=models.CASCADE)

    author_name = models.CharField('Имя автора', max_length=150)
    author_email = models.EmailField('Email автора')
    content = CKEditor5Field('Содержание', max_length=450)

    date_and_time = models.DateTimeField('Дата и время', auto_now_add=True)

    def __str__(self):
        return f'{ self.author_name } - {self.author_email}'

    class Meta:
        verbose_name = 'Комментарий к новости'
        verbose_name_plural = 'Комментарии к новостям'
