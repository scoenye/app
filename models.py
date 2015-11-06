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
from django.db.models import Q


class Caller(models.Model):
    name      = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    active    = models.BooleanField(default=True)
    location  = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'caller'

    def __unicode__(self):
        if self.location is not None:
            return self.name + ' - ' + self.location
        else:
            return self.name

class Department(Caller):
    end_of_life = models.BooleanField(default=False)

    class Meta:
        db_table = 'department'

class Person(Caller):
    first_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'person'

    def __unicode__(self):
        return self.name

class RepairTechnician(Person):
    company = models.ForeignKey('Company')

    class Meta:
        db_table = 'repair_technician'

class Employee(Person):
    department = models.ForeignKey(Department)

    class Meta:
        db_table = 'employee'

class Technician(Employee):

    class Meta:
        db_table = 'technician'

# ---------------------------------------------------------------------
class Company(models.Model):
    name      = models.CharField(max_length=50)
    street    = models.CharField(max_length=40, null=True, blank=True)
    city      = models.CharField(max_length=20, null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    postcode  = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'company'
        verbose_name_plural = 'companies'

    def __unicode__(self):
        return self.name

class Contractor(Company):

    class Meta:
        db_table = 'contractor'

# ---------------------------------------------------------------------
class ItemType(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'item_type'

    def __unicode__(self):
        return self.name

class ConsumableItemType(ItemType):

    class Meta:
        db_table = 'consumable_item_type'


class HardwareItemType(ItemType):
    consumer = models.BooleanField(default=False)

    class Meta:
        db_table = 'hardware_item_type'


class SoftwareItemType(ItemType):

    class Meta:
        db_table = 'software_item_type'


# ---------------------------------------------------------------------
class CoverPeriod(models.Model):
    contract   = models.ForeignKey('MaintenanceContract')
    weekday    = models.ForeignKey("Weekday")
    start_time = models.TimeField()
    end_time   = models.TimeField()

    class Meta:
        db_table = 'cover_period'


class MaintenanceContract(models.Model):
    code        = models.CharField(max_length=4)
    contractor  = models.ForeignKey(Contractor)
    description = models.CharField(max_length=35, null=True, blank=True)

    class Meta:
        db_table = 'maintenance_contract'

    def __unicode__(self):
        return self.description

# ---------------------------------------------------------------------
class MaterialOrder(models.Model):
    order_no          = models.CharField(max_length=15)      # pg does not like 'order' as a field name
    order_date        = models.DateField()
    to_exec_committee = models.DateField(blank=True, null=True)
    to_supply_dept    = models.DateField(blank=True, null=True)
    description       = models.CharField(max_length=80, blank=True, null=True)
    comment           = models.TextField(blank=True, null=True)
    private_comment   = models.TextField(blank=True, null=True)
    supplier          = models.ForeignKey(Company)
    supplier_ref      = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'material_order'

    def __unicode__(self):
        return self.description

# ---------------------------------------------------------------------
class OrderItem(models.Model):
    mat_order   = models.ForeignKey(MaterialOrder)
    completed   = models.DateField(blank=True, null=True)
    department  = models.ForeignKey(Department)
    description = models.CharField(max_length=20, blank=True, null=True)
    quantity    = models.IntegerField(default=1)

    class Meta:
        db_table = 'order_item'

    def __unicode__(self):
        return unicode(self.description)


class OrderItemConsumable(OrderItem):
    item = models.ForeignKey('Consumable')

    class Meta:
        db_table = 'order_item_consumable'


class OrderItemMaterial(OrderItem):
    discount       = models.FloatField(blank=True, null=True)
    tax            = models.FloatField(blank=True, null=True)
    price_per_unit = models.FloatField(blank=True, null=True)
    item_type      = models.ForeignKey(ItemType)

    class Meta:
        db_table = 'order_item_material'

# ---------------------------------------------------------------------
class SupportItem(models.Model):
    contract    = models.ForeignKey(MaintenanceContract, blank=True, null=True)
    description = models.CharField(max_length=30)
    producer    = models.ForeignKey(Company, default=-1)
    comment     = models.TextField(null=True, blank=True)
    inventoried = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'support_item'

    def __unicode__(self):
        return unicode(self.description)

class Consumable(SupportItem):
    item_type = models.ForeignKey(ConsumableItemType)
    part_no   = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'consumable'

class Hardware(SupportItem):
    item_type   = models.ForeignKey(HardwareItemType)
    part_no     = models.CharField(max_length=20, blank=True, null=True)
    hostname    = models.CharField(max_length=20, blank=True, null=True)
    idms_name   = models.CharField(max_length=8, blank=True, null=True)
    ip_address  = models.IntegerField(verbose_name='IP address', blank=True, null=True)
    tag         = models.IntegerField(unique=True, blank=True, null=True)
    order_item  = models.ForeignKey(OrderItemMaterial, default=-1, limit_choices_to=Q())

    class Meta:
        db_table = 'hardware'
        verbose_name_plural = 'hardware'

class Software(SupportItem):
    item_type   = models.ForeignKey(SoftwareItemType)
    version     = models.CharField(max_length=15, blank=True, null=True)
    order_item  = models.ForeignKey(OrderItemMaterial, default=-1)

    class Meta:
        db_table = 'software'
        verbose_name_plural = 'software'

# ---------------------------------------------------------------------
class Placement(models.Model):
    support_item = models.ForeignKey("SupportItem")
    place_date   = models.DateTimeField()
    department   = models.ForeignKey(Department, default = -1)
    location     = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'placement'

    def __unicode__(self):
        return unicode(self.location)

class Dispensed(Placement):
    consumer = models.ForeignKey('Hardware')
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'dispensed'
        verbose_name_plural = 'dispensed'


# ---------------------------------------------------------------------
class HelpdeskCall(models.Model):
    caller          = models.ForeignKey(Caller)
    call_time       = models.DateTimeField()
    call_recorder   = models.ForeignKey('Technician', related_name='helpdeskcall_recorder')
    problem_type    = models.TextField(blank=True, null=True)
    item            = models.ForeignKey('NonConsumable')
    assigned_tech   = models.ForeignKey('Technician', blank=True, null=True, related_name='helpdeskcall_assignee')
    closing_time    = models.DateTimeField(blank=True, null=True)
    closing_comment = models.TextField(blank=True, null=True)
    closing_tech    = models.ForeignKey('Technician', blank=True, null=True, related_name='helpdeskcall_closer')

    class Meta:
        db_table = 'helpdesk_call'

    def __unicode__(self):
        return self.problem_type

# ---------------------------------------------------------------------
class RepairCall(models.Model):
    helpdeskcall   = models.ForeignKey(HelpdeskCall)
    call_tech      = models.ForeignKey('Technician', related_name='repaircall_caller')
    call_time      = models.DateTimeField()
    close_time     = models.DateTimeField(blank=True, null=True)
    call_problem   = models.TextField()
    call_reference = models.CharField(max_length=10, blank=True, null=True)
    close_comment  = models.TextField(blank=True, null=True)
    close_tech     = models.ForeignKey('Technician', blank=True, null=True, related_name='repaircall_closer')
    repair_tech    = models.ForeignKey(RepairTechnician, blank=True, null=True)

    class Meta:
        db_table = 'repaircall'
        verbose_name_plural = "repair calls"
    
    def __unicode__(self):
        return self.call_problem


class SerialNo(models.Model):
    support_item = models.ForeignKey("SupportItem")
    serial_no    = models.CharField(max_length=30)
    assign_date  = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'serial_no'

    def __unicode__(self):
        return unicode(self.serial_no)

class Weekday(models.Model):
    day = models.CharField(max_length=10)

    class Meta:
        db_table = 'weekday'


class WorkDone(models.Model):
    call       = models.ForeignKey(HelpdeskCall)
    technician = models.ForeignKey(Technician)
    start_time = models.DateTimeField()
    end_time   = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'work_done'
        verbose_name_plural = 'work done'


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


class ConsumableOnHand(models.Model):
    consumable = models.OneToOneField(Consumable, primary_key=True, db_column="consumable_id", related_name="inventory")
    on_hand = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vw_consumable_onhand'


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


class HardwareLastAssigned(models.Model):
    hardware = models.OneToOneField(Hardware, primary_key=True, db_column='support_item_id', related_name='last_assigned')
    department = models.ForeignKey(Department, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=50, blank=True)
    place_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_last_assigned_dept'


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


class NonConsumable(models.Model):
    support_item = models.OneToOneField(SupportItem, primary_key=True)
    description = models.CharField(max_length=30, blank=True)
    item_type = models.ForeignKey(ItemType)
    item_type_name = models.CharField(max_length=40, blank=True)
    tag_ver = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(Department)
    location = models.CharField(max_length=50, blank=True)
    serial_no = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'vw_nonconsumables'

    def __unicode__(self):
        return unicode(self.tag_ver) + ' - ' + unicode(self.item_type_name) + ' - ' + unicode(self.description)