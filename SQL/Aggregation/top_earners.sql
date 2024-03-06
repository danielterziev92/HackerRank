DROP TABLE IF EXISTS Employee;
CREATE TABLE Employee
(
    employee_id int,
    name        varchar(17),
    months      int,
    salary      int
);

INSERT INTO Employee
VALUES (12228, 'Rose', 15, 1968),
       (33645, 'Angela', 1, 3443),
       (45692, 'Frank', 17, 1608),
       (56118, 'Patrick', 7, 1345),
       (59725, 'Lisa', 11, 2330),
       (74197, 'Kimberly', 16, 4372),
       (78454, 'Bonnie', 8, 1771),
       (83565, 'Michael', 6, 2017),
       (98607, 'Todd', 5, 3396),
       (99989, 'Joe', 9, 3573)
;

WITH MaxEarnings AS (SELECT MAX(Employee.months * Employee.salary) AS MaxTotalEarnings
                     FROM Employee)

SELECT MaxTotalEarnings,
       COUNT(*) AS NumberOfEmployeesWithMaxEarnings
FROM Employee,
     MaxEarnings
WHERE Employee.months * Employee.salary = MaxTotalEarnings
GROUP BY MaxTotalEarnings;
