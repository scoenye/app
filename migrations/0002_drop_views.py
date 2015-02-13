# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        # Remove dependent views. They are immutable and will block the rekey.
        migrations.RunSQL(
            "drop view vw_inventory;",
            "create view vw_inventory as "
            "SELECT hardware.tag, hardware.description, hardware.part_no, hardware_item_type.name AS item_type, hardware.comment, "
            "       company.name AS mfg, "
            "       vw_last_assigned_serial.serial_no, vw_last_assigned_dept.location, "
            "       department.name AS department, department.location AS campus "
            "FROM hardware LEFT JOIN company ON hardware.producer = company.id "
            "              LEFT JOIN hardware_item_type ON hardware.item_type = hardware_item_type.id "
            "              LEFT JOIN vw_last_assigned_dept ON hardware.id = vw_last_assigned_dept.item "
            "              LEFT JOIN vw_last_assigned_serial ON hardware.id = vw_last_assigned_serial.item "
            "              LEFT JOIN department ON vw_last_assigned_dept.department = department.id;",
        ),
                  
        migrations.RunSQL(
            "drop view vw_first_assigned_dept;",
            "create view vw_first_assigned_dept as "
            "SELECT department.name::text || COALESCE(' - '::text || department.location::text, ''::text) AS department_name, "
            "       result.item, result.department, result.location, result.place_date "
            "FROM placement result, department "
            "WHERE result.place_date = (( SELECT min(crit.place_date) AS min "
            "                             FROM placement crit "
            "                             WHERE crit.item = result.item)) AND "
            "      result.department = department.id;"
        ),
                  
        migrations.RunSQL(
            "drop view vw_active_laptops;",
            "create view vw_active_laptops as "
            "SELECT hardware.tag, hardware.description, "
            "       vw_last_assigned_dept.name AS department, vw_last_assigned_dept.location AS assignee "
            "FROM vw_last_assigned_dept, department, hardware, item_type "
            "WHERE vw_last_assigned_dept.department = department.id AND "
            "      department.id > 0 AND department.end_of_life = false AND "
            "      vw_last_assigned_dept.item = hardware.id AND "
            "      hardware.item_type = item_type.id AND item_type.id = 22;"
        ),
        
        migrations.RunSQL(
            "drop view vw_active_desktops;",
            "create view vw_active_desktops as "
            "SELECT hardware.tag, hardware.description, "
            "       vw_last_assigned_dept.name AS department, vw_last_assigned_dept.location AS assignee "
            "FROM vw_last_assigned_dept, department, hardware, item_type "
            "WHERE vw_last_assigned_dept.department = department.id AND "
            "      department.id > 0 AND department.end_of_life = false AND "
            "      vw_last_assigned_dept.item = hardware.id AND " 
            "      hardware.item_type = item_type.id AND item_type.id = 21;"
        ),
        
        migrations.RunSQL(
            "drop view vw_supported_hard_soft;",
            "create view vw_supported_hard_soft as "
            "SELECT hardware.id, hardware.description, hardware.item_type, item_type.name AS item_type_name, hardware.hostname AS host_ver, vw_last_assigned_dept.department, vw_last_assigned_dept.location, vw_last_assigned_serial.serial_no "
            "FROM hardware, item_type, vw_last_assigned_serial, vw_last_assigned_dept "
            "WHERE hardware.id = vw_last_assigned_serial.item AND hardware.id = vw_last_assigned_dept.item AND hardware.item_type = item_type.id "
            "UNION "
            "SELECT software.id, software.description, software.item_type, item_type.name AS item_type_name, software.version AS host_ver, vw_last_assigned_dept.department, vw_last_assigned_dept.location, vw_last_assigned_serial.serial_no "
            "FROM software, item_type, vw_last_assigned_serial, vw_last_assigned_dept "
            "WHERE software.id = vw_last_assigned_serial.item AND software.id = vw_last_assigned_dept.item AND software.item_type = item_type.id;"
        ),
        
        migrations.RunSQL(
            "drop view vw_last_assigned_dept;",
            "create view vw_last_assigned_dept as "
            "SELECT result.item, result.department, department.name, result.location, result.place_date "
            "FROM placement result, department "
            "WHERE result.place_date = (( SELECT max(crit.place_date) AS max "
            "                             FROM placement crit "
            "                             WHERE crit.item = result.item)) AND "
            "result.department = department.id;"
        ),
        
        migrations.RunSQL(
            "drop view vw_consumables_onhand;",
            "create view vw_consumables_onhand as "
            "SELECT consumable.id, COALESCE(vw_consumables_delivered.quantity, 0::bigint) - COALESCE(vw_consumables_dispensed.dispensed, 0::bigint) AS on_hand "
            "FROM consumable LEFT JOIN vw_consumables_delivered ON consumable.id = vw_consumables_delivered.item "
            "                LEFT JOIN vw_consumables_dispensed ON consumable.id = vw_consumables_dispensed.item;"
        ),
        
        migrations.RunSQL(
            "drop view vw_consumables_delivered;",
            "create view vw_consumables_delivered as "
            "SELECT order_item_consumable.item, sum(order_item_consumable.quantity) AS quantity "
            "FROM order_item_consumable "
            "WHERE order_item_consumable.completed IS NOT NULL "
            "GROUP BY order_item_consumable.item;"
        ),
        
        migrations.RunSQL(
            "drop view vw_consumables_dispensed;",
            "create view vw_consumables_dispensed as "
            "SELECT dispensed.item, sum(dispensed.quantity) AS dispensed "
            "FROM dispensed "
            "GROUP BY dispensed.item;"
        ),
        
        migrations.RunSQL(
            "drop view vw_last_assigned_serial;",
            "create view vw_last_assigned_serial as "
            "SELECT result.item, result.serial_no, result.assign_date "
            "FROM serial_no result "
            "WHERE result.assign_date = (( SELECT max(crit.assign_date) AS max "
            "                              FROM serial_no crit "
            "                              WHERE crit.item = result.item));"
        ),
                  
        migrations.RunSQL(
            "drop view vw_support_item;",
            "create view vw_support_item as "
            "SELECT support_item.id FROM support_item;"
        )
    ]
