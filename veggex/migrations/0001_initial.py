# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(serialize=False, primary_key=True)),
                ('area', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('nameOfInstitution', models.CharField(max_length=300)),
                ('nameOfOwner', models.CharField(max_length=300)),
                ('institutionType', models.CharField(max_length=300, choices=[(b'hotels', b'hotels'), (b'juice vendors', b'juice vendors'), (b'veg. vendors', b'veg. vendors'), (b'other buyers', b'other buyers')])),
                ('mailId', models.CharField(max_length=300)),
                ('mobileNo', models.IntegerField()),
                ('password', models.CharField(max_length=300)),
                ('gpsLocation', models.CharField(max_length=300, null=True, blank=True)),
                ('address', models.ForeignKey(blank=True, to='veggex.Address', null=True)),
            ],
        ),
    ]
