# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veggex', '0004_auto_20150808_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cart_id',
            new_name='order_id',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='priceAtThatTime',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='priceType',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='unit',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_mode',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'PLACED', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
