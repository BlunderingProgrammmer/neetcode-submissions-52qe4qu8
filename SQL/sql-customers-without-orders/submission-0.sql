-- Write your query below
SELECT name
FROM customers
WHERE id NOT IN(SELECT customer_id FROM orders)  -- nested query to get one reult and another imp concept NOT in