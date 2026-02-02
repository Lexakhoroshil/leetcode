-- Write your PostgreSQL query statement below

with tab1 as (
select 
    departmentId,
    name as Employee,
    salary,
    max(salary) over (partition by departmentId) as max_Salary
    from Employee
)

select  Department.name as Department,
        tab1.Employee,
        tab1.max_Salary as Salary
from tab1
    inner join Department on tab1.departmentId = Department.id
    where tab1.max_Salary = tab1.salary 
