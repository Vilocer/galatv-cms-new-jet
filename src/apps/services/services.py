# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.db.models import Q

from .models import Service
from .forms import ServiceRequestForm


def get_all_services():
    """ Возвращает все услуги """
    return Service.objects.all().filter(placeholder__page__publisher_is_draft=False)

def get_last_services():
    """ Возвращает последние 3 услуги """
    return get_all_services().reverse()[:3]

def get_service_request_form(request):
    """ Возвращает словарь context с формой, для заявки на оказание Услуги """

    context = {}
    service_request_form = ServiceRequestForm()

    choosen_service_id = request.GET.get('id')
    if choosen_service_id:
        service_request_form.fields['service'].initial = get_object_or_404(Service, pk=choosen_service_id)

    context.update( { 'request_form': service_request_form } )
    context.update({
        'form_title': 'Заявка на оказание услуги',
        'form_action': request.path
    })
    return context

def save_service_request(request, context):
    """ Сохраняет объект заявки и возвращает конекст с данными формы, которые будут нужны в шаблоне """

    service_request_form = ServiceRequestForm(request.POST)
    context.update({ 'request_form': service_request_form })

    success_template = 'forms/connect_sended_widget.html'
    error_template = 'forms/connect_form_widget.html'

    if service_request_form.is_valid():
        service_request_form.save()

        context.update({
            'customer_name': service_request_form.cleaned_data['customer_name'],
            'customer_last_name': service_request_form.cleaned_data['customer_last_name'],
            'customer_email': service_request_form.cleaned_data['customer_email'],
            'customer_phone': service_request_form.cleaned_data['customer_phone']
        })

        return success_template, context

    else:
        context.update({
            'form_title': 'Заявка на оказание услуги',
            'form_action': request.path
        })
        return error_template, context


def get_admin_service_requests_actions(actions):
    """ Возвращает список методов для админ панели с их описанием """

    for status in settings.SERVICE_REQUEST_STATUS_CHOICES:

        def set_service_requests_status(model_admin, request, queryset, status=status[0]):
            """ Обновляет статус у всех полученных объектов """
            queryset.update(status=status)

        set_service_requests_status.short_description = f"Пометить выбранные заявки, как {status[1]}"
        set_service_requests_status.__name__  = f'set_service_requests_{status[0]}'

        actions.append(set_service_requests_status)

    return actions

def get_services_by_q(request):
    """ Возвращает результаты поиска по Услугам """
    q = request.GET.get('q')

    if q:
        services = Service.objects.filter(placeholder__page__publisher_is_draft=False).filter(
            Q(title__icontains=q)|
            Q(description__icontains=q)
        )

    else:
        services = None

    return services