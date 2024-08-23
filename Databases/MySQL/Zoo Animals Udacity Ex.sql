
-- @block
CREATE TABLE animals (  
       name text,
       species text,
       birthdate date);

CREATE TABLE diet (
       species text,
       food text);  

CREATE TABLE taxonomy (
       name text,
       species text,
       genus text,
       family text,
       t_order text); 
 
CREATE TABLE ordernames (
       t_order text,
       name text)
;


-- @block // Animals table Populating
INSERT INTO animals (name, species, birthdate)
VALUES 
('Andrea', 'alpaca', '2001-01-16'),
('Bruno', 'alpaca', '2004-09-23'),
('Charlie', 'alpaca', '2004-09-23'),
('Della', 'alpaca', '2006-01-09'),
('Emma', 'alpaca', '2013-03-16'),
('Fred', 'brown bear', '1993-05-02'),
('George', 'brown bear', '1997-06-24'),
('Molly', 'brown bear', '1981-10-17'),
('Eliezer', 'camel', '1971-03-08'),
('Giuseppe', 'camel', '1979-12-25'),
('Taro', 'camel', '1981-08-10'),
('Fido', 'dingo', '1999-08-04'),
('Spot', 'dingo', '2007-11-07'),
('Rover', 'dingo', '2008-08-24'),
('Medusa', 'echidna', '2003-01-31'),
('Zarathustra', 'ferret', '2006-09-18'),
('Zebediah', 'ferret', '2006-10-11'),
('Zephaniah', 'ferret', '2010-02-02'),
('Zenobia', 'ferret', '2099-09-03'),
('Zara', 'ferret', '2007-12-17'),
('Max', 'gorilla', '2001-04-23'),
('Dave', 'gorilla', '1988-09-29'),
('Becky', 'gorilla', '1979-07-04'),
('Liz', 'gorilla', '1998-06-12'),
('George', 'gorilla', '2011-01-09'),
('George', 'gorilla', '1998-05-18'),
('Wendell', 'gorilla', '1982-09-24'),
('Bjorn', 'gorilla', '2000-03-07'),
('Kristen', 'gorilla', '1990-04-25'),
('Cherries', 'hyena', '2007-06-08'),
('Biff', 'hyena', '2011-06-09'),
('Tinkerbell', 'hyena', '2009-11-10'),
('George', 'iguana', '2013-10-18'),
('Cheech', 'iguana', '2006-12-19'),
('Spot', 'iguana', '2010-07-23'),
('Andrea', 'iguana', '1999-09-09'),
('Devoe', 'jackal', '2009-09-25'),
('Duran', 'jackal', '2009-09-20'),
('Jethro', 'jackal', '2012-04-29'),
('Tiffany', 'jackal', '2007-12-26'),
('Sue', 'jackal', '2003-12-21'),
('Alison', 'llama', '1997-11-24'),
('Ben', 'llama', '1984-01-05'),
('Cordelia', 'llama', '1990-10-21'),
('Eli', 'llama', '2002-02-22'),
('John', 'llama', '1986-01-17'),
('Glenn', 'llama', '1986-04-13'),
('Meg', 'llama', '2011-09-08'),
('Mel', 'llama', '2000-10-31'),
('Veronica', 'llama', '1994-07-09'),
('Ricky', 'mongoose', '2006-02-28'),
('Charlie', 'moose', '2001-12-19'),
('Lucy', 'moose', '1990-03-27'),
('Patty', 'moose', '1996-04-19'),
('Max', 'moose', '2002-06-15'),
('Francis', 'narwhal', '1996-04-27'),
('Bacon', 'narwhal', '1975-02-07'),
('Raja', 'orangutan', '1975-04-09'),
('Ratu', 'orangutan', '1989-09-15'),
('Putera', 'orangutan', '1993-06-29'),
('Gajah', 'orangutan', '2011-05-26'),
('Singa', 'orangutan', '2012-11-03'),
('Kambing', 'orangutan', '1988-11-12'),
('Chris', 'platypus', '2003-12-21'),
('Sandy', 'platypus', '2008-09-09'),
('Pat', 'platypus', '2000-04-13'),
('Mary', 'raccoon', '2011-04-05'),
('Martha', 'raccoon', '2009-10-24'),
('John', 'raccoon', '2009-08-11'),
('Mal', 'sea lion', '1987-04-29'),
('Zoe', 'sea lion', '1991-05-19'),
('River', 'sea lion', '2004-07-08'),
('Inara', 'sea lion', '2001-08-18'),
('Simon', 'sea lion', '2000-12-16'),
('Morgan', 'unicorn', '1875-01-24'),
('Laylah', 'unicorn', '1752-05-20'),
('Bertrand', 'warthog', '2007-11-12'),
('Hypatia', 'warthog', '2007-05-20'),
('Emmy', 'warthog', '2008-04-15'),
('Jack', 'yak', '1996-09-20'),
('Mac', 'yak', '1996-10-19'),
('Slack', 'yak', '1997-09-05'),
('Pac', 'yak', '2000-08-09'),
('Track', 'yak', '2009-03-28'),
('Owuru', 'zebra', '1989-03-15'),
('Ekwensu', 'zebra', '1993-10-31'),
('Imaha', 'zebra', '1995-06-08'),
('Adiaha', 'zebra', '2005-05-12'),
('Obi Ike', 'zebra', '2014-04-30');



