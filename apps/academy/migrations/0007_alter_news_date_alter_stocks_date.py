# Generated by Django 4.2.3 on 2023-07-12 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0006_stocks_alter_news_date_stocksimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 12, 16, 25, 24, 41730, tzinfo=datetime.timezone.utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 12, 16, 25, 24, 42953, tzinfo=datetime.timezone.utc), verbose_name='Date'),
        ),
    ]