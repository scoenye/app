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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_no', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'db_table': 'consumable',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConsumableItemType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.OneToOneField(to='app.Company')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('end_of_life', models.NullBooleanField()),
                ('caller', models.OneToOneField(to='app.Caller')),
            ],
            options={
                'db_table': 'department',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dispensed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.ForeignKey(blank=True, to='app.Department', null=True)),
            ],
            options={
                'db_table': 'employee',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('contractor', models.ForeignKey(blank=True, to='app.Contractor', null=True)),
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
                ('order', models.CharField(max_length=15)),
                ('order_date', models.DateField()),
                ('to_exec_committee', models.DateField(null=True, blank=True)),
                ('to_supply_dept', models.DateField(null=True, blank=True)),
                ('description', models.CharField(max_length=80, blank=True)),
                ('comment', models.TextField(blank=True)),
                ('private_comment', models.TextField(blank=True)),
                ('supplier_ref', models.CharField(max_length=20, blank=True)),
                ('supplier', models.ForeignKey(to='app.Company')),
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
                ('completed', models.DateField(null=True, blank=True)),
                ('description', models.CharField(max_length=20, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('department', models.ForeignKey(to='app.Department')),
                ('mat_order', models.ForeignKey(to='app.MaterialOrder')),
            ],
            options={
                'db_table': 'order_item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItemConsumable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(blank=True, to='app.Consumable', null=True)),
                ('order_item', models.OneToOneField(to='app.OrderItem')),
            ],
            options={
                'db_table': 'order_item_consumable',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItemMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('discount', models.FloatField(null=True, blank=True)),
                ('tax', models.FloatField(null=True, blank=True)),
                ('price_per_unit', models.FloatField(null=True, blank=True)),
                ('item_type', models.IntegerField(null=True, blank=True)),
                ('order_item', models.OneToOneField(to='app.OrderItem')),
            ],
            options={
                'db_table': 'order_item_material',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('caller', models.OneToOneField(to='app.Caller')),
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
                ('place_date', models.DateTimeField()),
                ('location', models.CharField(max_length=50, blank=True)),
                ('department', models.ForeignKey(blank=True, to='app.Department', null=True)),
            ],
            options={
                'db_table': 'placement',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RepairCall',
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.ForeignKey(blank=True, to='app.Company', null=True)),
                ('person', models.OneToOneField(to='app.Person')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('item_type', models.OneToOneField(to='app.ItemType')),
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
                ('contract', models.ForeignKey(blank=True, to='app.MaintenanceContract', null=True)),
                ('item_type', models.ForeignKey(to='app.ItemType')),
                ('order_item', models.ForeignKey(blank=True, to='app.OrderItemMaterial', null=True)),
                ('producer', models.ForeignKey(blank=True, to='app.Company', null=True)),
            ],
            options={
                'db_table': 'support_item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee', models.OneToOneField(to='app.Employee')),
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
                ('call', models.ForeignKey(to='app.HelpdeskCall')),
                ('technician', models.ForeignKey(to='app.Technician')),
            ],
            options={
                'db_table': 'work_done',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='software',
            name='support_item',
            field=models.OneToOneField(to='app.SupportItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='serialno',
            name='support_item',
            field=models.ForeignKey(to='app.SupportItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='repaircall',
            name='call_tech',
            field=models.ForeignKey(related_name='repaircall_caller', to='app.Technician'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='repaircall',
            name='close_tech',
            field=models.ForeignKey(related_name='repaircall_closer', blank=True, to='app.Technician', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='repaircall',
            name='helpdeskcall',
            field=models.ForeignKey(to='app.HelpdeskCall'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='repaircall',
            name='repair_tech',
            field=models.ForeignKey(blank=True, to='app.RepairTechnician', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='placement',
            name='support_item',
            field=models.ForeignKey(to='app.SupportItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpdeskcall',
            name='assigned_tech',
            field=models.ForeignKey(related_name='helpdeskcall_assignee', blank=True, to='app.Technician', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpdeskcall',
            name='call_recorder',
            field=models.ForeignKey(related_name='helpdeskcall_recorder', blank=True, to='app.Technician', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpdeskcall',
            name='caller',
            field=models.ForeignKey(blank=True, to='app.Caller', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpdeskcall',
            name='closing_tech',
            field=models.ForeignKey(related_name='helpdeskcall_closer', blank=True, to='app.Technician', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpdeskcall',
            name='item',
            field=models.ForeignKey(to='app.SupportItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hardwareitemtype',
            name='item_type',
            field=models.OneToOneField(to='app.ItemType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hardware',
            name='support_item',
            field=models.OneToOneField(to='app.SupportItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='person',
            field=models.OneToOneField(to='app.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispensed',
            name='consumer',
            field=models.ForeignKey(blank=True, to='app.Hardware', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispensed',
            name='placement',
            field=models.OneToOneField(to='app.Placement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coverperiod',
            name='contract',
            field=models.ForeignKey(blank=True, to='app.MaintenanceContract', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coverperiod',
            name='weekday',
            field=models.ForeignKey(to='app.Weekday'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consumableitemtype',
            name='item_type',
            field=models.OneToOneField(to='app.ItemType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consumable',
            name='support_item',
            field=models.OneToOneField(to='app.SupportItem'),
            preserve_default=True,
        ),
    ]
