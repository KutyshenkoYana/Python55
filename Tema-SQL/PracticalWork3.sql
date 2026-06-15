-- CREATE TABLE Departments (
--     Id SERIAL PRIMARY KEY,
--     Building INT NOT NULL CHECK (Building BETWEEN 1 AND 5),
--     Financing NUMERIC NOT NULL DEFAULT 0 CHECK (Financing >= 0),
--     Name VARCHAR(100) NOT NULL UNIQUE
-- );


-- CREATE TABLE Diseases (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(100) NOT NULL UNIQUE,
--     Severity INT NOT NULL DEFAULT 1 CHECK (Severity >= 1)
-- );


-- CREATE TABLE Doctors (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(255) NOT NULL,
--     Phone CHAR(10),
--     Salary NUMERIC NOT NULL CHECK (Salary > 0),
--     Surname VARCHAR(255) NOT NULL
-- );


-- CREATE TABLE Examinations (
--     Id SERIAL PRIMARY KEY,
--     DayOfWeek INT NOT NULL CHECK (DayOfWeek BETWEEN 1 AND 7),
--     EndTime TIME NOT NULL,
--     Name VARCHAR(100) NOT NULL UNIQUE,
--     StartTime TIME NOT NULL CHECK (StartTime BETWEEN '08:00' AND '18:00')
-- );


-- CREATE TABLE Wards (
--     Id SERIAL PRIMARY KEY,
--     Building INT NOT NULL CHECK (Building BETWEEN 1 AND 5),
--     Floor INT NOT NULL CHECK (Floor >= 1),
--     Name VARCHAR(20) NOT NULL UNIQUE
-- );


-- INSERT INTO Departments (Building, Financing, Name) VALUES
-- (1, 25000, 'Surgery'),
-- (2, 15000, 'Therapy'),
-- (3, 9000, 'Cardiology'),
-- (4, 5000, 'Neurology'),
-- (5, 32000, 'Oncology');


-- INSERT INTO Diseases (Name, Severity) VALUES
-- ('Flu', 2),
-- ('Cancer', 5),
-- ('Diabetes', 3),
-- ('Cold', 1),
-- ('Tuberculosis', 4);


-- INSERT INTO Doctors (Name, Phone, Salary, Surname) VALUES
-- ('Ivan', '1234567890', 1200, 'Novak'),
-- ('Anna', '0987654321', 1400, 'Petrenko'),
-- ('Oleh', '1112223334', 1600, 'Shevchenko'),
-- ('Maria', '2223334445', 1100, 'Koval'),
-- ('Nazar', '3334445556', 1800, 'Nikitin');


-- INSERT INTO Examinations (DayOfWeek, EndTime, Name, StartTime) VALUES
-- (1, '10:00', 'Blood Test', '08:00'),
-- (2, '12:00', 'X-Ray', '09:00'),
-- (3, '14:00', 'MRI', '11:00'),
-- (4, '16:00', 'Ultrasound', '13:00'),
-- (5, '18:00', 'CT Scan', '15:00');


-- INSERT INTO Wards (Building, Floor, Name) VALUES
-- (1, 1, 'Ward A'),
-- (2, 2, 'Ward B'),
-- (3, 1, 'Ward C'),
-- (4, 3, 'Ward D'),
-- (5, 1, 'Ward E');


-- SELECT * FROM Wards;


-- SELECT Surname, Phone FROM Doctors;


-- SELECT DISTINCT Floor FROM Wards;


-- SELECT Name AS "Name of Disease",
--        Severity AS "Severity of Disease"
-- FROM Diseases;


-- SELECT Name
-- FROM Departments
-- WHERE Building = 5 AND Financing < 30000;


-- SELECT Name
-- FROM Departments
-- WHERE Building = 3 AND Financing BETWEEN 12000 AND 15000;


-- SELECT Name
-- FROM Wards
-- WHERE Building IN (4,5) AND Floor = 1;


-- SELECT Name, Building, Financing
-- FROM Departments
-- WHERE (Building IN (3,6))
-- AND (Financing < 11000 OR Financing > 25000);


-- SELECT Surname
-- FROM Doctors
-- WHERE Salary + 120 > 1500;


-- SELECT Surname
-- FROM Doctors
-- WHERE (Salary / 2) > 1500;


-- SELECT DISTINCT Name
-- FROM Examinations
-- WHERE DayOfWeek BETWEEN 1 AND 3
-- AND StartTime BETWEEN '12:00' AND '15:00';


-- SELECT Name, Building
-- FROM Departments
-- WHERE Building IN (1,3,8,10);


-- SELECT Name
-- FROM Diseases
-- WHERE Severity NOT IN (1,2);


-- SELECT Name
-- FROM Departments
-- WHERE Building NOT IN (1,3);


-- SELECT Name
-- FROM Departments
-- WHERE Building IN (1,3);


-- SELECT Surname
-- FROM Doctors
-- WHERE Surname LIKE 'N%';


