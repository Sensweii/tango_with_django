# Generated by Django 2.1.5 on 2019-06-24 07:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20190620_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='first_visit',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 24, 7, 13, 30, 100894, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='last_visit',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 24, 7, 13, 41, 200623, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
