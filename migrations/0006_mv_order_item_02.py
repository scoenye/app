# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_mv_order_item_01'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardware',
            name='order_item',
            field=models.ForeignKey(default=-1, to='app.OrderItemMaterial'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='software',
            name='order_item',
            field=models.ForeignKey(default=-1, to='app.OrderItemMaterial'),
            preserve_default=True,
        ),
    ]
