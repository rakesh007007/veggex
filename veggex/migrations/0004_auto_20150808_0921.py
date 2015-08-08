# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veggex', '0003_auto_20150808_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='timeOfUpdate',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
