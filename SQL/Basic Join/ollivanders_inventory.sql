SELECT wands.id, wands_property.age, wands.coins_needed, wands.power
FROM Wands
INNER JOIN Wands_Property ON wands.code = wands_property.code
WHERE (wands.power, wands.code, wands.coins_needed) IN (
    SELECT power, code, MIN(coins_needed)
    FROM Wands
    GROUP BY power, code
)
AND wands_property.is_evil = 0
ORDER BY wands.power DESC, wands_property.age DESC;