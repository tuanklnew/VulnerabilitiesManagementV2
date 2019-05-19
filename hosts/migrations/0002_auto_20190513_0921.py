# Generated by Django 2.2.1 on 2019-05-13 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osmodel',
            name='releaseDate',
            field=models.DateField(blank=True, verbose_name='Released Date of OS'),
        ),
        migrations.AlterField(
            model_name='osmodel',
            name='version',
            field=models.CharField(blank=True, max_length=32, verbose_name='Version Of OS'),
        ),
    ]