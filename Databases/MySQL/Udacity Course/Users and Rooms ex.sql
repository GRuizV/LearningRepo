-- Example from the fireship tutorial (Users & Rooms)
--  This example is to illustrate how to create relationships in MySQL

-- @block / Create the 'Rooms' table
CREATE TABLE Rooms(
    id INT PRIMARY KEY AUTO_INCREMENT, -- Room ID (PRIMARY KEY)
    street VARCHAR(255) UNIQUE,
    owner_id INT NOT NULL, -- Owner ID (FOREIGN KEY)
    FOREIGN KEY (owner_id) REFERENCES Users(id)
);


-- @block / Insert rooms
INSERT INTO Rooms (owner_id, street)
VALUES
(1, 'San Diego Sailboat'),
(1, 'Nantucket cottage'),
(1, 'Vail Cabin'),
(1, 'SF Cardboard Box');




-- @block / RELATION QUERIES (JOIN)

-- @block / INNER JOIN: Intersection - All rooms with a 'user' owner
SELECT * FROM Users
INNER JOIN Rooms
ON Rooms.owner_id = Users.id;

-- @block / LEFT JOIN: All users independent whether they have a room
SELECT * FROM Users
LEFT JOIN Rooms
ON Rooms.owner_id = Users.id;

-- @block / RIGHT JOIN: All room independent whether they have a owner
SELECT * FROM Users
RIGHT JOIN Rooms
ON Rooms.owner_id = Users.id;

-- @block / OUTER JOIN: It should supposedly show all the data from both tables but that's not supported in MySQL
SELECT * FROM Users
OUTER JOIN Rooms
ON Rooms.owner_id = Users.id;




-- @block / RENAMING: The use of 'AS'

-- @block / INNER JOIN: Intersection - All rooms with a 'user' owner
SELECT
    Users.id AS user_id,
    Rooms.id AS room_id,
    email,
    street

FROM Users
INNER JOIN Rooms ON Rooms.owner_id = Users.id;








-- @block / JOIN with a intermidiate table: Many-To-Many relationship

-- @block / CREATE the intermidiate TABLE
CREATE TABLE Bookings (
    id INT AUTO_INCREMENT,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY (guest_id) REFERENCES Users(id),
    FOREIGN KEY (room_id) REFERENCES Rooms(id)
);



-- @block / INSERT bookings in Bookings
INSERT INTO Bookings (guest_id, room_id, check_in)
VALUES
(1, 1, '2024-08-07 14:00:00'),
(2, 3, '2024-08-09 19:00:00'),
(4, 4, '2024-08-09 07:00:00'),
(5, 2, '2024-08-09 09:00:00'),
(1, 3, '2024-08-10 10:00:00'),
(1, 2, '2024-08-15 10:00:00'),
(1, 4, '2024-08-18 10:00:00'),
(3, 4, '2024-08-18 13:00:00');



-- @block / INSERT bookings in Bookings
SELECT * FROM Bookings
where room_id = 2;


-- @block / INNER JOIN to check all the rooms a specific user has booked
SELECT
    guest_id,
    Rooms.street,
    check_in
FROM Bookings
INNER JOIN Rooms ON Rooms.id = Bookings.room_id
WHERE guest_id = 3
;


-- @block / INNER JOIN to check all guests that have stayed at a rooms, ordered asccendingly by room_id
SELECT
    guest_id,
    room_id,    
    email,
    bio,
    check_in
FROM Bookings
INNER JOIN Users ON Users.id = guest_id
ORDER BY room_id ASC
;

















-- @block / Delete individual records
DELETE FROM Rooms where id = 8;

-- @block / Delete records in bulk
DELETE FROM Rooms where id BETWEEN 5 AND 7;


-- @block / Delete table
DROP TABLE Bookings;

-- @block / View all command
SELECT * FROM rooms;
SELECT * FROM users;