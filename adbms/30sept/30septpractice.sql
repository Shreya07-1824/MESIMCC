create database companyDB;
use companyDB;
create  table employees(empId int primary key,empname text,salary decimal,joinDate date);
desc employees;

create table department(deptId int primary key,deptname text);
alter table employees add  email varchar(100);
alter table department add dept_location text;
alter table employees add phone int(10) not null;
alter table employees modify empname varchar(100);
alter table employees add deptId int;
alter table employees add foreign key(deptId) references department(deptId);

desc department;
alter table employees rename column empname to employeename;
alter table employees drop column phone;
rename table employees to employeeDetails;
alter table department drop primary key (deptId);
alter table employeeDetails drop foreign key deptId;
insert into employeeDetails values(1,"shreya",50000.0,"20-9-2026");
desc employeeDetails;
insert into employeeDetails values(1,"shreya",50000.0,'2026-09-30',"sp@gmail.com",1);
insert into department values(1,"finance","pune"),(2,"marketing","pune"),(3,"sales","pune");
desc department;
insert into department values(3,"sales","pune");
insert into employeeDetails values(2,"sakshi",50000.0,'2026-09-10',"sakshi@gmail.com",2),
								   (3,"sneha",50000.0,'2026-09-15',"sneha@gmail.com",2),
                                   (4,"kunal",50000.0,'2026-09-20',"kunal@gmail.com",2),
                                   (5,"praveen",50000.0,'2026-09-13',"praveen@gmail.com",2);
select * from employeeDetails;
select * from department;







