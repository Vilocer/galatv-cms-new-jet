# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from cms.models import CMSPlugin, Page

from djangocms_text_ckeditor.fields import HTMLField
from easy_thumbnails.fields import ThumbnailerImageField

from apps.mails.services import check_mailings
from . import local_services


class Service(CMSPlugin):
    """ Модель Услуги для секции Services """

    title = models.CharField('Название', max_length=250)
    description = HTMLField('Описание', blank=True, null=True, help_text='Краткое описание')
    date = models.DateField('Дата', auto_now_add=True)
    image = ThumbnailerImageField('Изображение', upload_to=local_services.get_service_image_upload_path,
        resize_source={ 'quality': 70, 'size': (385, 512), 'crop': 'smart', 'upscale': True }
    )

    form_page = models.ForeignKey(
        Page,
        on_delete=models.SET_NULL,
        verbose_name='Форма заказа',
        help_text='Страница с формой, для заказа услуги',
        blank=True,
        null=True,
        related_name='form_page'
    )
    detail_page = models.ForeignKey(
        Page,
        on_delete=models.SET_NULL,
        verbose_name='Своя страница услуги',
        help_text='Страница с подробным описанием услуги, если она есть',
        blank=True,
        null=True,
        related_name='detail_page'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class ServiceRequest(models.Model):
    """ Модель Заказа услугии """

    service = models.ForeignKey(Service, verbose_name='Выбранная услуга', on_delete=models.CASCADE)

    customer_name = models.CharField('Имя заказчика', max_length=250)
    customer_last_name = models.CharField('Фамилия заказчика', max_length=250)
    customer_phone = models.CharField('Номер телефона заказчика', max_length=250, help_text='Номер телефона в формате +7 (9**) (***)...')
    customer_email = models.EmailField('Email заказчика', max_length=250, help_text='Например: my@email.ru')

    customer_address = models.CharField('Адрес заказчика', max_length=250, help_text='Физический адрес', null=True)
    customer_comment = models.TextField('Комментарий к заказу', blank=True, null=True)

    date_and_time = models.DateTimeField('Дата и время', auto_now_add=True)

    status = models.CharField(
        'Статус заявки',
        max_length=10,
        choices=settings.SERVICE_REQUEST_STATUS_CHOICES,
        default=settings.SERVICE_REQUEST_STATUS_CHOICES[0][0],
    )

    class Meta:
        verbose_name = 'Заявка на оказания услуги'
        verbose_name_plural = 'Заявки на оказания услуги'

class ServiceRequestFormModel(CMSPlugin):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL,
        verbose_name='Конкретная услуга, для этой формы',
        help_text='Если нужна форма для конкретной услуги, для общей, оставьте поле пустым.',
        blank=True, null=True, default=None
    )

@receiver(post_save, sender=ServiceRequest)
def save_service_request(sender, instance, **kwargs):
    check_mailings(instance, settings.SERVICE_REQUEST_NAME_OF_MAILING_TYPES_CHOICES)
    