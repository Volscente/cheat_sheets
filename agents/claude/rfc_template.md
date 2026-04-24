# \[RFC\] {Team}: {Short Title}

## _{One-line subtitle — what this RFC proposes}_

| Author(s)           | {Full Name} |
| :------------------ | :---------- |
| **Owner(s)**        | {Team name} |
| **Org(s)**          | {Org name}  |
| **RFC status**      | Draft       |
| **Review deadline** | {Date}      |

<!-- Fill in author, owning team, and a realistic review deadline (typically 2 weeks out). -->

### Timeline

| Date         | Status | Note |
| :----------- | :----- | :--- |
| {YYYY-MM-DD} | Draft  |      |

<!-- Add a row each time the RFC changes status: Draft → In Review → Approved / Rejected. -->

### Reviews

| Team   | Reviewer | Required/optional | Status  | Comment |
| :----- | :------- | :---------------- | :------ | :------ |
| {Team} | {Name}   | Required          | Pending |         |
| {Team} | {Name}   | Optional          | Pending |         |

<!-- List all stakeholders whose sign-off is needed or whose input is valuable. Mark as Required only if their approval gates the work. -->

### Table of contents

[Project Context & Strategic Goals](#project-context-&-strategic-goals)

[Motivation](#motivation)

[Objectives](#objectives)

[Scope](#scope)

[{Main Technical Section Title}](#{main-technical-section-anchor})

[Tech Stack](#tech-stack)

[Effort Estimations](#effort-estimations)

[FAQs](#faqs)

[Appendix](#appendix)

[Risks & Mitigations](#risks-&-mitigations)

[References and further reading](#references-and-further-reading)

<!-- Update anchors to match your section headings exactly. Add or remove entries as needed. -->

---

# **Project Context & Strategic Goals** {#project-context-&-strategic-goals}

## Motivation {#motivation}

<!--
Describe the problem this RFC solves. Structure as:
1. What is the system or process being changed?
2. What is the current pain point or gap? Be specific — name the missing capability, visible symptom, or risk.
3. What happens if we do nothing?
4. State the primary requirement the proposal must satisfy.

Keep to 1–3 paragraphs. Avoid solution details here — this section is about why, not what.
-->

## Objectives {#objectives}

<!--
List 3–6 concrete, verifiable objectives. Each should:
- Start with a bold label (e.g., **Provide X**, **Enable Y**).
- Describe what the system will be able to do after this RFC is implemented.
- Be scoped to outcomes, not tasks.

Avoid vague objectives like "improve quality". Prefer "detect score regressions > 0.03 with 80% statistical power".
-->

- **{Objective 1}**: {Description}
- **{Objective 2}**: {Description}
- **{Objective 3}**: {Description}

## Scope {#scope}

**In-Scope:**

<!--
Bullet-list the capabilities, components, or workflows explicitly covered by this RFC.
Each bullet should name a concrete deliverable (e.g., "Reference Corpus Construction", "GitHub Actions workflow").
-->

- {Capability 1}
- {Capability 2}

**Out-of-Scope:**

<!--
Bullet-list anything a reader might reasonably expect to be included but isn't.
For each item, briefly state why it is excluded (e.g., dependency not ready, separate team, future phase).
Link to the relevant Appendix section if a future design exists.
-->

- **{Excluded item}**: {Reason. See [Appendix: {Section}](#link) if applicable.}

---

# **{Main Technical Section Title}** {#{main-technical-section-anchor}}

<!--
Name this section after the feature or system being designed (e.g., "Translations Evaluation Framework", "Online Catalog Dataset Pipeline").
This is the core of the RFC. Organise it into logical subsections that match the architecture of the proposed solution.
The subsections below are a starting point — add, rename, or remove them to fit the proposal.
-->

## Methodology Overview {#methodology-overview}

<!--
Describe the high-level approach: how the system works end-to-end, what its key design principles are, and how it fits into the existing architecture.
Include a reference to any diagram if one exists.

Useful structure:
1. What triggers the system?
2. What are the major stages or components?
3. What are the non-negotiable design principles (e.g., cost-controlled, auditable, dual execution)?
-->

## {Subsection 1} {#{subsection-1-anchor}}

<!--
Add one subsection per major component or design decision.
Each subsection should cover:
- What it is and why it was designed this way.
- Any schemas, algorithms, or decision rules that are precise enough to implement from.
- Tables or code blocks where useful.

Remove this comment block and replace with content.
-->

## {Subsection 2} {#{subsection-2-anchor}}

<!-- Same as above. Repeat as needed. -->

## Tech Stack {#tech-stack}

<!--
List the libraries, services, and infrastructure components the implementation depends on.
For each, include the specific package or version if relevant (e.g., "unbabel-comet (wmt22-comet-da)").
Keep this list minimal — only what is actually used, not aspirational dependencies.
-->

- **{Library / Service}**: {Why it is used}
- **{Library / Service}**: {Why it is used}

## Effort Estimations {#effort-estimations}

<!--
Use 1 FTE = 1 Day. Break the work into milestones with task descriptions and estimates.
State the recommended delivery order and any milestone dependencies.
-->

Estimates are 1 FTE = 1 Day. Total estimated effort: **{X–Y FTE}**.

### Milestone Breakdown

| Milestone   | Tasks               | Est. FTE  |
| :---------- | :------------------ | :-------- |
| M1 — {Name} | {Task descriptions} | {N} FTE   |
| M2 — {Name} | {Task descriptions} | {N–M} FTE |

### Recommended Delivery Order

1. M1 — {Name} ({reason, e.g., prerequisite for everything else})
2. M2 — {Name} ({dependency note})

---

# **FAQs** {#faqs}

<!--
Anticipate the questions reviewers or implementers are most likely to ask.
Each Q&A should:
- Address a real decision point or design tradeoff (not a tutorial question).
- Explain *why* the chosen approach was taken, not just *what* it is.
- Be written as if answering a skeptical senior engineer.

Aim for 5–8 questions. Remove placeholder entries below and replace with real ones.
-->

**Q: {Question about a key design decision}**

A: {Explain the reasoning. Reference relevant constraints, prior incidents, or tradeoffs considered.}

**Q: {Question about a boundary or exclusion}**

A: {Explain why this is out of scope and what the alternative or future plan is.}

**Q: Terminology?**

A: {Define acronyms and domain terms used in this RFC.}

- {ACRONYM} → {Full name and brief description}

---

# **Appendix** {#appendix}

## Risks & Mitigations {#risks-&-mitigations}

<!--
List the top risks (3–6) that could derail implementation or degrade the outcome.
For each: estimate likelihood (Low / Medium / High) and describe the mitigation.
Include a "Recommended First Step" callout if there is a high-risk unknown that should be resolved before coding begins.
-->

| Risk               | Likelihood          | Mitigation          |
| :----------------- | :------------------ | :------------------ |
| {Risk description} | Low / Medium / High | {Mitigation action} |

| Recommended First Step: {Describe the highest-risk unknown and what to do before implementation starts.} |
| :------------------------------------------------------------------------------------------------------- |

## Future: {Future Capability 1} {#{future-capability-1-anchor}}

<!--
Use one subsection per deferred capability. Describe:
1. What this capability would do.
2. Why it is deferred (dependency, infrastructure gap, cost, etc.).
3. Enough design detail that a future RFC author has a starting point.
-->

## References and further reading {#references-and-further-reading}

<!--
Link to relevant Confluence pages, JIRA epics, related RFCs, external papers, or documentation.
-->

- [{Title}]({URL})
