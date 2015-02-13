'''
@author: Sven Coenye

Copyright (C) 2015  Sven Coenye

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/
'''

from __future__ import unicode_literals

from django.db import models


class Caller(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15, blank=True)
    active = models.NullBooleanField()
    location = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'caller'


class Company(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=40, blank=True)
    city = models.CharField(max_length=20, blank=True)
    telephone = models.CharField(max_length=15, blank=True)
    postcode = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'company'


class Consumable(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    contract = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=30)
    producer = models.ForeignKey(Company, db_column='producer', blank=True, null=True)
    item_type = models.IntegerField()
    order_item = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True)
    part_no = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'consumable'


class ConsumableItemType(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'consumable_item_type'


class Contractor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=40, blank=True)
    city = models.CharField(max_length=20, blank=True)
    telephone = models.CharField(max_length=15, blank=True)
    postcode = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'contractor'


class CoverPeriod(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    contract = models.ForeignKey('MaintenanceContract', db_column='contract', blank=True, null=True)
    weekday = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'cover_period'


class Department(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15, blank=True)
    active = models.NullBooleanField()
    location = models.CharField(max_length=30, blank=True)
    end_of_life = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'department'


class Dispensed(models.Model):
    id = models.IntegerField()
    item = models.IntegerField(blank=True, null=True)
    place_date = models.DateTimeField()
    department = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True)
    consumer = models.ForeignKey('Hardware', db_column='consumer', blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispensed'


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15, blank=True)
    active = models.NullBooleanField()
    location = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=20)
    department = models.ForeignKey(Department, db_column='department', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Hardware(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    contract = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=30)
    producer = models.IntegerField(blank=True, null=True)
    item_type = models.IntegerField()
    order_item = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True)
    part_no = models.CharField(max_length=20, blank=True)
    hostname = models.CharField(max_length=20, blank=True)
    idms_name = models.CharField(max_length=8, blank=True)
    ip_address = models.IntegerField(blank=True, null=True)
    tag = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hardware'


class HardwareItemType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=40)
    consumer = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'hardware_item_type'


class HelpdeskCall(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    caller = models.ForeignKey(Caller, db_column='caller', blank=True, null=True)
    call_time = models.DateTimeField()
    call_recorder = models.ForeignKey('Technician', db_column='call_recorder', blank=True, null=True)
    problem_type = models.TextField(blank=True)
    item = models.ForeignKey('SupportItem', db_column='item')
    assigned_tech = models.ForeignKey('Technician', db_column='assigned_tech', blank=True, null=True)
    closing_time = models.DateTimeField(blank=True, null=True)
    closing_comment = models.TextField(blank=True)
    closing_tech = models.ForeignKey('Technician', db_column='closing_tech', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'helpdesk_call'


class ItemType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'item_type'


class MaintenanceContract(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=4)
    contractor = models.ForeignKey(Contractor, db_column='contractor', blank=True, null=True)
    description = models.CharField(max_length=35, blank=True)

    class Meta:
        managed = False
        db_table = 'maintenance_contract'


class MaterialOrder(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    order_id = models.CharField(max_length=15)
    order_date = models.DateField()
    to_exec_committee = models.DateField(blank=True, null=True)
    to_supply_dept = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=80, blank=True)
    comment = models.TextField(blank=True)
    private_comment = models.TextField(blank=True)
    supplier = models.ForeignKey(Company, db_column='supplier')
    supplier_ref = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'material_order'


class OldInventory(models.Model):
    contract = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=30, blank=True)
    producer = models.IntegerField(blank=True, null=True)
    item_type = models.IntegerField(blank=True, null=True)
    order_item = models.IntegerField(blank=True, null=True)
    part_no = models.CharField(max_length=20, blank=True)
    hostname = models.CharField(max_length=20, blank=True)
    tag = models.IntegerField(blank=True, null=True)
    place_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True)
    department = models.IntegerField(blank=True, null=True)
    purchased = models.DateField(blank=True, null=True)
    serial_no = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'old_inventory'


class OrderItem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    mat_order = models.IntegerField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=20, blank=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item'


