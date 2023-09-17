# -*- coding: utf-8 -*-

from django.conf import settings
from django.db.models import Q
from django.shortcuts  import get_object_or_404
from django.utils import timezone

from .models import News, NewsComment
from .forms import NewsCommentForm


def add_news_view(self):
    """ Увеличивает количество просмотром новости на 1 и возвращает их количество """
    self.views_count += 1
    self.save()

    return self.views_count

def get_comments_count(self):
    """ Возращает количество комментариев к Новости """
    comments_count = NewsComment.objects.filter(news=self).count()
    return comments_count

def get_comments(self):
    """ Возращает все комментарии к Новости """
    comments = NewsComment.objects.filter(news=self).order_by('-date_and_time')
    return comments

def get_news_month_name(self):
    """ Возвращает короткое название месяца создания Новости """
    return self.date_and_time.strftime("%b")

def get_news_time(self):
    """ Возвращает время создания Новости """
    tz = timezone.get_default_timezone()

    return self.date_and_time.astimezone(tz).strftime('%H:%M')

def get_all_news():
    """ Возвращает все новости """
    news = News.objects.all().order_by('-date_and_time')
    return news

def get_last_news():
    """ Возвращает последние новости """
    news = get_all_news()[:settings.COUNT_NEWS_ON_MAIN_PAGE]
    return news

def get_news_by_q(request):
    """ Возвращает новости c учётом поиска """
    q = request.GET.get('q')

    if q:
        news = News.objects.filter(
            Q(title__icontains=q)|
            Q(content__icontains=q)
        ).order_by('-date_and_time')

    else:
        news = get_all_news()

    return news, q

def get_news_by_pk(pk):
    """ Возвращает отдельную Новость по уникальному ключу и увеличивает кол-во лайков на 1 если передан like"""
    news = get_object_or_404(News, pk=pk)

    return news

def get_news_by_q_or_all(request):
    """ Возвращает новости c учётом поиска """
    q = request.GET.get('q')

    if q:
        news = News.objects.filter(
            Q(title__icontains=q)|
            Q(content__icontains=q)
        ).order_by('-date_and_time')

    else:
        news = get_all_news()

    return news

def get_news_by_q_or_none(request):
    """ Возвращает новости c учётом поиска """
    q = request.GET.get('q')

    if q:
        news = News.objects.filter(
            Q(title__icontains=q)|
            Q(content__icontains=q)
        ).order_by('-date_and_time')

    else:
        news = None

    return news

def get_news_page(request):
    "Если есть ?id, то возвращает контекст с новостью by id, если нет то get_news_by_q_or_none"

    context = {}

    if request.GET.get('id'):
        template = 'news/news_view_widget.html'
        news = get_news_by_pk(request.GET.get('id'))

        if request.method == 'POST':
            context = save_comment_form(request, request.GET.get('id'))

        else:
            if settings.NEWS_ALLOW_COMMENTS:
                context.update({'news_comments': news.get_comments()})
            context.update({'comment_form': get_comment_form()})
    else:
        if request.GET.get('q'):
            news = get_news_by_q_or_all(request)
            context.update({'q': request.GET.get('q')})
            
        else:
            news = get_all_news()

        template = 'news/all_news_widget.html'

    context.update({'news': news })

    return template, context

def get_comment_form():
    """ Возвращает форму отправки комментария к Новости """
    comment_form = NewsCommentForm()
    return comment_form


def save_comment_form(request, pk):
    """ Сохраняет форму с комменатрием к Новости """
    news = get_news_by_pk(pk)
    comment_form = NewsCommentForm(request.POST)
    news_comments = news.get_comments()
    context = { 'news': news, 'comment_form': comment_form, 'news_comments': news_comments }

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.news = news
        comment.save()

    return context

# Add Custom Methods to News Model
News.add_view = add_news_view
News.get_comments_count = get_comments_count
News.get_comments = get_comments
News.get_month_name = get_news_month_name
News.get_time = get_news_time