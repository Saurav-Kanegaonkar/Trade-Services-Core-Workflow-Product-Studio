const files = {
  opportunities: "data/workflow_opportunities.csv",
  themes: "data/customer_research_themes.csv",
  requirements: "data/prd_requirements.csv",
  gates: "data/launch_gates.csv",
  assets: "data/enablement_assets.csv"
};

const numberFields = new Set([
  "frequency_pct",
  "severity",
  "adoption_impact",
  "cash_flow_impact",
  "effort",
  "dependency_risk",
  "confidence",
  "priority_score",
  "evidence_count",
  "readiness"
]);

function parseCsv(text) {
  const rows = [];
  let row = [];
  let value = "";
  let quoted = false;

  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    const next = text[i + 1];

    if (char === '"' && quoted && next === '"') {
      value += '"';
      i += 1;
    } else if (char === '"') {
      quoted = !quoted;
    } else if (char === "," && !quoted) {
      row.push(value);
      value = "";
    } else if ((char === "\n" || char === "\r") && !quoted) {
      if (value || row.length) {
        row.push(value);
        rows.push(row);
        row = [];
        value = "";
      }
      if (char === "\r" && next === "\n") i += 1;
    } else {
      value += char;
    }
  }

  if (value || row.length) {
    row.push(value);
    rows.push(row);
  }

  const headers = rows.shift() || [];
  return rows.map((cells) => Object.fromEntries(headers.map((header, index) => {
    const raw = cells[index] || "";
    return [header, numberFields.has(header) ? Number(raw) : raw];
  })));
}

async function loadCsv(path) {
  const response = await fetch(path);
  if (!response.ok) throw new Error(`Unable to load ${path}`);
  return parseCsv(await response.text());
}

function scoreBar(value) {
  return `<span class="bar"><span style="width:${Math.max(6, value)}%"></span></span>`;
}

function statusClass(value) {
  return value.toLowerCase().replaceAll(" ", "-");
}

function renderTabs() {
  const buttons = [...document.querySelectorAll(".tab")];
  const views = [...document.querySelectorAll(".view")];

  function activate(view) {
    buttons.forEach((button) => button.classList.toggle("is-active", button.dataset.view === view));
    views.forEach((panel) => panel.classList.toggle("is-visible", panel.id === `view-${view}`));
    history.replaceState(null, "", `#${view}`);
  }

  buttons.forEach((button) => {
    button.addEventListener("click", () => activate(button.dataset.view));
  });

  const initial = location.hash.replace("#", "") || "cockpit";
  activate(["cockpit", "prd", "launch"].includes(initial) ? initial : "cockpit");
}

function render(data) {
  const opportunities = [...data.opportunities].sort((a, b) => b.priority_score - a.priority_score);
  const top = opportunities[0];

  document.getElementById("top-brief").innerHTML = `
    <span>Top product bet</span>
    <strong>${top.product_area}</strong>
    <p>${top.hypothesis}</p>
    <small>${top.opportunity_id} / ${top.trade_vertical} / ${top.company_size}</small>
  `;

  document.getElementById("kpis").innerHTML = [
    ["Top score", top.priority_score.toFixed(1), "weighted opportunity"],
    ["Research themes", data.themes.length, "coded signals"],
    ["P0 requirements", data.requirements.filter((item) => item.priority === "P0").length, "ready to shape"],
    ["At-risk gates", data.gates.filter((item) => item.status === "At risk").length, "needs attention"]
  ].map(([label, value, detail]) => `
    <article>
      <span>${label}</span>
      <strong>${value}</strong>
      <em>${detail}</em>
    </article>
  `).join("");

  document.getElementById("priority-table").innerHTML = opportunities.map((row, index) => `
    <tr>
      <td>${index + 1}</td>
      <td>
        <b>${row.product_area}</b>
        <span>${row.workflow_stage} / ${row.trade_vertical}</span>
      </td>
      <td>${row.persona}</td>
      <td>
        <b>${row.priority_score.toFixed(1)}</b>
        ${scoreBar(row.priority_score)}
      </td>
      <td><span class="pill">${row.decision}</span></td>
    </tr>
  `).join("");

  document.getElementById("research-themes").innerHTML = `
    <h3>Customer research themes</h3>
    <div class="theme-list">
      ${data.themes.map((theme) => `
        <article>
          <div>
            <b>${theme.theme}</b>
            <span>${theme.persona} / ${theme.evidence_count} signals</span>
          </div>
          <p>${theme.observed_friction}</p>
          <small>${theme.product_response}</small>
        </article>
      `).join("")}
    </div>
  `;

  const topRequirements = data.requirements.filter((item) => item.opportunity_id === top.opportunity_id);
  document.getElementById("prd-main").innerHTML = `
    <h3>${top.product_area}: ${top.workflow_stage}</h3>
    <div class="problem-card">
      <span>Problem</span>
      <p>${top.customer_pain}</p>
    </div>
    <div class="problem-card">
      <span>Hypothesis</span>
      <p>${top.hypothesis}</p>
    </div>
    <h4>Requirements</h4>
    <div class="requirements">
      ${topRequirements.map((requirement) => `
        <article>
          <div class="req-head">
            <b>${requirement.requirement_id}</b>
            <span>${requirement.priority}</span>
          </div>
          <h5>${requirement.requirement}</h5>
          <p>${requirement.user_story}</p>
          <small>${requirement.acceptance_criteria}</small>
          <code>${requirement.instrumentation_event}</code>
        </article>
      `).join("")}
    </div>
  `;

  document.getElementById("launch-gates").innerHTML = data.gates.map((gate) => `
    <article class="gate">
      <div>
        <b>${gate.gate}</b>
        <span>${gate.owner}</span>
      </div>
      <p>${gate.required_evidence}</p>
      <div class="gate-meta">
        <span class="status ${statusClass(gate.status)}">${gate.status}</span>
        <small>${gate.next_step}</small>
      </div>
    </article>
  `).join("");

  document.getElementById("enablement-assets").innerHTML = data.assets.map((asset) => `
    <article class="asset">
      <div>
        <b>${asset.asset}</b>
        <span>${asset.audience}</span>
      </div>
      <p>${asset.purpose}</p>
      ${scoreBar(asset.readiness)}
      <small>${asset.owner} / ${asset.due_stage} / ${asset.readiness}% ready</small>
    </article>
  `).join("");
}

async function init() {
  renderTabs();
  const entries = await Promise.all(Object.entries(files).map(async ([key, path]) => [key, await loadCsv(path)]));
  render(Object.fromEntries(entries));
}

init().catch((error) => {
  document.querySelector(".shell").insertAdjacentHTML("beforeend", `<p class="load-error">${error.message}</p>`);
});
