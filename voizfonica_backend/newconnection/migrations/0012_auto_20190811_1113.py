# Generated by Django 2.2.4 on 2019-08-11 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newconnection', '0011_auto_20190811_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porting',
            name='requested_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 11, 11, 13, 54, 365500)),
        ),
    ]