# Generated by Django 4.1.7 on 2023-04-04 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_companyinfo_logo_img_alter_card_logo_img_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social',
            name='odnoclassniki',
        ),
        migrations.AddField(
            model_name='social',
            name='odnoklassniki',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='odnoklassniki'),
        ),
    ]