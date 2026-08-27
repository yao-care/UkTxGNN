---
layout: default
title: Clobazam
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Clobazam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using the report template exactly as specified in your prompt (no additional skill applies to this task — it's a direct data-to-markdown transformation per your detailed spec). A few notes before the report:

- `taiwan_regulatory.licenses` is empty (0 UK marketing authorisations), so the UK Market Information table is replaced with a one-line statement per the "omit empty sections" rule.
- `original_indications` and `original_moa` are both empty/`[Data Gap]` in this pack. Per the fallback rule for missing MOA, I've stated Clobazam's original indication using its well-established pharmacological classification (benzodiazepine anticonvulsant/anxiolytic) rather than fabricating specific trial data.
- Clobazam is not an antineoplastic agent, so the Cytotoxicity section is omitted entirely.
- The evidence pack's `recommendation` field for rank-1 ("Research Question") doesn't map directly to the required Go/Hold/Proceed with Guardrails scale — given L4 evidence (case series only, no RCTs), a Blocking safety data gap (DG001), and zero UK marketing authorisations, I mapped this to **Hold**.

---

# Clobazam: From Epilepsy (Adjunctive Therapy) to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Clobazam is a 1,5-benzodiazepine anticonvulsant, established as adjunctive therapy for epilepsy (including Lennox-Gastaut syndrome) and for anxiety disorders. The TxGNN model predicts it may be effective for **febrile infection-related epilepsy syndrome (FIRES)**, but this direction is currently supported by only **0 clinical trials** and **2 publications** (both case series involving related GABA-ergic agents, not clobazam itself).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (adjunctive anticonvulsant therapy, e.g. Lennox-Gastaut syndrome); anxiety disorders *(based on established drug classification — no licence data available in this evidence pack)* |
| Predicted New Indication | Febrile infection-related epilepsy syndrome (FIRES) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, clobazam is a 1,5-benzodiazepine that acts as a positive allosteric modulator of the GABA-A receptor, enhancing inhibitory neurotransmission and suppressing abnormal cortical excitability. Its efficacy as an adjunctive anticonvulsant in focal and generalised epilepsies, including refractory syndromes, is well established.

FIRES is a severe, treatment-resistant form of new-onset refractory status epilepticus that typically requires prolonged pharmacological coma with GABA-ergic anaesthetics (e.g. midazolam) to control seizures. Because clobazam shares the same GABA-A receptor mechanism as the agents used acutely in FIRES, there is a plausible pharmacological rationale for its use as a maintenance or step-down anticonvulsant once patients are being weaned from anaesthetic coma.

However, the available literature does not evaluate clobazam directly in FIRES — the two retrieved publications discuss enteral lorazepam and perampanel, not clobazam, as weaning or adjunctive strategies. The mechanistic link is therefore indirect (drug-class analogy) rather than drug-specific evidence, which is why this prediction remains at evidence level L4.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Case series | Epileptic Disorders | Enteral lorazepam (a related GABA-ergic benzodiazepine) was an effective weaning strategy in midazolam-dependent FIRES patients, supporting the broader rationale for benzodiazepine step-down therapy in this condition. |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case report | Cureus | Perampanel reduced barbiturate dependency in a paediatric FIRES case, illustrating that non-anaesthetic adjunctive anticonvulsants can play a role in weaning protocols, though this does not directly involve clobazam. |

## UK Market Information

Clobazam currently holds **no UK marketing authorisation** on record in this evidence pack (0 licences; market status: Not Marketed). Prescribers should verify current MHRA/electronic Medicines Compendium (eMC) status directly, as products (e.g. Frisium) may be available via named-patient or specialist import routes even where standard marketing authorisation data is not captured here.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: this evidence pack flags a Blocking data gap — MHRA warnings/contraindications data was not available — which by itself is sufficient to prevent a preliminary safety assessment (S1) for this candidate.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently limited to mechanistic rationale and drug-class analogy (L4) — no clinical trials and no publications directly evaluating clobazam in FIRES exist. Combined with the absence of a UK marketing authorisation and a Blocking-severity gap in MHRA safety data (warnings/contraindications), this candidate is not ready to proceed past the research-question stage.

**To proceed, the following is needed:**
- MHRA SmPC/PIL retrieval for clobazam warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism of action data from DrugBank or equivalent source
- Drug-specific clinical evidence (case series, cohort study, or trial) evaluating clobazam — not just related benzodiazepines — in FIRES
- Regulatory pathway assessment given current "Not Marketed" status in the UK
- Consider prioritising higher-evidence candidates identified in the same evidence pack — notably **benign occipital epilepsy** (evidence level L2, supported by multiple Cochrane systematic reviews and direct clobazam literature, recommendation: Proceed with Guardrails), which may represent a more actionable near-term repurposing direction for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

