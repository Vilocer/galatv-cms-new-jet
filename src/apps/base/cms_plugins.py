# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from config.services import get_home_page_url
from apps.services.services import get_last_services
from .models import PageContentModel, PageImageModel, SearchPluginModel, FooterSocialLinkModel, IntroLinkPluginModel, BaseText

from apps.rates import services as rates_services
from apps.info import services as info_services
from apps.services import services as services_services
from apps.news import services as news_services
from apps.vacancies import services as vacancies_services
from apps.gallery import services as gallery_services


@plugin_pool.register_plugin
class PageImagePluginPublisher(CMSPluginBase):
    model = PageImageModel
    module =  _('Базовые плагины')
    name = _('page_image')
    render_template = 'page/page_image_view.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})

        return context

@plugin_pool.register_plugin
class PageContentPluginPublisher(CMSPluginBase):
    model = PageContentModel
    module =  _('Базовые плагины')
    name = _('page_content')
    allow_children = True
    render_template = 'page/page_content_view.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})

        return context


@plugin_pool.register_plugin
class ServicesLinksPlugin(CMSPluginBase):
    module =  _('Базовые плагины')
    name = _('footer_services_links')
    render_template = 'services/footer_services_links_widget.html'

    def render(self, context, instance, placeholder):
        context.update({'services': get_last_services(), 'home_page_url': get_home_page_url()})

        return context

@plugin_pool.register_plugin
class SearchPlugin(CMSPluginBase):
    model = SearchPluginModel
    module =  _('Базовые плагины')
    name = _('home_search_form_widget')
    render_template = 'home/search_widget.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})

        return context

@plugin_pool.register_plugin
class DefaultFormPlugin(CMSPluginBase):
    module =  _('Базовые плагины')
    name = _('default_page_form_container')
    allow_children = True
    render_template = 'home/default_form.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})

        return context

@plugin_pool.register_plugin
class FlexContainerPlugin(CMSPluginBase):
    module =  _('Базовые плагины')
    name = _('flex_container')
    allow_children = True
    render_template = 'home/flex_container_plugin.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})

        return context

@plugin_pool.register_plugin
class SearchPagePlugin(CMSPluginBase):
    module =  _('Базовые плагины')
    name = _('search_widget')
    render_template = 'home/search_page_widget.html'

    def render(self, context, instance, placeholder):
        request = context['request']

        search_results = {
            'rates': rates_services.get_rates_by_q(request),
            'services': services_services.get_services_by_q(request),
            'news': news_services.get_news_by_q_or_none(request),
            'vacancies': vacancies_services.get_vacancies_by_q(request),
            'gallery': gallery_services.get_gallery_images_by_q(request),
        }

        null_results = 0
        for result in search_results:
            if search_results[result] is not None:
                if search_results[result].count() == 0:
                    null_results += 1
            else:
                null_results += 1
        if len(search_results) == null_results:
            search_results = None
        
        context.update({
            'instance': instance, 
            'search_results': search_results,
            'home_page': get_home_page_url()
        })

        return context

@plugin_pool.register_plugin
class FooterSocialLinkPublisher(CMSPluginBase):
    model = FooterSocialLinkModel
    module =  _('Базовые плагины')
    name = _('footer_social_icon_widget')
    render_template = 'home/footer_social_icon_widget.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        
        return context

@plugin_pool.register_plugin
class IntroLinkPlugin(CMSPluginBase):
    model = IntroLinkPluginModel
    module = _('Базовые плагины')
    name = _('intro_link_widget')
    render_template = 'home/intro_link_widget.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        
        return context

@plugin_pool.register_plugin
class BaseTextPlugin(CMSPluginBase):
    model = BaseText
    module = _('Базовые плагины')
    name = _('base_text')
    render_template = 'home/base_text_plugin_widget.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        
        return context