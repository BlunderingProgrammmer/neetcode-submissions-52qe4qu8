-- Write your query below
SELECT customer_id 
FROM customers
WHERE customers.year = 2020 AND revenue > 0; -- first question so year can be customer.year or just year