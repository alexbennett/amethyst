# Generated by Django 2.1 on 2018-09-04 19:00

import ckeditor.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20180904_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 4, 19, 0, 38, 845409, tzinfo=utc)),
        ),
    ]
