# Generated by Django 3.1.12 on 2021-06-13 04:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 13, 4, 19, 36, 639635, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='job',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 13, 4, 19, 36, 639657, tzinfo=utc)),
        ),
    ]
