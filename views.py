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

from django.views import generic
from app import nav_tree

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'app/index.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        context['navigation'] = nav_tree['nav_root'].three_tier()
        
        return context

class InventoryTypesIndex(generic.TemplateView):
    template_name = 'app/inventory_types.html'
    
    def get_context_data(self, **kwargs):
        context = super(InventoryTypesIndex, self).get_context_data(**kwargs)
        context['navigation'] = nav_tree['nav_inventory_type'].three_tier()
        
        return context

class InventoryIndex(generic.TemplateView):
    template_name = 'app/inventory.html'
    
    def get_context_data(self, **kwargs):
        context = super(InventoryIndex, self).get_context_data(**kwargs)
        context['navigation'] = nav_tree['nav_inventory'].three_tier()
        
        return context
