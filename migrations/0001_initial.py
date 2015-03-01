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
                ('telephone', models.CharField(max_length=15, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('location', models.CharField(max_length=30, null=True, blank=True)),
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
                ('street', models.CharField(max_length=40, null=True, blank=True)),
                ('city', models.CharField(max_length=20, null=True, blank=True)),
                ('telephone', models.CharField(max_length=15, null=True, blank=True)),
                ('postcode', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'db_table': 'company',
                'verbose_name_plural': 'companies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('company_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Company')),
            ],
            options={
                'db_table': 'contractor',
            },
            bases=('app.company',),
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
                ('caller_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Caller')),
                ('end_of_life', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'department',
            },
            bases=('app.caller',),
        ),
        migrations.CreateModel(
            name='HelpdeskCall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('call_time', models.DateTimeField()),
                ('problem_type', models.TextField(null=True, blank=True)),
                ('closing_time', models.DateTimeField(null=True, blank=True)),
                ('closing_comment', models.TextField(null=True, blank=True)),
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
            name='HardwareItemType',
            fields=[
                ('itemtype_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.ItemType')),
                ('consumer', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'hardware_item_type',
            },
            bases=('app.itemtype',),
        ),
        migrations.CreateModel(
            name='ConsumableItemType',
            fields=[
                ('itemtype_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.ItemType')),
            ],
            options={
                'db_table': 'consumable_item_type',
            },
            bases=('app.itemtype',),
        ),
        migrations.CreateModel(
            name='MaintenanceContract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=4)),
                ('description', models.CharField(max_length=35, null=True, blank=True)),
                ('contractor', models.ForeignKey(to='app.Contractor')),
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
                ('order_no', models.CharField(max_length=15)),
                ('order_date', models.DateField()),
                ('to_exec_committee', models.DateField(null=True, blank=True)),
                ('to_supply_dept', models.DateField(null=True, blank=True)),
                ('description', models.CharField(max_length=80, null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('private_comment', models.TextField(null=True, blank=True)),
                ('supplier_ref', models.CharField(max_length=20, null=True, blank=True)),
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
                ('description', models.CharField(max_length=20, null=True, blank=True)),
                ('quantity', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'order_item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItemConsumable',
            fields=[
                ('orderitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.OrderItem')),
            ],
            options={
                'db_table': 'order_item_consumable',
            },
            bases=('app.orderitem',),
        ),
        migrations.CreateModel(
            name='OrderItemMaterial',
            fields=[
                ('orderitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.OrderItem')),
                ('discount', models.FloatField(null=True, blank=True)),
                ('tax', models.FloatField(null=True, blank=True)),
                ('price_per_unit', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'order_item_material',
            },
            bases=('app.orderitem',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('caller_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Caller')),
                ('first_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'person',
            },
            bases=('app.caller',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Person')),
            ],
            options={
                'db_table': 'employee',
            },
            bases=('app.person',),
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_date', models.DateTimeField()),
                ('location', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'placement',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dispensed',
            fields=[
                ('placement_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Placement')),
                ('quantity', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'dispensed',
                'verbose_name_plural': 'dispensed',
            },
            bases=('app.placement',),
        ),
        migrations.CreateModel(
            name='RepairCall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('call_time', models.DateTimeField()),
                ('close_time', models.DateTimeField(null=True, blank=True)),
                ('call_problem', models.TextField()),
                ('call_reference', models.CharField(max_length=10, null=True, blank=True)),
                ('close_comment', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'repaircall',
                'verbose_name_plural': 'repair calls',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RepairTechnician',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Person')),
                ('company', models.ForeignKey(to='app.Company')),
            ],
            options={
                'db_table': 'repair_technician',
            },
            bases=('app.person',),
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
            name='SoftwareItemType',
            fields=[
                ('itemtype_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.ItemType')),
            ],
            options={
                'db_table': 'software_item_type',
            },
            bases=('app.itemtype',),
        ),
        migrations.CreateModel(
            name='SupportItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=30)),
                ('comment', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'support_item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('supportitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.SupportItem')),
                ('version', models.CharField(max_length=15, null=True, blank=True)),
                ('item_type', models.ForeignKey(to='app.SoftwareItemType')),
            ],
            options={
                'db_table': 'software',
                'verbose_name_plural': 'software',
            },
            bases=('app.supportitem',),
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('supportitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.SupportItem')),
                ('part_no', models.CharField(max_length=20, null=True, blank=True)),
                ('hostname', models.CharField(max_length=20, null=True, blank=True)),
                ('idms_name', models.CharField(max_length=8, null=True, blank=True)),
                ('ip_address', models.IntegerField(null=True, verbose_name='IP address', blank=True)),
                ('tag', models.IntegerField(unique=True, null=True, blank=True)),
                ('item_type', models.ForeignKey(to='app.HardwareItemType')),
            ],
            options={
                'db_table': 'hardware',
                'verbose_name_plural': 'hardware',
            },
            bases=('app.supportitem',),
        ),
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('supportitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.SupportItem')),
                ('part_no', models.CharField(max_length=20, null=True, blank=True)),
                ('item_type', models.ForeignKey(to='app.ConsumableItemType')),
            ],
            options={
                'db_table': 'consumable',
            },
            bases=('app.supportitem',),
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('employee_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='app.Employee')),
            ],
            options={
                'db_table': 'technician',
            },
            bases=('app.employee',),
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
                'verbose_name_plural': 'work done',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='supportitem',
            name='contract',
            field=models.ForeignKey(blank=True, to='app.MaintenanceContract', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='supportitem',
            name='order_item',
            field=models.ForeignKey(default=-1, to='app.OrderItemMaterial'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='supportitem',
            name='producer',
            field=models.ForeignKey(default=-1, to='app.Company'),
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
            name='department',
            field=models.ForeignKey(to='app.Department'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='placement',
            name='support_item',
            field=models.ForeignKey(to='app.SupportItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderitemmaterial',
            name='item_type',
            field=models.ForeignKey(to='app.ItemType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderitemconsumable',
            name='item',
            field=models.ForeignKey(to='app.Consumable'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='department',
            field=models.ForeignKey(to='app.Department'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='mat_order',
            field=models.ForeignKey(to='app.MaterialOrder'),
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
            field=models.ForeignKey(related_name='helpdeskcall_recorder', to='app.Technician'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helpdeskcall',
            name='caller',
            field=models.ForeignKey(to='app.Caller'),
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
            model_name='employee',
            name='department',
            field=models.ForeignKey(to='app.Department'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dispensed',
            name='consumer',
            field=models.ForeignKey(to='app.Hardware'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coverperiod',
            name='contract',
            field=models.ForeignKey(to='app.MaintenanceContract'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coverperiod',
            name='weekday',
            field=models.ForeignKey(to='app.Weekday'),
            preserve_default=True,
        ),
    ]
