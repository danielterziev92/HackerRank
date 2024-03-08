WITH RN AS (SELECT X, Y, (POWER(X, 2) + POWER(Y, 2)) N
            FROM Functions
            ORDER BY N)
SELECT L.A, L.B
FROM (SELECT MIN(RN.X) A, MAX(RN.Y) B, COUNT(RN.N) C
      FROM RN
      GROUP BY RN.N) L
WHERE C > 1
ORDER BY L.A ASC, L.B ASC;