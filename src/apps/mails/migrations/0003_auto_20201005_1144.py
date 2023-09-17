# Generated by Django 3.1.2 on 2020-10-05 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0002_auto_20201005_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_mailing', models.CharField(choices=[('ConnectRequest', 'Заявки на подключение интернета'), ('ServiceRequest', 'Заявки на оказание услуг'), ('VacancyRequest', 'Заявки на вакансии')], help_text='Выберите, когда будет происходить рвссылка', max_length=250, verbose_name='Тип рассылки')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.RemoveField(
            model_name='mailingemail',
            name='mailings',
        ),
        migrations.DeleteModel(
            name='RequestsMailing',
        ),
        migrations.AddField(
            model_name='mailingemail',
            name='mailing',
            field=models.ForeignKey(blank=True, help_text='Выберите, для какой рассылки будет ипользоваться этот E-mail', null=True, on_delete=django.db.models.deletion.CASCADE, to='mails.mailing', verbose_name='Рассылка'),
        ),
    ]
