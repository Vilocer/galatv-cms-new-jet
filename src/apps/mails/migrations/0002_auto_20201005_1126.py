# Generated by Django 3.1.2 on 2020-10-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingemail',
            name='mailings',
            field=models.ManyToManyField(blank=True, help_text='Рассылки, которые будут приходить на этой E-mail.', null=True, to='mails.RequestsMailing', verbose_name='Расслыки'),
        ),
    ]
