SELECT c.algorithm                                                                                    AS algorithm_name,
       ROUND(SUM(CASE WHEN t.dt >= '2020-01-01' AND t.dt < '2020-04-01' THEN t.volume ELSE 0 END), 6) AS Q1,
       ROUND(SUM(CASE WHEN t.dt >= '2020-04-01' AND t.dt < '2020-07-01' THEN t.volume ELSE 0 END), 6) AS Q2,
       ROUND(SUM(CASE WHEN t.dt >= '2020-07-01' AND t.dt < '2020-10-01' THEN t.volume ELSE 0 END), 6) AS Q3,
       ROUND(SUM(CASE WHEN t.dt >= '2020-10-01' AND t.dt < '2021-01-01' THEN t.volume ELSE 0 END), 6) AS Q4
FROM coins c
         LEFT JOIN
     transactions t ON c.code = t.coin_code
WHERE t.dt >= '2020-01-01'
  AND t.dt < '2021-01-01'
GROUP BY c.algorithm
ORDER BY algorithm_name;
