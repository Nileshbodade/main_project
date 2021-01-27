# Generated by Django 2.2.5 on 2019-10-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datachart', '0005_auto_20191011_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='Speed',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='Temperature',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='Voltage',
            field=models.FloatField(default=0),
        ),
    ]