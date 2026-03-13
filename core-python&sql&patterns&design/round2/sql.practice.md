q1) select users.id,users.name, orders.amount
from users join 
orders on users.id = orders.user_id
group by users.name,users.id



q2) select users.name 
from users
left join
orders on users.id = orders.user_id

q3)
select users.name, orders.amount
from users
left join
orders on users.id = orders.user_id
where orders.id is NULL


q4) select users.name users.id, count(orders.id) as number_of_orders
from users
left join
orders on users.id = orders.user_id
group by  users.name,users.id

q5) 
select users.name,users.id, sum(orders.amount) as total_order_amount
from users
left join
orders on users.id = orders.user_id
group by  users.name,users.id



q6)


select users.name, users.id, count(orders.id)
from users
inner join
orders on users.id = orders.user_id
group by  users.name,users.id
having count(orders.id) > 1

q7)

select users.name, users.id, SUM(orders.amount)
from users
inner join
orders on users.id = orders.user_id
GROUP BY user.id, user.name
order by orders.amount desc limit 1


q8)
select users.name, users.id, MAX(orders.amount) AS highest_order
from users
inner join
orders on users.id = orders.user_id
GROUP BY  users.id , users.name


q9)
select users.name, users.id, orders.id AVG(orders.amount)
from users
left join
orders on users.id = orders.user_id
group by  users.name,users.id
having orders.amount > AVG(orders.amount)



q10)
select users.name, users.id, 
from users
left join
orders on users.id = orders.user_id
where orders.id is NULL





select users.name,orders.id,AVG(orders.id)
from users
left join orders
on users.id = orders.user_id
group by orders.id
having orders.id > AVG(orders.id)


select users.name,users.id MAX(orders.id) AS latest_order
from users
left join orders on 
users.id = orders.user_id
group by users.id ,users.name


SELECT users.name,users,id
FROM users LEFT JOIN orders
ON users.id = orders.user_id
WHERE orders.id IS NULL

SELECT users.name, users.id, SUM(orders.amount)
FROM users LEFT JOIN orders
ON users.id = orders.user_id
GROUP BY users.name,users.id

