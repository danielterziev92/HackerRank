DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION
(
    id     int,
    CITY   varchar(21),
    STATE  varchar(2),
    LAT_N  double,
    LONG_W double
);

INSERT INTO STATION
VALUES (1, 'DEF', '', 1, 1),
       (2, 'ABC', '', 1, 1),
       (3, 'PQRS', '', 1, 1),
       (4, 'WXY', '', 1, 1);


SELECT CITY,
       length(CITY) as c_l
FROM STATION
ORDER BY c_l ASC,
         CITY ASC
LIMIT 1;

SELECT CITY,
       LENGTH(CITY) AS c_l
FROM STATION
ORDER BY c_l DESC,
         CITY ASC
LIMIT 1;