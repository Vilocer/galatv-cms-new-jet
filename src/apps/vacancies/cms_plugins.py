# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from config.services import get_home_page_url

from .services import get_last_vacancies, get_all_vacancies, get_vacancy_request_form, save_vacancy_request_form


@plugin_pool.register_plugin
class VacanciesOnMainPagePublisher(CMSPluginBase):
    module =  _('Плагины к секции - Вакансии')
    name = _('vacancies_on_main_page')
    render_template = 'vacancies/vacancies_on_main_page_widget.html'

    def render(self, context, instance, placeholder):
        context.update({'vacancies': get_last_vacancies()})

        return context

@plugin_pool.register_plugin
class AllVacanciesPagePublisher(CMSPluginBase):
    module =  _('Плагины к секции - Вакансии')
    name = _('all_vacancies')
    render_template = 'vacancies/all_vacancies_widget.html'

    def render(self, context, instance, placeholder):
        context.update({'vacancies': get_all_vacancies()})

        return context

@plugin_pool.register_plugin
class VacancyRequestFormPublisher(CMSPluginBase):
    module = _("Плагины к секции - Вакансии")
    name = _("vacancy_request_form")
    render_template = "forms/connect_form_widget.html"

    def render(self, context, instance, placeholder):
        request = context['request']
        csrf_token = context['csrf_token']

        if request.method == 'POST':
            self.render_template, context = save_vacancy_request_form(request, context)
            context.update({
                'instance': instance,
                'home_page_url': get_home_page_url(),
                'csrf_token': csrf_token

            })
        else:
            context = get_vacancy_request_form(request)
            context.update({
                'instance': instance,
                'home_page_url': get_home_page_url(),
                'csrf_token': csrf_token

            })

        return context