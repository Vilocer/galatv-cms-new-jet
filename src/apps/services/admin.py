# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Service, ServiceRequest
from .services import get_admin_service_requests_actions


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    """"Класс, для представления модели Заявки на оказание Услуги в админ-панели"""
    fields  = ['customer_name', 'customer_last_name', 'customer_phone', 'customer_email', 'service', 'customer_address', 'customer_comment', 'status']
    list_display = ['status', 'customer_name', 'customer_last_name', 'customer_address', 'customer_phone', 'customer_email', 'service', 'date_and_time']
    list_filter = ['status', 'service']
    list_per_page = 30
    actions = get_admin_service_requests_actions([])
    ordering = ('-date_and_time',)
