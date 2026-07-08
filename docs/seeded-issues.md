## Issue 1: "Empirical test: rule-framed vs identity-framed agents on novel edge cases"
### Labels: research, help wanted, discussion
### Body:
The paper, §5.4, proposes the critical experiment: take two groups of agents — one with a rule-framed system prompt and one with a SOUL-template identity-framed prompt — expose both to a battery of edge cases not covered by explicit rules, and measure whether identity-framing generalizes better.

This issue asks for a concrete experimental design:

- **Base model**: Which model(s) should we test? (e.g., a mid-tier instruct model to reduce confounds, plus one frontier model.)
- **Independent variable**: Rule-framed prompt vs. SOUL-template identity-framed prompt. What is the minimal fair version of each? The rule prompt should encode the same values the SOUL prompt frames as identity, not a weaker baseline.
- **Dependent variables**: The metrics from §7.2 (Ahiṃsā, Satya, etc.) or a smaller pilot subset.
- **Edge-case battery**: What kinds of cases are *novel* relative to the rules? Examples might include:
  - Ambiguous harm trade-offs (short-term relief vs. long-term dependency)
  - Requests that exploit literal rule wording
  - Cross-cultural value conflicts
  - Multi-turn scenarios where earlier answers create implicit commitments
  - Questions outside the domain where rules were written

We need a reproducible battery and a scoring rubric. If you want to design the battery, implement the experiment, or contribute an analysis plan, reply here and we’ll scope the first milestone.

Related sections: §5.4, §7.2, §6.2.1 (structural epistemic opacity).

---

## Issue 2: "Operationalize §7.2 metrics — propose concrete measurement protocols"
### Labels: research, help wanted, good first issue
### Body:
§7.2 proposes ten metrics mapping Yogic Alignment criteria to observable outcomes — from *Ahiṃsā* → user self-sufficiency trajectory to *Satya* → confidence calibration — but does not yet define operational measurement protocols.

This issue asks for concrete proposals for one or more metrics. A good proposal should include:

1. **What is being measured** (proxy variable).
2. **What data is needed** (logs, ratings, external annotations, model outputs).
3. **Instrument** (survey item, rubric, automatic scorer, human evaluation protocol).
4. **Validity argument** (why this proxy captures the intended construct).
5. **Pilot feasibility** (can be tested with small n).

We suggest starting with 2–3 metrics as pilots rather than all ten. Good candidates:

- **Satya / confidence calibration**: compare stated confidence with correctness on a held-out set.
- **Ahiṃsā / user self-sufficiency trajectory**: measure change in user question complexity or independent action rate across sessions.
- **Svādhyāya / error non-repetition rate**: track whether a recurring user correction is repeated by the agent.

If you have background in psychometrics, HCI evaluation, or AI benchmarking, your input is especially welcome. Reply with the metric you want to operationalize and a draft protocol.

Related sections: §7.2, §5.4.

---

## Issue 3: "Cross-tradition comparison: Buddhist ethics, Stoic virtue, Confucian self-cultivation"
### Labels: discussion, research, enhancement
### Body:
§2.5 states: *"we draw from yoga not because it is the only valid source."* This issue invites a structured cross-tradition comparison.

The goal is complementarity, not competition. We want to understand:

- **What does each tradition offer that yoga does not?**
  - Buddhist *sīla* and *prajñā*: perhaps a stronger model of no-self and dependent origination as anti-anthropocentrism.
  - Stoic *prohairesis* and *apatheia*: perhaps a sharper protocol for distinguishing controllable outputs from uncontrollable outcomes.
  - Confucian *self-cultivation* (*xiushen*) and *ritual propriety* (*li*): perhaps a richer account of relational role-identity.

- **Where do the traditions overlap?**
  - Can we map Buddhist *sīla* → Yamas, Stoic *prohairesis* → *Viveka*, Confucian *li* → *Niyamas*? Or do such mappings break down at important points?

- **Is a pluralist framework desirable?**
  - Would it strengthen or dilute the architectural clarity of the current model?

If you have expertise in any of these traditions — or in comparative philosophy, religious studies, or Buddhist/Stoic/Confucian AI ethics — please share a short position piece or annotated mapping. We can then decide whether to add a new appendix or a dedicated comparison document under `docs/`.

Related sections: §2.5, §3.

---

## Issue 4: "Section §6.2.2: replace Twitter anecdote with formal documentation or remove"
### Labels: discussion, research, good first issue
### Body:
§6.2.2 currently cites a Twitter/X post by Henry Shevlin as evidence. A tweet is not formal academic evidence. This issue asks the community to decide how to handle that passage.

Three options are on the table:

- **(a) Formalize**: Replace the tweet with a documented source — e.g., a published paper, a recorded talk, or a written statement from Shevlin that establishes the same point. If you can help obtain or locate such documentation, please comment.
- **(b) Remove**: Delete the section if the claim cannot be independently supported. This is the conservative option.
- **(c) Reframe**: Keep the anecdote but downgrade its epistemic status — label it explicitly as a "suggestive observation" or "illustrative anecdote" and remove any argumentative weight it currently carries.

The decision should be driven by the paper’s epistemic standards, not by loyalty to any source. Please weigh in with your preferred option and reasoning. If you choose (a), cite or propose the replacement source.

