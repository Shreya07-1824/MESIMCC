create database dbconstrains;
use dbconstrains;
create table employee(empId int not null,fistNAme text,lastName text,empAge int);
desc employee;
insert into employee values(1,'riya','rao',20);

-- table 2
create table employee1(empId int not null,fistNAme text,lastName text,unique(empId));
desc employee1;
insert into employee1 values(1,'ravi','kumar');

-- table 3
create table employee3(empId int not null,firstNAme text,lastName text,empAge int,check(empAge>20) );

alter table employee3 add salary double , add check(salary>=50000);
insert into employee3 values(1,"shreya","patil",21,50000);

-- check constraint can be applied to multipla colums in row







