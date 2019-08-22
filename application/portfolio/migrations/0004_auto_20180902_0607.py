# Generated by Django 2.1 on 2018-09-02 06:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20180902_0603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subskill',
            old_name='skills',
            new_name='parent_skill',
        ),
        migrations.RemoveField(
            model_name='subskill',
            name='skill',
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 2, 6, 7, 2, 28615, tzinfo=utc)),
        ),
    ]