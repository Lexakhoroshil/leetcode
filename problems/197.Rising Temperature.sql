# Write your MySQL query statement below
with lag_weather as (
    select 
            id,
            recordDate,
            temperature,
            lag(recordDate) over (order by recordDate) as lag_recordDate,
            lag(temperature) over (order by recordDate) as lag_temp
 from Weather)
 select id from lag_weather where lag_temp < temperature
                and datediff(recordDate,lag_recordDate) = 1