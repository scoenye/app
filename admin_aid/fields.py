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

from django import forms

# Attempt to get more control over the values displayed for
# dropdown fields in inlines.
from __future__ import unicode_literals

class NameLocationChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.description + ' - ' + obj.last_assigned.location

class ItemTypeDescChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.item_type.name + ' - ' + obj.description

class OrderItemOrderChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.mat_order.order_no + ' - ' + obj.description