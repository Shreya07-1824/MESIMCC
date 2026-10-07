use democlg;
create table employee(empId int,firstName text,lastName text,age int ,zone text);
insert into employee values(1,"shreya","patil",21,"pune"),
							(2,"sakshi","suryawanshi",21,"pune"),
                            (3,"sneha","chawla",21,"wagholi"),
                            (4,"asha","patil",21,"hatnur"),
                            (5,"sanika","patil",21,"pune");
update employee set lastName="patil" where empId=3;
-- 7/10/2026
-- DML command

select * from employee;
update employee set firstName="asharani",age=28 where empId=4;
update employee set firstname=null where empId=5;
delete from employee where firstName="";
truncate table employee;

-- constraints in dbms

-- primary key-cannot be null and should be unique values
-- unique key
-- foreign key-prevent the action that would destroy the links between tables
-- check-ensures values in coloumn should satisfies the condition




