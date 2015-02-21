# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_orderitem_mat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportitem',
            name='comment',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='supportitem',
            name='order_item',
            field=models.ForeignKey(default=-1, to='app.OrderItemMaterial'),
        ),
        migrations.AlterField(
            model_name='supportitem',
            name='producer',
            field=models.ForeignKey(default=-1, to='app.Company'),
        ),
    ]
