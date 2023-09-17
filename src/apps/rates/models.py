# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from cms.models import CMSPlugin, Page
from colorfield.fields import ColorField

from apps.mails.services import check_mailings


class Place(models.Model):
    """Горрод, Посёлок и т.д. Где действует Данный тариф"""

    title = models.CharField('Название', max_length=250, help_text='Например: Киров или Мурыгино')
    description = models.TextField('Описание', help_text='Например: Эта зона тарифов действует в Ленинском районе города Кирова', blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Зона Охвата Тарифа (Город, Посёлок, и т.д)'
        verbose_name_plural = 'Зоны Охвата Тарифов'

class Rate(CMSPlugin):
    """Модель Интернет-Тарифа"""

    title = models.CharField('Название', max_length=250, help_text='Например: Premium или Lite', unique=True)
    description = models.TextField(
        'Описание',
        help_text='Например: Этот тариф идеально подходит, для домашнего использования, т.к. в нём есть кабельное ТВ',
        null=True,
        blank = True
    )

    view_position = models.PositiveIntegerField(
        'Позиция',
        default=0,
        blank=False,
        null=False
    )

    internet_speed = models.PositiveIntegerField('Скорость интернета', help_text='(В МБТ/C)')
    price = models.PositiveIntegerField('Цена тарифа', help_text='(В РУБ/МЕСЯЦ) Без учёта Телевидения')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Место, зоны охвата тарифа", default=None)

    color = ColorField('Свой цвет', default='#54AC8A', help_text='Отличительный цвет тарифа')
    show_on_main_page = models.BooleanField(
        'Показывать на Главной странице',
        help_text="Тариф будет виден на главной в секции тарифы"
    )

    form_page = models.ForeignKey(Page, on_delete=models.SET_NULL, verbose_name='Форма для заказа', help_text='Страница с формой, для заказа тарифа, если она есть', blank=True, null=True)

    have_tv = models.BooleanField('Имеется в тарифе ТВ')
    price_tv = models.PositiveIntegerField(
        'Цена ТВ',
        help_text='В РУБ (Если оно имеется). Эта цена будет суммироваться с обычной',
        null=True,
        blank=True,
    )

    def __str__(self):
        string = f'{ self.place.title } - { self.title } - { self.internet_speed } МБТ/с - { self.price } РУБ/месяц'
        if self.have_tv:
            tv = ' - ТВ +' + str(self.price_tv) + ' руб/мес'
        return string

    def save(self, *args, **kwargs):
        if self.view_position == 0:
                self.view_position = self.pk
        super(Rate, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Интернет-Тариф'
        verbose_name_plural = 'Интернет тарифы'
        ordering = ['view_position']

class ConnectRequest(models.Model):
    """Модель Заявки на подключения тарифа"""

    rate = models.ForeignKey(Rate, verbose_name='Выбранный тариф', on_delete=models.CASCADE)
    connect_tv = models.BooleanField('Подключать ТВ', blank=True, null=True)

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
        choices=settings.RATE_CONNECT_REQUEST_STATUS_CHOICES,
        default=settings.RATE_CONNECT_REQUEST_STATUS_CHOICES[0][0],
    )

    class Meta:
        verbose_name = 'Заявка на подключение'
        verbose_name_plural = 'Заявки на подключение'

@receiver(post_save, sender=ConnectRequest)
def save_connect_request(sender, instance, **kwargs):
    """" Вызывается, после сохранения Заявки на подключение тарифа """
    check_mailings(instance, settings.CONNECT_REQUEST_NAME_OF_MAILING_TYPES_CHOICES)
    