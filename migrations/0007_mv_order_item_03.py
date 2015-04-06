# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_mv_order_item_02'),
    ]

    operations = [
        migrations.RunSQL(
            "update hardware set order_item_id = support_item.order_item_x_id from support_item where hardware.supportitem_ptr_id = support_item.id;",
            "update support_item set order_item_x_id = hardware.order_item_id from hardware where hardware.supportitem_ptr_id = support_item.id;"
        ),
        migrations.RunSQL(
            "update software set order_item_id = support_item.order_item_x_id from support_item where software.supportitem_ptr_id = support_item.id;",
            "update support_item set order_item_x_id = software.order_item_id from software where software.supportitem_ptr_id = support_item.id;"
        ),
    ]
