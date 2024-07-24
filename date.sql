-- date

use aravind;

alter table company add  column Hire_Date date;

select * from company;
update company set hire_date = "2024-03-18";

update company set hire_date = "2024-11-11"
where jobdesc  = "analyst";

update company set hire_date = "2024-12-22"
where jobdesc  = "manager";

-- ====================================================================
select now();  -- finds the current time
select date(now());
select curdate();
select Date_format(curdate(),"%d/%m/%Y")  Name;
select Date_format(curdate(),"%d/%m/%y")  Name;

select datediff(curdate(), "2023/01/01")  Name; -- finds how many days between them

select date_add(curdate(), interval 1 day)  "after one day";

select date_add(curdate(), interval 1 week)  "after one week";

select curdate() 'start date',
date_add(curdate(), interval 1 day)  "after one day",
date_add(curdate(), interval 1 week)  "after one week",
date_add(curdate(), interval 1 month)  "after one month",
date_add(curdate(), interval 1 year)  "after one year";

select * from company;

