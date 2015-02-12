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

# Base of the Employee/Technician/Department/... inheritance chain
# TODO: see what happens if we make this abstract
class Caller(models.Model):
    """Base entity which can interact with the helpdesk system.""" 
    name      = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    active    = models.BooleanField(default=True)
    location  = models.CharField(max_length=30, blank=True, null=True)
    
    class Meta:
        db_table = 'caller'
    
    def __unicode__(self):
        if self.location is not None:
            return self.name + ' - ' + self.location
        else:
            return self.name

# Inherits from Caller
class Department(models.Model):
    """A business unit to which support items can be assigned."""
    name        = models.CharField(max_length=30)
    telephone   = models.CharField(max_length=15, blank=True, null=True)
    active      = models.BooleanField(default=True)
    location    = models.CharField(max_length=30, blank=True, null=True)
    end_of_life = models.BooleanField(default=False)

    class Meta:
        db_table = 'department'

    def __unicode__(self):
        if self.location is not None:
            return self.name + ' - ' + self.location
        else:
            return self.name

# Inherits caller
class Person(models.Model):
    """An actual person who can interact with the helpdesk."""
    name       = models.CharField(max_length=30)
    telephone  = models.CharField(max_length=15, blank=True, null=True)
    active     = models.BooleanField(default=True)
    location   = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'person'
    
    def __unicode__(self):
        return self.name

#Inherits from Person
class Employee(models.Model):
    """A person working for the business"""
    name       = models.CharField(max_length=30)
    telephone  = models.CharField(max_length=15, blank=True, null=True)
    active     = models.BooleanField(default=True)
    location   = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    department = models.ForeignKey(Department)

    class Meta:
        db_table = 'employee'

    def __unicode__(self):
        return self.name

# Inherits employee
class Technician(models.Model):
    """A person working for the business who can resolve tickets."""
    name       = models.CharField(max_length=30)
    telephone  = models.CharField(max_length=15, blank=True, null=True)
    active     = models.BooleanField(default=True)
    location   = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    department = models.ForeignKey(Department)

    class Meta:
        db_table = 'technician'
    
    def __unicode__(self):
        return self.name

# Inherits person
class RepairTechnician(models.Model):
    """A person working for an external entity who can provide support resolving tickets."""
    name       = models.CharField(max_length=30)
    telephone  = models.CharField(max_length=15, blank=True, null=True)
    active     = models.BooleanField(default=True)
    location   = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    company    = models.ForeignKey('Company', null=True)

    class Meta:
        db_table = 'repair_technician'
    
    def __unicode__(self):
        return self.name


class Company(models.Model):
    name      = models.CharField(max_length=50)
    street    = models.CharField(max_length=40, blank=True, null=True)
    city      = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    postcode  = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'company'
        verbose_name_plural = 'companies'
    
    def __unicode__(self):
        return self.name

# Inherits from Company
class Contractor(models.Model):
    name      = models.CharField(max_length=50)
    street    = models.CharField(max_length=40, blank=True, null=True)
    city      = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    postcode  = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'contractor'
    
    def __unicode__(self):
        return self.name

# Handled by the MaintenanceContract admin page
class CoverPeriod(models.Model):
    contract   = models.ForeignKey('MaintenanceContract')
    weekday    = models.IntegerField()
    start_time = models.TimeField()
    end_time   = models.TimeField()

    class Meta:
        db_table = 'cover_period'

# Base of hardware_item_type and software_item_type
# TODO: Can this be made abstract?
class ItemType(models.Model):
    """Base of all support item types"""
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'item_type'
    
    def __unicode__(self):
        return self.name

# Inherits item_type
class HardwareItemType(models.Model):
    """Supported hardware types"""
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'hardware_item_type'
    
    def __unicode__(self):
        return self.name

# Inherits item_type
class SoftwareItemType(models.Model):
    """Supported software types"""
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'software_item_type'
    
    def __unicode__(self):
        return self.name


