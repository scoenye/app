# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 05:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_supportitem_inventoried'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='department',
            new_name='work_department',
        ),
    ]