# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Rate, Place, ConnectRequest
from .services import get_admin_connect_requests_actions

from adminsortable2.admin import SortableAdminMixin


@admin.register(Place)
class RateAdmin(admin.ModelAdmin):
    """Класс, для представления модели зоны Охвата Тарифов в админ-панели"""
    fields = list_display = [ 'title', 'description']

@admin.register(Rate)
class RateAdmin(SortableAdminMixin, admin.ModelAdmin):
    """Класс, для представления модели Тарифа в админ-панели"""
    list_display = [ 'title', 'internet_speed', 'price', 'place', 'show_on_main_page', 'have_tv', 'price_tv' ]
    fields = [ 'title', 'description', 'internet_speed', 'price', 'place', 'color', 'show_on_main_page', 'form_page', 'have_tv', 'price_tv' ]
    list_filter = ['place', 'show_on_main_page']

@admin.register(ConnectRequest)
class ConnectRequestAdmin(admin.ModelAdmin):
    """"Класс, для представления модели Заявки на потключение тарифа в админ-панели"""
    fields  = ['customer_name', 'customer_last_name', 'customer_address', 'customer_phone', 'customer_email', 'rate', 'connect_tv', 'customer_comment', 'status']
    list_display = ['status', 'customer_name', 'customer_last_name', 'customer_address', 'customer_phone', 'customer_email', 'rate', 'connect_tv', 'date_and_time']
    list_filter = ['status', 'rate', 'connect_tv']
    list_per_page = 30
    actions = get_admin_connect_requests_actions([])
    ordering = ('-date_and_time',)
