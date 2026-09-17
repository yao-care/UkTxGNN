---
layout: default
title: Disopyramide
parent: Model Prediction Only (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Disopyramide
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

# Disopyramide: From Cardiac Arrhythmia to Tourette Syndrome

## One-Sentence Summary

Disopyramide is a Class Ia sodium-channel blocking antiarrhythmic (with additional anticholinergic activity), historically used for ventricular and atrial arrhythmias. The TxGNN model predicts it may be effective for **Tourette syndrome**, but this is a **score-only prediction (99.86%) with zero supporting clinical trials or literature**, and the model's own mechanistic assessment flags it as a likely spurious association rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cardiac arrhythmias (Class Ia antiarrhythmic) — not formally captured in the evidence pack's regulatory fields |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data was not returned by DrugBank for this evidence pack (flagged as a High-severity data gap, DG002). Based on the pharmacological class information embedded in the evidence pack's own rationale fields, disopyramide is a Class Ia sodium-channel blocker with anticholinergic properties, used to suppress ventricular and atrial tachyarrhythmias by prolonging the cardiac refractory period.

For the top-ranked prediction, Tourette syndrome, the evidence pack's own mechanistic assessment is explicit and should be read carefully: there is **no known biological link** between sodium-channel blockade/anticholinergic activity and the dopaminergic–striatal pathology underlying Tourette syndrome. The evidence pack itself characterises this as a possible spurious association arising from the TxGNN knowledge-graph embedding, not a pharmacologically grounded hypothesis. A high similarity score alone is not sufficient grounds to proceed — that is why the recommendation attached to this prediction is "Hold" despite the score being one of the highest in the candidate set.

It is worth noting that two lower-ranked candidates in this evidence pack are mechanistically more coherent: **idiopathic neonatal atrial flutter** (rank 7, L4) and **multifocal atrial tachycardia** (rank 9, L4, supported by one case-series publication) both fall within the same arrhythmia pathology class that disopyramide is already used to treat, and are flagged as "Research Question" rather than "Hold". These may warrant separate follow-up outside the scope of this report, which is scoped to the rank-1 candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Disopyramide currently holds **no MHRA marketing authorisations** in this evidence pack (0 licences recorded; market status: Not marketed). No product, dosage form, or approved-indication data is available to tabulate.

---

## Safety Considerations

Key warnings, contraindications, and drug–drug interaction data were not returned in this evidence pack (DG001, a Blocking-severity gap preventing initial safety screening). Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The rank-1 prediction (Tourette syndrome) has no clinical trials, no literature, and the evidence pack's own mechanistic review found no plausible pharmacological link — this is an L5, model-only signal. Combined with the drug's unmarketed status in the UK and a blocking gap in safety/contraindication data, there is no basis to progress this candidate beyond hypothesis stage.

**To proceed, the following is needed:**
- SmPC-derived warnings, contraindications, and DDI data (currently blocking — DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- An independent pharmacological plausibility review of the dopaminergic/movement-disorder pathway before any preclinical or literature-search investment
- If pursued further, consider redirecting evidence-gathering effort toward the mechanistically coherent candidates in this pack (idiopathic neonatal atrial flutter, multifocal atrial tachycardia) rather than the rank-1 signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

