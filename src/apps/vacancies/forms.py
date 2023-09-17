# -*- coding: utf-8 -*-

from django import forms
from .models import Vacancy, VacancyRequest

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

class VacancyRequestForm(forms.ModelForm):
    """" Представление формы для отправки заявки на вакансию """

    vacancy = forms.ModelChoiceField(label='Выбранная вакансия', queryset=Vacancy.objects, initial='')

    customer_name = forms.CharField(label='Ваше имя')
    customer_last_name = forms.CharField(label='Ваша фамилия')
    customer_phone = forms.RegexField(label='Ваша номер телефона', regex=r'^\+?1?\d{7,11}$', help_text='В формате +7 (9**) (***) (**) (**).')
    customer_email = forms.EmailField(label='Ваш Email', help_text='Например: gala@tv.ru')

    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible(attrs={'data-theme': 'dark'}), label='')

    def save(self, commit=True):
        instance = super(VacancyRequestForm, self).save(commit=commit)
        return instance

    class Meta:
        model = VacancyRequest
        fields = ['vacancy', 'customer_name', 'customer_last_name', 'customer_phone', 'customer_email', 'captcha']