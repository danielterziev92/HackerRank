SELECT d.submission_date,
       (SELECT COUNT(*)
        FROM (SELECT s.submission_date,
                     s.hacker_id,
                     @n:=if(COUNT(1) > 1, 1, COUNT(1)) alt,
             (SELECT COUNT(hacker_id)
                  FROM
                      (SELECT s.submission_date, s.hacker_id, COUNT(1),
                      @n:=if(COUNT(1) > 1, 1, COUNT(1)) alt
                      from submissions s GROUP BY 1, 2 ORDER BY 1, 3 DESC, 2) t
                WHERE submission_date<=s.submission_date AND hacker_id=s.hacker_id) agg
              FROM submissions s
              GROUP BY 1, 2
              ORDER BY 1, 3 DESC, 2) oi
        WHERE submission_date <= d.submission_date
          AND agg = extract(DAY FROM d.submission_date))  uniq_COUNT,
       (SELECT s.hacker_id
        FROM submissions s
                 INNER JOIN hackers h ON s.hacker_id = h.hacker_id
        WHERE s.submission_date = d.submission_date
        GROUP BY s.hacker_id, h.name
        ORDER BY COUNT(s.hacker_id) DESC, s.hacker_id ASC limit 1) id_highest_sub,
    (SELECT h.name FROM submissions s INNER JOIN hackers h ON s.hacker_id = h.hacker_id WHERE s.submission_date = d.submission_date
        GROUP BY s.hacker_id, h.name ORDER BY COUNT(s.hacker_id) DESC, s.hacker_id ASC limit 1) name_highest_sub
from (SELECT distinct s.submission_date FROM submissions s ORDER BY s.submission_date) d;