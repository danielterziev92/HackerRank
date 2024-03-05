DROP TABLE IF EXISTS CITY;
CREATE TABLE CITY
(
    ID          int,
    NAME        varchar(17),
    COUNTRYCODE varchar(3),
    DISTRICT    varchar(20),
    POPULATION  int
);


SELECT max(CITY.POPULATION) - min(CITY.POPULATION)
FROM CITY;