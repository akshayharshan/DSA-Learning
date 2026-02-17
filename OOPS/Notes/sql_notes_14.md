Now As Promised – Short Revision Note (Push to Git)

You can copy this as day_sql_notes.md.

📌 SQL Notes – Day 1 (Ranking, MAX, Index Basics)
1️⃣ MAX vs ORDER BY
SELECT MAX(salary) FROM users;


Aggregate

Returns scalar

Efficient

SELECT salary FROM users ORDER BY salary DESC LIMIT 1;


Sort + limit

Returns row-based value

2️⃣ Return Employee with Highest Salary
SELECT *
FROM users
WHERE salary = (SELECT MAX(salary) FROM users);

3️⃣ Second Highest Salary
SELECT MAX(salary)
FROM users
WHERE salary < (SELECT MAX(salary) FROM users);


OR

SELECT DISTINCT salary
FROM users
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

4️⃣ Index & Performance

Without index:

MAX → O(n)

ORDER BY → O(n log n)

With index:

Both can be O(log n)

5️⃣ Non-Sargable Conditions (Avoid)
WHERE salary + 1000 > 5000   ❌
WHERE UPPER(name) = 'A'      ❌


Rewrite as:

WHERE salary > 4000          ✅

6️⃣ Composite Index Rule (Leftmost Prefix)

Index: (salary, name)

Query	Index Used?
WHERE salary = ?	✅
WHERE salary > ?	✅
WHERE salary = ? AND name = ?	✅
WHERE name = ?





Today you covered:

Mutation vs rebinding (stabilized)

Decorator execution flow (clear now)

Decorator with parameters

SQL MAX vs ORDER BY

Subqueries for ranking

Index basics

SARGable queries

Leftmost prefix rule

Composite index behavior