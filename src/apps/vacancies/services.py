# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db.models import Q

from .models import Vacancy
from .forms import VacancyRequestForm


def get_all_vacancies():
    """ Возвращает все вакансии сортируя по дате добавления - сначала новые"""
    vacancies = Vacancy.objects.all().order_by('-date_and_time')
    return vacancies

def get_last_vacancies():
    """ Возвращает последние 3 вакансии для главной страницы """
    vacancies =  get_all_vacancies()[:3]
    return vacancies

def get_admin_vacancy_requests_actions(actions):
    """ Возвращает список методов для админ панели с их описанием """

    for status in settings.VACANCY_REQUEST_STATUS_CHOICES:

        def set_vacancy_requests_status(model_admin, request, queryset, status=status[0]):
            """ Обновляет статус у всех полученных объектов """
            queryset.update(status=status)

        set_vacancy_requests_status.short_description = f"Пометить выбранные заявки, как {status[1]}"
        set_vacancy_requests_status.__name__  = f'set_vacancy_requests_{status[0]}'

        actions.append(set_vacancy_requests_status)

    return actions

def get_vacancy_request_form(request):
    """ Возвращает словарь context с формой, для заявки на Вакансию """

    context = {}

    vacancy_request_form = VacancyRequestForm()

    choosen_vacancy_id = request.GET.get('id')
    if choosen_vacancy_id:
        vacancy_request_form.fields['vacancy'].initial = get_object_or_404(Vacancy, pk=choosen_vacancy_id)

    context.update( { 'request_form': vacancy_request_form } )
    context.update({
        'form_title': 'Заявка на Вакансию',
        'form_action': request.path
    })
    return context

def save_vacancy_request_form(request, context):
    """ Сохраняет объект заявки и возвращает конекст с данными формы, которые будут нужны в шаблоне """

    vacancy_request_form = VacancyRequestForm(request.POST)
    context.update({ 'request_form': vacancy_request_form })

    success_template = 'forms/connect_sended_widget.html'
    error_template = 'forms/connect_form_widget.html'

    if vacancy_request_form.is_valid():
        vacancy_request_form.save()

        context.update({
            'customer_name': vacancy_request_form.cleaned_data['customer_name'],
            'customer_last_name': vacancy_request_form.cleaned_data['customer_last_name'],
            'customer_email': vacancy_request_form.cleaned_data['customer_email'],
            'customer_phone': vacancy_request_form.cleaned_data['customer_phone']
        })

        return success_template, context

    else:
        return error_template, context

def get_vacancies_by_q(request):
    """ Возвращает Вакансии c учётом поиска """
    q = request.GET.get('q')

    if q:
        vacancies = Vacancy.objects.filter(
            Q(title__icontains=q)|
            Q(description__icontains=q)|
            Q(payment__icontains=q)
        ).order_by('-date_and_time')

    else:
        vacancies = None

    return vacancies
