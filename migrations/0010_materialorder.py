# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_repairtech'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materialorder',
            old_name='order',
            new_name='order_no',
        ),
        migrations.AlterField(
            model_name='materialorder',
            name='comment',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='materialorder',
            name='description',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='materialorder',
            name='private_comment',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='materialorder',
            name='supplier_ref',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
