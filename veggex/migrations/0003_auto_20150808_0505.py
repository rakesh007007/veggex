# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veggex', '0002_auto_20150808_0418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(serialize=False, primary_key=True)),
                ('timeOfCreate', models.DateTimeField(auto_now_add=True)),
                ('timeOfUpdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Cartitem',
            fields=[
                ('cartitem_id', models.AutoField(serialize=False, primary_key=True)),
                ('unit', models.CharField(default=b'kg', max_length=100)),
                ('qtyInUnits', models.IntegerField()),
                ('priceType', models.CharField(max_length=200, choices=[(b'as per mandi rates', b'as per mandi rates'), (b'custom rates', b'custom rates')])),
                ('priceAtThatTime', models.IntegerField()),
                ('cart', models.ForeignKey(to='veggex.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('cart_id', models.AutoField(serialize=False, primary_key=True)),
                ('timeOfCreate', models.DateTimeField(auto_now_add=True)),
                ('timeOfUpdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('orderitem_id', models.AutoField(serialize=False, primary_key=True)),
                ('unit', models.CharField(default=b'kg', max_length=100)),
                ('qtyInUnits', models.IntegerField()),
                ('priceType', models.CharField(max_length=200, choices=[(b'as per mandi rates', b'as per mandi rates'), (b'custom rates', b'custom rates')])),
                ('priceAtThatTime', models.IntegerField()),
                ('order', models.ForeignKey(to='veggex.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(null=True, blank=True)),
                ('popularityIndex', models.IntegerField(null=True, blank=True)),
                ('unit', models.CharField(default=b'kg', max_length=100)),
                ('priceType', models.CharField(max_length=300, choices=[(b'as per mandi rates', b'as per mandi rates'), (b'custom rates', b'custom rates')])),
                ('pricePerUnit', models.IntegerField()),
                ('coverphoto', models.ImageField(upload_to=b'')),
                ('origin', models.CharField(max_length=300)),
                ('maxAvailableUnits', models.IntegerField()),
                ('qualityRemarks', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='coverphoto',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profilePhoto',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='veggex.Category'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(to='veggex.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='veggex.User'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(to='veggex.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='veggex.User'),
        ),
    ]
