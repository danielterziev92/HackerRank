DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION
(
    ID     int,
    CITY   varchar(21),
    STATE  varchar(21),
    LAT_N  int,
    LONG_W int
);

SELECT ROUND(LAT_N, 4) AS median_lat_n
FROM (SELECT LAT_N,
             ROW_NUMBER() OVER (ORDER BY LAT_N) AS row_num,
             COUNT(*) OVER ()                   AS total_rows
      FROM STATION) sub
WHERE row_num IN ((total_rows + 1) / 2, (total_rows + 2) / 2);
