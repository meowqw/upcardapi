# Generated by Django 4.1.7 on 2023-03-30 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Appearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, verbose_name='Наименование')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Дизайн',
                'verbose_name_plural': 'Дизайн карточек',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(blank=True, max_length=250, verbose_name='Наименование карточки')),
                ('name', models.CharField(blank=True, max_length=250, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=250, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=250, verbose_name='Отчество')),
                ('spec', models.CharField(blank=True, max_length=250, verbose_name='Специализация')),
                ('phone', models.CharField(blank=True, max_length=250, verbose_name='Телефон')),
                ('home_phone', models.CharField(blank=True, max_length=250, verbose_name='Домашний телефон')),
                ('personal_site', models.CharField(blank=True, max_length=250, verbose_name='Сайт')),
                ('email', models.CharField(blank=True, max_length=250, verbose_name='Почта')),
                ('dob', models.DateTimeField(auto_now_add=True, verbose_name='Дата рождения')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='Адрес')),
                ('qr', models.CharField(blank=True, max_length=250, verbose_name='QR')),
                ('personal_pic', models.ImageField(upload_to='media/')),
                ('logo_pic', models.ImageField(upload_to='media/')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('id_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('id_appearance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.appearance')),
            ],
            options={
                'verbose_name': 'Карточка',
                'verbose_name_plural': 'Карточки',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg', models.CharField(blank=True, max_length=250, null=True, verbose_name='tg')),
                ('vk', models.CharField(blank=True, max_length=250, null=True, verbose_name='vk')),
                ('instagram', models.CharField(blank=True, max_length=250, null=True, verbose_name='instagram')),
                ('whatsapp', models.CharField(blank=True, max_length=250, null=True, verbose_name='whatsapp')),
                ('gmail', models.CharField(blank=True, max_length=250, null=True, verbose_name='gmail')),
                ('facebook', models.CharField(blank=True, max_length=250, null=True, verbose_name='facebook')),
                ('yandex', models.CharField(blank=True, max_length=250, null=True, verbose_name='yandex')),
                ('odnoclassniki', models.CharField(blank=True, max_length=250, null=True, verbose_name='odnoclassniki')),
                ('skype', models.CharField(blank=True, max_length=250, null=True, verbose_name='skype')),
                ('youtube', models.CharField(blank=True, max_length=250, null=True, verbose_name='youtube')),
                ('github', models.CharField(blank=True, max_length=250, null=True, verbose_name='github')),
                ('beehance', models.CharField(blank=True, max_length=250, null=True, verbose_name='beehance')),
                ('tiktok', models.CharField(blank=True, max_length=250, null=True, verbose_name='tiktok')),
                ('linkedin', models.CharField(blank=True, max_length=250, null=True, verbose_name='linkedin')),
                ('twitter', models.CharField(blank=True, max_length=250, null=True, verbose_name='twitter')),
                ('viber', models.CharField(blank=True, max_length=250, null=True, verbose_name='viber')),
                ('twitch', models.CharField(blank=True, max_length=250, null=True, verbose_name='twitch')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Соц сеть',
                'verbose_name_plural': 'Соц сети',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, verbose_name='Почта')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('description', models.CharField(blank=True, max_length=250, null=True, verbose_name='Описание')),
                ('pic', models.ImageField(upload_to='media/')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('id_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.card')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
            },
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, verbose_name='Наименование')),
                ('activity', models.CharField(blank=True, max_length=250, verbose_name='Деятельность')),
                ('foundation', models.CharField(blank=True, max_length=250, verbose_name='Год основания')),
                ('clientage', models.CharField(blank=True, max_length=250, verbose_name='Клиенты')),
                ('phone', models.CharField(blank=True, max_length=250, verbose_name='Телефон')),
                ('work_phone', models.CharField(blank=True, max_length=250, verbose_name='Рабочий телефон')),
                ('company_site', models.CharField(blank=True, max_length=250, verbose_name='Сайт компании')),
                ('fax', models.CharField(blank=True, max_length=250, verbose_name='Факс')),
                ('email', models.CharField(blank=True, max_length=250, verbose_name='Почта')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='Адрес')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('id_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.appearance')),
                ('id_social', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.social')),
            ],
            options={
                'verbose_name': 'Инфо о компании',
                'verbose_name_plural': 'Инфо о компании',
            },
        ),
        migrations.AddField(
            model_name='card',
            name='id_social',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.social'),
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.card')),
            ],
            options={
                'verbose_name': 'Календарь',
                'verbose_name_plural': 'Календарь',
            },
        ),
    ]
