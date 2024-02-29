DROP TABLE IF EXISTS TRIANGLES;
CREATE TABLE TRIANGLES
(
    a int,
    b int,
    c int
);

INSERT INTO TRIANGLES
VALUES (20, 20, 23),
       (20, 20, 20),
       (20, 21, 22),
       (13, 14, 30)
;


SELECT CASE
           WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
           WHEN A = B AND B = C THEN 'Equilateral'
           WHEN A = B OR B = C OR A = C THEN 'Isosceles'
           ELSE 'Scalene'
           END AS TriangleType
FROM TRIANGLES;