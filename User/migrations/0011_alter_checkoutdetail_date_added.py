# Generated by Django 4.1.7 on 2023-04-03 07:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_remove_ordermaster_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutdetail',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
