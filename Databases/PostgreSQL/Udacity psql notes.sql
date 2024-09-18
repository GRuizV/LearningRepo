

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




-- @block // Values Selection
SELECT * FROM fishies_table;










