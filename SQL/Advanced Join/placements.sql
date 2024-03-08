with fp as
         (select f.id, friend_id, p.salary
          from friends as f
                   join packages as p
                        on friend_id = p.id)

select name
from students as s
         join packages as p
              on s.id = p.id
         JOIN fp
              on fp.id = s.id
where fp.salary > p.salary
order by fp.salary