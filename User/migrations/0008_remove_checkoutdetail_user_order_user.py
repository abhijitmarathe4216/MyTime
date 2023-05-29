# Generated by Django 4.1.7 on 2023-04-02 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_alter_order_delivary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkoutdetail',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.userinfo'),
        ),
    ]