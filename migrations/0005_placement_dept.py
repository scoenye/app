# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_consumableonhand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='department',
            field=models.ForeignKey(default=-1, to='app.Department'),
        ),
    ]
