---
layout: default
title: Etilefrine
parent: Model Prediction Only (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
---

# Etilefrine
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

# Etilefrine: From Unrecorded Original Indication to Alopecia (Predicted)

## One-Sentence Summary

> Etilefrine (DrugBank DB08985) has no recorded original indication or mechanism-of-action data in this evidence pack.
> The TxGNN model's top prediction across a batch of 10 candidates is **Alopecia**, with a score of **97.61%**,
> but this is supported by **zero clinical trials and zero publications**, and the pack's own rationale flags the mechanism as running in the *opposite* direction to established hair-growth therapy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no licences or indication text on file |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 97.61% |
| Evidence Level | L5 (model prediction only, no trials or literature) |
| UK Market Status | Not marketed (per pack: 0 marketing authorisations on file) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). No original indication is recorded either, so the usual comparison between original and predicted indication cannot be made from the pack's data.

What the pack does provide is the model's own repurposing rationale, and it argues **against** biological plausibility rather than for it: established hair-loss therapy (e.g. minoxidil) works by vasodilation and potassium-channel opening to increase follicular blood flow, whereas Etilefrine is a sympathomimetic agent that acts as a vaso**constrictor**. The rationale explicitly describes this as a mechanistic mismatch, with no known physiological pathway supporting benefit in alopecia, and no trial or literature evidence to counter that concern.

This pattern repeats across the other nine candidates in this batch (see table below) — several show the same kind of directional mismatch (e.g. the drug would be expected to worsen benign prostatic hyperplasia and is contraindicated in phaeochromocytoma/paraganglioma), reinforcing that this batch's high TxGNN scores likely reflect knowledge-graph node proximity (shared adrenergic-receptor pathway) rather than genuine therapeutic potential.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications Reviewed in This Batch

For transparency, the other nine candidates generated alongside the top prediction are summarised below. All carry evidence level L5 (no trials, no literature).

| Rank | Predicted Indication | TxGNN Score | Recommendation | Note |
|---|---|---|---|---|
| 2 | Hypotrichosis simplex of the scalp | 97.52% | Hold | Monogenic follicular defect; no plausible mechanistic link |
| 3 | Congenital hypotrichosis milia | 97.41% | Hold | Ectodermal developmental disorder; no plausible link |
| 4 | Diffuse alopecia areata | 97.07% | Hold | Autoimmune pathology; no plausible link |
| 5 | Benign prostatic hyperplasia | 96.65% | Hold | α1-agonist would worsen, not treat, BPH — directional mismatch |
| 6 | Osteoarthritis | 96.11% | Hold | No known pathway link |
| 7 | Headache disorder | 95.54% | Research Question | Plausible only for hypotension-related headache subtype; too non-specific |
| 8 | Phaeochromocytoma | 95.27% | Hold | Adrenergic agonism is contraindicated in catecholamine-secreting tumours |
| 9 | Sympathetic paraganglioma | 95.08% | Hold | Same contraindication concern as phaeochromocytoma |
| 10 | Trigeminal autonomic cephalalgia | 94.89% | Research Question | Vasoconstrictive mechanism has some precedent (cf. triptans), but no supporting data |

## UK Market Information

No marketing authorisations are recorded for Etilefrine in this evidence pack (market status: not marketed; total licences: 0). No product name, dosage form, or approved indication text is available to extract.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: the pack flags product-label warnings/contraindications as a Blocking data gap — see Conclusion.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 across the entire batch — a model prediction alone, with no clinical trials or literature identified in 31 logged source queries. For the top candidate (alopecia), the pack's own mechanistic rationale argues the drug's vasoconstrictive action runs counter to the vasodilatory mechanism of established hair-loss therapy, undermining rather than supporting the prediction.
- A Blocking-severity data gap (product label warnings/contraindications) means this candidate cannot even enter initial safety screening (S1) yet.

**To proceed, the following is needed:**
- Product label warnings and contraindications (Blocking gap, DG001) — required before any safety screening can begin
- Confirmed mechanism of action (High-severity gap, DG002)
- Any preclinical or pharmacological data specifically linking adrenergic agonism to hair follicle biology, to test the mechanistic mismatch flagged above
- Given the batch-wide pattern (no evidence, several directional mismatches), consider deprioritising this drug for repurposing screening pending stronger signal from an updated TxGNN run or new literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

