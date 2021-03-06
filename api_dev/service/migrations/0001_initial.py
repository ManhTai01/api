# Generated by Django 3.1.12 on 2021-06-13 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='1:1', upload_to='service')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'service',
                'ordering': ['-id'],
            },
        ),
    ]
