-- CREATE TABLE Faculties (
--     Id SERIAL PRIMARY KEY,
--     Financing DECIMAL(10,2) NOT NULL DEFAULT 0 CHECK (Financing >= 0),
--     Name VARCHAR(100) NOT NULL UNIQUE
-- );

-- CREATE TABLE Departments (
--     Id SERIAL PRIMARY KEY,
--     Financing DECIMAL(10,2) NOT NULL DEFAULT 0 CHECK (Financing >= 0),
--     Name VARCHAR(100) NOT NULL UNIQUE,
--     FacultyId INT NOT NULL REFERENCES Faculties(Id)
-- );

-- CREATE TABLE Groups (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(10) NOT NULL UNIQUE,
--     Year INT NOT NULL CHECK (Year BETWEEN 1 AND 5),
--     DepartmentId INT NOT NULL REFERENCES Departments(Id)
-- );

-- CREATE TABLE Curators (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(255) NOT NULL,
--     Surname VARCHAR(255) NOT NULL
-- );

-- CREATE TABLE GroupsCurators (
--     Id SERIAL PRIMARY KEY,
--     CuratorId INT NOT NULL REFERENCES Curators(Id),
--     GroupId INT NOT NULL REFERENCES Groups(Id)
-- );

-- CREATE TABLE Teachers (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(255) NOT NULL,
--     Surname VARCHAR(255) NOT NULL,
--     Salary DECIMAL(10,2) NOT NULL CHECK (Salary > 0)
-- );

-- CREATE TABLE Subjects (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(100) NOT NULL UNIQUE
-- );

-- CREATE TABLE Lectures (
--     Id SERIAL PRIMARY KEY,
--     LectureRoom VARCHAR(255) NOT NULL,
--     SubjectId INT NOT NULL REFERENCES Subjects(Id),
--     TeacherId INT NOT NULL REFERENCES Teachers(Id)
-- );

-- CREATE TABLE GroupsLectures (
--     Id SERIAL PRIMARY KEY,
--     GroupId INT NOT NULL REFERENCES Groups(Id),
--     LectureId INT NOT NULL REFERENCES Lectures(Id)
-- );


-- INSERT INTO Faculties (Financing, Name) VALUES
-- (100000, 'Computer Science'),
-- (120000, 'Mathematics'),
-- (90000, 'Physics'),
-- (110000, 'Economics'),
-- (95000, 'Engineering');

-- INSERT INTO Departments (Financing, Name, FacultyId) VALUES
-- (50000, 'Software Engineering', 1),
-- (40000, 'Applied Mathematics', 2),
-- (30000, 'Quantum Physics', 3),
-- (45000, 'Business Analysis', 4),
-- (35000, 'Mechanical Engineering', 5);

-- INSERT INTO Groups (Name, Year, DepartmentId) VALUES
-- ('P107', 2, 1),
-- ('P207', 3, 1),
-- ('M101', 1, 2),
-- ('F303', 4, 3),
-- ('E404', 5, 5);

-- INSERT INTO Curators (Name, Surname) VALUES
-- ('Anna', 'Kovalenko'),
-- ('Ivan', 'Petrov'),
-- ('Olga', 'Shevchenko'),
-- ('Dmytro', 'Bondar'),
-- ('Svitlana', 'Tkachenko');

-- INSERT INTO GroupsCurators (CuratorId, GroupId) VALUES
-- (1,1),
-- (2,2),
-- (3,3),
-- (4,4),
-- (5,5);

-- INSERT INTO Teachers (Name, Surname, Salary) VALUES
-- ('Samantha', 'Adams', 3000),
-- ('John', 'Smith', 3200),
-- ('Emily', 'Clark', 2800),
-- ('Robert', 'Brown', 3500),
-- ('Laura', 'Wilson', 3100);

-- INSERT INTO Subjects (Name) VALUES
-- ('Database Theory'),
-- ('Algorithms'),
-- ('Physics'),
-- ('Economics'),
-- ('Mathematics');

-- INSERT INTO Lectures (LectureRoom, SubjectId, TeacherId) VALUES
-- ('B103', 1, 1),
-- ('B104', 2, 2),
-- ('B105', 3, 3),
-- ('B106', 4, 4),
-- ('B107', 5, 5);

-- INSERT INTO GroupsLectures (GroupId, LectureId) VALUES
-- (1,1),
-- (1,2),
-- (2,3),
-- (3,4),
-- (4,5);

-- SELECT t.Name, t.Surname, g.Name
-- FROM Teachers t
-- CROSS JOIN Groups g;

-- SELECT f.Name
-- FROM Faculties f
-- JOIN Departments d ON d.FacultyId = f.Id
-- GROUP BY f.Id
-- HAVING SUM(d.Financing) > f.Financing;


-- SELECT c.Surname, g.Name
-- FROM Curators c
-- JOIN GroupsCurators gc ON gc.CuratorId = c.Id
-- JOIN Groups g ON g.Id = gc.GroupId;

-- SELECT DISTINCT t.Name, t.Surname
-- FROM Teachers t
-- JOIN Lectures l ON l.TeacherId = t.Id
-- JOIN GroupsLectures gl ON gl.LectureId = l.Id
-- JOIN Groups g ON g.Id = gl.GroupId
-- WHERE g.Name = 'P107';

-- SELECT DISTINCT t.Surname, f.Name
-- FROM Teachers t
-- JOIN Lectures l ON l.TeacherId = t.Id
-- JOIN Subjects s ON s.Id = l.SubjectId
-- JOIN GroupsLectures gl ON gl.LectureId = l.Id
-- JOIN Groups g ON g.Id = gl.GroupId
-- JOIN Departments d ON d.Id = g.DepartmentId
-- JOIN Faculties f ON f.Id = d.FacultyId;

-- SELECT d.Name, g.Name
-- FROM Departments d
-- JOIN Groups g ON g.DepartmentId = d.Id;

-- SELECT s.Name
-- FROM Subjects s
-- JOIN Lectures l ON l.SubjectId = s.Id
-- JOIN Teachers t ON t.Id = l.TeacherId
-- WHERE t.Name = 'Samantha' AND t.Surname = 'Adams';

-- SELECT DISTINCT d.Name
-- FROM Departments d
-- JOIN Lectures l ON l.TeacherId IS NOT NULL
-- JOIN Subjects s ON s.Id = l.SubjectId
-- WHERE s.Name = 'Database Theory';

-- SELECT g.Name
-- FROM Groups g
-- JOIN Departments d ON d.Id = g.DepartmentId
-- JOIN Faculties f ON f.Id = d.FacultyId
-- WHERE f.Name = 'Computer Science';


-- SELECT g.Name, f.Name
-- FROM Groups g
-- JOIN Departments d ON d.Id = g.DepartmentId
-- JOIN Faculties f ON f.Id = d.FacultyId
-- WHERE g.Year = 5;

-- SELECT DISTINCT t.Name, t.Surname, s.Name AS Subject, g.Name AS GroupName
-- FROM Teachers t
-- JOIN Lectures l ON l.TeacherId = t.Id
-- JOIN Subjects s ON s.Id = l.SubjectId
-- JOIN GroupsLectures gl ON gl.LectureId = l.Id
-- JOIN Groups g ON g.Id = gl.GroupId
-- WHERE l.LectureRoom = 'B103';

