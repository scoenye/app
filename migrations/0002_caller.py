# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caller',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='caller',
            name='location',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='caller',
            name='telephone',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
