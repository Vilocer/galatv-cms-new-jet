from django.db import models
from django.conf import settings


class MailingEmail(models.Model):
    """ Модель адресса E-mail, для рассылок """

    email = models.EmailField('E-mail для рассылок',
        help_text='E-mail для которого можно установить рассылку, например: my@mail.com или info@galatv.ru'
    )

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = 'Почтовый адрес, для рассылки'
        verbose_name_plural = 'Почтовые адреса, для рассылки'

class Mailing(models.Model):
    """ Модель рассылки """

    type_of_mailing = models.CharField('Тип рассылки',
        max_length=250,
        help_text='Выберите, когда будет происходить рассылка',
        choices=settings.MAILINGS_TYPES_CHOICES
    )

    email_to_send = models.ForeignKey(MailingEmail,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='E-mail, для рассылки',
        help_text='E-mail, на который будет приходить рассылка'
    )

    def __str__(self):
        return str(self.type_of_mailing)

    class Meta:
        verbose_name = 'E-mail Рассылка'
        verbose_name_plural = 'E-mail Рассылки'
