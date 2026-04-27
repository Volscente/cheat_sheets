# \[RFC\] {Short Title}

## _{One-line subtitle — what this RFC proposes}_

| Author(s)        | {Full Name}                        |
| :--------------- | :--------------------------------- |
| **Project**      | {Project name}                     |
| **RFC status**   | Draft                              |
| **Review deadline** | {Date}                          |
| **Notion page**  | [{Title}]({URL}) _(optional)_      |
| **GitHub repo**  | [{owner/repo}]({URL}) _(optional)_ |

### Timeline

| Date         | Status | Note |
| :----------- | :----- | :--- |
| {YYYY-MM-DD} | Draft  |      |

<!-- Add a row each time the RFC changes status: Draft → In Review → Done. -->

### Reviews

| Reviewer | Required/optional | Status  | Comment |
| :------- | :---------------- | :------ | :------ |
| {Name}   | Required          | Pending |         |
| {Name}   | Optional          | Pending |         |

<!-- List anyone whose input you want. Mark Required only if you need their sign-off before moving forward. Remove this table entirely if you are working solo. -->

### Table of contents

[Context](#context)

[Motivation](#motivation)

[Objectives](#objectives)

[Scope](#scope)

[{Main Technical Section Title}](#{main-technical-section-anchor})

[Tech Stack](#tech-stack)

[Effort Estimations](#effort-estimations)

[FAQs](#faqs)

[Appendix](#appendix)

[Risks & Open Questions](#risks--open-questions)

[References](#references)

---

# **Context** {#context}

<!--
One paragraph describing the project this RFC belongs to and what already exists.
Link to relevant Notion pages, prior art, or related GitHub issues.
Keep this concise — just enough for someone unfamiliar with the project to understand the setting.
-->

## Motivation {#motivation}

<!--
Describe why you want to build this. Structure as:
1. What is the current situation or gap?
2. What is the specific pain point, limitation, or opportunity?
3. What would be different once this is built?

Keep to 1–3 paragraphs. Avoid solution details here — this section is about why, not what.
-->

## Objectives {#objectives}

<!--
List 3–6 concrete objectives. Each should:
- Start with a bold label (e.g., **Build X**, **Enable Y**, **Automate Z**).
- Describe what the system or project will be able to do after this RFC is implemented.
- Be specific enough that you can tell whether you achieved it.
-->

- **{Objective 1}**: {Description}
- **{Objective 2}**: {Description}
- **{Objective 3}**: {Description}

## Scope {#scope}

**In-Scope:**

- {Capability or feature 1}
- {Capability or feature 2}

**Out-of-Scope:**

- **{Excluded item}**: {Reason — e.g., future phase, separate project, not worth the complexity now.}

---

# **{Main Technical Section Title}** {#{main-technical-section-anchor}}

<!--
Name this section after the feature or system being designed.
Organise into logical subsections that match the architecture of the proposed solution.
-->

## Approach Overview {#approach-overview}

<!--
Describe the high-level approach end-to-end:
1. What triggers the system or workflow?
2. What are the major stages or components?
3. Key design decisions or constraints (e.g., offline-first, no external dependencies, single binary).
-->

## {Subsection 1} {#{subsection-1-anchor}}

<!--
One subsection per major component or design decision.
Cover: what it is, why it was designed this way, any schemas or algorithms precise enough to implement from.
-->

## {Subsection 2} {#{subsection-2-anchor}}

<!-- Same as above. Repeat as needed. -->

## Tech Stack {#tech-stack}

<!--
List libraries, services, and tools this depends on.
Keep it minimal — only what is actually used.
-->

- **{Library / Tool}**: {Why it is used}
- **{Library / Tool}**: {Why it is used}

## Effort Estimations {#effort-estimations}

<!--
Rough estimate broken into milestones. Use whatever unit makes sense to you (hours, days, sessions).
State the recommended order and any dependencies between milestones.
-->

Total estimated effort: **{X} sessions / hours / days**.

### Milestone Breakdown

| Milestone   | Description         | Est. effort |
| :---------- | :------------------ | :---------- |
| M1 — {Name} | {Task descriptions} | {N}         |
| M2 — {Name} | {Task descriptions} | {N}         |

### Recommended Order

1. M1 — {Name} ({reason})
2. M2 — {Name} ({dependency note})

---

# **FAQs** {#faqs}

<!--
Anticipate questions you or future readers might have about design decisions or exclusions.
Aim for 3–6 questions.
-->

**Q: {Question about a key design decision}**

A: {Explain the reasoning and tradeoffs.}

**Q: {Question about a boundary or exclusion}**

A: {Explain why this is out of scope.}

**Q: Terminology?**

A: {Define any abbreviations or domain terms used in this RFC.}

- {ACRONYM} → {Full name and brief description}

---

# **Appendix** {#appendix}

## Risks & Open Questions {#risks--open-questions}

| Risk / Question    | Likelihood          | Mitigation / Answer  |
| :----------------- | :------------------ | :------------------- |
| {Risk description} | Low / Medium / High | {Mitigation action}  |

## Future: {Deferred Capability} {#{deferred-capability-anchor}}

<!--
One subsection per deferred idea. Describe what it would do, why it is deferred, and enough detail for a future RFC.
-->

## References {#references}

<!--
Links to Notion pages, GitHub issues/PRs, related projects, docs, or papers.
-->

- [{Title}]({URL})
