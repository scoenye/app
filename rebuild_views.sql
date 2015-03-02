create view vw_last_assigned_dept as 
  SELECT result.support_item_id, result.department_id, caller.name, result.location, result.place_date
  FROM placement result inner join caller on result.department_id = caller.id
  WHERE result.place_date = (
      SELECT max(crit.place_date) AS max
      FROM placement crit
      WHERE crit.support_item_id = result.support_item_id);
