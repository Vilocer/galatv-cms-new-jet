# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext as _
from django.middleware.csrf import get_token
from .services import get_rates_on_main_page, get_sorted_by_place_rates, get_connect_request_form, save_connect_request
from config.services import get_home_page_url


@plugin_pool.register_plugin
class RatesOnMainPagePublisher(CMSPluginBase):
    module = _("Плагины к секции - Тарифы")
    name = _("rates_on_main_page")
    render_template = "rates/rates_on_main_page_widget.html"

    def render(self, context, instance, placeholder):
        context.update({'rates': get_rates_on_main_page})
        return context

@plugin_pool.register_plugin
class AllRatesPublisher(CMSPluginBase):
    module = _("Плагины к секции - Тарифы")
    name = _("all_rates")
    render_template = "rates/all_rates_widget.html"

    def render(self, context, instance, placeholder):
        context.update({'rates': get_sorted_by_place_rates})
        return context

@plugin_pool.register_plugin
class ConnectRateFormPublisher(CMSPluginBase):
    module = _("Плагины к секции - Тарифы")
    name = _("connect_rate_form")
    render_template = "forms/connect_form_widget.html"

    def render(self, context, instance, placeholder):
        request = context['request']
        csrf_token = context['csrf_token']

        if request.method == 'POST':
            self.render_template, context = save_connect_request(request, context)
            context.update({
                'instance': instance,
                'home_page_url': get_home_page_url(),
                'csrf_token': csrf_token

            })
        else:
            context = get_connect_request_form(request)
            context.update({
                'instance': instance,
                'home_page_url': get_home_page_url(),
                'csrf_token': csrf_token

            })

        return context