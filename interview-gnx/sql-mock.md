users
id
name
email

orders
id
user_id
amount

q1) select *users where name ilike "A%"

q2) select name from employees order by salary desc limit 3

q3) select users.name,COUNT(orders.id) as user_orders
from users 
left join orders on users.id = orders.user_id 
group by orders.id


q4)select users.name from users left join orders on users.id = orders.user_id 
where orders.id IS NULL

q5) select name , COUNT(email) as email_count
    from users 
    group by email
    having count(email) > 1


q6) 
select max(salary) from employee
where salary 
< (
select MAX(salary) from emplyees
)

q7)select users.name,orders.id COUNT(*)
from users left join orders on users.id = orders.user_id 
group by orders.id
having COUNT(*) > 2



q8) UPDATE users set name = "akshay" where id =5

q9)DELETE orders from users where amount < 100


q10)select users.name, orders.amount from users inner join orders on users.id = orders.user_id 

q11) where will apply filter to the row before aggreagation and having to do filtering after the aggregation

q12)will inclide all the rows from the left table even if the right table doesnt have data related eg the users doesnt have orders

q13)index is used to fasten the query but it increase the size of the databse and increase time to write to databse
q14)delete will only delete a row which is  able to roll back truncate delete all the tables and cant be roll abck

q15)i will remove the unimportant data feching from the db , index the tables properly and do pagination