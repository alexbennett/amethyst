# Generated by Django 2.1 on 2018-08-29 08:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('abstract', models.TextField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 29, 8, 14, 58, 684147, tzinfo=utc))),
            ],
        ),
    ]
