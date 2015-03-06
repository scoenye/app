# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_hardwarelastassigned'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonConsumable',
            fields=[
            ],
            options={
                'db_table': 'vw_nonconsumables',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        # Do not try to add a FK constraint pointing at a view...
        migrations.RunSQL(
            "select 1;",
            "select 1;",
            state_operations = [
                migrations.AlterField(
                    model_name='helpdeskcall',
                    name='item',
                    field=models.ForeignKey(to='app.NonConsumable'),
                ),
            ]
        )
    ]
