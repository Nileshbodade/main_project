# Generated by Django 3.0.2 on 2020-05-02 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datachart', '0007_auto_20191016_0033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parameter',
            old_name='timestamp',
            new_name='Current_timestamp',
        ),
    ]
