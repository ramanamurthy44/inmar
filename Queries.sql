-- Write the DDL statement that create a table named employees with the following
-- columns:
-- ○ id (integer, primary key, auto-increment)
-- ○ name (string)
-- ○ department (string)
-- ○ salary (decimal)
-- ○ hire_date (date)


CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    department VARCHAR(255),
    salary DECIMAL(10, 2),
    hire_date DATE
);

-- question 2 
-- Insert several records into the employees table.
INSERT INTO employees (name, department, salary, hire_date) VALUES
('Alice Smith', 'Sales', 60000.00, '2023-01-15'),
('Bob Johnson', 'Engineering', 75000.00, '2022-03-22'),
('Charlie Brown', 'Marketing', 50000.00, '2021-07-10'),
('Diana Prince', 'HR', 70000.00, '2023-05-05'),
('Ethan Hunt', 'IT', 90000.00, '2022-11-11');

-- Retrieve all employees in a specific department.
SELECT * FROM employees
WHERE department = 'Sales';
(SELECT * FROM employees
WHERE department = 'DepartmentName';)


-- Update the salary of a specific employee.
UPDATE employees
SET salary = 65000.00
WHERE id = 3;
(UPDATE employees
SET salary = NewSalary
WHERE id = EmployeeID;
)

-- Delete an employee record by ID.
DELETE FROM employees
WHERE id = 5;
(DELETE FROM employees
WHERE id = EmployeeID;)

-- Retrieve the average salary of employees in each department.
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;


-- Given two tables, employees and departments, where the departments table
-- contains information about department names and their IDs, write a query to
-- retrieve a list of all employees along with their department names. If an employee
-- does not belong to a department, their department name should show as NULL.
SELECT e.id, e.name, e.salary, e.hire_date, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department = d.id;

