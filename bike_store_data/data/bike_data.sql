create database if not exists bike_store;
use bike_store;

-- -----CREATE TABLE-------
CREATE TABLE if not exists brands (
  brand_id INT PRIMARY KEY,
  brand_name VARCHAR(25) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE if not exists categories (
  category_id INT PRIMARY KEY,
  category_name VARCHAR(25) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE if not exists customers (
  customer_id INT PRIMARY KEY,
  first_name VARCHAR(25) NOT NULL,
  last_name VARCHAR(25) NOT NULL,
  phone CHAR(14) NOT NULL UNIQUE,
  email VARCHAR(255) UNIQUE,
  street VARCHAR(255) NOT NULL,
  city VARCHAR(255) NOT NULL,
  state CHAR(2),
  zip_code INT NOT NULL
);

CREATE TABLE if not exists order_items (
  order_id INT PRIMARY KEY,
  item_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  list_price FLOAT NOT NULL,
  discount FLOAT NOT NULL
);

CREATE TABLE if not exists orders(
  order_id INT PRIMARY KEY,
  customer_id INT NOT NULL,
  order_status INT check (order_status in (1,2,3,4)),
  order_date DATE NOT NULL,
  required_date DATE NOT NULL,
  shipped_date DATE NOT NULL,
  store_id INT NOT NULL,
  staff_id INT NOT NULL
);

CREATE TABLE if not exists products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(25) NOT NULL,
  brand_id INT NOT NULL,
  category_id INT NOT NULL,
  model_year INT,
  list_price FLOAT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE if not exists staffs (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(25) NOT NULL,
  brand_id INT NOT NULL,
  category_id INT NOT NULL,
  model_year INT,
  list_price FLOAT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE if not exists stocks (
  store_id INT PRIMARY KEY,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE if not exists stores (
  store_id INT PRIMARY KEY,
  store_name VARCHAR(25) NOT NULL,
  phone CHAR(14) NOT NULL UNIQUE,
  email VARCHAR(255) UNIQUE,
  street VARCHAR(255) NOT NULL,
  city VARCHAR(255) NOT NULL,
  state CHAR(2),
  zip_code INT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
-- ------------------------------

-- -----LOAD FILE-------
LOAD DATA LOCAL INFILE '/home/trung/bike_store_data/data/brands.csv' INTO TABLE brands
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/home/trung/bike_store_data/data/categories.csv' INTO TABLE categories
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/home/trung/bike_store_data/data/customers.csv' INTO TABLE customers
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/home/trung/bike_store_data/data/order_items.csv' INTO TABLE order_items
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/home/trung/bike_store_data/data/orders.csv' INTO TABLE orders
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/home/trung/bike_store_data/data/products.csv' INTO TABLE products
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/home/trung/bike_store_data/data/staffs.csv' INTO TABLE staffs
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/home/trung/bike_store_data/data/stocks.csv' INTO TABLE stocks
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE '/home/trung/bike_store_data/data/stores.csv' INTO TABLE stores
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

-- ------------------------------


