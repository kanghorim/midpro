# Generated by Django 4.0.2 on 2022-03-03 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='reg_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 16, 18, 38, 333855)),
        ),
    ]