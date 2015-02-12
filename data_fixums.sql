# Inheritance shenanigans. Manual fix to prevent problems with the FK constraints.

update contractor set name = 'NECI - Contractor' where id = -1;
insert into company(name) values ('NECI as Company');
insert into co(name) values ('NECI as Contractor');
update material_order set supplier = company.id from company where company.name = 'NECI as Company' and material_order.supplier = -1;
update support_item set producer = company.id from company where company.name = 'NECI as Company' and support_item.producer = -1;
update repair_technician set company = company.id from company where company.name = 'NECI as Company' and repair_technician.company = -1;
update maintenance_contract set contractor = contractor.id from contractor where contractor.name = 'NECI as Contractor' and maintenance_contract.contractor = -1;
delete from contractor where id = -1;
delete from company where id = -1;