-- @block // Diet table Populating
INSERT INTO diet (species, food)
VALUES 
('alpaca', 'plants'),
('brown bear', 'fish'),
('brown bear', 'meat'),
('brown bear', 'plants'),
('camel', 'plants'),
('dingo', 'meat'),
('echidna', 'insects'),
('ferret', 'meat'),
('ferret', 'eggs'),
('gorilla', 'plants'),
('hyena', 'meat'),
('iguana', 'plants'),
('jackal', 'meat'),
('llama', 'plants'),
('moose', 'plants'),
('mongoose', 'snakes'),
('mongoose', 'eggs'),
('narwhal', 'fish'),
('orangutan', 'plants'),
('orangutan', 'insects'),
('platypus', 'insects'),
('platypus', 'shellfish'),
('quetzal', 'insects'),
('quetzal', 'plants'),
('raccoon', 'insects'),
('raccoon', 'plants'),
('raccoon', 'meat'),
('raccoon', 'shellfish'),
('sea lion', 'fish'),
('unicorn', 'plants'),
('warthog', 'plants'),
('warthog', 'meat'),
('warthog', 'insects'),
('yak', 'plants'),
('zebra', 'plants');



-- @block // Taxonomy table Populating
INSERT INTO taxonomy (name, species, genus, family, t_order )
VALUES
('alpaca', 'pacos', 'Vicugna', 'Camelidae', 'Artiodactyla'),
('brown bear', 'arctos', 'Ursus', 'Ursidae', 'Carnivora'),
('camel', 'dromedarius', 'Camelus', 'Camelidae', 'Artiodactyla'),
('dingo', 'lupus', 'Canis', 'Canidae', 'Carnivora'),
('echidna', 'aculeatus', 'Tachyglossus', 'Tachyglossidae', 'Monotremata'),
('ferret', 'putorius', 'Mustela', 'Mustelidae', 'Carnivora'),
('gorilla', 'gorilla', 'Gorilla', 'Hominidae', 'Primates'),
('hyena', 'crocuta', 'Crocuta', 'Hyaenidae', 'Carnivora'),
('iguana', 'iguana', 'Iguana', 'Iguanidae', 'Squamata'),
('jackal', 'aureus', 'Canis', 'Canidae', 'Carnivora'),
('llama', 'glama', 'Lama', 'Camelidae', 'Artiodactyla'),
('moose', 'alces', 'Alces', 'Cervidae', 'Artiodactyla'),
('mongoose', 'parvula', 'Helogale', 'Herpestidae', 'Carnivora'),
('narwhal', 'monoceros', 'Monodon', 'Monodontidae', 'Cetacea'),
('orangutan', 'borneo', 'Pongo', 'Hominidae', 'Primates'),
('platypus', 'anatinus', 'Ornithorhynchus', 'Ornithorhynchidae', 'Monotremata'),
('quetzal', 'mocinno', 'Pharomachrus', 'Trogonidae', 'Trogoniformes'),
('raccoon', 'lotor', 'Procyon', 'Procyonidae', 'Carnivora'),
('sea lion', 'californianus', 'Zalophus', 'Otariidae', 'Carnivora'),
('unicorn', 'monoceros', 'Equus', 'Equidae', 'Perissodactyla'),
('warthog', 'africanus', 'Phacochoerus', 'Suidae', 'Artiodactyla'),
('yak', 'grunniens', 'Bos', 'Bovidae', 'Artiodactyla'),
('zebra', 'quagga', 'Equus', 'Equidae', 'Perissodactyla');




-- @block // ordernames table Populating
INSERT INTO ordernames (t_order, name)
VALUES
('Artiodactyla', 'even-toed ungulates'),
('Carnivora', 'carnivores'),
('Monotremata', 'monotremes'),
('Primates', 'primates'),
('Squamata', 'lizards and snakes'),
('Cetacea', 'whales and dolphins'),
('Trogoniformes', 'trogons and quetzals'),
('Perissodactyla', 'odd-toed ungulates'),
('Chiroptera', 'bats')





-- @block // Udacity exercise
-- Find the one food that is eaten by only one animal.
-- The animals table has columns (name, species, birthdate) for each individual.
-- The diet table has columns (species, food) for each food that a species eats.

SELECT food, count(animals.name) AS num FROM diet
INNER JOIN animals ON animals.species = diet.species
GROUP BY food
ORDER BY num ASC
LIMIT 1;


-- @block / Alternate solution
select food, count(animals.name) as num
from diet join animals 
on diet.species = animals.species
group by food
having num = 1;




-- @block // Summing up the total amount of animals in base
SELECT species, sum(*) AS num FROM animals
GROUP BY species
ORDER BY num DESC;


-- @block // Counting up the amount of animals of each species
SELECT species, count(*) AS num FROM animals
GROUP BY species
ORDER BY num DESC;