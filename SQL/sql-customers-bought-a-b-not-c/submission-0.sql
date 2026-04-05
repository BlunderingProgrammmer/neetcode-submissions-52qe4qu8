-- Write your query below
SELECT customer_id ,customer_name
FROM customers c
WHERE 
    c.customer_id IN (
        SELECT o.customer_id FROM orders o WHERE product_name = 'A'
    ) AND
    c.customer_id IN (
        SELECT o.customer_id FROM orders o WHERE product_name = 'B'
    ) AND
    c.customer_id NOT IN (
        SELECT o.customer_id FROM orders o WHERE product_name = 'C'
    ) 

ORDER BY C.customer_name