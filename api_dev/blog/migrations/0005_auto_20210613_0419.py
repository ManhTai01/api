# Generated by Django 3.1.12 on 2021-06-13 04:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210613_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 13, 4, 19, 36, 638507, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 13, 4, 19, 36, 638532, tzinfo=utc)),
        ),
    ]
