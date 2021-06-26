# Generated by Django 3.2 on 2021-06-19 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profile'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('O', 'Others'), ('F', 'Female'), ('M', 'Male')], default='', max_length=6),
        ),
    ]