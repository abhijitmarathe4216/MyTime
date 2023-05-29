# Generated by Django 4.1.7 on 2023-04-04 15:54

import User.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0026_rename_username_userinfo_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(default=User.models.next_day_dt),
        ),
        migrations.AlterField(
            model_name='checkoutdetail',
            name='orderdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 4, 21, 24, 54, 567072)),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 4, 21, 24, 54, 567072)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 4, 21, 24, 54, 567072)),
        ),
    ]