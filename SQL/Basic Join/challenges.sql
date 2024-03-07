WITH common_table AS (
   SELECT H.hacker_id, H.name, COUNT(C.challenge_id) AS challenges
   FROM Hackers H
   INNER JOIN Challenges C
   ON H.hacker_id = C.hacker_id
   GROUP BY H.hacker_id, H.name)

SELECT hacker_id, name, challenges
FROM common_table
WHERE challenges IN (SELECT MAX(challenges) FROM common_table)
      OR
      challenges IN (SELECT challenges FROM common_table
                     GROUP BY challenges
                     HAVING COUNT(challenges)=1)
ORDER BY challenges DESC, hacker_id ASC;