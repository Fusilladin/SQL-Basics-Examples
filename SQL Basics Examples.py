BASIC:

create = INSERT
read = SELECT
update = UPDATE
delete = DELETE

SELECT review "Reviews" FROM reviews;

SELECT title, author FROM books WHERE first_published = 1997;

SELECT * FROM books WHERE auther = "Yo Mama" OR/AND author = "Deez Nuts";

SELECT * FROM books WHERE auther IN/NOT IN ("J.K. Rowling", "Semore Butts", 'Jake Tran');

SELECT title, author FROM books WHERE first_published BETWEEN 1800 AND 1899;

SELECT title FROM books WHERE title ILIKE/LIKE "Harry Potter%";
"Alien%"
"%drew"
"%Brief History%"

SELECT * FROM loans WHERE returned_by > "2015-12-18" AND IS/IS NOT NULL; --Null means nothing is there

SELECT * FROM loans, books
WHERE loans.books_id = books.id;

----
INSERT NEW:

INSERT INTO books VALUES (16/NULL, "1984", "George Orwell", "Fiction", 1949,);

INSERT INTO loans (id, book_id, patron_id, loaned_on, return_by, reutrned_on)
VALUES (NULL, 2, 4, "2015-12-14", "2015-12-21", NULL),
	(NULL, 3, 6, "2016-12-24", "2016-12-30", NULL),
	(NULL, 4, 8, "2017-06-03", "2017-10-19", NULL),

-----
UPDATE EXISTING VALUES:

UPDATE patrons SET email="anon@email.com", last_name="Anonymous";

UPDATE loans SET returned_on = "2015-12-18" WHERE patron_id = 1
AND returned_on IS NULL
AND book_id IN (4, 8);

-----
DELETE

DELETE FROM patrons;

DELETE FROM books WHERE title LIKE "harry potter%";

DELETE FROM loans WHERE patron_id = 4;

-----
AUTO-COMMIT:

BEGIN TRANSACTION;

INSERT INTO genres rpg VALUES "Non-Fiction";
SELECT * FROM genres;
ROLLBACK;
SELECT 8 FROM genres;

COMMIT;

-------
ORDERING THINGS:

DESC = Descending
ASC = Ascending
LIMIT # = how many will be shown in ordered list
OFFSET # = skip this many rows in ordered list
ORDER BY = how to order a list


SELECT * FROM products ORDER BY stock_count DESC/ASC, last_name ASC;
SELECT * FROM products ORDER BY title LIMIT <skipped rows>, <# of rows>;
SELECT TOP 50 name FROM people;

-------
SQL FUNCTIONS:

