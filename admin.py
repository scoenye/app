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

from admin_aid.forms import OrderItemMaterialForm, OrderItemConsumableForm
from admin_aid.forms import HelpdeskCallForm, DispenseForm
from admin_aid.filters import HardwareItemTypeFilter, SoftwareItemTypeFilter, ConsumableItemTypeFilter
from admin_aid.filters import DispensedItemTypeFilter, PlacementFilter, ConsumerFilter
from navigation.admin import NavigableModelAdmin
from app.models import *

# Register your models here.
class CallerAdmin(NavigableModelAdmin):
    nav_item = 'nav_caller'

    ordering = ('name',)
    list_filter = ['active']
    list_display = ['name', 'location']
    list_display_links = list_display
    
admin.site.register(Caller, CallerAdmin)


class DepartmentAdmin(NavigableModelAdmin):
    nav_item = 'nav_department'

    ordering = ('name',)
    list_filter = ['active']
    list_display = ['name', 'location']
    list_display_links = list_display
    
admin.site.register(Department, DepartmentAdmin)


class PersonAdmin(NavigableModelAdmin):
    nav_item = 'nav_person'

    ordering = ('name', 'first_name')
    list_filter = ['active']
    list_display = ['name', 'first_name']
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


class RepairTechnicianAdmin(NavigableModelAdmin):
    nav_item = 'nav_repairtech'
    
    ordering = ('name', 'first_name')
    list_filter = ['active']
    list_display = ['name', 'first_name']
    list_display_links = list_display

    fieldsets = (
        (None, {
            'fields': (('first_name', 'name'), 'telephone', 'active')
        }),
        ('Workplace', {
            'fields': ('company', 'location')
        }),
    )

admin.site.register(RepairTechnician, RepairTechnicianAdmin)


class EmployeeAdmin(NavigableModelAdmin):
    nav_item = 'nav_employee'
    
    ordering = ('name', 'first_name')
    list_filter = ['active']
    list_display = ['name', 'first_name']
    list_display_links = list_display

    fieldsets = (
        (None, {
            'fields': (('first_name', 'name'), 'telephone', 'active')
        }),
        ('Workplace', {
            'fields': ('department', 'location')
        }),
    )

admin.site.register(Employee, EmployeeAdmin)


class TechnicianAdmin(NavigableModelAdmin):
    nav_item = 'nav_technician'

    ordering = ('name', 'first_name')
    list_filter = ['active']
    list_display = ['name', 'first_name']
    list_display_links = list_display

    fieldsets = (
        (None, {
            'fields': (('first_name', 'name'), 'telephone', 'active')
        }),
        ('Workplace', {
            'fields': ('department', 'location')
        }),
    )

admin.site.register(Technician, TechnicianAdmin)

#------------------------------------------------------------------------------
class CompanyAdmin(NavigableModelAdmin):
    nav_item = 'nav_company'
    ordering = ('name',) 
    
admin.site.register(Company, CompanyAdmin)


class ContractorAdmin(NavigableModelAdmin):
    nav_item = 'nav_contractor'
    ordering = ('name',)

admin.site.register(Contractor, ContractorAdmin)

#------------------------------------------------------------------------------
class WorkDoneInline(admin.TabularInline):
    model = WorkDone
    extra = 0

class HelpdeskCallAdmin(NavigableModelAdmin):
    nav_item = 'nav_helpdesk'
    inlines = [WorkDoneInline]
    form = HelpdeskCallForm

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

#------------------------------------------------------------------------------
class ItemTypeAdmin(NavigableModelAdmin):
    nav_item = 'nav_inventory_type'
    ordering = ('name',)
    
admin.site.register(ItemType, ItemTypeAdmin)


class HardwareItemTypeAdmin(NavigableModelAdmin):
    nav_item = 'nav_inv_type_hardw'
    
    ordering = ('name',)

admin.site.register(HardwareItemType, HardwareItemTypeAdmin)


class SoftwareItemTypeAdmin(NavigableModelAdmin):
    nav_item = 'nav_inv_type_softw'
    
    ordering = ('name',)

admin.site.register(SoftwareItemType, SoftwareItemTypeAdmin)


class ConsumableItemTypeAdmin(NavigableModelAdmin):
    nav_item = 'nav_inv_type_cons'
    
    ordering = ('name',)
                
admin.site.register(ConsumableItemType, ConsumableItemTypeAdmin)

#------------------------------------------------------------------------------
class SupportItemAdmin(NavigableModelAdmin):
    nav_item = 'nav_inventory'

admin.site.register(SupportItem, SupportItemAdmin)


class SerialInline(admin.TabularInline):
    model = SerialNo
    ordering = ['-assign_date']
    extra = 0

class PlacementInline(admin.TabularInline):
    model = Placement
    ordering = ['-place_date']
    extra = 0

