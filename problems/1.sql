# Write your MySQL query statement below


select distinct email from (select
                    row_number() over (partition by email) as dup,
                    email from Person) as t
where dup >1



