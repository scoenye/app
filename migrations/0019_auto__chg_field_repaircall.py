# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Repaircall.close_tech' to match new field type.
        db.rename_column(u'repaircall', u'close_tech', 'close_tech_id')
        # Changing field 'Repaircall.close_tech'
        db.alter_column(u'repaircall', 'close_tech_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['app.Technician']))

        # Renaming column for 'Repaircall.helpdeskcall' to match new field type.
        db.rename_column(u'repaircall', u'helpdeskcall', 'helpdeskcall_id')
        # Changing field 'Repaircall.helpdeskcall'
        db.alter_column(u'repaircall', 'helpdeskcall_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.HelpdeskCall']))

        # Renaming column for 'Repaircall.repair_tech' to match new field type.
        db.rename_column(u'repaircall', u'repair_tech', 'repair_tech_id')
        # Changing field 'Repaircall.repair_tech'
        db.alter_column(u'repaircall', 'repair_tech_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.RepairTechnician'], null=True))

        # Renaming column for 'Repaircall.call_tech' to match new field type.
        db.rename_column(u'repaircall', u'call_tech', 'call_tech_id')
        # Changing field 'Repaircall.call_tech'
        db.alter_column(u'repaircall', 'call_tech_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Technician']))

    def backwards(self, orm):

        # Renaming column for 'Repaircall.close_tech' to match new field type.
        db.rename_column(u'repaircall', 'close_tech_id', u'close_tech')
        # Changing field 'Repaircall.close_tech'
        db.alter_column(u'repaircall', u'close_tech', self.gf('django.db.models.fields.related.ForeignKey')(null=True, db_column=u'close_tech', to=orm['app.Technician']))

        # Renaming column for 'Repaircall.helpdeskcall' to match new field type.
        db.rename_column(u'repaircall', 'helpdeskcall_id', u'helpdeskcall')
        # Changing field 'Repaircall.helpdeskcall'
        db.alter_column(u'repaircall', u'helpdeskcall', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.HelpdeskCall'], db_column=u'helpdeskcall'))

        # Renaming column for 'Repaircall.repair_tech' to match new field type.
        db.rename_column(u'repaircall', 'repair_tech_id', u'repair_tech')
        # Changing field 'Repaircall.repair_tech'
        db.alter_column(u'repaircall', u'repair_tech', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.RepairTechnician'], null=True, db_column=u'repair_tech'))

        # Renaming column for 'Repaircall.call_tech' to match new field type.
        db.rename_column(u'repaircall', 'call_tech_id', u'call_tech')
        # Changing field 'Repaircall.call_tech'
        db.alter_column(u'repaircall', u'call_tech', self.gf('django.db.models.fields.related.ForeignKey')(db_column=u'call_tech', to=orm['app.Technician']))

    models = {
        u'app.caller': {
            'Meta': {'object_name': 'Caller', 'db_table': "u'caller'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.MaintenanceContract']"}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'weekday': ('django.db.models.fields.IntegerField', [], {})
        },
        u'app.department': {
            'Meta': {'object_name': 'Department', 'db_table': "u'department'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'end_of_life': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'app.employee': {
            'Meta': {'object_name': 'Employee', 'db_table': "u'employee'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Department']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'app.hardware': {
            'Meta': {'object_name': 'Hardware', 'db_table': "u'hardware'"},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.MaintenanceContract']", 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idms_name': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'ip_address': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.HardwareItemType']"}),
            'order_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.OrderItem']", 'null': 'True'}),
            'part_no': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'producer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Company']", 'null': 'True'}),
            'tag': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'app.hardwareitemtype': {
            'Meta': {'object_name': 'HardwareItemType', 'db_table': "u'hardware_item_type'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'app.hardwareplacement': {
            'Meta': {'object_name': 'HardwarePlacement', 'db_table': "u'placement'"},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Hardware']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'place_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'app.hardwareserialno': {
            'Meta': {'object_name': 'HardwareSerialNo', 'db_table': "u'serial_no'"},
            'assign_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Hardware']"}),
            'serial_no': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'app.helpdeskcall': {
            'Meta': {'object_name': 'HelpdeskCall', 'db_table': "u'helpdesk_call'"},
            'assigned_tech': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'assigned_tech'", 'null': 'True', 'to': u"orm['app.Technician']"}),
            'call_recorder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'call_recorder'", 'to': u"orm['app.Technician']"}),
            'call_time': ('django.db.models.fields.DateTimeField', [], {}),
            'caller': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Caller']", 'null': 'True'}),
            'closing_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'closing_tech': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'closing_tech'", 'null': 'True', 'to': u"orm['app.Technician']"}),
            'closing_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.SupportItem']"}),
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
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Department']", 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.ItemType']"}),
            'mat_order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.MaterialOrder']"}),
            'price_per_unit': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tax': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app.person': {
            'Meta': {'object_name': 'Person', 'db_table': "u'person'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'app.placement': {
            'Meta': {'object_name': 'Placement', 'db_table': "u'placement'"},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.SupportItem']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'place_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'app.repaircall': {
            'Meta': {'object_name': 'Repaircall', 'db_table': "u'repaircall'"},
            'call_problem': ('django.db.models.fields.TextField', [], {}),
            'call_reference': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'call_tech': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'call_tech'", 'to': u"orm['app.Technician']"}),
            'call_time': ('django.db.models.fields.DateTimeField', [], {}),
            'close_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'close_tech': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'close_tech'", 'null': 'True', 'to': u"orm['app.Technician']"}),
            'close_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'helpdeskcall': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.HelpdeskCall']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repair_tech': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.RepairTechnician']", 'null': 'True'})
        },
        u'app.repairtechnician': {
            'Meta': {'object_name': 'RepairTechnician', 'db_table': "u'repair_technician'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Company']", 'null': 'True'}),
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
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.SupportItem']"}),
            'serial_no': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'app.software': {
            'Meta': {'object_name': 'Software', 'db_table': "u'software'"},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.MaintenanceContract']", 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.SoftwareItemType']"}),
            'order_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.OrderItem']", 'null': 'True'}),
            'producer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Company']", 'null': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'})
        },
        u'app.softwareitemtype': {
            'Meta': {'object_name': 'SoftwareItemType', 'db_table': "u'software_item_type'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'app.softwareplacement': {
            'Meta': {'object_name': 'SoftwarePlacement', 'db_table': "u'placement'"},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Software']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'place_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'app.softwareserialno': {
            'Meta': {'object_name': 'SoftwareSerialNo', 'db_table': "u'serial_no'"},
            'assign_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Software']"}),
            'serial_no': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'app.supportitem': {
            'Meta': {'object_name': 'SupportItem', 'db_table': "u'support_item'"},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.MaintenanceContract']", 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.ItemType']"}),
            'order_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.OrderItem']", 'null': 'True'}),
            'producer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Company']", 'null': 'True'})
        },
        u'app.technician': {
            'Meta': {'object_name': 'Technician', 'db_table': "u'technician'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Department']"}),
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