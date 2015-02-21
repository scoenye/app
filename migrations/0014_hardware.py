# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_supportitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='hostname',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='idms_name',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='part_no',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
