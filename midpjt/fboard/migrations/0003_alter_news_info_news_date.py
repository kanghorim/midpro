# Generated by Django 4.0.2 on 2022-03-03 07:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fboard', '0002_alter_news_info_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_info',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 16, 32, 47, 634301)),
        ),
    ]
