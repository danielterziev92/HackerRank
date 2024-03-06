DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION
(
    ID     int,
    CITY   varchar(21),
    STATE  varchar(21),
    LAT_N  int,
    LONG_W int
);

SELECT ROUND(ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W)), 4) AS Manhattan_Distance
FROM STATION;
