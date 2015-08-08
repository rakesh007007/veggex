# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veggex', '0005_auto_20150808_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timeOfCreate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='timeOfUpdate',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
