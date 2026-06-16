-- CREATE TABLE Departments (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(100) NOT NULL UNIQUE
-- );

-- CREATE TABLE Doctors (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(255) NOT NULL,
--     Surname VARCHAR(255) NOT NULL,
--     Premium NUMERIC(10,2) NOT NULL DEFAULT 0 CHECK (Premium >= 0),
--     Salary NUMERIC(10,2) NOT NULL CHECK (Salary > 0)
-- );

-- CREATE TABLE Specializations (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(100) NOT NULL UNIQUE
-- );

-- CREATE TABLE DoctorsSpecializations (
--     Id SERIAL PRIMARY KEY,
--     DoctorId INT NOT NULL REFERENCES Doctors(Id),
--     SpecializationId INT NOT NULL REFERENCES Specializations(Id)
-- );

-- CREATE TABLE Sponsors (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(100) NOT NULL UNIQUE
-- );

-- CREATE TABLE Donations (
--     Id SERIAL PRIMARY KEY,
--     Amount NUMERIC(12,2) NOT NULL CHECK (Amount > 0),
--     Date DATE NOT NULL DEFAULT CURRENT_DATE,
--     DepartmentId INT NOT NULL REFERENCES Departments(Id),
--     SponsorId INT NOT NULL REFERENCES Sponsors(Id)
-- );

-- CREATE TABLE Vacations (
--     Id SERIAL PRIMARY KEY,
--     StartDate DATE NOT NULL,
--     EndDate DATE NOT NULL,
--     DoctorId INT NOT NULL REFERENCES Doctors(Id),
--     CHECK (EndDate > StartDate)
-- );

-- CREATE TABLE Wards (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(20) NOT NULL UNIQUE,
--     DepartmentId INT NOT NULL REFERENCES Departments(Id)
-- );

-- CREATE TABLE Examinations (
--     Id SERIAL PRIMARY KEY,
--     DoctorId INT NOT NULL REFERENCES Doctors(Id),
--     DepartmentId INT NOT NULL REFERENCES Departments(Id),
--     ExamDate DATE NOT NULL
-- );



-- INSERT INTO Departments (Name) VALUES
-- ('Intensive Treatment'),
-- ('Surgery'),
-- ('Cardiology'),
-- ('Neurology'),
-- ('Pediatrics');

-- INSERT INTO Doctors (Name, Surname, Premium, Salary) VALUES
-- ('Ivan', 'Petrov', 500, 3000),
-- ('Olena', 'Shevchenko', 700, 3200),
-- ('Andrii', 'Kovalenko', 0, 2800),
-- ('Maria', 'Bondar', 300, 3100),
-- ('Dmytro', 'Tkachenko', 1000, 4000);

-- INSERT INTO Specializations (Name) VALUES
-- ('Surgeon'),
-- ('Therapist'),
-- ('Cardiologist'),
-- ('Neurologist'),
-- ('Pediatrician');

-- INSERT INTO DoctorsSpecializations (DoctorId, SpecializationId) VALUES
-- (1,1),
-- (2,2),
-- (3,3),
-- (4,4),
-- (5,5);

-- INSERT INTO Sponsors (Name) VALUES
-- ('Umbrella Corporation'),
-- ('Wayne Enterprises'),
-- ('Stark Industries'),
-- ('Globex'),
-- ('Oscorp');

-- INSERT INTO Donations (Amount, Date, DepartmentId, SponsorId) VALUES
-- (150000, CURRENT_DATE - INTERVAL '10 days', 1, 1),
-- (50000, CURRENT_DATE - INTERVAL '20 days', 2, 2),
-- (200000, CURRENT_DATE - INTERVAL '5 days', 3, 1),
-- (80000, CURRENT_DATE - INTERVAL '40 days', 4, 3),
-- (120000, CURRENT_DATE - INTERVAL '15 days', 5, 1);

-- INSERT INTO Vacations (StartDate, EndDate, DoctorId) VALUES
-- (CURRENT_DATE - INTERVAL '30 days', CURRENT_DATE - INTERVAL '20 days', 1),
-- (CURRENT_DATE - INTERVAL '10 days', CURRENT_DATE + INTERVAL '10 days', 2),
-- (CURRENT_DATE - INTERVAL '60 days', CURRENT_DATE - INTERVAL '50 days', 3),
-- (CURRENT_DATE - INTERVAL '5 days', CURRENT_DATE + INTERVAL '5 days', 4),
-- (CURRENT_DATE - INTERVAL '100 days', CURRENT_DATE - INTERVAL '90 days', 5);

