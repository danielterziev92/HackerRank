DROP TABLE IF EXISTS OCCUPATIONS;
CREATE TABLE OCCUPATIONS
(
    Name       varchar(50),
    Occupation varchar(50)
);

INSERT INTO OCCUPATIONS
VALUES ('Samantha', 'Doctor'),
       ('Julia', 'Actor'),
       ('Maria', 'Actor'),
       ('Meera', 'Singer'),
       ('Ashely', 'Professor'),
       ('Ketty', 'Professor'),
       ('Christeen', 'Professor'),
       ('Jane', 'Actor'),
       ('Jenny', 'Doctor'),
       ('Priya', 'Singer')
;

SELECT MAX(CASE WHEN Occupation = 'Doctor' THEN Name END)    AS Doctor,
       MAX(CASE WHEN Occupation = 'Professor' THEN Name END) AS Professor,
       MAX(CASE WHEN Occupation = 'Singer' THEN Name END)    AS Singer,
       MAX(CASE WHEN Occupation = 'Actor' THEN Name END)     AS Actor
FROM (SELECT Name,
             Occupation,
             ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS rn
      FROM OCCUPATIONS)
GROUP BY rn
ORDER BY rn;

