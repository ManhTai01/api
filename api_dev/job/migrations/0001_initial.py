# Generated by Django 3.1.12 on 2021-06-13 04:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('location', models.CharField(help_text='Company location', max_length=255)),
                ('vacancies', models.IntegerField(default=1)),
                ('content', models.TextField(blank=True, help_text='Job introductions')),
                ('image', models.ImageField(help_text='Image logo company', upload_to='jobDescription/')),
                ('urgent', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(default=datetime.datetime(2021, 6, 13, 4, 19, 29, 897789, tzinfo=utc))),
                ('update_at', models.DateTimeField(default=datetime.datetime(2021, 6, 13, 4, 19, 29, 897813, tzinfo=utc))),
            ],
            options={
                'db_table': 'job',
                'ordering': ['-id'],
            },
        ),
    ]
