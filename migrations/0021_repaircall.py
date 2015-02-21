# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_orderitem_cons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repaircall',
            name='call_reference',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='repaircall',
            name='close_comment',
            field=models.TextField(null=True, blank=True),
        ),
    ]
