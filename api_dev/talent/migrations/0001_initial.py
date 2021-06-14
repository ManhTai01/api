# Generated by Django 3.1.12 on 2021-06-13 04:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dateOfBirth', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=12)),
                ('regency', models.CharField(max_length=250)),
                ('avt', models.ImageField(help_text='1:1', upload_to='talent')),
            ],
            options={
                'db_table': 'talent',
                'ordering': ['-id'],
            },
        ),
    ]
