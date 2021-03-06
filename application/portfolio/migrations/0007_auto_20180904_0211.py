# Generated by Django 2.1 on 2018-09-04 02:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20180903_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=100)),
                ('organization_url', models.CharField(max_length=200)),
                ('when', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Honor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=100)),
                ('organization_url', models.CharField(max_length=200)),
                ('when', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='skills',
        ),
        migrations.AddField(
            model_name='skill',
            name='related_projects',
            field=models.ManyToManyField(blank=True, to='portfolio.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 4, 2, 11, 2, 178390, tzinfo=utc)),
        ),
    ]
