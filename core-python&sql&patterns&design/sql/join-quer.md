# users table

| id | name   |
| -- | ------ |
| 1  | Akshay |
| 2  | Ravi   |
| 3  | Meera  |

# orders table

| id | user_id | amount |
| -- | ------- | ------ |
| 1  | 1       | 500    |
| 2  | 1       | 700    |
| 3  | 2       | 300    |

# Return all users and their total order amount?

SELECT users.name, COALESCE(SUM(orders.amount), 0) AS total_amount
FROM users
LEFT JOIN orders
ON users.id = orders.user_id
GROUP BY users.id, users.name;



SELECT user.name, COALESCE(SUM(orders.amount),0) AS total_amount

From users
LEFT JOIN orders 
ON users.id =orders.user_id
GROUP BY user-id,user.name

# Return only users whose total order amount is greater than 500?

SELECT users.name, COALESCE(SUM(orders.amount), 0) AS total_amount
FROM users
LEFT JOIN orders
ON users.id = orders.user_id
GROUP BY users.id, users.name
HAVING COALESCE(SUM(orders.amount), 0) > 500;


SELECT users.name,users.id
FROM users LEFT JOIN 
orders ON users.id = orders.user_id
WHERE orders.id IS NULL



SELECT users.name,users.id, COALESCE(SUM(orders.amount),0) AS total_aamount
FROM users LEFT JOIN 
orders ON users.id = orders.user_id 
GROUP BY users.id



