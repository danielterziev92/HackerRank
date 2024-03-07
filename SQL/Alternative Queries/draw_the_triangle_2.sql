WITH RECURSIVE Pattern AS (
    SELECT CAST('* ' AS CHAR(255)) AS Line, 1 AS Level
    UNION ALL
    SELECT CONCAT(Line, '* ') AS Line, Level + 1
    FROM Pattern
    WHERE Level < 20
)
SELECT Line
FROM Pattern;
