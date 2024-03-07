DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Grades;

CREATE TABLE Grades
(
    Grade    int,
    Min_Mark int,
    Max_Mark int
);

CREATE TABLE Students
(
    ID    int,
    Name  varchar(17),
    Marks int
);

INSERT INTO Grades
VALUES (1, 0, 9),
       (2, 10, 19),
       (3, 20, 29),
       (4, 30, 39),
       (5, 40, 49),
       (6, 50, 59),
       (7, 60, 69),
       (8, 70, 79),
       (9, 80, 89),
       (10, 90, 100)
;

INSERT INTO Students
VALUES (1, 'Julia', 88),
       (2, 'Samantha', 68),
       (3, 'Maria', 99),
       (4, 'Scarlet', 78),
       (5, 'Ashley', 63),
       (6, 'Jane', 81)
;


WITH Student_info AS (SELECT Students.Name as name, Students.Marks as mark, Grades.Grade as grade
                      FROM Students
                               LEFT JOIN Grades
                                         ON Students.Marks >= Min_Mark AND Students.Marks <= Max_Mark)
SELECT CASE WHEN GRADE >= 8 THEN NAME ELSE NULL END AS NAME, grade, mark
FROM Student_info
ORDER BY CASE
             WHEN grade >= 8 THEN grade
             WHEN grade < 8 THEN grade
             END DESC,
         CASE
             WHEN grade >= 8 THEN name
             WHEN grade < 8 THEN mark
             END ASC;