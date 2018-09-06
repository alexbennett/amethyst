# Generated by Django 2.1 on 2018-09-05 15:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20180905_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 5, 15, 29, 51, 157359, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='projectdocument',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document', to='portfolio.Project'),
        ),
    ]
