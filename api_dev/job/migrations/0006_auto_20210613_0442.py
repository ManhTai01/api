# Generated by Django 3.1.12 on 2021-06-13 04:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20210613_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 13, 4, 42, 19, 340263, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='job',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 13, 4, 42, 19, 340285, tzinfo=utc)),
        ),
    ]
