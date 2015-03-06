# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_nonconsumable'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumableOnHand',
            fields=[
            ],
            options={
                'db_table': 'vw_consumable_onhand',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
