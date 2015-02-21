# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_consumable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='department',
            field=models.ForeignKey(to='app.Department'),
        ),
        migrations.AlterField(
            model_name='placement',
            name='location',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
