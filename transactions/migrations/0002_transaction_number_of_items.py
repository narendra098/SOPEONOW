# Generated by Django 4.1.2 on 2023-06-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='number_of_items',
            field=models.IntegerField(default=1),
        ),
    ]