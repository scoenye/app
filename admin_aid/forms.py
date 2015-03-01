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

from django import forms
from django.forms import widgets
from django.contrib.admin.util import label_for_field
from django.forms.forms import pretty_name

from app.models import OrderItem, Dispensed, Hardware

#class OrderItemForm(forms.ModelForm):
#    """Custom form for the OrderItem inline"""
#
#    meta    = OrderItem._meta
#    
#    # Setting "required" is superfluous if TabularInlineForm is used, but just in case that changes...
#    discount = forms.FloatField(widget = widgets.NumberInput(attrs = {'size':'5'}),
#                                label = pretty_name(label_for_field('discount', OrderItem)),
#                                required = not meta.get_field('discount').blank)
#    
#    tax = forms.FloatField(widget = widgets.NumberInput(attrs = {'size':'5'}),
#                           label = pretty_name(label_for_field('tax', OrderItem)),
#                           required = not meta.get_field('tax').blank)
#    
#    price_per_unit = forms.FloatField(widget = widgets.NumberInput(attrs = {'size':'10'}),
#                                      label = pretty_name(label_for_field('price_per_unit', OrderItem)),
#                                      required = not meta.get_field('price_per_unit').blank)
#
#    class Meta:
#        model = OrderItem
#        fields  = ["discount", "tax", "price_per_unit"]

class DispenseForm(forms.ModelForm):
    """ Custom entry form for the Dispensed inline """
    
    consumer = forms.ModelChoiceField(queryset=Hardware.objects.filter(item_type__consumer=True))

    class Meta:
        model = Dispensed
        fields = ["place_date", "consumer", "quantity"]
