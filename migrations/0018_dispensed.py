# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_placement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispensed',
            name='consumer',
            field=models.ForeignKey(to='app.Hardware'),
        ),
        migrations.AlterField(
            model_name='dispensed',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
