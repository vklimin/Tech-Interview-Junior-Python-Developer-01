## Создание таблицы
```sql
CREATE TABLE texts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    txt VARCHAR(255),
    num INT
)
```
```sql
CREATE TABLE dates (
    id INT PRIMARY KEY AUTO_INCREMENT,
    dt DATE
)
```

## Вставка одной строки
```sql
INSERT INTO texts (id, txt, num)
VALUES (1, 'пример', 123)
```
```sql
INSERT INTO dates (id, dt)
VALUES (1, '2025-09-02')
```

## Вставка нескольких строк
```sql
INSERT INTO texts (id, txt, num)
VALUES (2, 'пример', 222), (3, 'строка 3', 456), (4, 'строка 4', 789)
```
```sql
INSERT INTO dates (id, dt)
VALUES (2, '2025-09-03'), (4, '2025-09-04')
```

## Выборка с условием и сортировкой
```sql
SELECT * 
FROM texts 
WHERE id > 1 AND num > 400
ORDER BY id DESC, num
```

## Обновление одного поля одной конкретной записи
```sql
UPDATE texts
SET num = 555
WHERE id = 2
```

## Обновление нескольких полей нескольких записей по условию
```sql
UPDATE texts
SET num = 999, txt = 'обновлено'
WHERE txt LIKE '%ример'
```

## Математические операции
```sql
SELECT 1 + 2, 10 / 5
```

## Агрегация числовых данных
```sql
SELECT SUM(num), AVG(num), MAX(num) 
FROM `texts`
```

## Группировка данных
```sql
SELECT txt, COUNT(*) AS 'шт.'
FROM texts
GROUP BY txt
```

## Вложенные запросы
```sql
SELECT *
FROM texts
WHERE id IN (
    SELECT id 
    FROM dates
)
```

## Объединение таблиц
```sql
SELECT a.id, a.txt, b.dt AS date
FROM texts AS a
LEFT JOIN dates AS b 
    ON a.id = b.id
```

Типичные объединения:
* LEFT JOIN, RIGHT JOIN, INNER JOIN (обычный JOIN)
* CROSS JOIN (все на все, используется без ON)
* FULL OUTER JOIN (реализовано не во всех движках SQL)

## Удаление строки
```sql
DELETE FROM dates
WHERE id = 2
```

## Очистка содержимого таблицы
```sql
TRUNCATE TABLE texts
```

## Удаление таблицы
```sql
DROP TABLE dates
```
