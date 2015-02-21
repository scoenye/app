# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_dispensed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpdeskcall',
            name='call_recorder',
            field=models.ForeignKey(related_name='helpdeskcall_recorder', to='app.Technician'),
        ),
        migrations.AlterField(
            model_name='helpdeskcall',
            name='caller',
            field=models.ForeignKey(to='app.Caller'),
        ),
        migrations.AlterField(
            model_name='helpdeskcall',
            name='closing_comment',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='helpdeskcall',
            name='problem_type',
            field=models.TextField(null=True, blank=True),
        ),
    ]