class HardwareAdmin(NavigableModelAdmin):
    nav_item = 'nav_inv_hardw'

    ordering = ('item_type', 'part_no', 'description')
    list_display = ['tag', 'manufacturer', 'part_no', 'description', 'placement']
    list_display_links = list_display
    list_filter = [HardwareItemTypeFilter, PlacementFilter]
    search_fields = ['tag', 'last_assigned__location']
    inlines = [SerialInline, PlacementInline]

    fieldsets = (
        (None, {
            'fields': (('tag', 'description'), ('producer', 'part_no'), 'item_type', 'comment', ('hostname', 'ip_address'))
        }),
        ('Paperwork', {
            'classes': ('collapse', ),
            'fields': (('contract', 'order_item'), )
        })
    )
    
    def manufacturer(self, obj):
        return obj.producer.name

    def placement(self, obj):
        return obj.last_assigned.location
    
    def get_queryset(self, request):
        hardware = super(HardwareAdmin, self).get_queryset(request)
        hardware = hardware.select_related("inventory", "item_type", "last_assigned", "producer")

        return hardware

admin.site.register(Hardware, HardwareAdmin)


class SoftwareAdmin(NavigableModelAdmin):
    nav_item = 'nav_inv_softw'

    ordering = ('item_type', 'description', 'version')
    list_display = ['description', 'version']
    list_display_links = list_display
    list_filter = [SoftwareItemTypeFilter]
    inlines = [SerialInline, PlacementInline]

    fieldsets = (
        (None, {
            'fields': ('description', ('producer', 'item_type'), 'comment')
        }),
        ('Paperwork', {
            'classes': ('collapse', ),
            'fields': (('contract', 'order_item'), )
        })
    )

    def get_queryset(self, request):
        software = super(SoftwareAdmin, self).get_queryset(request)
        software = software.select_related("inventory", "item_type", "last_assigned", "producer")

        return software

admin.site.register(Software, SoftwareAdmin)

#--------------------------------------------------------------------
class ConsumableAdmin(NavigableModelAdmin):
    nav_item = 'nav_inv_cons'

    ordering = ('-item_type', 'description')
    list_display = ['item_type', 'part_no', 'description', 'on_hand']
    list_display_links = list_display
    list_filter = [ConsumableItemTypeFilter]
    
    fieldsets = (
        (None, {
            'fields': ('description', ('producer', 'item_type'), 'comment')
        }),
    )
    
    def get_queryset(self, request):
        consumables = super(ConsumableAdmin, self).get_queryset(request)
        consumables = consumables.select_related("inventory", "item_type")

        return consumables

    def on_hand(self, obj):
        return obj.inventory.on_hand
    
admin.site.register(Consumable, ConsumableAdmin)


class DispensedAdmin(NavigableModelAdmin):
    nav_item = 'nav_inv_dispensed'

    form = DispenseForm
    ordering = ['-place_date']
    list_display = ['item_type', 'support_item', 'place_date', 'consumer', 'consumer_location']
    list_filter = [ConsumerFilter, DispensedItemTypeFilter]
    
    def item_type(self, obj):
        return obj.support_item.consumable.item_type
    
    def consumer_location(self, obj):
        return obj.consumer.last_assigned.location

    def get_queryset(self, request):
        dispensed = super(DispensedAdmin, self).get_queryset(request)
        dispensed = dispensed.select_related("consumer", "consumer__last_assigned", "support_item", "support_item__consumable", "support_item__consumable__item_type")

        return dispensed

admin.site.register(Dispensed, DispensedAdmin)

#------------------------------------------------------------------------------
class CoverPeriodInline(admin.TabularInline):
    model = CoverPeriod
    extra = 0
    
class MaintenanceContractAdmin(NavigableModelAdmin):
    nav_item = 'nav_contract'
    inlines = [CoverPeriodInline,]
    
admin.site.register(MaintenanceContract, MaintenanceContractAdmin)

#------------------------------------------------------------------------------
class OrderItemMaterialInline(admin.TabularInline):
    form = OrderItemMaterialForm
    model = OrderItemMaterial
    extra = 0

    fieldsets = (
        (None, {
            'fields': ('quantity', 'description', 'department', 'item_type', 'completed')
        }),
        ('Extended', {
            'fields': ('discount', 'tax', 'price_per_unit')
        }),
    )

class OrderItemConsumableInline(admin.TabularInline):
    model = OrderItemConsumable
    form = OrderItemConsumableForm
    extra = 0

class MaterialOrderAdmin(NavigableModelAdmin):
    nav_item = 'nav_order'
    
    date_hierarchy = 'order_date'
    ordering = ['-order_date']
    list_display = ['order_no', 'description']
    list_display_links = list_display
    inlines = [OrderItemMaterialInline, OrderItemConsumableInline]

    fieldsets = (
        (None, {
            'fields': (('order_no', 'supplier'), ('order_date', 'to_exec_committee', 'to_supply_dept'), 'description')
        }),
        ('Comments', {
            'classes': ('collapse',),
           'fields': ('comment', 'private_comment')
        }),
    )

admin.site.register(MaterialOrder, MaterialOrderAdmin)

#------------------------------------------------------------------------------
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


