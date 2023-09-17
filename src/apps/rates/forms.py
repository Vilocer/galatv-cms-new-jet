# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from .models import ConnectRequest, Rate

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

class ConnectRequestForm(forms.ModelForm):
    """ Форма для заказа Тарифа """

    rate = forms.ModelChoiceField(label='Выбранный тариф', queryset=Rate.objects, initial='')

    customer_name = forms.CharField(label='Ваше имя')
    customer_last_name = forms.CharField(label='Ваша фамилия')
    customer_phone = forms.RegexField(label='Ваша номер телефона', regex=r'^\+?1?\d{7,11}$', help_text='В формате +7 (9**) (***) (**) (**).')
    customer_email = forms.EmailField(label='Ваш Email', help_text='Например: gala@tv.ru')

    customer_address = forms.CharField(label='Ваш физический адрес', help_text='Например: г. Киров Октябрьский пр-т, 58')
    customer_comment = forms.CharField(label='Комментарий к заявке', widget=forms.Textarea( attrs={'cols': 2, 'rows': 2 } ), help_text='Сообщение к администрации, можно оставить пустым', required=False)

    connect_tv = forms.BooleanField(label='Кабельное ТВ', required=False)

    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible(attrs={'data-theme': 'dark'}), label='')

    def save(self, commit=True):
        instance = super(ConnectRequestForm, self).save(commit=commit)
        return instance

    class Meta:
        model = ConnectRequest
        fields = ('rate', 'customer_name', 'customer_last_name', 'customer_phone', 'customer_email', 'customer_address', 'customer_comment', 'connect_tv', 'captcha')