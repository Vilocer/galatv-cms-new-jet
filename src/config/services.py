from django.contrib.sites.models import Site
from cms.models import Page

def get_home_page_url():
    """ Возврашает url до домашней страницы """

    is_home_pages = Page.objects.filter(is_home=True)

    if is_home_pages.count() > 0:
        return is_home_pages[0].get_absolute_url()
    
    else:
        return '/'

def get_full_home_page_url():
    """ Возврашает полный url до домашней страницы """

    domain = Site.objects.get_current().domain

    return f'http://{ domain }{ get_home_page_url() }'