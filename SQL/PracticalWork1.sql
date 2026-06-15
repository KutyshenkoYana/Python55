-- CREATE TABLE StudentGrades (
--     id SERIAL PRIMARY KEY,
--     full_name VARCHAR(100) NOT NULL,
--     city VARCHAR(50),
--     country VARCHAR(50),
--     birth_date DATE,
--     email VARCHAR(100),
--     phone VARCHAR(20),
--     group_name VARCHAR(50),
--     average_grade DECIMAL(4,2),
--     min_subject VARCHAR(50),
--     max_subject VARCHAR(50)
-- );

-- INSERT INTO StudentGrades
-- (full_name, city, country, birth_date, email, phone, group_name, average_grade, min_subject, max_subject)
-- VALUES
-- ('Іван Петренко', 'Київ', 'Україна', '2003-05-12', 'ivan@gmail.com', '+380671111111', 'КН-21', 88.5, 'Фізика', 'Математика'),

-- ('Марія Коваль', 'Львів', 'Україна', '2002-09-18', 'maria@gmail.com', '+380672222222', 'КН-22', 91.2, 'Історія', 'Інформатика'),

-- ('Олександр Шевченко', 'Одеса', 'Україна', '2003-01-25', 'alex@gmail.com', '+380673333333', 'КН-21', 76.8, 'Хімія', 'Фізкультура');

-- SELECT * FROM StudentGrades;

-- SELECT full_name
-- FROM StudentGrades;

-- SELECT average_grade
-- FROM StudentGrades;

-- SELECT full_name
-- FROM StudentGrades
-- WHERE average_grade > 80;

-- SELECT DISTINCT country
-- FROM StudentGrades;

-- SELECT DISTINCT city
-- FROM StudentGrades;

-- SELECT DISTINCT group_name
-- FROM StudentGrades;

-- SELECT DISTINCT min_subject
-- FROM StudentGrades;