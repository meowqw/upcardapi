# Generated by Django 4.2.1 on 2023-08-30 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_alter_payment_account_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscribe',
            name='payment_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.payment'),
        ),
        migrations.AddField(
            model_name='usersubscribe',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
