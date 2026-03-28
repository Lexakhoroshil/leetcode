-- Write your PostgreSQL query statement below
select 
t1.product_id, 
    round(coalesce(sum((t1.price*t2.units))::decimal /sum(t2.units)::decimal, 0.0),2) as average_price
from Prices t1 left join UnitsSold t2 
on t1.product_id = t2.product_id and t2.purchase_date between start_date and end_date
group by 1