Find employees who earn more than the minimum salary.?

SELECT name 
FROM emplyees
WHERE salary  >(
    SELECT MIN(salary)
    FROM employees
)

Second Highest Salary

SELECT MAX(salary) 
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees

)

Q1) SELECT MAX(salary)
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
    WHERE salary <(
        SELECT MAX(salary)
        FROM employees
    )
)

SELECT salary FROM employees ORDER BY DESC LIMIT 1 OFFSET 2


Q2) SELECT name, salary FROM employees
where salary > (
    SELECT AVG(salary)
    FROM employees
)