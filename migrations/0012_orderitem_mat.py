# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemmaterial',
            name='item_type',
            field=models.ForeignKey(to='app.ItemType'),
        ),
    ]