class OrderItemConsumable(models.Model):
    id = models.IntegerField()
    mat_order = models.IntegerField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=20, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    item = models.ForeignKey(Consumable, db_column='item', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_consumable'


class OrderItemMaterial(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    mat_order = models.ForeignKey(MaterialOrder, db_column='mat_order', blank=True, null=True)
    completed = models.DateField(blank=True, null=True)
    department = models.ForeignKey(Department, db_column='department', blank=True, null=True)
    description = models.CharField(max_length=20, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    price_per_unit = models.FloatField(blank=True, null=True)
    item_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_material'


class Person(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15, blank=True)
    active = models.NullBooleanField()
    location = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'person'


class Placement(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    item = models.IntegerField(blank=True, null=True)
    place_date = models.DateTimeField()
    department = models.ForeignKey(Department, db_column='department', blank=True, null=True)
    location = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'placement'


class RepairTechnician(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15, blank=True)
    active = models.NullBooleanField()
    location = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=20)
    company = models.ForeignKey(Company, db_column='company', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repair_technician'


class Repaircall(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    helpdeskcall = models.ForeignKey(HelpdeskCall, db_column='helpdeskcall')
    call_tech = models.ForeignKey('Technician', db_column='call_tech')
    call_time = models.DateTimeField()
    close_time = models.DateTimeField(blank=True, null=True)
    call_problem = models.TextField()
    call_reference = models.CharField(max_length=10, blank=True)
    close_comment = models.TextField(blank=True)
    close_tech = models.ForeignKey('Technician', db_column='close_tech', blank=True, null=True)
    repair_tech = models.ForeignKey(RepairTechnician, db_column='repair_tech', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repaircall'


class SerialNo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    item = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=30)
    assign_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serial_no'


class Software(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    contract = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=30)
    producer = models.IntegerField(blank=True, null=True)
    item_type = models.IntegerField()
    order_item = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True)
    version = models.CharField(max_length=15, blank=True)

    class Meta:
        managed = False
        db_table = 'software'


class SoftwareItemType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'software_item_type'


class SupportItem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    contract = models.ForeignKey(MaintenanceContract, db_column='contract', blank=True, null=True)
    description = models.CharField(max_length=30)
    producer = models.ForeignKey(Company, db_column='producer', blank=True, null=True)
    item_type = models.ForeignKey(ItemType, db_column='item_type')
    order_item = models.ForeignKey(OrderItemMaterial, db_column='order_item', blank=True, null=True)
    comment = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'support_item'


class Technician(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15, blank=True)
    active = models.NullBooleanField()
    location = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=20)
    department = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'technician'


class Weekday(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    day = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'weekday'


class WorkDone(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    call = models.ForeignKey(HelpdeskCall, db_column='call')
    technician = models.ForeignKey(Technician, db_column='technician')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_done'


# The support views - hide until the real tables are migrated
#class VwActiveDesktops(models.Model):
#    tag = models.IntegerField(blank=True, null=True)
#    description = models.CharField(max_length=30, blank=True)
#    department = models.CharField(max_length=30, blank=True)
#    assignee = models.CharField(max_length=50, blank=True)
#
#    class Meta:
#        managed = False
#        db_table = 'vw_active_desktops'


#class VwActiveLaptops(models.Model):
#    tag = models.IntegerField(blank=True, null=True)
#    description = models.CharField(max_length=30, blank=True)
#    department = models.CharField(max_length=30, blank=True)
#    assignee = models.CharField(max_length=50, blank=True)
#
#    class Meta:
#        managed = False
#        db_table = 'vw_active_laptops'


#class VwConsumablesDelivered(models.Model):
#    item = models.IntegerField(blank=True, null=True)
#    quantity = models.BigIntegerField(blank=True, null=True)
#
#    class Meta:
#        managed = False
#        db_table = 'vw_consumables_delivered'


#class VwConsumablesDispensed(models.Model):
#    item = models.IntegerField(blank=True, null=True)
#    dispensed = models.BigIntegerField(blank=True, null=True)
#
#    class Meta:
#        managed = False
#        db_table = 'vw_consumables_dispensed'


#class VwConsumablesOnhand(models.Model):
#    id = models.IntegerField(blank=True, null=True)
#    on_hand = models.BigIntegerField(blank=True, null=True)
#
#    class Meta:
#        managed = False
#        db_table = 'vw_consumables_onhand'


#class VwFirstAssignedDept(models.Model):
#    item = models.IntegerField(blank=True, null=True)
#    department = models.IntegerField(blank=True, null=True)
#    department_name = models.TextField(blank=True)
#    location = models.CharField(max_length=50, blank=True)
#    place_date = models.DateTimeField(blank=True, null=True)
#
#    class Meta:
#        managed = False
#        db_table = 'vw_first_assigned_dept'


#class VwInventory(models.Model):
#    tag = models.IntegerField(blank=True, null=True)
#    description = models.CharField(max_length=30, blank=True)
#    mfg = models.CharField(max_length=50, blank=True)
#    part_no = models.CharField(max_length=20, blank=True)
#    serial_no = models.CharField(max_length=30, blank=True)
#    item_type = models.CharField(max_length=40, blank=True)
#    department = models.CharField(max_length=30, blank=True)
#    campus = models.CharField(max_length=30, blank=True)
#    location = models.CharField(max_length=50, blank=True)
#    comment = models.TextField(blank=True)
#
#    class Meta:
#        managed = False
#        db_table = 'vw_inventory'


#class VwLastAssignedDept(models.Model):
#    item = models.IntegerField(blank=True, null=True)
#    department = models.IntegerField(blank=True, null=True)
#    name = models.CharField(max_length=30, blank=True)
#    location = models.CharField(max_length=50, blank=True)
#    place_date = models.DateTimeField(blank=True, null=True)
#
#    class Meta:
#        managed = False
#        db_table = 'vw_last_assigned_dept'


#class VwLastAssignedSerial(models.Model):
#    item = models.IntegerField(blank=True, null=True)
#    serial_no = models.CharField(max_length=30, blank=True)
#    assign_date = models.DateField(blank=True, null=True)
#
#    class Meta:
#        managed = False
#        db_table = 'vw_last_assigned_serial'


#class VwSupportItem(models.Model):
#    id = models.IntegerField(blank=True, null=True)
#
#    class Meta:
#        managed = False
#        db_table = 'vw_support_item'


#class VwSupportedHardSoft(models.Model):
#    id = models.IntegerField(blank=True, null=True)
#    description = models.CharField(max_length=30, blank=True)
#    item_type = models.IntegerField(blank=True, null=True)
#    item_type_name = models.CharField(max_length=40, blank=True)
#    host_ver = models.CharField(max_length=-1, blank=True)
#    department = models.IntegerField(blank=True, null=True)
#    location = models.CharField(max_length=50, blank=True)
#    serial_no = models.CharField(max_length=30, blank=True)
#
#    class Meta:
#        managed = False
#        db_table = 'vw_supported_hard_soft'

