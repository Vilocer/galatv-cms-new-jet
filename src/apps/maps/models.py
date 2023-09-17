from django.db import models
from cms.models import CMSPlugin

from djangocms_text_ckeditor.fields import HTMLField


class GoogleMapModel(CMSPlugin):
    """ Модель плагина Google Карты """

    title = HTMLField('Заголовок', max_length=250, blank=True, null=True)
    location_map = models.CharField('Iframe код из Google Maps', max_length=500)

    def __str__(self):
        if self.title:
            return str(self.title)
        else:
            return f'Локация - { str(self.pk) }'