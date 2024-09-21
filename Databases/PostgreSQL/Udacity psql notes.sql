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

-- @block 'products' table population
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

-- @block 'sales' table population
INSERT INTO sales (sku, sales_date, count) 
    VALUES
    ('222', '2009-04-13', 4),
    ('343', '2010-05-31', 4),
    ('222', '2011-11-11', 4)
;

-- @block 'sales' table repeated foreign key
INSERT INTO sales (sku, sales_date, count) VALUES ('111', '2019-04-13', 4)
-- Not possible since '111' doesn't exist in products
;


-- ANOTHER WAYS OF COUNTING / LEFT JOIN
-- @block Count in a JOIN: Number of times a product was sold 
SELECT products.name, products.sku, count(*) AS num
FROM products JOIN sales
ON products.sku = sales.sku
GROUP BY products.sku

    -- The problem with this query is that is not showing when a product is not sold, it only omits it
;

-- @block Count in a JOIN: Number of times a product was sold, including products not sold yet
SELECT products.name, products.sku, count(sales.sku) AS num
FROM products LEFT JOIN sales
ON products.sku = sales.sku
GROUP BY products.sku;


-- Programs & Bugs
-- @block 'programs' and 'bugs' table creation
CREATE TABLE programs (
    name TEXT,
    filename TEXT
)

CREATE TABLE bugs (
    filename TEXT,
    description TEXT,
    id SERIAL PRIMARY KEY
);

-- @block 'programs' table population
INSERT INTO programs (name, filename) VALUES
('Your Database Code', 'database.py'),
('Fancy Website', 'index.html'),
('Fancy Website', 'styles.css'),
('Fancy Website', 'buttons.js'),
('Sweet Spreadsheet', 'cells.hs'),
('Sweet Spreadsheet', 'sheets.hs'),
('Sweet Spreadsheet', 'interface.hs')
;

-- @block 'bugs' table population
INSERT INTO bugs (filename, description) VALUES
('index.html', 'Add microformat tags for search engines'),
('styles.css', 'Pink Comic Sans is a silly thing'),
('styles.css', 'Make graphs colorblind-friendly'),
('sheets.hs', 'Recalculations cons too much'),
('interface.hs', 'UI needs to support Mac')
;

-- @block Count in a JOIN: Programs with their number of bugs
SELECT programs.name, count(*) AS num
FROM programs JOIN bugs
ON programs.filename = bugs.filename
GROUP BY programs.name
ORDER BY num;

-- @block Count in a JOIN: Programs with their number of bugs
SELECT programs.name, count(bugs.filename) AS num
FROM programs LEFT JOIN bugs
ON programs.filename = bugs.filename
GROUP BY programs.name
ORDER BY num;




-- SELF JOINS
-- @block 'residences' table creation
CREATE TABLE residences(
    id INT PRIMARY KEY,
    building TEXT,
    room TEXT)
;

-- @block 'residences' table population
INSERT INTO residences (id, building, room) VALUES
(104131, 'Dolliver', '14'),
(105540, 'Kendrick', '3B'),
(118199, 'Kendrick', '1A'),
(161282, 'Dolliver', '7'),
(170267, 'Dolliver', '1'),
(231742, 'Kendrick', '3B'),
(250841, 'Kendrick', '2B'),
(410315, 'Crosby', '20'),
(413001, 'Crosby', '10'),
(427611, 'Dolliver', '10'),
(477801, 'Dolliver', '8'),
(496747, 'Crosby', '19'),
(498446, 'Crosby', '21'),
(505241, 'Dolliver', '8'),
(612413, 'Crosby', '31'),
(707536, 'Dolliver', '14'),
(741532, 'Crosby', '19'),
(762907, 'Dolliver', '9'),
(824292, 'Kendrick', '1A'),
(851866, 'Crosby', '22'),
(881256, 'Crosby', '10'),
(931027, 'Crosby', '31'),
(958827, 'Dolliver', '1')
;

-- @block SELF JOIN / Almost there
SELECT a.id, b.id, a.building, a.room
FROM residences AS a, residences AS b
WHERE a.building = b.building AND a.room = b.room and a.id != b.id
ORDER BY a.building, a.room

    -- The Issue with this query is that doesn't eliminate the repeated pairs,
    -- Say it catches (a,b), but later the permutation (b,a) appears.

;

-- @block SELF JOIN / Corrected
SELECT a.id, b.id, a.building, a.room
FROM residences AS a, residences AS b
WHERE a.building = b.building AND a.room = b.room and a.id < b.id
ORDER BY a.building, a.room;




-- SUBQUERIES
-- @block 'mooseball' table creation
CREATE TABLE mooseball(
    player TEXT,
    team TEXT,
    score INT
);

-- @block 'mooseball' table population
INSERT INTO mooseball (player, team, score) VALUES
('Martha Moose', 'Ice Wesels', 17),
('Bullwinkle', 'Frostbiters', 23),
('Joe Moosington', 'Ice Wesels', 11),
('Mighty Moose', 'Frostbiters', 41),
('Mickey Moose', 'Traffic Stoppers', 36),
('La Moosarina', 'Traffic Stoppers', 12)
;

-- @block SELECT: To show the highest score per team
SELECT team, max(score) AS bigscore 
FROM mooseball 
GROUP BY team
ORDER BY bigscore DESC;

-- @block SUBQUERY - SELECT: To show the average high-scorer's score
SELECT avg(bigscore) FROM (

    SELECT team, max(score) AS bigscore 
    FROM mooseball 
    GROUP BY team
    ORDER BY bigscore DESC
) 
AS maxes
    -- This last line doesn't really is used anywhere, but PostgreSQL makes us name the result syntactically
;


-- @block SUBQUERY - EXECISE (IN SQLITE): Instead of one query, two.

    -- Base: Two Queries
    SELECT avg(weight) AS av FROM players
    SELECT name, weight FROM players WHERE weight < 

    -- My Solution
    SELECT name, weight
        FROM players
        WHERE weight < (
            SELECT avg(weight) FROM players
    )   

    -- STR FORM
    SELECT name, weight FROM players WHERE weight < (SELECT avg(weight) FROM players)
;




-- VIEWS
-- @block 'enrollment' table creation
CREATE TABLE enrollment(
    student_id TEXT,
    course_id TEXT
);

-- @block 'enrollment' table population
INSERT INTO enrollment (student_id, course_id) VALUES
    ('413011', 'CS101'),
    ('612123', 'B102'),
    ('102542', 'CS101'),
    ('231705', 'CS101'),
    ('341024', 'MATH413')
;

-- @block View creation
CREATE VIEW course_size AS
SELECT course_id, count(*) AS num
FROM enrollment
GROUP BY course_id;

-- @block Accesing to the created view
SELECT * FROM course_size;





-- MISC
-- @block // Values Selection
SELECT * FROM residences;

-- @block // Table deletion
DROP TABLE products;

-- @block // Deleting specific rows
DELETE FROM mooseball WHERE player = 'La Moosarina'
;









