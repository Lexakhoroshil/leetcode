-- Write your PostgreSQL query statement below
select  query_name, 
        ROUND((sum(rating*1.0/position))/COUNT(*),2) AS quality,
        ROUND(100.0*(COUNT(*) FILTER (WHERE rating<3) ) /COUNT(*),2) AS poor_query_percentage

         
    from Queries
group by query_name