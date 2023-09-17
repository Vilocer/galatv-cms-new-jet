# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Vacancy, VacancyRequest
from .services import get_admin_vacancy_requests_actions


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """ Представление Модели Вакансии в Админ-панели """

    fields = ['title', 'image', 'description', 'payment', 'form_page']
    list_display = ['title', 'image', 'payment', 'date_and_time', 'form_page']

@admin.register(VacancyRequest)
class VacancyRequestAdmin(admin.ModelAdmin):
    """ Представление Модели Заявки на вакансию в Админ-панели """

    fields  = ['customer_name', 'customer_last_name', 'customer_phone', 'customer_email', 'vacancy', 'status']
    list_display = ['status', 'customer_name', 'customer_last_name', 'customer_phone', 'customer_email', 'vacancy', 'date_and_time']
    list_filter = ['status', 'vacancy']
    list_per_page = 30
    actions = get_admin_vacancy_requests_actions([])
    ordering = ('-date_and_time',)
