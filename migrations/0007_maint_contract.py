# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_hw_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancecontract',
            name='contractor',
            field=models.ForeignKey(to='app.Contractor'),
        ),
        migrations.AlterField(
            model_name='maintenancecontract',
            name='description',
            field=models.CharField(max_length=35, null=True, blank=True),
        ),
    ]
