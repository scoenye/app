# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_mv_order_item_04'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportitem',
            name='inventoried',
            field=models.DateField(null=True, blank=True),
        ),
    ]
