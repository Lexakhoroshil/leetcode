-- Write your PostgreSQL query statement below
select t1.user_id,
       round(coalesce(t2.confirmation_rate,0.0), 2) as confirmation_rate

from Signups t1
left join ( select  user_id, 
                    ((count(*) FILTER (where action = 'confirmed'))::decimal) /(count(*)::decimal) as confirmation_rate
            from Confirmations
            group by 1) t2 on t1.user_id = t2.user_id
            
