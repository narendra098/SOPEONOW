# Generated by Django 4.1.2 on 2023-06-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='received_order',
            name='order_type',
            field=models.CharField(max_length=15),
        ),
    ]