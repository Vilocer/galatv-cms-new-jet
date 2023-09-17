# -*- coding: utf-8 -*-

from django import forms
from .models import NewsComment


class NewsCommentForm(forms.ModelForm):
    """ Класс представлени формы Добавление комментария к новости """
    author_name = forms.CharField(label='Ваше имя', max_length=150, help_text='Пожалуйста, представтесь', widget=forms.TextInput(attrs={'autocomplete':'off'}))
    author_email = forms.EmailField(label='Ваш Email', help_text='Остальные пользователи его не увидят', widget=forms.EmailInput(attrs={'autocomplete':'off'}))
    content = forms.CharField(label='Ваш комментарий', widget=forms.Textarea( attrs={'cols': 5, 'rows': 5 } ), help_text='')

    def save(self, commit=True):
        instance = super(NewsCommentForm, self).save(commit=commit)
        return instance

    class Meta:
        model = NewsComment
        fields = ['author_name', 'author_email', 'content']