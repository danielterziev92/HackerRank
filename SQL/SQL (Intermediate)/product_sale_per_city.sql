DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS invoice;
DROP TABLE IF EXISTS invoice_item;
DROP TABLE IF EXISTS product;

CREATE TABLE city
(
    id          int,
    city_name   varchar(128),
    postal_code varchar(16),
    country_id  int
);

CREATE TABLE customer
(
    id               int,
    customer_name    varchar(255),
    city_id          int,
    customer_address varchar(255),
    contact_person   varchar(255),
    email            varchar(128),
    phone            varchar(128),
    is_active        int
);

CREATE TABLE invoice
(
    id              int,
    invoice_number  varchar(255),
    customer_id     int,
    user_account_id int,
    total_price     decimal(8, 2)
);

CREATE TABLE invoice_item
(
    id               int,
    invoice_id       int,
    product_id       int,
    quantity         decimal(8, 2),
    price            decimal(8, 2),
    line_total_price decimal(8, 2)
);

CREATE TABLE product
(
    id                  int,
    sku                 varchar(32),
    product_name        varchar(128),
    product_description varchar(255),
    current_price       decimal(8, 2),
    quantity_in_stock   decimal(8, 2),
    is_active           int
);

SELECT c.city_name,
       p.product_name,
       ROUND(SUM(ii.line_total_price), 2) AS total_amount_spent
FROM city c
         JOIN
     customer cu ON c.id = cu.city_id
         JOIN
     invoice inv ON cu.id = inv.customer_id
         JOIN
     invoice_item ii ON inv.id = ii.invoice_id
         JOIN
     product p ON ii.product_id = p.id
GROUP BY c.city_name,
         p.product_name
ORDER BY total_amount_spent DESC,
         c.city_name ASC,
         p.product_name ASC;