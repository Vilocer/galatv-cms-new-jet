# Generated by Django 3.0.10 on 2020-10-17 17:56

from django.db import migrations, models
import django.db.models.deletion
import fontawesome_5.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterSocialLinkModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='base_footersociallinkmodel', serialize=False, to='cms.CMSPlugin')),
                ('icon', fontawesome_5.fields.IconField(blank=True, help_text='Специальная иконка для соц. сети', max_length=60, verbose_name='Икона Font-Awesome')),
                ('link_url', models.URLField(verbose_name='Ссыллка на соц. сеть')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SearchPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='base_searchpluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('indexing_pages', multiselectfield.db.fields.MultiSelectField(choices=[('rates', 'Тарифы'), ('services', 'Услуги'), ('news', 'Новости'), ('vacancies', 'Вакансии'), ('gallery', 'Галерея')], help_text='Разделы, по которым будет проводится поиск', max_length=37, verbose_name='Где искать')),
                ('search_page', models.ForeignKey(help_text='В нее будет приходить GET запрос с параметром "q". ', on_delete=django.db.models.deletion.CASCADE, to='cms.Page', verbose_name='Поисковая страница')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
