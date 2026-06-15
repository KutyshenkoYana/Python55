-- SELECT *
-- FROM FruitsVegetables
-- WHERE type = 'Овоч'
-- AND calories < 50;


-- SELECT *
-- FROM FruitsVegetables
-- WHERE type = 'Фрукт'
-- AND calories BETWEEN 40 AND 90;


-- SELECT *
-- FROM FruitsVegetables
-- WHERE type = 'Овоч'
-- AND name ILIKE '%капуста%';


-- SELECT *
-- FROM FruitsVegetables
-- WHERE description ILIKE '%гемоглобін%';


-- SELECT *
-- FROM FruitsVegetables
-- WHERE color IN ('Жовтий', 'Червоний');


-- SELECT COUNT(*)
-- FROM FruitsVegetables
-- WHERE type = 'Овоч';


-- SELECT COUNT(*)
-- FROM FruitsVegetables
-- WHERE type = 'Фрукт';


-- SELECT COUNT(*)
-- FROM FruitsVegetables
-- WHERE color = 'Червоний';


-- SELECT color, COUNT(*) AS count_items
-- FROM FruitsVegetables
-- GROUP BY color;


-- SELECT color
-- FROM FruitsVegetables
-- GROUP BY color
-- ORDER BY COUNT(*) ASC
-- LIMIT 1;


-- SELECT color
-- FROM FruitsVegetables
-- GROUP BY color
-- ORDER BY COUNT(*) DESC
-- LIMIT 1;


-- SELECT MIN(calories)
-- FROM FruitsVegetables;


-- SELECT MAX(calories)
-- FROM FruitsVegetables;


-- SELECT AVG(calories)
-- FROM FruitsVegetables;


-- SELECT *
-- FROM FruitsVegetables
-- WHERE type = 'Фрукт'
-- ORDER BY calories ASC
-- LIMIT 1;


-- SELECT *
-- FROM FruitsVegetables
-- WHERE type = 'Фрукт'
-- ORDER BY calories DESC
-- LIMIT 1;