-- Write your PostgreSQL query statement below

select name 

from Employee t1  inner join (select managerId, count(*) as num_reports 
                            from Employee
                            where managerId is not null
                            group by 1) t2 on t1.id = t2.managerId and t2.num_reports>=5

-- where t1.managerId is null 
