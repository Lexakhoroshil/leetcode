-- Write your PostgreSQL query statement below
with table_start as (
    select * from Activity
    where activity_type = 'start'
)
, table_end as (
    select * from Activity
    where activity_type = 'end'
)

select 
    t1.machine_id,
    ROUND(avg(t2.timestamp - t1.timestamp)::numeric, 3) as processing_time
from table_start t1 inner join table_end t2 on t1.machine_id = t2.machine_id and t1.process_id = t2.process_id
group by 1