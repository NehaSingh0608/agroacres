# Generated by Django 3.2 on 2021-05-31 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210531_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='seed',
            name='price',
            field=models.FloatField(default=25.0),
        ),
    ]