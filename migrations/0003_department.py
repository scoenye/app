# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_caller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='end_of_life',
            field=models.BooleanField(default=False),
        ),
    ]
