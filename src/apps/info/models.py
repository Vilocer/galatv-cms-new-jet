# -*- coding: utf-8 -*-

from django.db import models
from cms.models import CMSPlugin
from easy_thumbnails.fields import ThumbnailerImageField
from djangocms_text_ckeditor.fields import HTMLField

from . import info_services


class InfoItem(CMSPlugin):
    """ Модель инфо объекта, секции о нас, в виде Django-CMS плагина """

    content = HTMLField('Текст', max_length=250)
    font_awesome_class = models.CharField('Класс Font-Awesome', max_length=250,
        help_text='Font-Awesome класс, например: "fas fa-eye" или "fab fa-vk". Определяет иконку объекта, можно подобрать на https://fontawesome.com/icons'
    )

    def __str__(self):
        return str(self.content)

class InfoText(CMSPlugin):
    """ Текст, для секции Info, в модальном окне 'Подробнее' """
    
    title = models.CharField('Название', max_length=250, help_text='Например: Гала ТВ')
    text = HTMLField('Содержание', blank=True, null=True)

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Информационный текст'
        verbose_name_plural = 'Информационные текста'

class InfoImage(CMSPlugin):
    """ Изображение к тексту, для секции Info, в модальном окне """

    title = models.CharField('Название для изображения', max_length=250, help_text='Краткое описание')
    date = models.DateField('Дата', auto_now_add=True)
    image = ThumbnailerImageField('Изображение', upload_to=info_services.get_upload_info_image_path,
        resize_source={ 'quality': 70, 'size': (600, 900), 'crop': 'smart' }
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Изображение к инфо секции'
        verbose_name_plural = 'Изображения к инфо секции'