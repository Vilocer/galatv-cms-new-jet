# -*- coding: utf-8 -*-

from .models import InfoText, InfoImage


def get_all_info_texts():
    """ Возвращает все модели InfoText """

    return InfoText.objects.all()

def get_all_info_images(): 
    """ Возвращает все модели InfoImage """

    return InfoImage.objects.all()