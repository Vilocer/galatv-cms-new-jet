# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.db.models import Q

from .models import Rate, Place
from .forms import ConnectRequestForm


def get_rates():
    """ Возвращает все тарифы """
    return Rate.objects.all().order_by('view_position')

def get_rates_on_main_page():
    """ Возвращает все тарифы, которые показываються на главной странице """
    return Rate.objects.filter(show_on_main_page=True).order_by('view_position')

def get_rates_by_place(place):
    """ Возвращает тарифы отсортированные по place """
    return Rate.objects.filter(place=place).order_by('view_position')

def get__places():
    """ Возвращает все Зоны Охватов тарифов (Place) """
    return Place.objects.all()

def get_sorted_by_place_rates():
    """" Возвращает словарь тарифов отсортрованные по зоне охватов """
    places = get__places()
    rates_dict = {}

    for place in places:
        rates_dict.update( { place: [ get_rates_by_place(place) ] } )

    return rates_dict

def get_connect_request_form(request):
    """ Возвращает словарь context с формой, для заявки на подключение интернета """

    context = {}
    rate_connect_request_form = ConnectRequestForm()

    if request.GET.get('tv', False) == 'on':
        rate_connect_request_form.fields['connect_tv'].initial = True

    choosen_rate_id = request.GET.get('rate_id')

    if choosen_rate_id:
        rate_connect_request_form.fields['rate'].initial = get_object_or_404(Rate, pk=choosen_rate_id)

    context.update( { 'request_form': rate_connect_request_form } )
    context.update({
        'form_title': 'Заявка на подключение',
        'form_action': request.path
    })
    return context

def save_connect_request(request, context):
    """ Сохраняет объект заявки и возвращает конекст с данными формы, которые будут нужны в шаблоне """

    connect_request_form = ConnectRequestForm(request.POST)
    context.update({ 'request_form': connect_request_form })

    success_template = 'forms/connect_sended_widget.html'
    error_template = 'forms/connect_form_widget.html'

    if connect_request_form.is_valid():
        connect_request_form.save()

        context.update({
            'customer_name': connect_request_form.cleaned_data['customer_name'],
            'customer_last_name': connect_request_form.cleaned_data['customer_last_name'],
            'customer_email': connect_request_form.cleaned_data['customer_email'],
            'customer_phone': connect_request_form.cleaned_data['customer_phone']
        })

        return success_template, context

    else:
        return error_template, context


def get_admin_connect_requests_actions(actions):
    """ Возвращает список методов для админ панели с их описанием """

    for status in settings.RATE_CONNECT_REQUEST_STATUS_CHOICES:

        def set_connect_requests_status(model_admin, request, queryset, status=status[0]):
            """ Обновляет статус у всех полученных объектов """
            queryset.update(status=status)

        set_connect_requests_status.short_description = f"Пометить выбранные заявки, как {status[1]}"
        set_connect_requests_status.__name__  = f'set_connect_requests_{status[0]}'

        actions.append(set_connect_requests_status)

    return actions

def get_rates_by_q(request):
    """ Возвращает результаты поиска по всем тарифам """
    q = request.GET.get('q')

    if q:
        rates = Rate.objects.filter(
            Q(title__icontains=q)|
            Q(description__icontains=q)
        )

    else:
        rates = None

    return rates
    