---
layout: default
title: Cycloserine
parent: Model Prediction Only (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Cycloserine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Cycloserine: From Tuberculosis to Irritable Bowel Syndrome

## One-Sentence Summary

Cycloserine is a second-line antibiotic used mainly for multidrug-resistant tuberculosis (MDR-TB). The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome**, with a very high prediction score of **99.95%**, but currently **no clinical trials and no published literature** support this specific link — the prediction is model-driven only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis, particularly multidrug-resistant TB (based on evidence-pack rationale text; no formal UK licence data available — see below) |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the regulatory registry for this drug (flagged as a High-severity data gap). Based on information available elsewhere in the evidence pack, cycloserine is a second-line anti-tuberculosis antibiotic that inhibits bacterial cell-wall synthesis (D-alanine racemase/ligase inhibition), and its D-isomer also acts centrally as an NMDA receptor glycine-site partial agonist.

Its efficacy in MDR-TB is well established. However, no mechanistic or clinical connection between this profile and irritable bowel syndrome — a gut-brain axis / visceral hypersensitivity disorder — has been identified in the trials or literature reviewed. The evidence pack's own rationale explicitly flags this: the TxGNN score is extremely high (99.95%) yet is entirely unsupported by trial or publication evidence, and should be treated as a potential knowledge-graph artefact rather than a genuine pharmacological signal. The same pattern (very high score, zero supporting evidence, no mechanistic rationale) recurs across most of the other top-10 predictions for this drug (acne, gastroparesis, conjunctivitis, pharyngitis, nasal cavity disease, acute laryngopharyngitis, postgastrectomy syndrome, rhinitis), suggesting a possible model clustering bias around antimicrobial/mucosal-disease nodes that warrants separate methodological review.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Cycloserine currently holds no UK marketing authorisations (market status: **not marketed**, total licences: **0**). No dosage form or product information is available for the UK market.

---

## Safety Considerations

No structured warnings, contraindications, or interaction data are currently available in the registry for cycloserine (flagged as a Blocking-severity data gap — TFDA/SmPC label data has not yet been obtained). Please refer to the SmPC and BNF for safety information once available. Report suspected adverse reactions via the Yellow Card Scheme.

**Note:** literature identified during evidence review for a separate, unrelated candidate indication (insomnia) describes cycloserine-induced insomnia and psychosis in a patient treated for MDR-TB (PMID 36712725), consistent with cycloserine's known CNS/neuropsychiatric adverse effect profile (dose-related seizures, psychosis, confusion, sleep disturbance). This should be considered when evaluating any centrally active repurposing candidate for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (irritable bowel syndrome) has an Evidence Level of L5 — a high TxGNN score with no supporting clinical trials or literature — and no plausible mechanistic link has been established. Cycloserine is also not currently marketed in the UK, and critical safety data (SmPC warnings/contraindications, confirmed MOA) remain outstanding, which blocks even a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA/SmPC warning and contraindication data (currently a Blocking gap)
- Confirmed mechanism-of-action data via DrugBank (currently a High-severity gap)
- Dedicated mechanistic or preclinical studies linking cycloserine to gut-brain axis pathophysiology, since none currently exist
- A methodological review of whether the cluster of unsupported high-scoring predictions (IBS, acne, gastroparesis, and the ENT/mucosal-disease group) reflects a genuine signal or a knowledge-graph co-occurrence artefact
- If pursuing repurposing in the UK at all, a new marketing authorisation pathway, since the drug is not currently licensed here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

