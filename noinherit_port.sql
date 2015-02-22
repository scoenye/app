-- Commands to transfer data from the inherited table version to the no inherit version
update app_orig.order_item set department=-1 where department is null;
update app_orig.order_item_material set item_type = -1 where item_type is null;
update app_orig.placement set department = -1 where department is null;

insert into caller(id, name, telephone, active, location) select id, name, telephone, active, location from app_orig.caller;
insert into department(caller_ptr_id, end_of_life) select id, end_of_life from app_orig.department;
insert into person(caller_ptr_id, first_name) select id, first_name from app_orig.person;
insert into employee(person_ptr_id, department_id) select id, department from app_orig.employee;
insert into technician(employee_ptr_id) select id from app_orig.technician;
insert into repair_technician(person_ptr_id, company_id) select id, company from app_orig.repair_technician;

insert into company(id, name, street, city, telephone, postcode) select distinct id, name, street, city, telephone, postcode from app_orig.company;
insert into contractor(company_ptr_id) select id from app_orig.contractor;

insert into item_type(id, name) select id, name from app_orig.item_type;
insert into hardware_item_type(itemtype_ptr_id, consumer) select id, consumer from app_orig.hardware_item_type;
insert into software_item_type(itemtype_ptr_id) select id from app_orig.software_item_type;
insert into consumable_item_type(itemtype_ptr_id) select id from app_orig.consumable_item_type;

insert into maintenance_contract(id, code, contractor_id, description) select id, code, contractor, description from app_orig.maintenance_contract;
insert into weekday(id, day) select id, day from app_orig.weekday;
insert into cover_period(id, start_time, end_time, contract_id, weekday_id) select id, start_time, end_time, contract, weekday from app_orig.cover_period;
insert into material_order(id, order_no, order_date, to_exec_committee, to_supply_dept, description, comment, private_comment, supplier_id, supplier_ref) select id, order_id, order_date, to_exec_committee, to_supply_dept, description, comment, private_comment, supplier, supplier_ref from app_orig.material_order;

insert into order_item(id, completed, description, quantity, department_id, mat_order_id) select id, completed, description, quantity, department, mat_order from app_orig.order_item;
insert into order_item_material(orderitem_ptr_id, discount, tax, price_per_unit, item_type_id) select id, discount, tax, price_per_unit, item_type from app_orig.order_item_material;

insert into support_item(id, contract_id, description, producer_id, item_type_id, order_item_id, comment) select id, contract, description, producer, item_type, order_item, comment from app_orig.support_item;
insert into hardware(supportitem_ptr_id, part_no, hostname, idms_name, ip_address, tag) select id, part_no, hostname, idms_name, ip_address, tag from app_orig.hardware;
insert into software(supportitem_ptr_id, version) select id, version from app_orig.software;
insert into consumable(supportitem_ptr_id, part_no) select id, part_no from app_orig.consumable;

insert into order_item_consumable (orderitem_ptr_id, item_id) select id, item from app_orig.order_item_consumable ;

insert into placement(id, place_date, location, department_id, support_item_id) select id, place_date, location, department, item from app_orig.placement;
insert into dispensed(placement_ptr_id, quantity, consumer_id) select id, quantity, consumer from app_orig.dispensed;

insert into helpdesk_call(caller_id, call_time, call_recorder_id, problem_type, item_id, assigned_tech_id, closing_time, closing_comment, closing_tech_id) select id, call_time, call_recorder, problem_type, item, assigned_tech, closing_time, closing_comment, closing_tech from app_orig.helpdesk_call;
insert into repaircall(id, helpdeskcall_id, call_tech_id, call_time, close_time, call_problem, call_reference, close_comment, close_tech_id, repair_tech_id) select id, helpdeskcall, call_tech, call_time, close_time, call_problem, call_reference, close_comment, close_tech, repair_tech from app_orig.repaircall;
insert into serial_no(id, support_item_id, serial_no, assign_date) select id, item, serial_no, assign_date from app_orig.serial_no;
insert into work_done(id, start_time, end_time, call_id, technician_id) select id, start_time, end_time, call, technician from app_orig.work_done;
