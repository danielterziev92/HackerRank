WITH RECURSIVE Pattern AS (
    SELECT RPAD('* ', 20 * 2 - 1, '* ') AS Line, 1 AS Level
    UNION ALL
    SELECT TRIM(SUBSTR(Line, 1, LENGTH(Line) - 2)) AS Line, Level + 1
    FROM Pattern
    WHERE Level < 20
)
SELECT Line
FROM Pattern;
