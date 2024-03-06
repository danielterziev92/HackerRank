DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION
(
    ID     int,
    CITY   varchar(21),
    STATE  varchar(21),
    LAT_N  int,
    LONG_W int
);

SELECT ROUND(SQRT(POW(MAX(LAT_N) - MIN(LAT_N), 2) + POW(MAX(LONG_W) - MIN(LONG_W), 2)), 4) AS Euclidean_Distance
FROM STATION;
