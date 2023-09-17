# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext as _

from .models import InfoText, InfoImage, InfoItem


@plugin_pool.register_plugin
class InfoMorePublisher(CMSPluginBase):
    module = _("Плагины к секции - О нас")
    name = _("info_more")
    allow_children = True
    render_template = "info/info_more_widget.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin
class InfoImagePublisher(CMSPluginBase):
    model = InfoImage
    module = _("Плагины к секции - О нас")
    name = _("info_more_image")
    render_template = "info/info_image_widget.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin
class InfoTextPublisher(CMSPluginBase):
    model = InfoText
    module = _("Плагины к секции - О нас")
    name = _("info_more_text")
    render_template = "info/info_text_widget.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin
class InfoItemPublisher(CMSPluginBase):
    model = InfoItem
    module = _("Плагины к секции - О нас")
    name = _('info_item')
    render_template = "info/info_item_widget.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context