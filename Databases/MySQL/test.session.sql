-- Comments in this files are preceeded by double hyphen '--'

-- The '@block' marker indicates that the code below is an individual block of code to be executed individually

-- From the 'The Fireship' Tutorial


-- @block // Initial commands
CREATE TABLE Users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    country VARCHAR(2)
);


-- @block // Individual entry insert
INSERT INTO Users(email, bio, country)
VALUES(
    'hey@world.com',
    'Something else!',
    'US'
)
;-- Returned an error: 'Column count doesn't match value count at row 1' when country = 'USA'


-- @block // Multiple entries insert
INSERT INTO Users(email, bio, country)
VALUES
('hello@world.com', 'foo', 'US'),
('hola@mundo.com', 'bar', 'MX'),
('bonjour@monde.com', 'baz', 'FR') 




-- SELECT STATEMENTS

-- @block
SELECT * FROM Users;

-- @block / With limtis
SELECT email, id FROM Users
LIMIT 2;

-- @block / With order
SELECT * FROM Users
ORDER BY email DESC;

-- @block
SELECT * FROM Users
ORDER BY id ASC;

-- @block / With conditionals
SELECT * FROM Users
WHERE country = 'US';

-- @block
SELECT * FROM Users
WHERE country = 'US'
AND id > 1;

-- @block / With conditionals & a pattern (Stars with 'h')
SELECT * FROM Users
WHERE email LIKE 'h%';




-- INDEX
-- PENDING













-- My Queries

-- @block // Correcting the mistype of the column 'emai'
ALTER TABLE users
CHANGE COLUMN emai email VARCHAR(255) NOT NULL UNIQUE;


-- @block // Changing the name of the table to 'Users' and deleting one of the duplicated 'email' columns
ALTER TABLE users
DROP COLUMN email;


-- @block // Show the column fields
DESCRIBE Users;


-- @block // Drop the whole table
DROP TABLE users;