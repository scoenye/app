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
    name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    active = models.BooleanField(default=True)
    location = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'caller'


class Company(models.Model):
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'company'


class Consumable(models.Model):
    support_item = models.OneToOneField("SupportItem")
    part_no = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'consumable'


class ConsumableItemType(models.Model):
    item_type = models.OneToOneField("ItemType")
    name = models.CharField(max_length=40)  # TODO: Remove. See ItemType

    class Meta:
        db_table = 'consumable_item_type'


class Contractor(models.Model):
    company = models.OneToOneField(Company)

    class Meta:
        db_table = 'contractor'


class CoverPeriod(models.Model):
    contract = models.ForeignKey('MaintenanceContract')
    weekday = models.ForeignKey("Weekday")
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = 'cover_period'


class Department(models.Model):
    caller = models.OneToOneField(Caller)
    end_of_life = models.BooleanField(default=False)

    class Meta:
        db_table = 'department'


class Dispensed(models.Model):
    placement = models.OneToOneField("Placement")
    consumer = models.ForeignKey('Hardware')
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'dispensed'


class Employee(models.Model):
    person = models.OneToOneField("Person")
    department = models.ForeignKey(Department)

    class Meta:
        db_table = 'employee'


class Hardware(models.Model):
    support_item = models.OneToOneField("SupportItem")
    part_no = models.CharField(max_length=20, blank=True, null=True)
    hostname = models.CharField(max_length=20, blank=True, null=True)
    idms_name = models.CharField(max_length=8, blank=True, null=True)
    ip_address = models.IntegerField(blank=True, null=True)
    tag = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        db_table = 'hardware'


class HardwareItemType(models.Model):
    item_type = models.OneToOneField("ItemType")
    name = models.CharField(max_length=40)  # TODO: Remove. See ItemType
    consumer = models.BooleanField(default=False)

    class Meta:
        db_table = 'hardware_item_type'


class HelpdeskCall(models.Model):
    caller = models.ForeignKey(Caller)
    call_time = models.DateTimeField()
    call_recorder = models.ForeignKey('Technician', related_name='helpdeskcall_recorder')
    problem_type = models.TextField(blank=True, null=True)
    item = models.ForeignKey('SupportItem')
    assigned_tech = models.ForeignKey('Technician', blank=True, null=True, related_name='helpdeskcall_assignee')
    closing_time = models.DateTimeField(blank=True, null=True)
    closing_comment = models.TextField(blank=True, null=True)
    closing_tech = models.ForeignKey('Technician', blank=True, null=True, related_name='helpdeskcall_closer')

    class Meta:
        db_table = 'helpdesk_call'


class ItemType(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'item_type'


class MaintenanceContract(models.Model):
    code = models.CharField(max_length=4)
    contractor = models.ForeignKey(Contractor)
    description = models.CharField(max_length=35, null=True, blank=True)

    class Meta:
        db_table = 'maintenance_contract'


class MaterialOrder(models.Model):
    order_no = models.CharField(max_length=15)      # pg does not like 'order' as a field name
    order_date = models.DateField()
    to_exec_committee = models.DateField(blank=True, null=True)
    to_supply_dept = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=80, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    private_comment = models.TextField(blank=True, null=True)
    supplier = models.ForeignKey(Company)
    supplier_ref = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'material_order'


class OrderItem(models.Model):
    mat_order = models.ForeignKey(MaterialOrder)
    completed = models.DateField(blank=True, null=True)
    department = models.ForeignKey(Department)
    description = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'order_item'


class OrderItemConsumable(models.Model):
    order_item = models.OneToOneField(OrderItem)
    item = models.ForeignKey(Consumable)

    class Meta:
        db_table = 'order_item_consumable'


class OrderItemMaterial(models.Model):
    order_item = models.OneToOneField(OrderItem)
    discount = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    price_per_unit = models.FloatField(blank=True, null=True)
    item_type = models.ForeignKey(ItemType)

    class Meta:
        db_table = 'order_item_material'


class Person(models.Model):
    caller = models.OneToOneField(Caller)
    first_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'person'


class Placement(models.Model):
    support_item = models.ForeignKey("SupportItem")
    place_date = models.DateTimeField()
    department = models.ForeignKey(Department)
    location = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'placement'


class RepairTechnician(models.Model):
    person = models.OneToOneField(Person)
    company = models.ForeignKey(Company)

    class Meta:
        db_table = 'repair_technician'


class RepairCall(models.Model):
    helpdeskcall = models.ForeignKey(HelpdeskCall)
    call_tech = models.ForeignKey('Technician', related_name='repaircall_caller')
    call_time = models.DateTimeField()
    close_time = models.DateTimeField(blank=True, null=True)
    call_problem = models.TextField()
    call_reference = models.CharField(max_length=10, blank=True, null=True)
    close_comment = models.TextField(blank=True, null=True)
    close_tech = models.ForeignKey('Technician', blank=True, null=True, related_name='repaircall_closer')
    repair_tech = models.ForeignKey(RepairTechnician, blank=True, null=True)

    class Meta:
        db_table = 'repaircall'


class SerialNo(models.Model):
    support_item = models.ForeignKey("SupportItem")
    serial_no = models.CharField(max_length=30)
    assign_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'serial_no'


class Software(models.Model):
    support_item = models.OneToOneField("SupportItem")
    version = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'software'


class SoftwareItemType(models.Model):
    item_type = models.OneToOneField(ItemType)
    name = models.CharField(max_length=40)  # TODO: Remove. See ItemType

    class Meta:
        db_table = 'software_item_type'


class SupportItem(models.Model):
    contract = models.ForeignKey(MaintenanceContract, blank=True, null=True)
    description = models.CharField(max_length=30)
    producer = models.ForeignKey(Company, default=-1)
    item_type = models.ForeignKey(ItemType)
    order_item = models.ForeignKey(OrderItemMaterial, default=-1)
    comment = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'support_item'


class Technician(models.Model):
    employee = models.OneToOneField(Employee)

    class Meta:
        db_table = 'technician'


class Weekday(models.Model):
    day = models.CharField(max_length=10)

    class Meta:
        db_table = 'weekday'


class WorkDone(models.Model):
    call = models.ForeignKey(HelpdeskCall)
    technician = models.ForeignKey(Technician)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
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

