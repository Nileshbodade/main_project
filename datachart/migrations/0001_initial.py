# Generated by Django 2.2.5 on 2019-09-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_name', models.CharField(max_length=20)),
                ('parameter_value', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField()),
                ('time', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
