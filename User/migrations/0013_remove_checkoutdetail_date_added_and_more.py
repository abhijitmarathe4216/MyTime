# Generated by Django 4.1.7 on 2023-04-03 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_remove_review_datetime_review_date_added_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkoutdetail',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='ordermaster',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='review',
            name='date_added',
        ),
        migrations.AddField(
            model_name='checkoutdetail',
            name='orderdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 15, 44, 18, 780615)),
        ),
        migrations.AddField(
            model_name='ordermaster',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 15, 44, 18, 780615)),
        ),
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 15, 44, 18, 780615)),
        ),
    ]
