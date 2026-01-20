# Write your MySQL query statement below
delete from Person
where id not in (
select id from (select id, row_number() over (partition by email order by id) as n from Person) p1
where p1.n=1
);
