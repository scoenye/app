# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_repaircall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumableitemtype',
            name='name',
        ),
        migrations.RemoveField(
            model_name='hardwareitemtype',
            name='name',
        ),
        migrations.RemoveField(
            model_name='softwareitemtype',
            name='name',
        ),
    ]
