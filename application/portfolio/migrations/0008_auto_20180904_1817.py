# Generated by Django 2.1 on 2018-09-04 18:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20180904_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('started', models.DateField()),
                ('ended', models.DateField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'activities'},
        ),
        migrations.AlterModelOptions(
            name='skillcategory',
            options={'verbose_name_plural': 'skill categories'},
        ),
        migrations.RemoveField(
            model_name='honor',
            name='organization_url',
        ),
        migrations.AlterField(
            model_name='activity',
            name='organization_url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 4, 18, 17, 51, 65227, tzinfo=utc)),
        ),
    ]