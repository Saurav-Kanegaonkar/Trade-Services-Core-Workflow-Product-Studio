-- Product readiness checks for the synthetic trade services workflow artifact.

select
  opportunity_id,
  product_area,
  priority_score,
  decision
from priority_queue
where decision = 'Build PRD now'
order by priority_score desc;

select
  opportunity_id,
  count(*) as p0_requirements
from prd_requirements
where priority = 'P0'
group by opportunity_id;

select
  status,
  count(*) as launch_gates
from launch_gates
group by status;
