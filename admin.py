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

# from admin_aid.forms import OrderItemForm
from admin_aid.filters import HardwareItemTypeFilter, SoftwareItemTypeFilter
from navigation.admin import NavigableModelAdmin
from app.models import *

# Evil wart to solve the list_display mess
# See https://code.djangoproject.com/ticket/5863
def lookup(field_name):
    def accessor(obj):
        val = obj
        for part in field_name.split('__'):
            val = getattr(val, part)
        return val
    accessor.__name__ = field_name
    return accessor

# Register your models here.
class CallerAdmin(NavigableModelAdmin):
    nav_item = 'nav_caller'
    ordering = ('name',)
    
admin.site.register(Caller, CallerAdmin)


class CompanyAdmin(NavigableModelAdmin):
    nav_item = 'nav_company'
    ordering = ('name',) 
    
admin.site.register(Company, CompanyAdmin)


class ContractorAdmin(NavigableModelAdmin):
    nav_item = 'nav_contractor'
    ordering = ('company__name',)

admin.site.register(Contractor, ContractorAdmin)


class DepartmentAdmin(NavigableModelAdmin):
    nav_item = 'nav_department'

    ordering = ('caller__name',)
    list_filter = ['caller__active']
    list_display = [lookup('caller__name'), lookup('caller__location')]
    list_display_links = list_display
    
admin.site.register(Department, DepartmentAdmin)


class EmployeeAdmin(NavigableModelAdmin):
    nav_item = 'nav_employee'
    
    ordering = ('person__caller__name', 'person__first_name')
    list_display = [lookup('person__caller__name'), lookup('person__first_name')]
    list_display_links = list_display
#    fieldsets = (
#        (None, {
#            'fields': (('first_name', 'name'), 'telephone', 'active')
#        }),
#        ('Workplace', {
#            'fields': ('department', 'location')
#        }),
#    )

admin.site.register(Employee, EmployeeAdmin)


class WorkDoneInline(admin.TabularInline):
    model = WorkDone
    extra = 0

class HelpdeskCallAdmin(NavigableModelAdmin):
    nav_item = 'nav_helpdesk'
    inlines = [WorkDoneInline]
    fieldsets = (
        (None, {
            'fields': (('caller', 'call_time', 'call_recorder'), 'problem_type', 'item')
        }),
        ('Techs', {
            'fields': ('assigned_tech', )
        }),
        ('Closing', {
            'classes': ('collapse', ),
            'fields': (('closing_time', 'closing_tech'), 'closing_comment')
        })
    )

admin.site.register(HelpdeskCall, HelpdeskCallAdmin)


class ItemTypeAdmin(NavigableModelAdmin):
    nav_item = 'nav_inventory_type'
    ordering = ('name',)
    
admin.site.register(ItemType, ItemTypeAdmin)


class SupportItemAdmin(NavigableModelAdmin):
    nav_item = 'nav_inventory'

admin.site.register(SupportItem, SupportItemAdmin)


class HardwareItemTypeAdmin(NavigableModelAdmin):
    nav_item = 'nav_inv_type_hardw'
    
    ordering = ('item_type__name',)

admin.site.register(HardwareItemType, HardwareItemTypeAdmin)


class SoftwareItemTypeAdmin(NavigableModelAdmin):
    nav_item = 'nav_inv_type_softw'
    
    ordering = ('item_type__name',)

admin.site.register(SoftwareItemType, SoftwareItemTypeAdmin)


#class HardwareSerialInline(admin.TabularInline):
#    model = HardwareSerialNo
#    extra = 0

#class HardwarePlacementInline(admin.TabularInline):
#    model = HardwarePlacement
#    extra = 0

class HardwareAdmin(NavigableModelAdmin):
    nav_item = 'nav_inv_hardw'
    
    ordering = ('support_item__item_type', 'part_no', 'support_item__description')
    list_display = ['tag', 'part_no', lookup('support_item__description')]
    list_display_links = list_display
    list_filter = [HardwareItemTypeFilter]
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
    
admin.site.register(Hardware, HardwareAdmin)


#class SoftwareSerialInline(admin.TabularInline):
#    model = SoftwareSerialNo
#    extra = 0

#class SoftwarePlacementInline(admin.TabularInline):
#    model = SoftwarePlacement
#    extra = 0

class SoftwareAdmin(NavigableModelAdmin):
    nav_item = 'nav_inv_softw'

    ordering = ('support_item__item_type', 'support_item__description', 'version')
    list_display = [lookup('support_item__description'), 'version']
    list_display_links = list_display
    list_filter = [SoftwareItemTypeFilter]
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

admin.site.register(Software, SoftwareAdmin)


class CoverPeriodInline(admin.TabularInline):
    model = CoverPeriod
    extra = 0
    
class MaintenanceContractAdmin(NavigableModelAdmin):
    nav_item = 'nav_contract'
    inlines = [CoverPeriodInline,]
    
admin.site.register(MaintenanceContract, MaintenanceContractAdmin)


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

class MaterialOrderAdmin(NavigableModelAdmin):
    nav_item = 'nav_order'
    
    date_hierarchy = 'order_date'
    ordering = ['-order_date']
    list_display = ['order_no', 'description']
    list_display_links = list_display
#    inlines = [OrderItemInline]
    fieldsets = (
        (None, {
            'fields': (('order_id', 'supplier'), ('order_date', 'to_exec_committee', 'to_supply_dept'), 'description')
        }),
        ('Comments', {
            'classes': ('collapse',),
           'fields': ('comment', 'private_comment')
        }),
    )

admin.site.register(MaterialOrder, MaterialOrderAdmin)


class PersonAdmin(NavigableModelAdmin):
    nav_item = 'nav_person'

    ordering = ('caller__name', 'first_name')
    list_display = [lookup('caller__name'), 'first_name']
    list_display_links = list_display
    fieldsets = (
        (None, {
            'fields': (('first_name', 'name'), 'telephone', 'active')
        }),
        ('Workplace', {
            'fields': ('location',)
        }),
    )
    
admin.site.register(Person, PersonAdmin)


class TechnicianAdmin(NavigableModelAdmin):
    nav_item = 'nav_technician'

    ordering = ('employee__person__caller__name', 'employee__person__first_name')
    list_display = [lookup('employee__person__caller__name'), lookup('employee__person__first_name')]
    list_display_links = list_display
#    fieldsets = (
#        (None, {
#            'fields': (('first_name', 'name'), 'telephone', 'active')
#        }),
#        ('Workplace', {
#            'fields': ('department', 'location')
#        }),
#    )

admin.site.register(Technician, TechnicianAdmin)


class RepairCallAdmin(NavigableModelAdmin):
    nav_item = 'nav_repaircall'

    fieldsets = (
        (None, {
            'fields': ('helpdeskcall', ('call_tech', 'call_time', 'call_reference'), 'call_problem', 'repair_tech')
        }),
        ('Closing', { 
            'classes': ('collapse', ),
            'fields': ('close_comment', ('close_time', 'close_tech'))
        })
    )

admin.site.register(RepairCall, RepairCallAdmin)


class RepairTechnicianAdmin(NavigableModelAdmin):
    nav_item = 'nav_repairtech'
    
    ordering = ('person__caller__name', 'person__first_name')
    list_display = [lookup('person__caller__name'), lookup('person__first_name')]
    list_display_links = list_display
#    fieldsets = (
#        (None, {
#            'fields': (('first_name', 'name'), 'telephone', 'active')
#        }),
#        ('Workplace', {
#            'fields': ('company', 'location')
#        }),
#    )

admin.site.register(RepairTechnician, RepairTechnicianAdmin)