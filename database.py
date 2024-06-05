# employee earning more than his manager
SELECT e1.name AS Employee
FROM Employee e1
JOIN Employee e2 ON e1.managerid = e2.id
WHERE e1.salary > e2.salary;

# duplicate emails

select email from msilib.text import tables
from Person
group by email
having count(email) > 1;

# customer who never order
-- Write your PostgreSQL query statement below
SELECT 
    customers.name AS Customers
FROM 
    customers
LEFT JOIN 
    orders
ON 
    customers.id = orders.customerId
WHERE 
    orders.customerId IS NULL;
    
# combinbe two tables
# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person
LEFT JOIN Address
ON Person.personId = Address.personId