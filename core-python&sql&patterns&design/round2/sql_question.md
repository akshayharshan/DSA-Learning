# users table

| id | name |
| -- | ---- |
| 1  | A    |
| 2  | B    |
| 3  | C    |

# orders table

| id | user_id | amount |
| -- | ------- | ------ |
| 1  | 1       | 500    |
| 2  | 1       | 300    |
| 3  | 2       | 200    |


# q1 Find all users with their order amounts

select users.name,orders.amount
from users 
inner join orders
on user.id = orders.user_id




# q2 Find users with no orders

select users.name 
from users
left join orders
on user.id = orders.user_id
where orders.user_id is NULL


# q3 Find total order amount per user

select users.name, sum(orders.amount) as order_amount
from users 
inner join orders
where users.id = orders.user_id
group by users.id, users.name

# q4 Find users who placed more than 1 order

select users.name
from users 
inner join orders
on users.id == orders.user_id
group by users.id, users.name
having count(orders.id) > 1


# q5 Find total number of orders per user including users with no orders

select users.name , count(orders.id) as order_count
from users left join
orders on users.id = orders.user_id
group by users.id,users.name

# Find the user who placed the highest total order amount

select users.name , sum(orders.amount) as total_amount
from users join
 orders
 on users.id = orders.user_id
 group by user.id, user.name
 order by total_amount desc
 limit 1




