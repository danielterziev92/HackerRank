DROP TABLE IF EXISTS student_information;
DROP TABLE IF EXISTS faculty_information;

CREATE TABLE student_information
(
    roll_number int,
    name        varchar(20),
    advisor     int
);

CREATE TABLE faculty_information
(
    employee_ID int,
    gender      varchar(20),
    salary      int
);

INSERT INTO student_information
VALUES (1, 'Robert', 2),
       (2, 'Claire', 1),
       (3, 'Kimmy', 2)
;

INSERT INTO faculty_information
VALUES (1, 'M', 21000),
       (2, 'F', 18000)
;

SELECT si.roll_number, si.name
FROM student_information si
JOIN faculty_information fi ON si.advisor = fi.employee_ID
WHERE
    (fi.gender = 'M' AND fi.salary > 15000)
    OR
    (fi.gender = 'F' AND fi.salary > 20000);
