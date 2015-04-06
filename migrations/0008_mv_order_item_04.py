# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_mv_order_item_03'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supportitem',
            name='order_item_x',
        ),
    ]
