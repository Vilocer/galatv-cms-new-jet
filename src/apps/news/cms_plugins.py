# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from .services import get_last_news, get_news_page


@plugin_pool.register_plugin
class NewsOnMainPagePublisher(CMSPluginBase):
    module =  _('Плагины к секции - Новости')
    name = _('news_on_main_page')
    render_template = 'news/news_on_main_page_widget.html'

    def render(self, context, instance, placeholder):
        context.update({'news': get_last_news()})

        return context

@plugin_pool.register_plugin
class AllNewsPagePublisher(CMSPluginBase):
    module = _('Плагины к секции - Новости')
    name = _('all_news_page')
    render_template = 'news/all_news_widget.html'

    def render(self, context, instance, placeholder):
        csrf_token = context['csrf_token']
        self.render_template, context = get_news_page(context['request'])

        context.update({'csrf_token': csrf_token})

        return context