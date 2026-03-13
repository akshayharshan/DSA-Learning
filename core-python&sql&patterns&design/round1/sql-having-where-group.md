# SQL Notes – GROUP BY, HAVING, COUNT

## 1. GROUP BY

GROUP BY groups rows that have the same values in specified columns.

Example:

SELECT customer, SUM(amount)
FROM orders
GROUP BY customer;

Explanation:
- Rows are grouped by customer
- Aggregate functions operate on each group


## 2. Aggregate Functions

Aggregate functions perform calculations on groups of rows.

Common aggregate functions:

COUNT()
SUM()
AVG()
MAX()
MIN()


Example:

SELECT customer, SUM(amount)
FROM orders
GROUP BY customer;


## 3. COUNT()

COUNT() counts rows.

### COUNT(*)

Counts all rows.

SELECT COUNT(*)
FROM orders;


### COUNT(column)

Counts non-null values in a column.

SELECT COUNT(amount)
FROM orders;


### COUNT with GROUP BY

SELECT customer, COUNT(*) AS order_count
FROM orders
GROUP BY customer;


## 4. GROUP BY without Aggregate Functions

GROUP BY can also return unique values.

SELECT department
FROM employees
GROUP BY department;

This behaves similar to:

SELECT DISTINCT department
FROM employees;


## 5. WHERE

WHERE filters rows before grouping.

Example:

SELECT customer, COUNT(*)
FROM orders
WHERE amount > 100
GROUP BY customer;

Steps:
1. Rows filtered using WHERE
2. Remaining rows grouped
3. Aggregation performed


## 6. HAVING

HAVING filters groups after grouping.

Example:

SELECT customer, COUNT(*)
FROM orders
GROUP BY customer
HAVING COUNT(*) > 2;


## 7. WHERE vs HAVING

WHERE:
- Filters rows before grouping
- Cannot use aggregate functions

HAVING:
- Filters groups after aggregation
- Used with aggregate functions


## 8. SQL Execution Order

Typical logical execution order:

FROM
WHERE
GROUP BY
HAVING
SELECT
ORDER BY


## 9. Example Queries

### Count orders per customer

SELECT customer, COUNT(*) AS order_count
FROM orders
GROUP BY customer;


### Customers with more than 2 orders

SELECT customer, COUNT(*) AS order_count
FROM orders
GROUP BY customer
HAVING COUNT(*) > 2;


### Total amount per customer for orders above 100

SELECT customer, SUM(amount) AS total_amount
FROM orders
WHERE amount > 100
GROUP BY customer;