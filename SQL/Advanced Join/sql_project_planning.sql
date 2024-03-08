with recursive
    grp_gen as
        (select task_id, start_date, end_date, row_number() over(order by start_date) rn from projects),
    grp_alloc as
        (select task_id, start_date, end_date, 1 as grp, rn
         from grp_gen
         where rn = 1
         union all
         select a.task_id,
                a.start_date,
                a.end_date,
                case when b.end_date = a.start_date then b.grp else b.grp + 1 end as grp,
                a.rn
         from grp_gen a
                  join grp_alloc b on a.rn = b.rn + 1)
select min(start_date) as start_date, max(end_date) end_date
from grp_alloc
group by grp
order by max(end_date) - min(start_date), 1;