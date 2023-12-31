# Generated by Django 3.0.10 on 2020-10-20 21:02

from django.db import migrations, models
import fontawesome_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_introlinkpluginmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introlinkpluginmodel',
            name='icon',
            field=fontawesome_5.fields.IconField(blank=True, max_length=60, null=True, verbose_name='Своя иконка для кнопки, если есть'),
        ),
        migrations.AlterField(
            model_name='introlinkpluginmodel',
            name='link_url',
            field=models.URLField(blank=True, help_text='Если кнопка открывает модальное окно, то поле можно оставить пустым', null=True, verbose_name='Куда введет кнопка'),
        ),
    ]
