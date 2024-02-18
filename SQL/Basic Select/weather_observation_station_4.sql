DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION
(
    id     int,
    CITY   varchar(21),
    STATE  varchar(2),
    LAT_N  double,
    LONG_W double
);

SELECT COUNT(CITY) - COUNT(DISTINCT CITY) AS difference
FROM STATION;