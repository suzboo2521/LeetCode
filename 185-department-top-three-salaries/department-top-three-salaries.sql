SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
INNER JOIN Department d 
    ON e.departmentId = d.id
WHERE 3 > (
    SELECT COUNT(DISTINCT t.salary)
    FROM Employee t
    WHERE t.salary > e.salary
      AND t.departmentId = e.departmentId
);
