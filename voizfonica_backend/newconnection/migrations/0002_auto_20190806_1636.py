# Generated by Django 2.2.4 on 2019-08-06 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newconnection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portin',
            name='requested_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 6, 16, 36, 7, 550067)),
        ),
    ]