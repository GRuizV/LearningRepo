
-- BASICS
-- @block // Table creation query: With a serial id key
CREATE TABLE fishies_table (id SERIAL PRIMARY KEY, name TEXT);

-- @block // Values insertion into a table
INSERT INTO fishies_table (name) VALUES
    ('Goldfish'),
    ('Betta'),
    ('Angelfish')
;

-- @block // Single value adding
INSERT INTO fishies_table (name) VALUES
    ('Catfish')
;

-- @block // Inserting a blank value
INSERT INTO fishies_table (name) VALUES (NULL);

-- @block // Alternative form of the same
INSERT INTO fishies_table DEFAULT VALUES;

-- @block // Deleting specific rows
DELETE FROM fishies_table WHERE id IN (6,7,8);


-- RERENTIAL CONSTRAINTS
-- @block Initial reference table creation
CREATE TABLE products(
    sku TEXT PRIMARY KEY,
    price TEXT,
    name TEXT)
;

-- @block 'product' table population
INSERT INTO products (sku, price, name) VALUES
    ('101', '$413', 'Ash Diffuser'),
    ('222', '$11.11', 'Circular Fluid'),
    ('343', '$61.20', 'Auxiliary Vise'),
    ('1025', '$0.33', 'Coaxial Grommet')
;

-- @block referential 'sales' table creation
CREATE TABLE sales(
    sku TEXT REFERENCES products,
    /* alternatively, is the two tables don't share the same column name,
        the correct statment should be 'col_name TEXT REFERENCES products (sku)'
    */
    sales_date DATE,
    count INTEGER
)
;

-- @block 'product' table population
INSERT INTO sales (sku, sales_date, count) 
    VALUES
    ('222', '2009-04-13', 4),
    ('343', '2010-05-31', 4),
    ('222', '2011-11-11', 4)
;

-- @block 'product' table population
INSERT INTO sales (sku, sales_date, count) VALUES ('111', '2019-04-13', 4)
-- Not possible since '111' doesn't exist in products
;
    




-- MISC
-- @block // Values Selection
SELECT * FROM sales;

-- @block // Table deletion
DROP TABLE products;









