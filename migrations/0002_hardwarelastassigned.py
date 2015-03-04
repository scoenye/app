# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HardwareLastAssigned',
            fields=[
            ],
            options={
                'db_table': 'vw_last_assigned_dept',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
