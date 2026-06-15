-- SELECT full_name
-- FROM StudentGrades
-- WHERE average_grade BETWEEN 70 AND 90;


-- SELECT *
-- FROM StudentGrades
-- WHERE EXTRACT(YEAR FROM AGE(CURRENT_DATE, birth_date)) = 20;


-- SELECT *
-- FROM StudentGrades
-- WHERE EXTRACT(YEAR FROM AGE(CURRENT_DATE, birth_date)) BETWEEN 18 AND 22;


-- SELECT *
-- FROM StudentGrades
-- WHERE full_name LIKE 'Борис%';


-- SELECT *
-- FROM StudentGrades
-- WHERE phone LIKE '%777%';


-- SELECT email
-- FROM StudentGrades
-- WHERE email LIKE 'i%';


-- SELECT MIN(average_grade)
-- FROM StudentGrades;


-- SELECT MAX(average_grade)
-- FROM StudentGrades;


-- SELECT city, COUNT(*) AS students_count
-- FROM StudentGrades
-- GROUP BY city;


-- SELECT country, COUNT(*) AS students_count
-- FROM StudentGrades
-- GROUP BY country;


-- SELECT COUNT(*)
-- FROM StudentGrades
-- WHERE average_grade = (
--     SELECT MIN(average_grade)
--     FROM StudentGrades
-- );


-- SELECT COUNT(*)
-- FROM StudentGrades
-- WHERE average_grade = (
--     SELECT MAX(average_grade)
--     FROM StudentGrades
-- );


-- SELECT group_name, COUNT(*) AS students_count
-- FROM StudentGrades
-- GROUP BY group_name;


-- SELECT group_name, AVG(average_grade) AS average_group_grade
-- FROM StudentGrades
-- GROUP BY group_name;