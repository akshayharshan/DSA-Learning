SQL Joins – Interview Notes (Day 2)
==================================

1. INNER JOIN
-------------

Used when we want only matching rows from both tables.

**Example Tables**

users

```
id	name
1	A
2	B
3	C
```

orders

```
id	user_id	amount
1	1	500
2	1	300
3	2	200
```

**Query**

```sql
SELECT users.name, orders.amount
FROM users
INNER JOIN orders
ON users.id = orders.user_id;
```

**Result**

```
name	amount
A	500
A	300
B	200
```

User C disappears because there is no matching order.

2. LEFT JOIN
------------

Used when we want all rows from the left table, even if there is no match.

**Query**

```sql
SELECT users.name, orders.amount
FROM users
LEFT JOIN orders
ON users.id = orders.user_id;
```

**Result**

```
name	amount
A	500
A	300
B	200
C	NULL
```

User C appears with NULL.

3. Find Users With No Orders
----------------------------

Pattern used in interviews.

**Query**

```sql
SELECT users.name
FROM users
LEFT JOIN orders
ON users.id = orders.user_id
WHERE orders.user_id IS NULL;
```

**Concept**

LEFT JOIN + NULL filter

Used to find missing relationships.

4. Total Order Amount Per User
------------------------------

**Query**

```sql
SELECT users.name, SUM(orders.amount) AS total_amount
FROM users
INNER JOIN orders
ON users.id = orders.user_id
GROUP BY users.id, users.name;
```

**Result**

```
name	total_amount
A	800
B	200
```

5. Users Who Placed More Than One Order
---------------------------------------

**Query**

```sql
SELECT users.name
FROM users
INNER JOIN orders
ON users.id = orders.user_id
GROUP BY users.id, users.name
HAVING COUNT(orders.id) > 1;
```

**Result**

```
name
A
```

6. Total Number of Orders Per User (Including Users With No Orders)
-------------------------------------------------------------------

**Query**

```sql
SELECT users.name, COUNT(orders.id) AS order_count
FROM users
LEFT JOIN orders
ON users.id = orders.user_id
GROUP BY users.id, users.name;
```

**Result**

```
name	order_count
A	2
B	1
C	0
```

7. User With Highest Total Order Amount
---------------------------------------

**Query**

```sql
SELECT users.name, SUM(orders.amount) AS total_amount
FROM users
JOIN orders
ON users.id = orders.user_id
GROUP BY users.id, users.name
ORDER BY total_amount DESC
LIMIT 1;
```

**Result**

```
name	total_amount
A	800
```

8. COUNT(*) vs COUNT(column)
----------------------------

**COUNT(*)**

Counts all rows, including NULL.

**COUNT(column)**

Counts only non-null values.

**Example:**

```sql
COUNT(*)
COUNT(orders.id)
```

For LEFT JOIN queries, prefer:

```sql
COUNT(orders.id)
```

9. GROUP BY Rule
----------------

When using aggregation functions (SUM, COUNT, AVG):

Every column in SELECT must either be:

- aggregated
- or
- included in GROUP BY.

**Example:**

```sql
GROUP BY users.id, users.name
```

Common SQL Interview Patterns
-----------------------------

Pattern 1 – Find Missing Records

```sql
LEFT JOIN
WHERE other_table.id IS NULL
```

Pattern 2 – Aggregation Per Group

```sql
GROUP BY
SUM()
COUNT()
```

Pattern 3 – Top Record

```sql
ORDER BY DESC
LIMIT 1
```