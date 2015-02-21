# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_helpdeskcall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemconsumable',
            name='item',
            field=models.ForeignKey(to='app.Consumable'),
        ),
    ]
