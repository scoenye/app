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

from django.contrib import admin

#from admin_aid.forms import OrderItemForm
from admin_aid.filters import HardwareItemTypeFilter, SoftwareItemTypeFilter
from app.models import *

# Register your models here.
#class CompanyAdmin(admin.ModelAdmin):
#    ordering = ('name',) 
#    
#admin.site.register(Company, CompanyAdmin)

# Recycle the CompanyAdmin as long as the tables are identical
#admin.site.register(Contractor, CompanyAdmin)

#class DepartmentAdmin(admin.ModelAdmin):
#    ordering = ('name',)
#    list_filter = ['active']
#    list_display = ['name', 'location']
#    list_display_links = list_display
#    
#admin.site.register(Department, DepartmentAdmin)

#class EmployeeAdmin(admin.ModelAdmin):
#    ordering = ('name', 'first_name')
#    list_display = ['name', 'first_name']
#    list_display_links = list_display
#    fieldsets = (
#        (None, {
#            'fields': (('first_name', 'name'), 'telephone', 'active')
#        }),
#        ('Workplace', {
#            'fields': ('department', 'location')
#        }),
#    )
#
#admin.site.register(Employee, EmployeeAdmin)

#class WorkDoneInline(admin.TabularInline):
#    model = WorkDone
#    extra = 0

#class HelpdeskCallAdmin(admin.ModelAdmin):
#    inlines = [WorkDoneInline]
#    fieldsets = (
#        (None, {
#            'fields': (('caller', 'call_time', 'call_recorder'), 'problem_type', 'item')
#        }),
#        ('Techs', {
#            'fields': ('assigned_tech', )
#        }),
#        ('Closing', {
#            'classes': ('collapse', ),
#            'fields': (('closing_time', 'closing_tech'), 'closing_comment')
#        })
#    )

#admin.site.register(HelpdeskCall, HelpdeskCallAdmin)

#class ItemTypeAdmin(admin.ModelAdmin):
#    ordering = ('name',)

#admin.site.register(HardwareItemType, ItemTypeAdmin)

#admin.site.register(SoftwareItemType, ItemTypeAdmin)

#class HardwareSerialInline(admin.TabularInline):
#    model = HardwareSerialNo
#    extra = 0

#class HardwarePlacementInline(admin.TabularInline):
#    model = HardwarePlacement
#    extra = 0

#class HardwareAdmin(admin.ModelAdmin):
#    ordering = ('item_type', 'part_no', 'description')
#    list_display = ['tag', 'part_no', 'description']
#    list_display_links = list_display
#    list_filter = [HardwareItemTypeFilter]
#    inlines = [HardwareSerialInline, HardwarePlacementInline]
#    fieldsets = (
#        (None, {
#            'fields': (('tag', 'description'), ('producer', 'part_no'), 'item_type', 'comment', ('hostname', 'ip_address'))
#        }),
#        ('Paperwork', {
#            'classes': ('collapse', ),
#            'fields': (('contract', 'order_item'), )
#        })
#    )
#    
#admin.site.register(Hardware, HardwareAdmin)

#class SoftwareSerialInline(admin.TabularInline):
#    model = SoftwareSerialNo
#    extra = 0

#class SoftwarePlacementInline(admin.TabularInline):
#    model = SoftwarePlacement
#    extra = 0

#class SoftwareAdmin(admin.ModelAdmin):
#    ordering = ('item_type', 'description', 'version')
#    list_display = ['description', 'version']
#    list_display_links = list_display
#    list_filter = [SoftwareItemTypeFilter]
#    inlines = [SoftwareSerialInline, SoftwarePlacementInline]
#    fieldsets = (
#        (None, {
#            'fields': ('description', ('producer', 'item_type'), 'comment')
#        }),
#        ('Paperwork', {
#            'classes': ('collapse', ),
#            'fields': (('contract', 'order_item'), )
#        })
#    )
#
#admin.site.register(Software, SoftwareAdmin)

#class CoverPeriodInline(admin.TabularInline):
#    model = CoverPeriod
#    extra = 0
    
#class MaintenanceContractAdmin(admin.ModelAdmin):
#    inlines = [CoverPeriodInline,]
#    
#admin.site.register(MaintenanceContract, MaintenanceContractAdmin)

#class OrderItemInline(admin.TabularInline):
#    form = OrderItemForm
#    model = OrderItem
#    extra = 0
#    fieldsets = (
#        (None, {
#            'fields': ('quantity', 'description', 'department', 'item_type', 'completed')
#        }),
#        ('Extended', {
#            'fields': ('discount', 'tax', 'price_per_unit')
#        }),
#    )

#class MaterialOrderAdmin(admin.ModelAdmin):
#    date_hierarchy = 'order_date'
#    ordering = ['-order_date']
#    list_display = ['order_id', 'description']
#    list_display_links = list_display
#    inlines = [OrderItemInline]
#    fieldsets = (
#        (None, {
#            'fields': (('order_id', 'supplier'), ('order_date', 'to_exec_committee', 'to_supply_dept'), 'description')
#        }),
#        ('Comments', {
#            'classes': ('collapse',),
#            'fields': ('comment', 'private_comment')
#        }),
#    )
#
#admin.site.register(MaterialOrder, MaterialOrderAdmin)

#class PersonAdmin(admin.ModelAdmin):
#    ordering = ('name', 'first_name')
#    list_display = ['name', 'first_name']
#    list_display_links = list_display
#    fieldsets = (
#        (None, {
#            'fields': (('first_name', 'name'), 'telephone', 'active')
#        }),
#        ('Workplace', {
#            'fields': ('location',)
#        }),
#    )
#    
#admin.site.register(Person, PersonAdmin)

#admin.site.register(Technician, EmployeeAdmin)

#class RepairCallAdmin(admin.ModelAdmin):
#    fieldsets = (
#        (None, {
#            'fields': ('helpdeskcall', ('call_tech', 'call_time', 'call_reference'), 'call_problem', 'repair_tech')
#        }),
#        ('Closing', { 
#            'classes': ('collapse', ),
#            'fields': ('close_comment', ('close_time', 'close_tech'))
#        })
#    )
#
#admin.site.register(Repaircall, RepairCallAdmin)

#class RepairTechnicianAdmin(admin.ModelAdmin):
#    ordering = ('name', 'first_name')
#    list_display = ['name', 'first_name']
#    list_display_links = list_display
#    fieldsets = (
#        (None, {
#            'fields': (('first_name', 'name'), 'telephone', 'active')
#        }),
#        ('Workplace', {
#            'fields': ('company', 'location')
#        }),
#    )
#
#admin.site.register(RepairTechnician, RepairTechnicianAdmin)