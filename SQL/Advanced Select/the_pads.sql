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

SELECT Name || '(' || UPPER(SUBSTR(Occupation, 1, 1)) || ')' as NameWithProfession
FROM OCCUPATIONS
ORDER BY NameWithProfession;

SELECT 'There are a total of ' || COUNT(*) || ' ' || LOWER(Occupation) || 's.' AS OccupationCount
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(*), LOWER(Occupation);
