from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from config.services import get_full_home_page_url
from .models import Mailing


def get_mailings():
    """ Возвращает все рассылки """
    mailings = Mailing.objects.all()

    return mailings

def get_mailings_by_type(type_of_mailings):
    """ Возвращает все рассылки с фильтром поля type_of_mailing  """
    mailings = Mailing.objects.filter(type_of_mailing=type_of_mailings)

    return mailings

def send_html_mail(subject_template, content_template, to_email, render_message_context):
    " Отправляет письмо, рендеря шаблоны"

    subject_of_mail = render_to_string(subject_template, render_message_context)
    html_content = render_to_string(content_template, render_message_context)
    text_content = strip_tags(html_content)

    message = EmailMultiAlternatives(subject_of_mail,
        text_content,
        to=to_email
    )

    message.attach_alternative(html_content, "text/html")
    message.send()

def check_mailings(instance, type_of_request):
    """
    Функция, которая вызывается signals, при создании в бд объекти модели какой-либо заявки.
    Получает список всех рассылок mailings, отфилтрованных по данному type_of_request.
    Если такие mailings существуют, то совершает mail рассылку на указаный в ней адрес.
    """
    mailings = get_mailings_by_type(type_of_request)

    if mailings:
        for mailing in mailings:
            to_email = [mailing.email_to_send]
            from_email = settings.EMAIL_HOST_MAIL_ADDRESS

            render_message_context = {
                'site': Site.objects.get_current(),
                'home_page_url': get_full_home_page_url(),
                'from_email': from_email
            }

            if mailing.type_of_mailing == settings.CONNECT_REQUEST_NAME_OF_MAILING_TYPES_CHOICES:
                render_message_context.update({
                    'connect_request': instance
                })
                subject_template = 'mails/connect_request/mail_subject.html'
                content_template = 'mails/connect_request/mail_content.html'

                send_html_mail(subject_template, content_template, to_email, render_message_context)

            elif mailing.type_of_mailing == settings.SERVICE_REQUEST_NAME_OF_MAILING_TYPES_CHOICES:
                render_message_context.update({
                    'service_request': instance
                })
                subject_template = 'mails/service_request/mail_subject.html'
                content_template = 'mails/service_request/mail_content.html'

                send_html_mail(subject_template, content_template, to_email, render_message_context)

            elif mailing.type_of_mailing == settings.VACANCY_REQUEST_NAME_OF_MAILING_TYPES_CHOICES:
                render_message_context.update({
                    'vacancy_request': instance
                })
                subject_template = 'mails/vacancy_request/mail_subject.html'
                content_template = 'mails/vacancy_request/mail_content.html'

                send_html_mail(subject_template, content_template, to_email, render_message_context)

# К сожалению, сейчас уже ночь, и у меня нету времени наводить красоту, по этому не пугайтесь, что она выглядит так ужасно, она совсем не сложная.