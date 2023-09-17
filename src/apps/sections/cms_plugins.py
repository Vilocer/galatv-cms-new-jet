# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext as _

from .models import Section


@plugin_pool.register_plugin
class SectionPlugin(CMSPluginBase):
    model = Section
    module = _("Секции")
    name = _("Section")
    allow_children = True
    render_template = "home/section_widget.html"

    def render(self, context, instance, placeholder):
        context.update({'section': instance})
        return context