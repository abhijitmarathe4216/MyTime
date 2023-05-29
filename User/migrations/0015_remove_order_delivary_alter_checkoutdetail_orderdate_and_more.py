# Generated by Django 4.1.7 on 2023-04-03 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_alter_checkoutdetail_orderdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivary',
        ),
        migrations.AlterField(
            model_name='checkoutdetail',
            name='orderdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 19, 6, 7, 168372)),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 19, 6, 7, 168372)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 19, 6, 7, 168372)),
        ),
    ]