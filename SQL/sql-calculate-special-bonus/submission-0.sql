-- Write your query below
SELECT employee_id ,--case-when then else struct imp and also substring fuc to get first name
CASE 
    WHEN employee_id % 2 =1 AND SUBSTRING(name,1,1) != 'M' THEN salary
    ELSE 0
END AS Bonus 
FROM employees
GROUP BY employee_id
