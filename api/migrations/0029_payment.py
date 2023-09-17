# Generated by Django 4.1.7 on 2023-08-30 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_rename_usersubsctibe_usersubscribe_remove_card_dob_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=288)),
                ('status', models.CharField(choices=[('NEW', 'Новый платеж'), ('CONFIRMED', 'Платеж подтвержден'), ('CANCELED', 'Платеж отменен'), ('FAIL', 'Ошибка')], max_length=20)),
                ('payment_url', models.CharField(max_length=288)),
                ('amount', models.FloatField()),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Оплаты',
                'verbose_name_plural': 'Оплаты',
            },
        ),
    ]