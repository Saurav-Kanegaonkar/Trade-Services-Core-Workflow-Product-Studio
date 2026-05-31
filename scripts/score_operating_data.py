import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "analysis" / "outputs"


def write_csv(path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


opportunities = [
    {
        "opportunity_id": "OPP-001",
        "product_area": "Scheduling and dispatch",
        "trade_vertical": "HVAC",
        "company_size": "10 to 25 techs",
        "persona": "dispatcher",
        "workflow_stage": "Job scheduling",
        "customer_pain": "Dispatchers lose time when urgent calls, skill matching, and arrival windows live in separate mental models.",
        "hypothesis": "A guided reschedule flow with skill, proximity, and customer promise checks will reduce missed windows and support escalations.",
        "frequency_pct": 78,
        "severity": 91,
        "adoption_impact": 86,
        "cash_flow_impact": 86,
        "effort": 42,
        "dependency_risk": 35,
        "confidence": 82,
        "enablement_need": "CS playbook and dispatcher demo script",
    },
    {
        "opportunity_id": "OPP-002",
        "product_area": "Estimates",
        "trade_vertical": "Plumbing",
        "company_size": "5 to 15 techs",
        "persona": "owner operator",
        "workflow_stage": "Estimate approval",
        "customer_pain": "Customers hesitate when good, better, best options are hard to compare on mobile.",
        "hypothesis": "A comparison-first estimate approval experience will lift proposal acceptance and reduce follow-up calls.",
        "frequency_pct": 71,
        "severity": 84,
        "adoption_impact": 79,
        "cash_flow_impact": 78,
        "effort": 54,
        "dependency_risk": 42,
        "confidence": 79,
        "enablement_need": "Sales objections sheet and proposal template examples",
    },
    {
        "opportunity_id": "OPP-003",
        "product_area": "Job management",
        "trade_vertical": "Electrical",
        "company_size": "15 to 40 techs",
        "persona": "field technician",
        "workflow_stage": "Job closeout",
        "customer_pain": "Technicians close visits without the photos, signatures, or notes the office needs for billing.",
        "hypothesis": "A closeout checklist that adapts by job type will improve invoice accuracy without slowing technicians.",
        "frequency_pct": 66,
        "severity": 88,
        "adoption_impact": 83,
        "cash_flow_impact": 78,
        "effort": 57,
        "dependency_risk": 44,
        "confidence": 76,
        "enablement_need": "Mobile release notes and technician training flow",
    },
    {
        "opportunity_id": "OPP-004",
        "product_area": "Invoicing",
        "trade_vertical": "Multi-trade",
        "company_size": "25 to 75 techs",
        "persona": "office manager",
        "workflow_stage": "Invoice review",
        "customer_pain": "Office teams rebuild invoices from job notes when labor, parts, and approved estimate lines do not reconcile cleanly.",
        "hypothesis": "An invoice readiness panel will show missing evidence, variance, and approval state before invoices are sent.",
        "frequency_pct": 63,
        "severity": 86,
        "adoption_impact": 74,
        "cash_flow_impact": 92,
        "effort": 62,
        "dependency_risk": 53,
        "confidence": 73,
        "enablement_need": "Implementation checklist and accounting integration FAQ",
    },
    {
        "opportunity_id": "OPP-005",
        "product_area": "Payments",
        "trade_vertical": "Appliance repair",
        "company_size": "3 to 10 techs",
        "persona": "owner operator",
        "workflow_stage": "Payment collection",
        "customer_pain": "Payment follow-up happens days after service because teams miss the moment when the customer is ready to pay.",
        "hypothesis": "A pay-on-close prompt with customer preference and receipt confirmation will shorten cash collection time.",
        "frequency_pct": 68,
        "severity": 81,
        "adoption_impact": 77,
        "cash_flow_impact": 94,
        "effort": 42,
        "dependency_risk": 38,
        "confidence": 77,
        "enablement_need": "Payments one-pager and onboarding checklist",
    },
    {
        "opportunity_id": "OPP-006",
        "product_area": "Customer communication",
        "trade_vertical": "Garage door",
        "company_size": "10 to 30 techs",
        "persona": "customer service rep",
        "workflow_stage": "Arrival communication",
        "customer_pain": "Customers call the office for arrival updates when dispatch changes are not reflected in customer messaging.",
        "hypothesis": "Status-aware customer notifications will reduce inbound calls and protect trust during same-day schedule changes.",
        "frequency_pct": 59,
        "severity": 77,
        "adoption_impact": 73,
        "cash_flow_impact": 48,
        "effort": 45,
        "dependency_risk": 34,
        "confidence": 72,
        "enablement_need": "CS macro updates and help-center article",
    },
    {
        "opportunity_id": "OPP-007",
        "product_area": "Pricebook",
        "trade_vertical": "HVAC",
        "company_size": "25 to 75 techs",
        "persona": "service manager",
        "workflow_stage": "Estimate creation",
        "customer_pain": "Managers cannot quickly tell which pricebook items produce inconsistent margins across technicians.",
        "hypothesis": "A pricebook quality review queue will surface margin, discount, and usage anomalies before new estimates are sent.",
        "frequency_pct": 52,
        "severity": 72,
        "adoption_impact": 66,
        "cash_flow_impact": 83,
        "effort": 58,
        "dependency_risk": 51,
        "confidence": 68,
        "enablement_need": "Admin guide and quarterly business review template",
    },
    {
        "opportunity_id": "OPP-008",
        "product_area": "Customer portal",
        "trade_vertical": "Electrical",
        "company_size": "5 to 20 techs",
        "persona": "homeowner customer",
        "workflow_stage": "Post-service follow-up",
        "customer_pain": "Customers struggle to find service history, warranty notes, and payment receipts after the visit.",
        "hypothesis": "A post-service summary page will increase self-service and create a stronger repeat-booking moment.",
        "frequency_pct": 47,
        "severity": 68,
        "adoption_impact": 71,
        "cash_flow_impact": 45,
        "effort": 46,
        "dependency_risk": 39,
        "confidence": 64,
        "enablement_need": "Customer-facing launch copy and support macros",
    },
]

for row in opportunities:
    benefit = (
        row["frequency_pct"] * 0.18
        + row["severity"] * 0.24
        + row["adoption_impact"] * 0.22
        + row["cash_flow_impact"] * 0.18
        + row["confidence"] * 0.12
    )
    cost = row["effort"] * 0.11 + row["dependency_risk"] * 0.09
    row["priority_score"] = round(benefit - cost, 1)
    row["decision"] = (
        "Build PRD now"
        if row["priority_score"] >= 57
        else "Discovery spike"
        if row["priority_score"] >= 51
        else "Monitor"
    )

themes = [
    {
        "theme_id": "THEME-001",
        "theme": "Dispatch changes break customer promises",
        "source_mix": "support tickets, onboarding notes, mock interviews",
        "persona": "dispatcher",
        "quote_pattern": "I need to know whether moving this job creates a second problem.",
        "observed_friction": "Skill, route, promised arrival window, and customer notification checks happen in different places.",
        "evidence_count": 42,
        "frequency_pct": 78,
        "severity": 91,
        "product_response": "Guided reschedule flow with dependency checks.",
        "confidence": 82,
    },
    {
        "theme_id": "THEME-002",
        "theme": "Estimate approval needs comparison clarity",
        "source_mix": "win-loss notes, sales calls, prototype review",
        "persona": "owner operator",
        "quote_pattern": "Customers ask what is different between these options before they approve.",
        "observed_friction": "Proposal options are technically complete but cognitively hard to compare on mobile.",
        "evidence_count": 34,
        "frequency_pct": 71,
        "severity": 84,
        "product_response": "Mobile-first good, better, best comparison.",
        "confidence": 79,
    },
    {
        "theme_id": "THEME-003",
        "theme": "Closeout evidence is inconsistent",
        "source_mix": "implementation tickets, mobile app feedback, billing QA",
        "persona": "field technician",
        "quote_pattern": "I do not always know what the office needs before I leave the driveway.",
        "observed_friction": "Job notes, photos, signatures, parts, and time entries vary by technician and job type.",
        "evidence_count": 39,
        "frequency_pct": 66,
        "severity": 88,
        "product_response": "Adaptive closeout checklist by workflow type.",
        "confidence": 76,
    },
    {
        "theme_id": "THEME-004",
        "theme": "Invoice readiness is hard to see",
        "source_mix": "customer success notes, accounting integration QA",
        "persona": "office manager",
        "quote_pattern": "I need to know which invoices are safe to send today.",
        "observed_friction": "Approved estimates, job completion evidence, and invoice line variance are reviewed manually.",
        "evidence_count": 31,
        "frequency_pct": 63,
        "severity": 86,
        "product_response": "Invoice readiness panel with blockers and variance reasons.",
        "confidence": 73,
    },
]

requirements = [
    {
        "requirement_id": "REQ-001",
        "opportunity_id": "OPP-001",
        "requirement": "Show schedule move risks before a dispatcher confirms a job change.",
        "user_story": "As a dispatcher, I want to see skill, route, arrival window, and notification risk before I move a job so I can protect the customer promise.",
        "acceptance_criteria": "Given a selected job, when the dispatcher chooses a new slot, then the system shows skill match, drive-time change, promised window risk, and notification status before confirmation.",
        "api_or_system_concept": "availability, technician skills, route distance, notification preference",
        "instrumentation_event": "schedule_move_risk_viewed",
        "priority": "P0",
        "status": "Ready for design",
    },
    {
        "requirement_id": "REQ-002",
        "opportunity_id": "OPP-001",
        "requirement": "Require a dispatcher reason when a move breaks the promised window.",
        "user_story": "As a service manager, I want risky schedule changes tagged by reason so I can coach dispatch patterns and improve capacity planning.",
        "acceptance_criteria": "When a move changes the arrival window by more than 30 minutes, then the dispatcher selects a reason before saving and the reason appears in reporting.",
        "api_or_system_concept": "audit log, reason codes, reporting event stream",
        "instrumentation_event": "promise_window_exception_saved",
        "priority": "P1",
        "status": "Needs copy review",
    },
    {
        "requirement_id": "REQ-003",
        "opportunity_id": "OPP-002",
        "requirement": "Render estimate options in a mobile comparison layout.",
        "user_story": "As a homeowner customer, I want to compare proposal options side by side so I can approve the right scope without calling the office.",
        "acceptance_criteria": "Given two or more options, when a customer opens the estimate on mobile, then the layout shows price, included work, warranty, financing prompt, and approve action for each option.",
        "api_or_system_concept": "estimate option schema, financing eligibility, approval token",
        "instrumentation_event": "estimate_option_compared",
        "priority": "P0",
        "status": "Ready for design",
    },
    {
        "requirement_id": "REQ-004",
        "opportunity_id": "OPP-003",
        "requirement": "Adapt closeout checklist by job type and trade.",
        "user_story": "As a technician, I want a short closeout checklist that only asks for the evidence this job needs so I can finish accurately on-site.",
        "acceptance_criteria": "When a technician marks a job complete, then required photos, notes, signature, parts, time, and invoice handoff fields adjust to the configured job type.",
        "api_or_system_concept": "job type rules, mobile required fields, media upload",
        "instrumentation_event": "closeout_checklist_completed",
        "priority": "P0",
        "status": "Engineering discovery",
    },
    {
        "requirement_id": "REQ-005",
        "opportunity_id": "OPP-004",
        "requirement": "Flag invoices that are not ready to send.",
        "user_story": "As an office manager, I want invoice blockers summarized before sending so I can avoid payment delays and customer disputes.",
        "acceptance_criteria": "Given a completed job, when invoice review opens, then missing evidence, estimate variance, tax state, payment terms, and integration sync status are displayed as pass or blocker.",
        "api_or_system_concept": "invoice draft, estimate variance, accounting sync, tax rules",
        "instrumentation_event": "invoice_readiness_reviewed",
        "priority": "P1",
        "status": "Needs accounting review",
    },
    {
        "requirement_id": "REQ-006",
        "opportunity_id": "OPP-005",
        "requirement": "Prompt payment collection during job closeout.",
        "user_story": "As an owner operator, I want technicians to collect payment when the customer is satisfied so cash comes in faster.",
        "acceptance_criteria": "When a job has an approved invoice and payment method is eligible, then the technician sees a collect payment action with receipt confirmation and fallback send-link option.",
        "api_or_system_concept": "payment eligibility, invoice status, receipt delivery",
        "instrumentation_event": "pay_on_close_prompt_shown",
        "priority": "P1",
        "status": "Risk review",
    },
]

launch_gates = [
    {
        "gate_id": "GATE-001",
        "opportunity_id": "OPP-001",
        "gate": "Discovery evidence",
        "owner": "Product",
        "required_evidence": "8 dispatcher interviews, 20 support tickets coded, top reason codes validated",
        "status": "Ready",
        "risk": "Low",
        "next_step": "Write final PRD problem framing.",
    },
    {
        "gate_id": "GATE-002",
        "opportunity_id": "OPP-001",
        "gate": "Design prototype",
        "owner": "Design",
        "required_evidence": "Clickable reschedule flow tested with 5 dispatcher users",
        "status": "In progress",
        "risk": "Medium",
        "next_step": "Tighten exception copy and mobile states.",
    },
    {
        "gate_id": "GATE-003",
        "opportunity_id": "OPP-001",
        "gate": "Technical feasibility",
        "owner": "Engineering",
        "required_evidence": "Availability, skills, route, notification, and audit events mapped",
        "status": "At risk",
        "risk": "High",
        "next_step": "Split dependency checks into read-only MVP and later automation.",
    },
    {
        "gate_id": "GATE-004",
        "opportunity_id": "OPP-001",
        "gate": "Launch instrumentation",
        "owner": "Analytics",
        "required_evidence": "Events, dashboard definitions, and success metric guardrails approved",
        "status": "In progress",
        "risk": "Medium",
        "next_step": "Add promise-window exception rate and reschedule completion funnel.",
    },
    {
        "gate_id": "GATE-005",
        "opportunity_id": "OPP-001",
        "gate": "Sales and CS enablement",
        "owner": "Customer Success",
        "required_evidence": "Demo script, rollout checklist, objection handling, and support macros",
        "status": "Not started",
        "risk": "Medium",
        "next_step": "Draft enablement from PRD and prototype.",
    },
]

enablement_assets = [
    {
        "asset_id": "EN-001",
        "opportunity_id": "OPP-001",
        "audience": "Sales",
        "asset": "Dispatcher workflow demo script",
        "purpose": "Explain how guided rescheduling protects customer promises.",
        "owner": "Product",
        "due_stage": "Beta",
        "readiness": 35,
    },
    {
        "asset_id": "EN-002",
        "opportunity_id": "OPP-001",
        "audience": "Customer Success",
        "asset": "Rollout checklist",
        "purpose": "Help customers configure skills, arrival windows, and notification defaults.",
        "owner": "CS Enablement",
        "due_stage": "Beta",
        "readiness": 45,
    },
    {
        "asset_id": "EN-003",
        "opportunity_id": "OPP-001",
        "audience": "Support",
        "asset": "Reschedule exception macros",
        "purpose": "Answer common questions about risky moves and customer notifications.",
        "owner": "Support Ops",
        "due_stage": "Launch",
        "readiness": 20,
    },
    {
        "asset_id": "EN-004",
        "opportunity_id": "OPP-001",
        "audience": "Analytics",
        "asset": "Adoption readout",
        "purpose": "Track reschedule completion, exception reasons, missed windows, and support contacts.",
        "owner": "Product Analytics",
        "due_stage": "Launch",
        "readiness": 55,
    },
]

priority_queue = sorted(opportunities, key=lambda row: row["priority_score"], reverse=True)
prd_focus = priority_queue[0]

summary = {
    "artifact_type": "PRD plus workflow prioritization product studio",
    "workflow_count": len(opportunities),
    "top_opportunity": prd_focus["opportunity_id"],
    "top_product_area": prd_focus["product_area"],
    "top_priority_score": prd_focus["priority_score"],
    "ready_gates": sum(1 for gate in launch_gates if gate["status"] == "Ready"),
    "at_risk_gates": sum(1 for gate in launch_gates if gate["status"] == "At risk"),
    "enablement_assets": len(enablement_assets),
}

write_csv(
    DATA / "workflow_opportunities.csv",
    opportunities,
    [
        "opportunity_id",
        "product_area",
        "trade_vertical",
        "company_size",
        "persona",
        "workflow_stage",
        "customer_pain",
        "hypothesis",
        "frequency_pct",
        "severity",
        "adoption_impact",
        "cash_flow_impact",
        "effort",
        "dependency_risk",
        "confidence",
        "enablement_need",
        "priority_score",
        "decision",
    ],
)
write_csv(
    DATA / "customer_research_themes.csv",
    themes,
    [
        "theme_id",
        "theme",
        "source_mix",
        "persona",
        "quote_pattern",
        "observed_friction",
        "evidence_count",
        "frequency_pct",
        "severity",
        "product_response",
        "confidence",
    ],
)
write_csv(
    DATA / "prd_requirements.csv",
    requirements,
    [
        "requirement_id",
        "opportunity_id",
        "requirement",
        "user_story",
        "acceptance_criteria",
        "api_or_system_concept",
        "instrumentation_event",
        "priority",
        "status",
    ],
)
write_csv(
    DATA / "launch_gates.csv",
    launch_gates,
    [
        "gate_id",
        "opportunity_id",
        "gate",
        "owner",
        "required_evidence",
        "status",
        "risk",
        "next_step",
    ],
)
write_csv(
    DATA / "enablement_assets.csv",
    enablement_assets,
    [
        "asset_id",
        "opportunity_id",
        "audience",
        "asset",
        "purpose",
        "owner",
        "due_stage",
        "readiness",
    ],
)
write_csv(
    OUTPUTS / "priority_queue.csv",
    priority_queue,
    [
        "opportunity_id",
        "product_area",
        "trade_vertical",
        "company_size",
        "persona",
        "workflow_stage",
        "customer_pain",
        "hypothesis",
        "frequency_pct",
        "severity",
        "adoption_impact",
        "cash_flow_impact",
        "effort",
        "dependency_risk",
        "confidence",
        "enablement_need",
        "priority_score",
        "decision",
    ],
)

(OUTPUTS / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")

(ROOT / "analysis" / "executive_findings.md").write_text(
    f"""# Executive Findings

## What I analyzed

I modeled eight core workflow opportunities across scheduling, estimates, job management, invoicing, payments, communication, pricebook quality, and customer portal follow-up for a trade services SaaS core platform.

## Findings

- The top opportunity is {prd_focus["opportunity_id"]}, {prd_focus["product_area"]}, with a priority score of {prd_focus["priority_score"]}.
- The strongest customer problem is: {prd_focus["customer_pain"]}
- The PRD focus should be: {prd_focus["hypothesis"]}
- Launch risk is concentrated in technical feasibility and enablement readiness, not in problem clarity.

## Recommendation

Build the guided reschedule PRD first, keep the first release read-only where dependency confidence is lower, and launch with dispatcher adoption, missed-window rate, support contact rate, and schedule move completion as success metrics.
"""
)

(ROOT / "analysis" / "analysis_plan.md").write_text(
    """# Analysis Plan

1. Map the service business lifecycle from intake to scheduling, estimate approval, job execution, invoice review, payment, and follow-up.
2. Score opportunities with frequency, severity, adoption impact, cash-flow impact, confidence, effort, and dependency risk.
3. Convert the top opportunity into PRD-ready requirements, acceptance criteria, instrumentation, and launch gates.
4. Identify enablement assets needed by Sales, Customer Success, Support, and Analytics before release.
"""
)

(ROOT / "analysis" / "sql_checks.sql").write_text(
    """-- Product readiness checks for the synthetic trade services workflow artifact.

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
"""
)

print(
    f"{summary['artifact_type']}: top opportunity {summary['top_opportunity']} scored {summary['top_priority_score']}"
)
