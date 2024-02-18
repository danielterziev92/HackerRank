DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION
(
    id     int,
    CITY   varchar(21),
    STATE  varchar(2),
    LAT_N  double,
    LONG_W double
);

SELECT DISTINCT CITY FROM STATION
WHERE ID % 2 = 0;