use institute;
desc staff;
alter table staff add primary key(staff_id);
desc department;
alter table department add  primary key(dept_id);
alter table staff add foreign key (dept_id) references department(dept_id);

-- alternate way to add foreign key
 alter table staff add constraint FK_staff_department foreign key(dept_id) references department(dept_id);


-- to rename the table
alter table staff rename staff1;

-- alternative method to rename table
rename table staff1 to staff;

-- rename the column name
alter table staff rename column first_name to  First_name;

-- here the table didnt drop cause of foreign key so first need to drop the staff table then only the department table can be deleted
drop table department;

-- to drop database 
drop database institute;