-- INSERT INTO Wards (Name, DepartmentId) VALUES
-- ('Ward A', 1),
-- ('Ward B', 1),
-- ('Ward C', 2),
-- ('Ward D', 3),
-- ('Ward E', 4);

-- INSERT INTO Examinations (DoctorId, DepartmentId, ExamDate) VALUES
-- (1,1,CURRENT_DATE - INTERVAL '3 days'),
-- (2,2,CURRENT_DATE - INTERVAL '4 days'),
-- (3,3,CURRENT_DATE - INTERVAL '6 days'),
-- (4,4,CURRENT_DATE - INTERVAL '2 days'),
-- (5,5,CURRENT_DATE - INTERVAL '1 day');



-- CREATE TABLE Diseases (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(100) NOT NULL UNIQUE
-- );


-- INSERT INTO Diseases (Name) VALUES
-- ('Flu'),
-- ('Diabetes'),
-- ('Cancer'),
-- ('Migraine'),
-- ('Asthma');


-- SELECT d.Name, d.Surname, s.Name AS Specialization
-- FROM Doctors d
-- JOIN DoctorsSpecializations ds ON d.Id = ds.DoctorId
-- JOIN Specializations s ON s.Id = ds.SpecializationId;

-- SELECT Surname, (Salary + Premium) AS TotalSalary
-- FROM Doctors
-- WHERE Id NOT IN (
--     SELECT DoctorId
--     FROM Vacations
--     WHERE CURRENT_DATE BETWEEN StartDate AND EndDate
-- );

-- SELECT w.Name
-- FROM Wards w
-- JOIN Departments d ON w.DepartmentId = d.Id
-- WHERE d.Name = 'Intensive Treatment';

-- SELECT DISTINCT d.Name
-- FROM Departments d
-- JOIN Donations dn ON dn.DepartmentId = d.Id
-- JOIN Sponsors s ON s.Id = dn.SponsorId
-- WHERE s.Name = 'Umbrella Corporation';

-- SELECT
--     d.Name AS Department,
--     s.Name AS Sponsor,
--     dn.Amount,
--     dn.Date
-- FROM Donations dn
-- JOIN Departments d ON d.Id = dn.DepartmentId
-- JOIN Sponsors s ON s.Id = dn.SponsorId
-- WHERE dn.Date >= CURRENT_DATE - INTERVAL '1 month';

-- SELECT DISTINCT d.Surname, dep.Name AS Department
-- FROM Examinations e
-- JOIN Doctors d ON d.Id = e.DoctorId
-- JOIN Departments dep ON dep.Id = e.DepartmentId
-- WHERE EXTRACT(DOW FROM e.ExamDate) BETWEEN 1 AND 5;

-- SELECT DISTINCT dep.Name AS Department, d.Surname AS Doctor
-- FROM Donations dn
-- JOIN Departments dep ON dep.Id = dn.DepartmentId
-- JOIN Examinations e ON e.DepartmentId = dep.Id
-- JOIN Doctors d ON d.Id = e.DoctorId
-- WHERE dn.Amount > 100000;

-- SELECT DISTINCT dep.Name
-- FROM Departments dep
-- JOIN Doctors d ON d.Id IS NOT NULL
-- WHERE d.Premium = 0;


-- ALTER TABLE Examinations
-- ADD COLUMN DiseaseId INT;

-- ALTER TABLE Examinations
-- ADD CONSTRAINT fk_disease
-- FOREIGN KEY (DiseaseId) REFERENCES Diseases(Id);

-- SELECT * FROM EXAMINATIONS;

-- INSERT INTO Examinations (DoctorId, DepartmentId, DiseaseId, ExamDate) VALUES
-- (1, 1, 1, CURRENT_DATE - INTERVAL '10 days'),
-- (2, 2, 2, CURRENT_DATE - INTERVAL '20 days'),
-- (3, 3, 3, CURRENT_DATE - INTERVAL '5 days'),
-- (4, 4, 4, CURRENT_DATE - INTERVAL '15 days'),
-- (5, 5, 5, CURRENT_DATE - INTERVAL '2 days');

-- SELECT DISTINCT dep.Name, dis.Name
-- FROM Departments dep
-- JOIN Examinations e ON e.DepartmentId = dep.Id
-- JOIN Diseases dis ON dis.Id = e.DiseaseId
-- WHERE e.ExamDate >= CURRENT_DATE - INTERVAL '6 months';