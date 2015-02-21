# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_hardware'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='version',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
