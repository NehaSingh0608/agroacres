# Generated by Django 3.1.4 on 2021-06-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20210611_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='total_amt',
            field=models.IntegerField(default=0.0),
        ),
    ]
