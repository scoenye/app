create view vw_last_assigned_dept as 
  SELECT result.support_item_id, result.department_id, caller.name, result.location, result.place_date
  FROM placement result inner join caller on result.department_id = caller.id
  WHERE result.place_date = (
      SELECT max(crit.place_date) AS max
      FROM placement crit
      WHERE crit.support_item_id = result.support_item_id);

 create view vw_last_assigned_serial as  
   SELECT item_serial.support_item_id, item_serial.serial_no, item_serial.assign_date                        
   FROM serial_no item_serial
   WHERE item_serial.assign_date = (
       SELECT max(serial_date.assign_date) AS max
       FROM serial_no serial_date
       WHERE serial_date.support_item_id = item_serial.support_item_id);

create view vw_nonconsumables as
	SELECT support_item.id as support_item_id, support_item.description, 
	       hardware.item_type_id, to_char(hardware.tag, '0000') AS tag_ver, 
	       item_type.name AS item_type_name, 
	       vw_last_assigned_dept.department_id, vw_last_assigned_dept.location, 
	       vw_last_assigned_serial.serial_no 
	FROM hardware inner join support_item on hardware.supportitem_ptr_id = support_item.id 
	              inner join item_type on hardware.item_type_id = item_type.id
	              inner join vw_last_assigned_serial on hardware.supportitem_ptr_id = vw_last_assigned_serial.support_item_id
	              inner join vw_last_assigned_dept on hardware.supportitem_ptr_id = vw_last_assigned_dept.support_item_id
	UNION
	SELECT support_item.id as support_item_id, support_item.description, 
	       software.item_type_id, software.version AS tag_ver, 
	       item_type.name AS item_type_name, 
	       vw_last_assigned_dept.department_id, vw_last_assigned_dept.location, 
	       vw_last_assigned_serial.serial_no
	FROM software inner join support_item on software.supportitem_ptr_id = support_item.id 
	              inner join item_type on software.item_type_id = item_type.id
	              inner join vw_last_assigned_serial on software.supportitem_ptr_id = vw_last_assigned_serial.support_item_id
	              inner join vw_last_assigned_dept on software.supportitem_ptr_id = vw_last_assigned_dept.support_item_id;

create view vw_consumables_delivered as
	SELECT order_item_consumable.item_id AS consumable_id, sum(order_item.quantity) AS quantity
    FROM order_item_consumable INNER JOIN order_item ON order_item_consumable.orderitem_ptr_id = order_item.id
    WHERE order_item.completed IS NOT NULL
    GROUP BY order_item_consumable.item_id;

create view vw_consumables_dispensed as
	SELECT placement.support_item_id as consumable_id, sum(dispensed.quantity) AS dispensed
    FROM dispensed INNER JOIN placement ON dispensed.placement_ptr_id = placement.id
    GROUP BY placement.support_item_id;

create view vw_consumables_onhand as
	SELECT consumable.supportitem_ptr_id as consumable_id, 
	       COALESCE(vw_consumables_delivered.quantity, 0) - COALESCE(vw_consumables_dispensed.dispensed, 0) AS on_hand 
	FROM consumable LEFT JOIN vw_consumables_delivered ON vw_consumables_delivered.consumable_id = consumable.supportitem_ptr_id 
	                LEFT JOIN vw_consumables_dispensed ON vw_consumables_dispensed.consumable_id = consumable.supportitem_ptr_id;
