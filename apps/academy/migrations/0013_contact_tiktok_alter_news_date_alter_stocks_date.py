# Generated by Django 4.2.3 on 2023-07-14 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0012_alter_news_date_alter_stocks_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='tiktok',
            field=models.URLField(default=1, max_length=255, verbose_name='TikTok'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 14, 14, 10, 42, 580039, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 14, 14, 10, 42, 582035, tzinfo=datetime.timezone.utc), verbose_name='Дата'),
        ),
    ]
