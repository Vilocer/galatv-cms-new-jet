# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from config.services import get_home_page_url

from .services import get_last_gallery_images, get_all_gallery_images


@plugin_pool.register_plugin
class GalleryOnMainPagePublisher(CMSPluginBase):
    module =  _('Плагины к секции - Галерея')
    name = _('gallery_on_main_page')
    render_template = 'gallery/gallery_on_main_page_widget.html'

    def render(self, context, instance, placeholder):
        context.update({'gallery_images': get_last_gallery_images()})

        return context

@plugin_pool.register_plugin
class AllGalleryPagePublisher(CMSPluginBase):
    module =  _('Плагины к секции - Галерея')
    name = _('all_gallery')
    render_template = 'gallery/all_gallery_widget.html'

    def render(self, context, instance, placeholder):
        context.update({'gallery_images': get_all_gallery_images()})

        return context