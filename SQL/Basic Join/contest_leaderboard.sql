SELECT A.hacker_id, B.name, SUM(max_score) total_max_score
FROM (SELECT hacker_id, challenge_id, MAX(score) as max_score FROM Submissions GROUP BY hacker_id, challenge_id) AS A
         JOIN Hackers B on A.hacker_id = B.hacker_id
GROUP BY A.hacker_id, B.name
HAVING total_max_score > 0
ORDER BY total_max_score DESC, A.hacker_id ASC;