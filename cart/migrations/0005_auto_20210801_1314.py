# Generated by Django 2.2 on 2021-08-01 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20091221_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartlist'),
        ),
    ]
