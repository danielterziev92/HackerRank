DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION
(
    id     int,
    CITY   varchar(21),
    STATE  varchar(2),
    LAT_N  double,
    LONG_W double
);


SELECT ROUND(CAST(SUM(LAT_N) AS DECIMAL(12, 2)), 2)  as "lat",
       ROUND(CAST(SUM(LONG_W) AS DECIMAL(12, 2)), 2) as "lon"
FROM STATION;