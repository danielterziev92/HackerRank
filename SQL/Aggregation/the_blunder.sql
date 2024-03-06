DROP TABLE IF EXISTS EMPLOYEES;
CREATE TABLE EMPLOYEES
(
    ID     int,
    Name   varchar(17),
    Salary int
);

INSERT INTO EMPLOYEES
VALUES (1, 'Kristeen', 1420),
       (2, 'Ashley', 2006),
       (3, 'Julia', 2210),
       (4, 'Maria', 3000)
;

SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary, '0', '')))
FROM EMPLOYEES;
