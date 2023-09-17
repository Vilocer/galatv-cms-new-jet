from django.db import models
from django.conf import settings

from cms.models import CMSPlugin, Page
from cms.models.fields import PlaceholderField

from easy_thumbnails.fields import ThumbnailerImageField
from multiselectfield import MultiSelectField
from fontawesome_5.fields import IconField
from django_summernote.fields import SummernoteTextField

from . import models_services


class PageImageModel(CMSPlugin):
    """ Модель плагина фотографии для пустой страницы """

    title = models.CharField('Заголовок', max_length=250)
    date_and_time = models.DateTimeField('Дата Создания', auto_now_add=True)
    image = ThumbnailerImageField('Изображение', upload_to=models_services.get_upload_page_image_path,
        resize_source={ 'quality': 70, 'size': (1240, 835), 'crop': 'smart', 'upscale': True },
        default=models_services.get_default_page_image_path

    )

    def __str__(self):
        return f'Изображение к странице - {str(self.title)}'

    class Meta:
        verbose_name = 'Изображение к странице'
        verbose_name_plural = 'Изображения к страницам'

class PageContentModel(CMSPlugin):
    """ Модель плагина содержания пустой страницы """

    title = models.CharField('Заголовок', max_length=250)
    date_and_time = models.DateTimeField('Дата Создания', auto_now_add=True)

    def __str__(self):
        return f'Содрежание страницы - {str(self.title)}'

    class Meta:
        verbose_name = 'Содержание страницы'
        verbose_name_plural = 'Содержания страниц'

class IntroLinkPluginModel(CMSPlugin): 
    """ Модель плагина кнопки в интро секции на главной странице сайта """
    
    title = models.CharField('Название кнопки', max_length=250)

    link_url = models.URLField(
        'Куда введет кнопка',
        help_text='Если кнопка открывает модальное окно, то поле можно оставить пустым',
        blank=True,
        null=True
    
    )

    icon = IconField('Своя иконка для кнопки, если есть', blank=True, null=True)

    target_modal_id = models.CharField(
        'ID модально окна, без #',
        help_text='Если ссылка должна его открывать, когда такое есть, то link_url не работает, а самой ссылке добавляется класс .modal__link',
        max_length=250,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{ self.title } - Кнопка'

class SearchPluginModel(CMSPlugin):
    """ Модель плагина поиска по всему сайту """

    search_page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        verbose_name='Поисковая страница',
        help_text='В нее будет приходить GET запрос с параметром "q". '
    )

    indexing_pages =  MultiSelectField(
        'Где искать',
        choices=settings.SEARCH_PLUGIN_INDEXING_PAGES_CHOICES,
        help_text='Разделы, по которым будет проводится поиск'
    )

    def __str__(self):
        return f'Поисковой плагин ({ str(self.pk) })'

class FooterSocialLinkModel(CMSPlugin):
    """ Модель плагина, для отображения своих social icons и ссылок на наих """

    icon = IconField('Икона Font-Awesome', help_text='Специальная иконка для соц. сети')
    link_url = models.URLField('Ссыллка на соц. сеть')

    def __str__(self):
        return f'Иконка соц. сети ({ str(self.pk) })'

class BaseText(CMSPlugin):
    content = SummernoteTextField()