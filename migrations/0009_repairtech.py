# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_coverperiod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairtechnician',
            name='company',
            field=models.ForeignKey(to='app.Company'),
        ),
    ]