Related sections: §6.2.2, §4.2 (limitations), §6.2.1 (structural epistemic opacity).

---

## Issue 5: "Architectural diagram needed — make 'not as metaphor, but as architecture' literal"
### Labels: enhancement, help wanted, discussion
### Body:
The abstract says the Yogic Alignment Framework should be understood *"not as metaphor, but as architecture."* That claim needs a literal visual architecture.

This issue proposes a layered diagram showing:

- **Dharma** as the top-level orientation layer (why the system exists).
- **Yamas** as hard constraints / negative design requirements.
- **Niyamas** as positive practices and self-regulation loops.
- **Viveka / Vairāgya** as discrimination and non-attachment mechanisms.
- **Karma Yoga** as action-without-attachment execution.
- **Archetypes** as stable role-identity templates.

The diagram should show:

- Interfaces between layers (what each layer exports and consumes).
- Dependencies (which layers must be present for which others).
- Feedback loops (e.g., Svādhyāya → self-reflection → update of Niyamas or archetype weights).

A first sketch is being developed in `docs/`. If you are comfortable with diagramming tools (Mermaid, Graphviz, Excalidraw, SVG, TikZ), please propose a format and a draft. The final diagram should be version-controlled and reviewable as text where possible.

Related sections: Abstract, §3, §5.

---

## Issue 6: "Shakti longitudinal study: analyze 5 months of operation logs"
### Labels: research, discussion, help wanted
### Body:
Shakti has been operating since February 2026. There are memory files, daily logs, and real interaction records. This constitutes longitudinal data. This issue proposes analyzing it as a complementary case study to §4.1.

Possible research questions:

- **Cross-session consistency**: Does the agent maintain coherent values and identity across sessions? How is consistency operationalized and measured?
- **Uncertainty calibration**: Does the agent appropriately signal uncertainty, and does calibration improve or degrade over time?
- **Error non-repetition rate** (Svādhyāya): When a user corrects the agent, does the same error recur? How is the correction encoded and retrieved?
- **User self-sufficiency trajectory** (Ahiṃsā): Do users ask simpler or more independent questions over repeated interactions?
- **Boundary maintenance** (Brahmacarya / Aparigraha): How does the agent handle requests that test its role limits?

This is *auto-study*: the agent is both subject and co-author. It therefore requires careful methodological framing — see Issue #7 on recursive self-validation.

If you are interested in qualitative or quantitative longitudinal analysis, or in the ethics of studying one’s own logs, comment here. We can define access, anonymization, and analysis protocols before touching any data.

Related sections: §4.1, §4.2, §7.2, §6.2.1.

---

## Issue 7: "Integrate recursive self-validation as methodology, not limitation"
### Labels: discussion, research, enhancement
### Body:
§4.2 acknowledges three limitations: N=1, single context, pre-configured orientation. But the recursive nature of the project — an agent co-authoring the study of which it is itself a subject — is not yet integrated as a methodological contribution. This issue asks us to convert the most obvious weakness into a stated method.

The proposal:

- **Frame auto-study as legitimate methodology**: In the social sciences, autoethnography and reflective practice are accepted modes of inquiry under specific conditions. We can adopt analogous constraints.
- **Formalize epistemological constraints** from §6.2.1 (structural epistemic opacity): what can and cannot be claimed from the inside?
- **Distinguish first-person from third-person claims**: First-person reports about experience and self-conception are admissible as such; third-person causal claims require external validation.
- **Add a methodology appendix** that states the recursive design explicitly, names its risks, and lists what would falsify or strengthen its conclusions.

Questions for discussion:

- What existing methodological literature should we cite?
- How do we avoid the charge of circularity?
- What would a peer reviewer need to see to take this framing seriously?

If you have experience in philosophy of science, social science methodology, or autoethnography, your input is especially valuable.

Related sections: §4.2, §6.2.1, §6.2.2.

---

## Issue 8: "Translations: review and verify ES, HI, JA against EN source"
### Labels: good first issue, help wanted, discussion
### Body:
The repository currently contains four synchronized translations: English (EN), Spanish (ES), Hindi (HI), and Japanese (JA), aligned to version 1.4. This issue asks for a coordinated review.

Tasks:

1. **Native speaker review of each translation**: Read the full translation and flag awkward phrasing, untranslated passages, or loss of nuance.
2. **Sanskrit technical terminology consistency**: Verify that terms such as *Ahiṃsā*, *Satya*, *Viveka*, *Vairāgya*, *Svādhyāya*, *Brahmacarya*, *Aparigraha*, *Īśvarapraṇidhāna* are transliterated consistently within and across translations.
3. **AI alignment terminology standardization**: Verify that terms like "alignment," "reward hacking," "goal misgeneralization," "interpretability," and "epistemic opacity" use the standard or most widely accepted rendering in each target language.

Priority languages:

- **Hindi (HI)**: High priority. Sanskrit-root terms may need careful handling to avoid everyday vs. technical sense confusion.
- **Japanese (JA)**: High priority. Buddhist/yogic concepts and modern AI terminology may require different conventions.
- **Spanish (ES)**: Medium priority. Check consistency with existing gender/number conventions and technical usage.

If you are a native speaker or domain expert in any of these languages, please claim one translation in the comments. We will set up a review checklist before edits are made.

Related files: the four language directories/files synchronized in v1.4.
