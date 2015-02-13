# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=15, blank=True)),
                ('active', models.NullBooleanField()),
                ('location', models.CharField(max_length=30, blank=True)),
            ],
            options={
                'db_table': 'caller',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=40, blank=True)),
                ('city', models.CharField(max_length=20, blank=True)),
                ('telephone', models.CharField(max_length=15, blank=True)),
                ('postcode', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'db_table': 'company',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('contract', models.IntegerField(null=True, blank=True)),
                ('description', models.CharField(max_length=30)),
                ('item_type', models.IntegerField()),
                ('order_item', models.IntegerField(null=True, blank=True)),
                ('comment', models.TextField(blank=True)),
                ('part_no', models.CharField(max_length=20, blank=True)),
                ('producer', models.ForeignKey(db_column='producer', blank=True, to='app.Company', null=True)),
            ],
            options={
                'db_table': 'consumable',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConsumableItemType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'consumable_item_type',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=40, blank=True)),
                ('city', models.CharField(max_length=20, blank=True)),
                ('telephone', models.CharField(max_length=15, blank=True)),
                ('postcode', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'db_table': 'contractor',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoverPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weekday', models.IntegerField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
                'db_table': 'cover_period',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=15, blank=True)),
                ('active', models.NullBooleanField()),
                ('location', models.CharField(max_length=30, blank=True)),
                ('end_of_life', models.NullBooleanField()),
            ],
            options={
                'db_table': 'department',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dispensed',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('item', models.IntegerField(null=True, blank=True)),
                ('place_date', models.DateTimeField()),
                ('department', models.IntegerField(null=True, blank=True)),
                ('location', models.CharField(max_length=50, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'dispensed',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=15, blank=True)),
                ('active', models.NullBooleanField()),
                ('location', models.CharField(max_length=30, blank=True)),
                ('first_name', models.CharField(max_length=20)),
                ('department', models.ForeignKey(db_column='department', blank=True, to='app.Department', null=True)),
            ],
            options={
                'db_table': 'employee',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('contract', models.IntegerField(null=True, blank=True)),
                ('description', models.CharField(max_length=30)),
                ('producer', models.IntegerField(null=True, blank=True)),
                ('item_type', models.IntegerField()),
                ('order_item', models.IntegerField(null=True, blank=True)),
                ('comment', models.TextField(blank=True)),
                ('part_no', models.CharField(max_length=20, blank=True)),
                ('hostname', models.CharField(max_length=20, blank=True)),
                ('idms_name', models.CharField(max_length=8, blank=True)),
                ('ip_address', models.IntegerField(null=True, blank=True)),
                ('tag', models.IntegerField(unique=True, null=True, blank=True)),
            ],
            options={
                'db_table': 'hardware',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HardwareItemType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('consumer', models.NullBooleanField()),
            ],
            options={
                'db_table': 'hardware_item_type',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HelpdeskCall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('call_time', models.DateTimeField()),
                ('problem_type', models.TextField(blank=True)),
                ('closing_time', models.DateTimeField(null=True, blank=True)),
                ('closing_comment', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'helpdesk_call',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'item_type',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MaintenanceContract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=4)),
                ('description', models.CharField(max_length=35, blank=True)),
                ('contractor', models.ForeignKey(db_column='contractor', blank=True, to='app.Contractor', null=True)),
            ],
            options={
                'db_table': 'maintenance_contract',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MaterialOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(max_length=15)),
                ('order_date', models.DateField()),
                ('to_exec_committee', models.DateField(null=True, blank=True)),
                ('to_supply_dept', models.DateField(null=True, blank=True)),
                ('description', models.CharField(max_length=80, blank=True)),
                ('comment', models.TextField(blank=True)),
                ('private_comment', models.TextField(blank=True)),
                ('supplier_ref', models.CharField(max_length=20, blank=True)),
                ('supplier', models.ForeignKey(to='app.Company', db_column='supplier')),
            ],
            options={
                'db_table': 'material_order',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mat_order', models.IntegerField(null=True, blank=True)),
                ('completed', models.DateField(null=True, blank=True)),
                ('department', models.IntegerField(null=True, blank=True)),
                ('description', models.CharField(max_length=20, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'order_item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItemConsumable',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('mat_order', models.IntegerField(null=True, blank=True)),
                ('completed', models.DateField(null=True, blank=True)),
                ('department', models.IntegerField(null=True, blank=True)),
                ('description', models.CharField(max_length=20, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('item', models.ForeignKey(db_column='item', blank=True, to='app.Consumable', null=True)),
            ],
            options={
                'db_table': 'order_item_consumable',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItemMaterial',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('completed', models.DateField(null=True, blank=True)),
                ('description', models.CharField(max_length=20, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('discount', models.FloatField(null=True, blank=True)),
                ('tax', models.FloatField(null=True, blank=True)),
                ('price_per_unit', models.FloatField(null=True, blank=True)),
                ('item_type', models.IntegerField(null=True, blank=True)),
                ('department', models.ForeignKey(db_column='department', blank=True, to='app.Department', null=True)),
                ('mat_order', models.ForeignKey(db_column='mat_order', blank=True, to='app.MaterialOrder', null=True)),
            ],
            options={
                'db_table': 'order_item_material',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=15, blank=True)),
                ('active', models.NullBooleanField()),
                ('location', models.CharField(max_length=30, blank=True)),
                ('first_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'person',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.IntegerField(null=True, blank=True)),
                ('place_date', models.DateTimeField()),
                ('location', models.CharField(max_length=50, blank=True)),
                ('department', models.ForeignKey(db_column='department', blank=True, to='app.Department', null=True)),
            ],
            options={
                'db_table': 'placement',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Repaircall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('call_time', models.DateTimeField()),
                ('close_time', models.DateTimeField(null=True, blank=True)),
                ('call_problem', models.TextField()),
                ('call_reference', models.CharField(max_length=10, blank=True)),
                ('close_comment', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'repaircall',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RepairTechnician',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=15, blank=True)),
                ('active', models.NullBooleanField()),
                ('location', models.CharField(max_length=30, blank=True)),
                ('first_name', models.CharField(max_length=20)),
                ('company', models.ForeignKey(db_column='company', blank=True, to='app.Company', null=True)),
            ],
            options={
                'db_table': 'repair_technician',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SerialNo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.IntegerField(null=True, blank=True)),
                ('serial_no', models.CharField(max_length=30)),
                ('assign_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'serial_no',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('contract', models.IntegerField(null=True, blank=True)),
                ('description', models.CharField(max_length=30)),
                ('producer', models.IntegerField(null=True, blank=True)),
                ('item_type', models.IntegerField()),
                ('order_item', models.IntegerField(null=True, blank=True)),
                ('comment', models.TextField(blank=True)),
                ('version', models.CharField(max_length=15, blank=True)),
            ],
            options={
                'db_table': 'software',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SoftwareItemType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'software_item_type',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SupportItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=30)),
                ('comment', models.TextField(blank=True)),
                ('contract', models.ForeignKey(db_column='contract', blank=True, to='app.MaintenanceContract', null=True)),
                ('item_type', models.ForeignKey(to='app.ItemType', db_column='item_type')),
                ('order_item', models.ForeignKey(db_column='order_item', blank=True, to='app.OrderItemMaterial', null=True)),
                ('producer', models.ForeignKey(db_column='producer', blank=True, to='app.Company', null=True)),
            ],
            options={
                'db_table': 'support_item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=15, blank=True)),
                ('active', models.NullBooleanField()),
                ('location', models.CharField(max_length=30, blank=True)),
                ('first_name', models.CharField(max_length=20)),
                ('department', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'technician',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'weekday',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkDone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('call', models.ForeignKey(to='app.HelpdeskCall', db_column='call')),
                ('technician', models.ForeignKey(to='app.Technician', db_column='technician')),
            ],
            options={
                'db_table': 'work_done',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='repaircall',
            name='call_tech',
            field=models.ForeignKey(related_name='repaircall_caller', db_column='call_tech', to='app.Technician'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='repaircall',
            name='close_tech',
            field=models.ForeignKey(related_name='repaircall_closer', db_column='close_tech', blank=True, to='app.Technician', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='repaircall',
            name='helpdeskcall',
            field=models.ForeignKey(to='app.HelpdeskCall', db_column='helpdeskcall'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='repaircall',
            name='repair_tech',
            field=models.ForeignKey(db_column='repair_tech', blank=True, to='app.RepairTechnician', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpdeskcall',
            name='assigned_tech',
            field=models.ForeignKey(related_name='helpdeskcall_assignee', db_column='assigned_tech', blank=True, to='app.Technician', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpdeskcall',
            name='call_recorder',
            field=models.ForeignKey(related_name='helpdeskcall_recorder', db_column='call_recorder', blank=True, to='app.Technician', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpdeskcall',
            name='caller',
            field=models.ForeignKey(db_column='caller', blank=True, to='app.Caller', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpdeskcall',
            name='closing_tech',
            field=models.ForeignKey(related_name='helpdeskcall_closer', db_column='closing_tech', blank=True, to='app.Technician', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpdeskcall',
            name='item',
            field=models.ForeignKey(to='app.SupportItem', db_column='item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispensed',
            name='consumer',
            field=models.ForeignKey(db_column='consumer', blank=True, to='app.Hardware', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coverperiod',
            name='contract',
            field=models.ForeignKey(db_column='contract', blank=True, to='app.MaintenanceContract', null=True),
            preserve_default=True,
        ),
    ]
