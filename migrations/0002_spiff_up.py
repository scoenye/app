# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.AlterModelOptions(
            name='hardware',
            options={'verbose_name_plural': 'hardware'},
        ),
        migrations.AlterModelOptions(
            name='repaircall',
            options={'verbose_name_plural': 'repair calls'},
        ),
        migrations.AlterModelOptions(
            name='software',
            options={'verbose_name_plural': 'software'},
        ),
        migrations.AlterModelOptions(
            name='workdone',
            options={'verbose_name_plural': 'work done'},
        ),
        migrations.AlterField(
            model_name='hardware',
            name='ip_address',
            field=models.IntegerField(null=True, verbose_name='IP address', blank=True),
        ),
    ]
