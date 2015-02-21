# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_maint_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverperiod',
            name='contract',
            field=models.ForeignKey(to='app.MaintenanceContract'),
        ),
    ]
