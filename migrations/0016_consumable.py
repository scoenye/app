# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_software'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumable',
            name='part_no',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
