SELECT c.contest_id,
       c.hacker_id,
       c.name,
       sum(ss.total_submissions),
       sum(ss.total_accepted_submissions),
       sum(vs.total_views),
       sum(vs.total_unique_views)
FROM contests c
         INNER JOIN colleges co on c.contest_id = co.contest_id
         INNER JOIN challenges ch on co.college_id = ch.college_id
         LEFT JOIN (SELECT challenge_id,
                           sum(total_submissions)          AS total_submissions,
                           sum(total_accepted_submissions) AS total_accepted_submissions
                    FROM Submission_Stats
                    GROUP BY challenge_id) ss ON ch.challenge_id = ss.challenge_id
         LEFT JOIN (SELECT challenge_id,
                           sum(total_views)        AS total_views,
                           sum(total_unique_views) AS total_unique_views
                    FROM view_stats
                    GROUP BY challenge_id) vs ON ch.challenge_id = vs.challenge_id
GROUP BY c.contest_id,
         c.hacker_id,
         c.name
HAVING sum(ss.total_submissions + ss.total_accepted_submissions + vs.total_views + vs.total_unique_views) > 0
ORDER BY c.contest_id;