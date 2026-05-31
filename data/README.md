# Data Sources

Synthetic product discovery and launch-readiness data for a trade services SaaS core platform.

The data models common field service management structures: scheduling and dispatch, estimates, job management, invoicing, payments, customer communication, pricebook quality, and customer portal follow-up. It is generated for portfolio demonstration only and does not represent real company, customer, support, revenue, or product telemetry.

## Files

- `workflow_opportunities.csv`: scored core workflow opportunities.
- `customer_research_themes.csv`: coded customer research themes and evidence counts.
- `prd_requirements.csv`: PRD-ready requirements, user stories, acceptance criteria, telemetry events, and statuses.
- `launch_gates.csv`: release gates with owners, evidence needs, risk, and next steps.
- `enablement_assets.csv`: Sales, Customer Success, Support, and Analytics enablement needs.

## Generation

Run:

```bash
npm run analyze
```

The scoring script regenerates the CSV files, `analysis/outputs/priority_queue.csv`, `analysis/outputs/summary.json`, and the analysis markdown files.
