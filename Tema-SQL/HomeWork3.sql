-- CREATE TABLE Departments (
--     Id SERIAL PRIMARY KEY,
--     Financing NUMERIC(12,2) NOT NULL DEFAULT 0 CHECK (Financing >= 0),
--     Name VARCHAR(100) NOT NULL UNIQUE
-- );

-- CREATE TABLE Faculties (
--     Id SERIAL PRIMARY KEY,
--     Dean VARCHAR(255) NOT NULL,
--     Name VARCHAR(100) NOT NULL UNIQUE
-- );

-- CREATE TABLE Groups (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(10) NOT NULL UNIQUE,
--     Rating INT NOT NULL CHECK (Rating BETWEEN 0 AND 5),
--     Year INT NOT NULL CHECK (Year BETWEEN 1 AND 5)
-- );

-- CREATE TABLE Teachers (
--     Id SERIAL PRIMARY KEY,
--     EmploymentDate DATE NOT NULL CHECK (EmploymentDate >= '1990-01-01'),
--     IsAssistant BOOLEAN NOT NULL DEFAULT FALSE,
--     IsProfessor BOOLEAN NOT NULL DEFAULT FALSE,
--     Name VARCHAR(255) NOT NULL,
--     Position VARCHAR(255) NOT NULL,
--     Premium NUMERIC(10,2) NOT NULL DEFAULT 0 CHECK (Premium >= 0),
--     Salary NUMERIC(10,2) NOT NULL CHECK (Salary > 0),
--     Surname VARCHAR(255) NOT NULL
-- );



-- INSERT INTO Departments (Financing, Name) VALUES
-- (10000, 'Software Development'),
-- (30000, 'Computer Science'),
-- (15000, 'Cyber Security'),
-- (5000, 'Mathematics'),
-- (27000, 'Physics');

-- INSERT INTO Faculties (Dean, Name) VALUES
-- ('Ivan Petrenko', 'Computer Science'),
-- ('Olena Shevchenko', 'Engineering'),
-- ('Mykola Koval', 'Mathematics'),
-- ('Anna Bondar', 'Physics'),
-- ('Taras Melnyk', 'Economics');

-- INSERT INTO Groups (Name, Rating, Year) VALUES
-- ('CS101', 5, 1),
-- ('CS201', 4, 2),
-- ('CS301', 3, 3),
-- ('CS401', 2, 4),
-- ('CS501', 4, 5);

-- INSERT INTO Teachers
-- (EmploymentDate, IsAssistant, IsProfessor, Name, Position, Premium, Salary, Surname)
-- VALUES
-- ('1995-03-10', TRUE, FALSE, 'Ivan', 'Assistant', 200, 500, 'Petrenko'),
-- ('1998-05-20', FALSE, TRUE, 'Olena', 'Professor', 400, 1200, 'Shevchenko'),
-- ('2005-09-01', TRUE, FALSE, 'Andrii', 'Assistant', 180, 700, 'Koval'),
-- ('1992-01-15', FALSE, TRUE, 'Nazar', 'Professor', 300, 1300, 'Novak'),
-- ('1999-11-30', TRUE, FALSE, 'Maria', 'Assistant', 600, 900, 'Bondar');



-- SELECT Name, Financing, Id
-- FROM Departments;


-- SELECT
--     Name AS "Group Name",
--     Rating AS "Group Rating"
-- FROM Groups;


-- SELECT
--     Surname,
--     ROUND((Salary * 100.0 / Premium), 2) AS SalaryToPremiumPercent,
--     ROUND((Salary * 100.0 / (Salary + Premium)), 2) AS SalaryToTotalPercent
-- FROM Teachers;


-- SELECT
-- 'The dean of faculty ' || Name || ' is ' || Dean || '.'
-- FROM Faculties;


-- SELECT Surname
-- FROM Teachers
-- WHERE IsProfessor = TRUE
-- AND Salary > 1050;


-- SELECT Name
-- FROM Departments
-- WHERE Financing < 11000
-- OR Financing > 25000;


-- SELECT Name
-- FROM Faculties
-- WHERE Name <> 'Computer Science';


-- SELECT Surname, Position
-- FROM Teachers
-- WHERE IsProfessor = FALSE;


-- SELECT Surname, Position, Salary, Premium
-- FROM Teachers
-- WHERE IsAssistant = TRUE
-- AND Premium BETWEEN 160 AND 550;


-- SELECT Surname, Salary
-- FROM Teachers
-- WHERE IsAssistant = TRUE;


-- SELECT Surname, Position
-- FROM Teachers
-- WHERE EmploymentDate < '2000-01-01';


-- SELECT Name AS "Name of Department"
-- FROM Departments
-- WHERE Name < 'Software Development';


-- SELECT Surname
-- FROM Teachers
-- WHERE IsAssistant = TRUE
-- AND (Salary + Premium) <= 1200;


-- SELECT Name
-- FROM Groups
-- WHERE Year = 5
-- AND Rating BETWEEN 2 AND 4;


-- SELECT Surname
-- FROM Teachers
-- WHERE IsAssistant = TRUE
-- AND (Salary < 550 OR Premium < 200);