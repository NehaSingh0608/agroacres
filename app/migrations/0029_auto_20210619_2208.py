# Generated by Django 3.2 on 2021-06-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20210619_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('O', 'Others'), ('F', 'Female'), ('M', 'Male')], default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='seed',
            name='price',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='seed',
            name='qty',
            field=models.CharField(default='', max_length=50),
        ),
    ]
