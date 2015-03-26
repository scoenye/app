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

from app.admin_aid.fields import NameLocationChoiceField, ItemTypeDescChoiceField
from app.models import OrderItemMaterial, OrderItemConsumable, Dispensed, Consumable
from app.models import HelpdeskCall, Hardware, NonConsumable, Department

class OrderItemMaterialForm(forms.ModelForm):
    """Custom form for the OrderItem inline"""

    meta    = OrderItemMaterial._meta
    
    # Setting "required" is superfluous if TabularInlineForm is used, but just in case that changes...
    # Do not use NumberInput. The size is uncontrollable. (HTML5 "new and improved")
    discount = forms.FloatField(widget = widgets.TextInput(attrs = {'size':'5'}),
                                label = pretty_name(label_for_field('discount', OrderItemMaterial)),
                                required = not meta.get_field('discount').blank)
    
    tax = forms.FloatField(widget = widgets.TextInput(attrs = {'size':'5'}),
                           label = pretty_name(label_for_field('tax', OrderItemMaterial)),
                           required = not meta.get_field('tax').blank)
    
    price_per_unit = forms.FloatField(widget = widgets.TextInput(attrs = {'size':'10'}),
                                      label = pretty_name(label_for_field('price_per_unit', OrderItemMaterial)),
                                      required = not meta.get_field('price_per_unit').blank)

    class Meta:
        model = OrderItemMaterial
        fields  = ["discount", "tax", "price_per_unit"]

class OrderItemConsumableForm(forms.ModelForm):
    """Custom form for the consumable OrderItem inlines """
    item = ItemTypeDescChoiceField(queryset = Consumable.objects.all().order_by("item_type__name", "description"),
                                   label = pretty_name(label_for_field('item', OrderItemConsumable)))
    
    class Meta:
        model  = OrderItemConsumable
        fields = ["completed", "department", "description", "quantity", "item"] 

class DispenseForm(forms.ModelForm):
    """ Custom entry form for the Dispensed inline """
    
    consumer = NameLocationChoiceField(queryset=Hardware.objects.filter(item_type__consumer=True).select_related("last_assigned"),
                                       label = pretty_name(label_for_field('consumer', Dispensed)))

    class Meta:
        model = Dispensed
        fields = ["place_date", "consumer", "quantity"]


class HelpdeskCallForm(forms.ModelForm):
    """ Custom form to get the supported items dropdown under control """
    
    # Find the non-consumable items not currently assigned to an EOL department
    item = forms.ModelChoiceField(queryset=NonConsumable.objects.filter(department__end_of_life=False).order_by("tag_ver"),
                                  label = pretty_name(label_for_field('item', HelpdeskCall)))

    class Meta:
        model = HelpdeskCall
        fields = ["item"]