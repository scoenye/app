# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_placement_dept'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supportitem',
            old_name='order_item',
            new_name='order_item_x',
        ),
    ]
