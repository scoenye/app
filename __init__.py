from navigation import tier

# Defined the nav_tree block for this application. This builds a tree and a flat addressable
# representation at the same time. The tree will generate the children/siblings lists,
# the dictionary makes it possible to address random parts of the tree.

# TODO: extend this mechanism to the project level so the upper level becomes the list of
#       all applications in the project.

nav_tree = {}

nav_tree['nav_root'] = tier.TieredNavigation('App', 'app:index')
tier.TieredNavigation.home = tier.TieredNavigation('Home', 'app:index')        # The Home static node. 

nav_tree['nav_company']    = tier.TieredNavigation('Company',     'admin:app_company_changelist', nav_tree.get('nav_root'))
nav_tree['nav_contractor'] = tier.TieredNavigation('Contractor',  'admin:app_contractor_changelist', nav_tree.get('nav_company'))

nav_tree['nav_caller']     = tier.TieredNavigation('Caller',      'admin:app_caller_changelist',     nav_tree.get('nav_root'))
nav_tree['nav_department'] = tier.TieredNavigation('Department',  'admin:app_department_changelist', nav_tree.get('nav_caller'))
nav_tree['nav_person']     = tier.TieredNavigation('Person',      'admin:app_person_changelist',     nav_tree.get('nav_caller'))
nav_tree['nav_employee']   = tier.TieredNavigation('Employee',    'admin:app_employee_changelist',   nav_tree.get('nav_person'))
nav_tree['nav_repairtech'] = tier.TieredNavigation('Repair Tech', 'admin:app_repairtechnician_changelist', nav_tree.get('nav_person'))
nav_tree['nav_technician'] = tier.TieredNavigation('Technician',  'admin:app_technician_changelist', nav_tree.get('nav_employee'))

nav_tree['nav_helpdesk']   = tier.TieredNavigation('Helpdesk',    'admin:app_helpdeskcall_changelist', nav_tree.get('nav_root'))
    
nav_tree['nav_inventory']  = tier.TieredNavigation('Inventory',   'admin:app_supportitem_changelist', nav_tree.get('nav_root'))
nav_tree['nav_inv_hardw']  = tier.TieredNavigation('Hardware',    'admin:app_hardware_changelist', nav_tree.get('nav_inventory'))
nav_tree['nav_inv_softw']  = tier.TieredNavigation('Software',    'admin:app_software_changelist', nav_tree.get('nav_inventory'))
nav_tree['nav_inv_cons']   = tier.TieredNavigation('Consumables', 'app:index', nav_tree.get('nav_inventory'))
    
nav_tree['nav_inventory_type'] = tier.TieredNavigation('Inventory type', 'admin:app_itemtype_changelist', nav_tree.get('nav_root'))
nav_tree['nav_inv_type_hardw'] = tier.TieredNavigation('Hardware',   'admin:app_hardwareitemtype_changelist', nav_tree.get('nav_inventory_type'))
nav_tree['nav_inv_type_softw'] = tier.TieredNavigation('Software',   'admin:app_softwareitemtype_changelist', nav_tree.get('nav_inventory_type'))
nav_tree['nav_inv_type_cons']  = tier.TieredNavigation('Consumable', 'app:index', nav_tree.get('nav_inventory_type'))
    
nav_tree['nav_contract']   = tier.TieredNavigation('Contracts',  'admin:app_maintenancecontract_changelist', nav_tree.get('nav_root'))
    
nav_tree['nav_order']      = tier.TieredNavigation('Order',      'admin:app_materialorder_changelist', nav_tree.get('nav_root'))
    
nav_tree['nav_repaircall'] = tier.TieredNavigation('Repaircall', 'admin:app_repaircall_changelist', nav_tree.get('nav_root'))
