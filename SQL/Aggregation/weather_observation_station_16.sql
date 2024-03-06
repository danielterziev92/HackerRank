DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION
(
    ID     int,
    CITY   varchar(21),
    STATE  varchar(21),
    LAT_N  int,
    LONG_W int
);

SELECT ROUND(MIN(LAT_N), 4) AS smallest_lat_n
FROM STATION
WHERE LAT_N > 38.7780;
