# Generated by Django 2.2.4 on 2019-08-13 04:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newconnection', '0027_auto_20190813_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porting',
            name='requested_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 13, 9, 38, 33, 864198)),
        ),
    ]
