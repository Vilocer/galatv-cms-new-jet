from django.db import models
from cms.models import CMSPlugin, Page
from cms.models.fields import PlaceholderField


class Section(CMSPlugin):
    """ Модель секции на главной странице, в виде Django-CMS плагина """

    title = models.CharField('Заголовок', max_length=250, blank=True, null=True)
    sub_title = models.CharField('Подзаголовок', max_length=250, blank=True, null=True)

    page = models.ForeignKey(Page, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Своя страница, для секции', help_text='Отдельная страница, для этой секции, если она есть')
    page_link_text = models.CharField('Текст ссылки на старинцу секции', help_text='Текст кнопки с ссылкой на отдельную страницу секции, если она есть', max_length=250, blank=True, null=True)

    def __str__(self):
        if self.title:
            return str(self.title)
        else:
            return 'Без названия'

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'
