# Generated by Django 3.1.3 on 2020-11-24 20:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201118_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date_added'),
            preserve_default=False,
        ),
    ]
