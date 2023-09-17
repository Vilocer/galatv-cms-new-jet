from .models import Mailing, MailingEmail
from django.contrib import admin


@admin.register(MailingEmail)
class MailingEmailAdmin(admin.ModelAdmin):
    fields = ['email']
    list_display = ['email']

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    fields = ['type_of_mailing', 'email_to_send']
    list_display = ['type_of_mailing', 'email_to_send']