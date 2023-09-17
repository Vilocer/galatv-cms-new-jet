# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from .models import GoogleMapModel


@plugin_pool.register_plugin
class GoogleMapPublisher(CMSPluginBase):
    model = GoogleMapModel
    module = _('Плагины к секции - Наше местоположение')
    name = _('our_location_map')
    render_template = 'maps/map_widget.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})

        return context

@plugin_pool.register_plugin
class AllGoogleMapsPublisher(CMSPluginBase):
    module = _('Плагины к секции - Наше местоположение')
    name = _('all_our_location_maps')
    allow_children = True
    render_template = 'maps/all_maps_widget.html'
    
    def render(self, context, instance, placeholder):
        context.update({'instance': instance})

        return context