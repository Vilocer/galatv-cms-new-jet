# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from cms.models import CMSPlugin, Page
from easy_thumbnails.fields import ThumbnailerImageField

from apps.mails.services import check_mailings
from . import models_services


class Vacancy(models.Model):
    """ Модель Вакансии на сайте """

    title = models.CharField('Название', max_length=250, help_text='Короткое название вакансии')
    description = models.TextField('Описание', help_text='Описание вакансии')
    payment = models.CharField('Оплата', max_length=250, help_text='Например: 30т. рублей/мес или 100р за каждый час')

    date_and_time = models.DateTimeField('Дата и Время создания', auto_now_add=True)

    image = ThumbnailerImageField('Изображение', upload_to=models_services.get_upload_vacancy_image_path,
        resize_source={ 'quality': 70, 'size': (375, 250), 'crop': 'smart' }
    )

    form_page = models.ForeignKey(Page, on_delete=models.SET_NULL, verbose_name='Форма для заявки', help_text='Страница с формой, чтобы оставить заявку, если она есть', blank=True, null=True)

    def __str__(self):
        return f'{ self.title } - Оплата: { str(self.payment) }'

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

class VacancyRequest(models.Model):
    """ Модель Заявки на Вакансию на сайте """

    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name='Выбранная вакансия')

    customer_name = models.CharField('Имя заказчика', max_length=250)
    customer_last_name = models.CharField('Фамилия заказчика', max_length=250)
    customer_phone = models.CharField('Номер телефона заказчика', max_length=250, help_text='Номер телефона в формате +7 (9**) (***)...')
    customer_email = models.EmailField('Email заказчика', max_length=250, help_text='Например: my@email.ru')

    date_and_time = models.DateTimeField('Дата и время', auto_now_add=True)
    status = models.CharField(
        'Статус заявки',
        max_length=10,
        choices=settings.VACANCY_REQUEST_STATUS_CHOICES,
        default=settings.VACANCY_REQUEST_STATUS_CHOICES[0][0],
    )

    class Meta:
        verbose_name = 'Заявка на вакансию'
        verbose_name_plural = 'Заявки на вакансии'

@receiver(post_save, sender=VacancyRequest)
def save_vacancy_request(sender, instance, **kwargs):
    check_mailings(instance, settings.VACANCY_REQUEST_NAME_OF_MAILING_TYPES_CHOICES)