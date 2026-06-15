-- CREATE TABLE FruitsVegetables (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50) NOT NULL,
--     type VARCHAR(10) NOT NULL,
--     color VARCHAR(30),
--     calories INT,
--     description TEXT
-- );


-- INSERT INTO FruitsVegetables
-- (name, type, color, calories, description)
-- VALUES
-- ('Яблуко', 'Фрукт', 'Червоний', 52, 'Солодкий фрукт'),

-- ('Банан', 'Фрукт', 'Жовтий', 89, 'Тропічний фрукт'),

-- ('Апельсин', 'Фрукт', 'Помаранчевий', 47, 'Цитрусовий фрукт'),

-- ('Огірок', 'Овоч', 'Зелений', 15, 'Свіжий овоч'),

-- ('Помідор', 'Овоч', 'Червоний', 18, 'Соковитий овоч'),

-- ('Морква', 'Овоч', 'Помаранчевий', 41, 'Коренеплід');


-- SELECT * FROM FruitsVegetables;


-- SELECT *
-- FROM FruitsVegetables
-- WHERE type = 'Овоч';


-- SELECT *
-- FROM FruitsVegetables
-- WHERE type = 'Фрукт';


-- SELECT name
-- FROM FruitsVegetables;


-- SELECT DISTINCT color
-- FROM FruitsVegetables;


-- SELECT *
-- FROM FruitsVegetables
-- WHERE type = 'Фрукт'
-- AND color = 'Червоний';


-- SELECT *
-- FROM FruitsVegetables
-- WHERE type = 'Овоч'
-- AND color = 'Зелений';