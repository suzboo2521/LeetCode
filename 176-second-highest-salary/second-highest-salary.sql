select max(salary) secondHighestSalary from Employee where
salary < (select max(salary) from Employee);