# Base of software and hardware
# TODO: see if this can be made abstract
class SupportItem(models.Model):
    """Base of all supported items"""
    contract    = models.ForeignKey('MaintenanceContract', null=True)
    description = models.CharField(max_length=30)
    producer    = models.ForeignKey(Company, null=True)
    item_type   = models.ForeignKey(ItemType)
    order_item  = models.ForeignKey('OrderItem', null=True)
    comment     = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'support_item'
    
    def __unicode__(self):
        return self.description

# Inherits from support_item
class Hardware(models.Model):
    """Supported hardware item"""
    contract    = models.ForeignKey('MaintenanceContract', null=True)
    description = models.CharField(max_length=30)
    producer    = models.ForeignKey(Company, null=True)
    item_type   = models.ForeignKey(HardwareItemType)
    order_item  = models.ForeignKey('OrderItem', null=True)
    comment     = models.TextField(blank=True, null=True)
    part_no     = models.CharField(max_length=20, blank=True, null=True)
    hostname    = models.CharField(max_length=20, blank=True, null=True)
    idms_name   = models.CharField(max_length=8, blank=True, null=True)
    ip_address  = models.IntegerField(verbose_name='IP address', blank=True, null=True)
    tag         = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        db_table = 'hardware'
        verbose_name_plural = 'hardware'
    
    def __unicode__(self):
        return self.description

# Inherits support_item
class Software(models.Model):
    """Supported software items"""
    contract    = models.ForeignKey('MaintenanceContract', null=True)
    description = models.CharField(max_length=30)
    producer    = models.ForeignKey(Company, null=True)
    item_type   = models.ForeignKey(SoftwareItemType)
    order_item  = models.ForeignKey('OrderItem', null=True)
    comment     = models.TextField(blank=True, null=True)
    version     = models.CharField(max_length=15, null=True)

    class Meta:
        db_table = 'software'
        verbose_name_plural = 'software'
    
    def __unicode__(self):
        return self.description

# This is a fake definition to stop Django complaining that there is no relationship with Hardware
class HardwareSerialNo(models.Model):
    item = models.ForeignKey(Hardware)
    serial_no = models.CharField(max_length=30)
    assign_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'serial_no'
    
    def __unicode__(self):
        return self.serial_no

# This is a fake definition to stop Django complaining that there is no relationship with Software
class SoftwareSerialNo(models.Model):
    item = models.ForeignKey(Software)
    serial_no = models.CharField(max_length=30)
    assign_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'serial_no'
    
    def __unicode__(self):
        return self.serial_no

# This is the real definition, but at the moment, no idea how to make Django like it.
class SerialNo(models.Model):
    item = models.ForeignKey(SupportItem)
    serial_no = models.CharField(max_length=30)
    assign_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'serial_no'
    
    def __unicode__(self):
        return self.serial_no

# Same problem as with the serial numbers: Django is not happy that there is no explicit FK
# relationship between the hardware & software classes and the placement class.
class HardwarePlacement(models.Model):
    item       = models.ForeignKey('Hardware')
    place_date = models.DateTimeField()
    department = models.ForeignKey(Department)
    location   = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'placement'
    
    def __unicode__(self):
        return self.location

class SoftwarePlacement(models.Model):
    item       = models.ForeignKey('Software')
    place_date = models.DateTimeField()
    department = models.ForeignKey(Department)
    location   = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'placement'
    
    def __unicode__(self):
        return self.location

# This is the true placement model but it can not be used in the Django admin module.
class Placement(models.Model):
    item       = models.ForeignKey('SupportItem')
    place_date = models.DateTimeField()
    department = models.ForeignKey(Department)
    location   = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'placement'
    
    def __unicode__(self):
        return self.location

class HelpdeskCall(models.Model):
    caller          = models.ForeignKey(Caller, null=True)
    call_time       = models.DateTimeField()
    call_recorder   = models.ForeignKey('Technician', related_name='call_recorder')
    problem_type    = models.TextField(blank=True, null=True)
    item            = models.ForeignKey('SupportItem')
    assigned_tech   = models.ForeignKey('Technician', blank=True, null=True, related_name = 'assigned_tech')
    closing_time    = models.DateTimeField(blank=True, null=True)
    closing_comment = models.TextField(blank=True, null=True)
    closing_tech    = models.ForeignKey('Technician', blank=True, null=True, related_name = 'closing_tech')

    class Meta:
        db_table = 'helpdesk_call'
    
    def __unicode__(self):
        return self.problem_type


