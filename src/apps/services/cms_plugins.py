from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.template import RequestContext
from django.utils.translation import ugettext as _

from config.services import get_home_page_url

from .models import Service, ServiceRequestFormModel
from .services import get_service_request_form, save_service_request


@plugin_pool.register_plugin
class ServicePublisher(CMSPluginBase):
    model = Service
    module = _('Плагины к секции - Услуги')
    name = _('services_item')
    render_template = "services/service_widget.html"

    def render(self, context, instance, placeholder):
        context.update({'service': instance})
        return context

@plugin_pool.register_plugin
class ServicesOnMainPagePublisher(CMSPluginBase):
    module = _('Плагины к секции - Услуги')
    name = _('services_on_main_page')
    render_template = "services/services.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin
class ServiceRequestFormPublisher(CMSPluginBase):
    model = ServiceRequestFormModel
    module = _("Плагины к секции - Услуги")
    name = _("service_request_form")
    render_template = "forms/connect_form_widget.html"

    def render(self, context, instance, placeholder):
        request = context['request']
        csrf_token = context['csrf_token']

        if request.method == 'POST':
            
            self.render_template, context = save_service_request(request, context)
            context.update({
                'instance': instance,
                'home_page_url': get_home_page_url(),
                'csrf_token': csrf_token

            })
        else:
            context = get_service_request_form(request)
            context.update({
                'instance': instance,
                'home_page_url': get_home_page_url(),
                'csrf_token': csrf_token

            })

        if instance.service:
            context['request_form'].fields['service'].initial = instance.service

        return context