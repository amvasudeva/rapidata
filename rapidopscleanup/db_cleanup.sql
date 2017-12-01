use petclinic;
delete from types where name like 'Elephant';
delete from types where name like 'Snake';
delete from types where name like 'Cow';
delete from types where name like 'Camel';
delete from owners where first_name like 'RR111UYXZAAAA';
delete from DATABASECHANGELOG where id in (106, 801, 800); 