class MaintenanceContract(models.Model):
    code = models.CharField(max_length=4)
    contractor = models.ForeignKey(Contractor, db_column='contractor', null=True)
    description = models.CharField(max_length=35, blank=True, null=True)
    
    class Meta:
        db_table = 'maintenance_contract'
    
    def __unicode__(self):
        return self.description

class MaterialOrder(models.Model):
    order_id = models.CharField(max_length=15)
    order_date = models.DateField()
    to_exec_committee = models.DateField(blank=True, null=True)
    to_supply_dept = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=80, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    private_comment = models.TextField(blank=True, null=True)
    supplier = models.ForeignKey(Company, db_column='supplier')

    class Meta:
        db_table = 'material_order'
    
    def __unicode__(self):
        return self.description

class OrderItem(models.Model):
    mat_order = models.ForeignKey(MaterialOrder)
    discount = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)
    department = models.ForeignKey(Department, null=True)
    description = models.CharField(max_length=20, blank=True, null=True)
    price_per_unit = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    item_type = models.ForeignKey(ItemType)

    class Meta:
        db_table = 'order_item'
    
    def __unicode__(self):
        return self.description

class Repaircall(models.Model):
    helpdeskcall   = models.ForeignKey(HelpdeskCall)
    call_tech      = models.ForeignKey('Technician', related_name='call_tech')
    call_time      = models.DateTimeField()
    close_time     = models.DateTimeField(blank=True, null=True)
    call_problem   = models.TextField()
    call_reference = models.CharField(max_length=10, blank=True, null=True)
    close_comment  = models.TextField(blank=True, null=True)
    close_tech     = models.ForeignKey('Technician', blank=True, null=True, related_name='close_tech')
    repair_tech    = models.ForeignKey(RepairTechnician, blank=True, null=True)
    
    class Meta:
        db_table = 'repaircall'
        verbose_name_plural = "repair calls"
    
    def __unicode__(self):
        return self.call_problem

class Weekday(models.Model):
    day = models.CharField(max_length=10)

    class Meta:
        db_table = 'weekday'
    
    def __unicode__(self):
        return self.day

class WorkDone(models.Model):
    call       = models.ForeignKey(HelpdeskCall)
    technician = models.ForeignKey(Technician)
    start_time = models.DateTimeField()
    end_time   = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'work_done'
        verbose_name_plural = 'work done'

# Views defined on the app database

class VwActiveDesktops(models.Model):
    tag         = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    department  = models.CharField(max_length=30, blank=True, null=True)
    assignee    = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_active_desktops'

class VwActiveLaptops(models.Model):
    tag = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)
    assignee = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vw_active_laptops'

class VwFirstAssignedDept(models.Model):
    item = models.IntegerField(blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    department_name = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    place_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vw_first_assigned_dept'

class VwInventory(models.Model):
    tag = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    mfg = models.CharField(max_length=50, blank=True, null=True)
    part_no = models.CharField(max_length=20, blank=True, null=True)
    serial_no = models.CharField(max_length=30, blank=True, null=True)
    item_type = models.CharField(max_length=40, blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)
    campus = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vw_inventory'

class VwLastAssignedDept(models.Model):
    item = models.IntegerField(blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    place_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vw_last_assigned_dept'

class VwLastAssignedSerial(models.Model):
    item = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=30, blank=True, null=True)
    assign_date = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vw_last_assigned_serial'

class VwSupportItem(models.Model):
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'vw_support_item'

class VwSupportedHardSoft(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    item_type = models.IntegerField(blank=True, null=True)
    item_type_name = models.CharField(max_length=40, blank=True, null=True)
    host_ver = models.CharField(max_length=20, blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    serial_no = models.CharField(max_length=30, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vw_supported_hard_soft'
