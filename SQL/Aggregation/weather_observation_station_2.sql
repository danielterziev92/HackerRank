DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION
(
    ID     int,
    CITY   varchar(21),
    STATE  varchar(21),
    LAT_N  int,
    LONG_W int
);

SELECT ROUND(SUM(LAT_N), 2)  AS sum_of_lat_n,
       ROUND(SUM(LONG_W), 2) AS sum_of_long_w
FROM STATION;