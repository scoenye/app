# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import dbs
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Caller'
        dbs['app'].create_table(u'caller', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        dbs['app'].send_create_signal(u'app', ['Caller'])

        # Adding model 'Company'
        dbs['app'].create_table(u'company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        dbs['app'].send_create_signal(u'app', ['Company'])

        # Adding model 'Contractor'
        dbs['app'].create_table(u'contractor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        dbs['app'].send_create_signal(u'app', ['Contractor'])

        # Adding model 'CoverPeriod'
        dbs['app'].create_table(u'cover_period', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contract', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.MaintenanceContract'], null=True, db_column=u'contract')),
            ('weekday', self.gf('django.db.models.fields.IntegerField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        dbs['app'].send_create_signal(u'app', ['CoverPeriod'])

        # Adding model 'Department'
        dbs['app'].create_table(u'department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('end_of_life', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        dbs['app'].send_create_signal(u'app', ['Department'])

        # Adding model 'Employee'
        dbs['app'].create_table(u'employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Department'], null=True, db_column=u'department')),
        ))
        dbs['app'].send_create_signal(u'app', ['Employee'])

        # Adding model 'Hardware'
        dbs['app'].create_table(u'hardware', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contract', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('producer', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item_type', self.gf('django.db.models.fields.IntegerField')()),
            ('order_item', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('part_no', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('idms_name', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tag', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True, blank=True)),
        ))
        dbs['app'].send_create_signal(u'app', ['Hardware'])

        # Adding model 'HardwareItemType'
        dbs['app'].create_table(u'hardware_item_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        dbs['app'].send_create_signal(u'app', ['HardwareItemType'])

        # Adding model 'HelpdeskCall'
        dbs['app'].create_table(u'helpdesk_call', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caller', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Caller'], null=True, db_column=u'caller')),
            ('call_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('call_recorder', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'call_recorder', null=True, db_column=u'call_recorder', to=orm['app.Technician'])),
            ('problem_type', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.SupportItem'], db_column=u'item')),
            ('assigned_tech', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'assigned_tech', null=True, db_column=u'assigned_tech', to=orm['app.Technician'])),
            ('closing_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('closing_comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('closing_tech', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'closing_tech', null=True, db_column=u'closing_tech', to=orm['app.Technician'])),
        ))
        dbs['app'].send_create_signal(u'app', ['HelpdeskCall'])

        # Adding model 'ItemType'
        dbs['app'].create_table(u'item_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        dbs['app'].send_create_signal(u'app', ['ItemType'])

        # Adding model 'MaintenanceContract'
        dbs['app'].create_table(u'maintenance_contract', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('contractor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Contractor'], null=True, db_column=u'contractor')),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
        ))
        dbs['app'].send_create_signal(u'app', ['MaintenanceContract'])

        # Adding model 'MaterialOrder'
        dbs['app'].create_table(u'material_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_id', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('order_date', self.gf('django.db.models.fields.DateField')()),
            ('to_exec_committee', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('to_supply_dept', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('private_comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Company'], db_column=u'supplier')),
        ))
        dbs['app'].send_create_signal(u'app', ['MaterialOrder'])

        # Adding model 'OrderItem'
        dbs['app'].create_table(u'order_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mat_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.MaterialOrder'], null=True)),
            ('discount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('tax', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('completed', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Department'], null=True, db_column=u'department')),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('price_per_unit', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.ItemType'], db_column=u'item_type')),
        ))
        dbs['app'].send_create_signal(u'app', ['OrderItem'])

        # Adding model 'Person'
        dbs['app'].create_table(u'person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        dbs['app'].send_create_signal(u'app', ['Person'])

        # Adding model 'Placement'
        dbs['app'].create_table(u'placement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('place_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Department'], null=True, db_column=u'department')),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        dbs['app'].send_create_signal(u'app', ['Placement'])

        # Adding model 'RepairTechnician'
        dbs['app'].create_table(u'repair_technician', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Company'], null=True, db_column=u'company')),
        ))
        dbs['app'].send_create_signal(u'app', ['RepairTechnician'])

        # Adding model 'Repaircall'
        dbs['app'].create_table(u'repaircall', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('helpdeskcall', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.HelpdeskCall'], db_column=u'helpdeskcall')),
            ('call_tech', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'call_tech', db_column=u'call_tech', to=orm['app.Technician'])),
            ('call_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('close_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('call_problem', self.gf('django.db.models.fields.TextField')()),
            ('call_reference', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('close_comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('close_tech', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'close_tech', null=True, db_column=u'close_tech', to=orm['app.Technician'])),
            ('repair_tech', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.RepairTechnician'], null=True, db_column=u'repair_tech')),
        ))
        dbs['app'].send_create_signal(u'app', ['Repaircall'])

        # Adding model 'SerialNo'
        dbs['app'].create_table(u'serial_no', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('serial_no', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('assign_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        dbs['app'].send_create_signal(u'app', ['SerialNo'])

        # Adding model 'Software'
        dbs['app'].create_table(u'software', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contract', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('producer', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item_type', self.gf('django.db.models.fields.IntegerField')()),
            ('order_item', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
        ))
        dbs['app'].send_create_signal(u'app', ['Software'])

        # Adding model 'SoftwareItemType'
        dbs['app'].create_table(u'software_item_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        dbs['app'].send_create_signal(u'app', ['SoftwareItemType'])

        # Adding model 'SupportItem'
        dbs['app'].create_table(u'support_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contract', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.MaintenanceContract'], null=True, db_column=u'contract')),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('producer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Company'], null=True, db_column=u'producer')),
            ('item_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.ItemType'], db_column=u'item_type')),
            ('order_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.OrderItem'], null=True, db_column=u'order_item')),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        dbs['app'].send_create_signal(u'app', ['SupportItem'])

        # Adding model 'Technician'
        dbs['app'].create_table(u'technician', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('department', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        dbs['app'].send_create_signal(u'app', ['Technician'])

        # Adding model 'Weekday'
        dbs['app'].create_table(u'weekday', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        dbs['app'].send_create_signal(u'app', ['Weekday'])

        # Adding model 'WorkDone'
        dbs['app'].create_table(u'work_done', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('call', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.HelpdeskCall'], db_column=u'call')),
            ('technician', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Technician'], db_column=u'technician')),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        dbs['app'].send_create_signal(u'app', ['WorkDone'])


    def backwards(self, orm):
        # Deleting model 'Caller'
        dbs['app'].delete_table(u'caller')

        # Deleting model 'Company'
        dbs['app'].delete_table(u'company')

        # Deleting model 'Contractor'
        dbs['app'].delete_table(u'contractor')

        # Deleting model 'CoverPeriod'
        dbs['app'].delete_table(u'cover_period')

        # Deleting model 'Department'
        dbs['app'].delete_table(u'department')

        # Deleting model 'Employee'
        dbs['app'].delete_table(u'employee')

        # Deleting model 'Hardware'
        dbs['app'].delete_table(u'hardware')

        # Deleting model 'HardwareItemType'
        dbs['app'].delete_table(u'hardware_item_type')

        # Deleting model 'HelpdeskCall'
        dbs['app'].delete_table(u'helpdesk_call')

        # Deleting model 'ItemType'
        dbs['app'].delete_table(u'item_type')

        # Deleting model 'MaintenanceContract'
        dbs['app'].delete_table(u'maintenance_contract')

        # Deleting model 'MaterialOrder'
        dbs['app'].delete_table(u'material_order')

        # Deleting model 'OrderItem'
        dbs['app'].delete_table(u'order_item')

        # Deleting model 'Person'
        dbs['app'].delete_table(u'person')

        # Deleting model 'Placement'
        dbs['app'].delete_table(u'placement')

        # Deleting model 'RepairTechnician'
        dbs['app'].delete_table(u'repair_technician')

        # Deleting model 'Repaircall'
        dbs['app'].delete_table(u'repaircall')

        # Deleting model 'SerialNo'
        dbs['app'].delete_table(u'serial_no')

        # Deleting model 'Software'
        dbs['app'].delete_table(u'software')

        # Deleting model 'SoftwareItemType'
        dbs['app'].delete_table(u'software_item_type')

        # Deleting model 'SupportItem'
        dbs['app'].delete_table(u'support_item')

        # Deleting model 'Technician'
        dbs['app'].delete_table(u'technician')

        # Deleting model 'Weekday'
        dbs['app'].delete_table(u'weekday')

        # Deleting model 'WorkDone'
        dbs['app'].delete_table(u'work_done')


    models = {
        u'app.caller': {
            'Meta': {'object_name': 'Caller', 'db_table': "u'caller'"},
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'app.company': {
            'Meta': {'object_name': 'Company', 'db_table': "u'company'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'app.contractor': {
            'Meta': {'object_name': 'Contractor', 'db_table': "u'contractor'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'app.coverperiod': {
            'Meta': {'object_name': 'CoverPeriod', 'db_table': "u'cover_period'"},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.MaintenanceContract']", 'null': 'True', 'db_column': "u'contract'"}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'weekday': ('django.db.models.fields.IntegerField', [], {})
        },
        u'app.department': {
            'Meta': {'object_name': 'Department', 'db_table': "u'department'"},
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'end_of_life': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'app.employee': {
            'Meta': {'object_name': 'Employee', 'db_table': "u'employee'"},
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Department']", 'null': 'True', 'db_column': "u'department'"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'app.hardware': {
            'Meta': {'object_name': 'Hardware', 'db_table': "u'hardware'"},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contract': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idms_name': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'ip_address': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item_type': ('django.db.models.fields.IntegerField', [], {}),
            'order_item': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'part_no': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'producer': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'app.hardwareitemtype': {
            'Meta': {'object_name': 'HardwareItemType', 'db_table': "u'hardware_item_type'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'app.helpdeskcall': {
            'Meta': {'object_name': 'HelpdeskCall', 'db_table': "u'helpdesk_call'"},
            'assigned_tech': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'assigned_tech'", 'null': 'True', 'db_column': "u'assigned_tech'", 'to': u"orm['app.Technician']"}),
            'call_recorder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'call_recorder'", 'null': 'True', 'db_column': "u'call_recorder'", 'to': u"orm['app.Technician']"}),
            'call_time': ('django.db.models.fields.DateTimeField', [], {}),
            'caller': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Caller']", 'null': 'True', 'db_column': "u'caller'"}),
            'closing_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'closing_tech': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'closing_tech'", 'null': 'True', 'db_column': "u'closing_tech'", 'to': u"orm['app.Technician']"}),
            'closing_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.SupportItem']", 'db_column': "u'item'"}),
            'problem_type': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app.itemtype': {
            'Meta': {'object_name': 'ItemType', 'db_table': "u'item_type'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'app.maintenancecontract': {
            'Meta': {'object_name': 'MaintenanceContract', 'db_table': "u'maintenance_contract'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'contractor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Contractor']", 'null': 'True', 'db_column': "u'contractor'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.materialorder': {
            'Meta': {'object_name': 'MaterialOrder', 'db_table': "u'material_order'"},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {}),
            'order_id': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'private_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Company']", 'db_column': "u'supplier'"}),
            'to_exec_committee': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'to_supply_dept': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app.orderitem': {
            'Meta': {'object_name': 'OrderItem', 'db_table': "u'order_item'"},
            'completed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Department']", 'null': 'True', 'db_column': "u'department'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.ItemType']", 'db_column': "u'item_type'"}),
            'mat_order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.MaterialOrder']", 'null': 'True'}),
            'price_per_unit': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tax': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app.person': {
            'Meta': {'object_name': 'Person', 'db_table': "u'person'"},
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'app.placement': {
            'Meta': {'object_name': 'Placement', 'db_table': "u'placement'"},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Department']", 'null': 'True', 'db_column': "u'department'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'place_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'app.repaircall': {
            'Meta': {'object_name': 'Repaircall', 'db_table': "u'repaircall'"},
            'call_problem': ('django.db.models.fields.TextField', [], {}),
            'call_reference': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'call_tech': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'call_tech'", 'db_column': "u'call_tech'", 'to': u"orm['app.Technician']"}),
            'call_time': ('django.db.models.fields.DateTimeField', [], {}),
            'close_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'close_tech': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'close_tech'", 'null': 'True', 'db_column': "u'close_tech'", 'to': u"orm['app.Technician']"}),
            'close_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'helpdeskcall': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.HelpdeskCall']", 'db_column': "u'helpdeskcall'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repair_tech': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.RepairTechnician']", 'null': 'True', 'db_column': "u'repair_tech'"})
        },
        u'app.repairtechnician': {
            'Meta': {'object_name': 'RepairTechnician', 'db_table': "u'repair_technician'"},
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Company']", 'null': 'True', 'db_column': "u'company'"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'app.serialno': {
            'Meta': {'object_name': 'SerialNo', 'db_table': "u'serial_no'"},
            'assign_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'serial_no': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'app.software': {
            'Meta': {'object_name': 'Software', 'db_table': "u'software'"},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contract': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.IntegerField', [], {}),
            'order_item': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'producer': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'})
        },
        u'app.softwareitemtype': {
            'Meta': {'object_name': 'SoftwareItemType', 'db_table': "u'software_item_type'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'app.supportitem': {
            'Meta': {'object_name': 'SupportItem', 'db_table': "u'support_item'"},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.MaintenanceContract']", 'null': 'True', 'db_column': "u'contract'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.ItemType']", 'db_column': "u'item_type'"}),
            'order_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.OrderItem']", 'null': 'True', 'db_column': "u'order_item'"}),
            'producer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Company']", 'null': 'True', 'db_column': "u'producer'"})
        },
        u'app.technician': {
            'Meta': {'object_name': 'Technician', 'db_table': "u'technician'"},
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'app.vwactivedesktops': {
            'Meta': {'object_name': 'VwActiveDesktops', 'db_table': "u'vw_active_desktops'", 'managed': 'False'},
            'assignee': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app.vwactivelaptops': {
            'Meta': {'object_name': 'VwActiveLaptops', 'db_table': "u'vw_active_laptops'", 'managed': 'False'},
            'assignee': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app.vwfirstassigneddept': {
            'Meta': {'object_name': 'VwFirstAssignedDept', 'db_table': "u'vw_first_assigned_dept'", 'managed': 'False'},
            'department': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'department_name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'place_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app.vwinventory': {
            'Meta': {'object_name': 'VwInventory', 'db_table': "u'vw_inventory'", 'managed': 'False'},
            'campus': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mfg': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'part_no': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'serial_no': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app.vwlastassigneddept': {
            'Meta': {'object_name': 'VwLastAssignedDept', 'db_table': "u'vw_last_assigned_dept'", 'managed': 'False'},
            'department': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'place_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app.vwlastassignedserial': {
            'Meta': {'object_name': 'VwLastAssignedSerial', 'db_table': "u'vw_last_assigned_serial'", 'managed': 'False'},
            'assign_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'serial_no': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'app.vwsupportedhardsoft': {
            'Meta': {'object_name': 'VwSupportedHardSoft', 'db_table': "u'vw_supported_hard_soft'", 'managed': 'False'},
            'department': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'host_ver': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item_type_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'serial_no': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'app.vwsupportitem': {
            'Meta': {'object_name': 'VwSupportItem', 'db_table': "u'vw_support_item'", 'managed': 'False'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'app.weekday': {
            'Meta': {'object_name': 'Weekday', 'db_table': "u'weekday'"},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.workdone': {
            'Meta': {'object_name': 'WorkDone', 'db_table': "u'work_done'"},
            'call': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.HelpdeskCall']", 'db_column': "u'call'"}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'technician': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Technician']", 'db_column': "u'technician'"})
        }
    }

    complete_apps = ['app']