|| = concatinate
" " = adding space between concatination
AS =  new field type name "x"
LENGTH() = length of item
UPPER() = upper case
LOWER() = lower case
<> = Angle brackets
SUBSTR = shorten word block SUBSTR(spot #start, #length)
... = elipse
REPLACE = replace the name of something


SELECT first_name || " " || last_name AS "Full Name" FROM customers;
SELECT maximum_weight || 'lbs' AS "Max Weight" FROM ELEVATOR_DATA;

SELECT username, LENGTH(username) AS length FROM customers ORDER BY length DESC LIMIT 1;
SELECT username AS length FROM customers WHERE length(username) < 7;

SELECT * FROM customers WHERE LOWER(email) = "andrewyang@email.com";
SELECT UPPER(zip) FROM addresses WHERE country = "UK";

SELECT name, SUBSTR(description, 1, 30) || "..." AS short_description, price FROM produccts;

SELECT street, city REPLACE(state, "California", "CA"), zip, FROM addressess
	WHERE REPLACE(state, "California", "CA") = "CA";

---------
GROUPING AND ADDING:

COUNT() = show number of items
GROUP BY = shows an entire group
SUM() = add together
 = same as WHERE after GROUP BY


SELECT COUNT(*) FROM customers ORDER BY id DESC LIMIT 1;
SELECT COUNT(*) FROM customers WHERE first_name = "Andrew";

SELECT category, COUNT(*) AS product_count FROM products GROUP BY category;

>>Find the total spend & best customer<<
SELECT SUM(cost) AS total_spend FROM orders
GROUP BY user_id
ORDER BY total_spend DESC
LIMIT 1;
SELECT * FROM customers WHERE id = 20;

>>Find everyone who spent over 250<<
SELECT SUM(cost) AS total_spend, user_id FROM orders
GROUP BY user_id
HAVING total_spend > 250
ORDER BY total_spend DESC;


------
AVERAGES, MAXIMUMS, AND MINIMUMS:

AVG() = find the avg for a specific type
MAX() = Maximum
MIN() = Minimum

SELECT AVG(cost) AS average, user_id FROM orders
GROUP BY user_id;

SELECT AVG(cost) AS average, MAX(cost) AS Maximum, MIN(cost) AS Minimum, user_id
FROM orders GROUP BY user_id;


-----
NUMERIC FUNCTION OPERATORS
+ = Addition
- = Subtraction
* = Multiplication
/ = Division
ROUND = Round number of decimal places

SELECT 1 + 4;

SELECT 5 - 3;

SELECT 2 * 5;

SELECT 5 / 2;
SELECT 5 / 2.0;

SELECT name, ROUND(price * 1.06, 2) AS "Price in Florida"
FROM products;


-----
DATES:

DISTINCT = used to return only distinct (different) values. no duplicates
DATE/TIME/DATETIME() = Date/time of item
CURRENT_DATE/TIME/TIMESTAMP = PostgreSQL Date/Time of item
STRFTIME() = string format time


SELECT * FROM orders WHERE status = "placed"
AND ordered_on = DATE("now");

SELECT COUNT(status) AS shipped_today FROM orders
WHERE status = "shipped"
AND ordered_on = DATE("now");

DATE("2016-02-01", "+7 days")
DATE("2016-02-01", "+2 months")
DATE("2016-02-01", "-12 years")

>>show past 7 days of sales<<
SELECT COUNT(*) FROM orders WHERE ordered_on
BETWEEN DATE("now", "-7 days") AND DATE("now", "-1 day");

>>show sales from 2 wks ago<<
SELECT COUNT(*) FROM orders WHERE ordered_on
BETWEEN DATE("now", "-7 days", "-7 days")
AND DATE("now", "-1 day", "-7 days");

>>UK Date format<<
SELECT *, STRFTIME("%d%m%Y", ordered_on) AS UK_date FROM orders;

SELECT title, STRFTIME("%m/%Y", date_released) AS month_year_released
FROM movies;


--------
JOINING TABLES:

INNER JOIN = Joins 2 tables into another
ON = chooses the column to join on
LEFT OUTER JOIN = Show all from first table & in both only


SELECT * FROM make INNER JOIN model ON make.MakeID = model.MakeID;

SELECT MakeName, ModelName FROM make
INNER JOIN model ON make.MakeID = model.MakeID;

SELECT mk.MakeName, md.ModelName FROM make AS mk
INNER JOIN model AS md ON mk.MakeID = md.MakeID;

SELECT mk.MakeName, md.ModelName FROM make AS mk
INNER JOIN model AS md ON mk.MakeID = md.MakeID
WHERE mk.MakeName = "Chevy";

SELECT mk.MakeName, md.ModelName FROM Make AS mk
LEFT OUTER JOIN model AS md ON mk.MakeID = md.MakeID;

SELECT mk.MakeName, COUNT(md.ModelName) AS NumberOfModels FROM Make AS mk
LEFT OUTER JOIN model AS md ON mk.MakeID = md.MakeID
GROUP BY mk.MakeName;

select
p.first_name,
p.email,
l.book_id,
l.loaned_on,
l.returned_on
from patrons as p
inner join loans as l on l.patron_id = p.id
where l.returned_on is null;

select DISTINCT
b.title,
p.first_name,
p.email,
P.last_name,
l.loaned_on,
l.return_by,
l.returned_on
from books as b
inner join loans as l on l.book_id = b.id
inner join patrons as p on l.patron_id = p.id;


------
SET OPERATIONS: COMBINE 2+ DATA SETS INTO ONE

UNION = combine data into one result section, no duplicates
UNION ALL = combine all data into one result section, includes duplicates
INTERSECT = creates a result set from values common in both tables
EXCEPT = creates a result set that are in first table but not second


SELECT makeid, Makename FROM Make
UNION SELECT foreignmakeid, makename FROM ForeignMake;

SELECT makeid, Makename FROM Make
WHERE makename < "D"
UNION
SELECT foreignmakeid, makename FROM ForeignMake
WHERE makename < "D"
ORDER BY makename;

SELECT MakeName FROM Make
UNION ALL SELECT MakeName FROM ForeignMake
ORDER BY makename;

SELECT MakeName FROM Make
INTERSECT
SELECT MakeName FROM ForeignMake
ORDER BY makename DESC;


------

IN () = used in WHERE clause to filter. Can only select 1 column in sub-query
NOt IN () = "" but not


SELECT * FROM Sale WHERE CarID IN (1, 3, 5);

SELECT * FROM Sale WHERE CarID
NOT/IN (SELECT CarID FROM Car WHERE ModelYear = 2015);

SELECT * FROM Sale AS s
INNER JOIN
(SELECT CarID, ModelYear FROM Car WHERE ModelYear = 2015) AS t
ON s.CarID = t.CarID;

SELECT sr.LastName, l.LocationName, SUM(s.SaleAmount) AS SaleAmount
  FROM Sale AS s
  INNER JOIN SalesRep AS sr ON s.SalesRepID = sr.SalesRepID
  INNER JOIN Location AS l ON s.LocationID = l.LocationID
  GROUP BY sr.LastName, l.LocationName;

SELECT sr.LastName FROM SalesRep AS sr;

SELECT SalesRepID, SUM(SaleAmount) AS StLuoisAmount
FROM Sales AS s WHERE s.LocationID = 1
GROUP BY SalesRepID;

SELECT sr.LastName, Loc1.StLouisAmount, Loc2.ColumbiaAmount
FROM SalesRep
AS sr
LEFT OUTER JOIN (SELECT SalesRepID, SUM(SaleAmount)
AS StLouisAmount
FROM Sale AS s
WHERE s.LocationID = 1
GROUP BY SalesRepID)
AS Loc1
ON sr.SalesRepID = loc1.SalesRepID
LEFT OUTER JOIN (SELECT SalesRepID, SUM(SaleAmount)
AS ColumbiaAmount
FROM Sale
AS s
WHERE s.LocationID = 2
GROUP BY SalesRepID)
AS Loc2
ON sr.SalesRepID = loc2.SalesRepID;

-

SELECT title, COUNT(title) AS Copies FROM
(SELECT title FROM books_south UNION ALL SELECT title FROM books_north)
AS allb GROUP BY title;

SELECT first_name, email, COUNT(email) AS "Loan Count"
FROM patrons AS P
INNER JOIN (SELECT patron_id, returned_on FROM loans_south
            UNION ALL
            SELECT patron_id, returned_on FROM loans_north) AS allLoans
      ON P.id = allLoans.patron_id
WHERE returned_on IS NULL
GROUP BY first_name, email;

-

SELECT customerid, freight, (SELECT AVG(freight) FROM orders)
FROM orders


-------
CTE: COMMON TABLE EXPRESSIONS

WITH = CREATES THE CTE


WITH product_details AS (
  SELECT productname, categoryname, unitprice, unitsinstock
  FROM products
  JOIN categories ON products.categoryID = categories.ID
  WHERE products.Discontinued = 0
)
SELECT * FROM product_details
ORDER BY categoryname, productname

WITH product_details AS (
  SELECT productname, categoryname, unitprice, unitsinstock
  FROM products
  JOIN categories ON products.categoryID = categories.ID
  WHERE products.Discontinued = 0
)
SELECT CATEGORNAME, count(*) as unique_product_count, SUM(unitsinstock) AS stock_count
FROM product_details
GROUP BY categoryname
ORDER BY unique_product_count
