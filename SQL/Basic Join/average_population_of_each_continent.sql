DROP TABLE IF EXISTS COUNTRY;
DROP TABLE IF EXISTS CITY;

CREATE TABLE COUNTRY
(
    CODE           varchar(3),
    NAME           varchar(44),
    CONTINENT      varchar(13),
    REGION         varchar(25),
    SURFACEAREA    int,
    INDEPYEAR      varchar(5),
    POPULATION     int,
    LIFEEXPECTANCY varchar(4),
    GNP            int,
    GNPOLD         varchar(9),
    LOCALNAME      varchar(44),
    GOVERMENTFORM  varchar(44),
    HEADOFSTATE    varchar(32),
    CAPITAL        varchar(4),
    CODE2          varchar(2)
);

CREATE TABLE CITY
(
    ID          int,
    NAME        varchar(17),
    COUNTRYCODE varchar(3),
    DISTRICT    varchar(20),
    POPULATION  int
);

SELECT COUNTRY.Continent, FLOOR(AVG(CITY.Population)) AS average_population
FROM CITY
         JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
GROUP BY COUNTRY.Continent;

