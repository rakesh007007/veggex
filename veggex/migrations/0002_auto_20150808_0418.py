# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veggex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='mobileNo',
            field=models.BigIntegerField(),
        ),
    ]
