use democlg;
create table emp7(empId int primary key,firstName text,lastName text,empAge int,salary double);

-- for single column to apply check
alter table emp7 add constraint check(salary>=5000);

alter table emp7 add constraint chk_empAge_salary check(empAge>=20 and salary>=5000);
desc emp7; 
show create table emp7;
-- to drop constraints two methods 
-- one
alter table emp7 drop constraint chk_empAge_salary;

-- two
alter table emp7 drop  check chk_empAge_salary;
insert into emp7 values(1,"shreya","patil",20,6000);


-- create index statetment is used to create indexex in tables 
-- indexex used to retrieve the data from the database  more quickl and user cannot see the indexex
alter table emp7 modify firstName varchar(20);
alter table emp7 modify lastName varchar(20);
create index demoindex on emp7(firstName);
show index from emp7;

create index demoindex2 on emp7(firstName,lastName);
show index from emp7;

drop index demoindex on emp7;







