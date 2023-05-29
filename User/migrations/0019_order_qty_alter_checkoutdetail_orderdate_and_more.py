# Generated by Django 4.1.7 on 2023-04-03 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0018_alter_checkoutdetail_orderdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='qty',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='checkoutdetail',
            name='orderdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 21, 28, 1, 351810)),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 21, 28, 1, 351810)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 21, 28, 1, 351810)),
        ),
    ]
