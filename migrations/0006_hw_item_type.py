# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardwareitemtype',
            name='consumer',
            field=models.BooleanField(default=False),
        ),
    ]
