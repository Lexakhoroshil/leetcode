-- Write your PostgreSQL query statement below
select 
t1.student_id,
t1.student_name,
t2.subject_name,
coalesce(t3.attended_exams, 0) as attended_exams
from Students t1 cross join Subjects t2
left join (select student_id, subject_name, count(*) as attended_exams 
                from Examinations group by 1,2) t3
                
                on t1.student_id = t3.student_id and t2.subject_name = t3.subject_name
order by 1,2,3