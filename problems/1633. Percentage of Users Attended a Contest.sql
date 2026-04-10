-- Write your PostgreSQL query statement below
with total as (select count(*) as total from Users)
select contest_id, round(count(*)*100.0 /total.total,2) as percentage
from Register full join total on True
group by contest_id, total.total
order by 2 desc ,1