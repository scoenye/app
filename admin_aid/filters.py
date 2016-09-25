'''
@author: Sven Coenye

Copyright (C) 2014  Sven Coenye

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

from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from app.models import Department, Hardware, HardwareItemType, SoftwareItemType, ConsumableItemType

class HardwareItemTypeFilter(SimpleListFilter):
    title = _('item type')

    parameter_name = 'item_type'

    def lookups(self, request, model_admin):
        return HardwareItemType.objects.all().order_by('name').values_list('id', 'name')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(item_type__exact=self.value())


class SoftwareItemTypeFilter(SimpleListFilter):
    title = _('item type')

    parameter_name = 'item_type'

    def lookups(self, request, model_admin):
        return SoftwareItemType.objects.all().order_by('name').values_list('id', 'name')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(item_type__exact=self.value())


class ConsumableItemTypeFilter(SimpleListFilter):
    title = _('item type')

    parameter_name = 'item_type'

    def lookups(self, request, model_admin):
        return ConsumableItemType.objects.all().order_by('name').values_list('id', 'name')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(item_type__exact=self.value())


# For use by the Dispensed admin, unlike the Hardware and Software item type filters
class DispensedItemTypeFilter(SimpleListFilter):
    title = _('item type')

    parameter_name = 'item_type'

    def lookups(self, request, model_admin):
        return ConsumableItemType.objects.all().order_by('name').values_list('id', 'name')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(support_item__consumable__item_type=self.value())


class PlacementFilter(SimpleListFilter):
    title = _('placement')
    
    parameter_name = 'test'

    def lookups(self, request, model_admin):
        return Department.objects.filter(active=True).order_by('name').values_list('id', 'name')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(last_assigned__department=self.value())


class TerminalPlacementFilter(SimpleListFilter):
    title = _('status')
    
    parameter_name = 'status'
    
    def lookups(self, request, model_admin):
        return (
            ('1', _('Decommissioned')), 
            ('0', _('Active'))
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(last_assigned__department__end_of_life=self.value())


class ConsumerFilter(SimpleListFilter):
    title = _('consumer')
    
    parameter_name = 'consumer'
    
    def lookups(self, request, model_admin):
        qs = Hardware.objects.filter(item_type__consumer=True).select_related("last_assigned").values_list("id", "last_assigned__location")
        return qs.values_list('id', 'last_assigned__location')
    
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(consumer=self.value())
