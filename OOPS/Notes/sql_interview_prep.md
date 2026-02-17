| id | name | salary |
| -- | ---- | ------ |
| 1  | A    | 1000   |
| 2  | B    | 2000   |
| 3  | C    | 2000   |
| 4  | D    | 3000   |

Write a SQL query to find the second highest salary.?

SELECT DISTINCT SALARY FROM users ORDER BY salary DESC LIMIT 1 OFFSET 1

SELECT MAX(salary)

SELECT MAX(salary)
FROM users
WHERE salary < (SELECT MAX(salary) FROM users);
                         |
                        this part return 3000  
                        |
                then run where salary < 3000
                        |
                        so upto 2000 came up and then apply MAX(salary) --> results to 2000

SELECT id,name,salary
FROM users WHERE SALARY = (
    SELECT MAX(salary)
    FROM users
    where salary < (SELECT MAX(salary) FROM users)
);


SELECT id,name,salary 
FROM users WHERE  
salary = (SELECT MAX(salary) 
FROM users 
WHERE salary < (SELECT MAX(salary) FROM users)
);


Q ) if the third most salary

SELECT id,name,salary WHERE salary = 
(SELECT DISTINCT salary FROM users ORDER BY salary DESC LIMIT 1 OFFSET 2);



(SELECT MAX(salary) 
FROM users) 
WHERE salary <(
    SELECT MAX(salary) 
FROM users) WHERE salary<(
    SELECT MAX(salary) FROM users)


# Arbitrary return 

SELECT id,name,salary 
FROM users WHERE salary = (
    SELECT MAX(salary) FROM users
) LIMIT 1




