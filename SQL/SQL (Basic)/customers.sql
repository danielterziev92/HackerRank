DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS country_codes;

CREATE TABLE country_codes
(
    country      varchar(20),
    country_code varchar(20)
);

CREATE TABLE customers
(
    customer_id  int,
    name         varchar(20),
    phone_number varchar(13),
    country      varchar(20)
);

INSERT INTO customers
VALUES (1, 'Raghav', 951341341, 'India'),
       (2, 'Jake', 52341351, 'USA'),
       (3, 'Alice', 61341351, 'USA')
;

INSERT INTO country_codes
VALUES ('USA', 1),
       ('India', 91)
;

SELECT c.customer_id,
       c.name,
       CONCAT('+', cc.country_code, '', REPLACE(c.phone_number, ' ', '')) AS phone_with_country_code
FROM customers c
         JOIN
     country_codes cc ON c.country = cc.country
ORDER BY c.customer_id;
