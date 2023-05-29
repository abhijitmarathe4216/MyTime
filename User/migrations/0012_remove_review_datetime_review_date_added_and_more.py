# Generated by Django 4.1.7 on 2023-04-03 07:52

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_alter_checkoutdetail_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='datetime',
        ),
        migrations.AddField(
            model_name='review',
            name='date_added',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='checkoutdetail',
            name='date_added',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivary',
            field=models.DateTimeField(verbose_name=datetime.timedelta(days=5)),
        ),
    ]
