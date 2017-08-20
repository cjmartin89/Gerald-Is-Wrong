# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 18:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20170819_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotes',
            name='Subject',
        ),
        migrations.AddField(
            model_name='quotes',
            name='Person',
            field=models.CharField(default='Ralph', max_length=999, verbose_name='Who said it?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quotes',
            name='DateTime',
            field=models.DateField(default=datetime.datetime(2017, 8, 19, 18, 6, 56, 514532, tzinfo=utc), verbose_name='Date: '),
        ),
    ]