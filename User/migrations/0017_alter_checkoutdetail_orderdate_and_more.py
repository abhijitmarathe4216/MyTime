# Generated by Django 4.1.7 on 2023-04-03 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0016_order_payment_method_alter_checkoutdetail_orderdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutdetail',
            name='orderdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 19, 58, 53, 865615)),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 19, 58, 53, 865615)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 19, 58, 53, 865615)),
        ),
    ]
