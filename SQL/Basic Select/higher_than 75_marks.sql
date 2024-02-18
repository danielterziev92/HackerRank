DROP TABLE IF EXISTS STUDENTS;
CREATE TABLE STUDENTS
(
    ID    int,
    Name  varchar(20),
    Marks int
);

INSERT INTO STUDENTS
VALUES (1, 'Ashley', 81),
       (2, 'Samantha', 75),
       (3, 'Julia', 76),
       (4, 'Belvet', 84);


SELECT STUDENTS.Name
FROM STUDENTS
WHERE Marks > 75
ORDER BY RIGHT (Name, 3), ID;
