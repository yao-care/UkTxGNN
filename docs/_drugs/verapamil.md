---
layout: default
title: Verapamil
parent: Model Prediction Only (L5)
nav_order: 611
evidence_level: L5
indication_count: 7
---

# Verapamil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Verapamil: From Cardiac Arrhythmia/Hypertension to Obsolete Bundle Branch Block

## One-Sentence Summary

Verapamil is a Class IV calcium-channel blocker traditionally used in cardiovascular disease (arrhythmia and hypertension); detailed original indication and mechanism-of-action data were not supplied in this Evidence Pack. TxGNN's top-ranked prediction, **Obsolete Bundle Branch Block**, is scored at **99.62%** but carries **no supporting clinical trials or literature**, and the Evidence Pack's own mechanistic analysis suggests this high score likely reflects a known **safety risk** (worsening of AV conduction) rather than a genuine therapeutic opportunity. Across all seven candidate indications in this pack, evidence remains weak (L4–L5), and only one candidate reaches a "Research Question" stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not separately specified in the Evidence Pack; rationale text identifies verapamil as an approved Class IV (L-type calcium-channel blocker) antiarrhythmic, also used as an antihypertensive |
| Predicted New Indication | Obsolete Bundle Branch Block |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for verapamil could not be extracted from this Evidence Pack (flagged as a High-severity data gap). However, the rationale accompanying the top prediction supplies relevant pharmacological context: verapamil is a Class IV calcium-channel blocker known to suppress atrioventricular (AV) nodal conduction and prolong the PR interval.

Critically, this pharmacology argues **against**, not for, the top-ranked prediction. In patients with bundle branch block — particularly bifascicular block — verapamil's AV-nodal suppression carries a risk of precipitating complete heart block. The Evidence Pack's own analysis concludes that the high TxGNN score most likely reflects a "verapamil–cardiac conduction system" co-occurrence within the knowledge graph rather than a genuine treatment association. In other words, the model may be capturing a **contraindication signal**, not a repurposing opportunity, and no clinical trials or publications were retrieved to support therapeutic use.

Among the remaining candidates, rank 2 (malignant renovascular hypertension) has a somewhat more plausible — though still weak — rationale, since verapamil is an established antihypertensive and could theoretically contribute to blood pressure control in severe hypertension. However, calcium-channel blockers are not first-line therapy where renal artery stenosis is present (ACE inhibitors/ARBs or revascularisation are preferred), and the two literature items retrieved discuss renovascular hypertension generally without directly evaluating verapamil.

---

## Other Predicted Indications Considered

This Evidence Pack ranks seven candidate indications for verapamil. For transparency, all are summarised below, as the top-ranked candidate (above) is flagged as a likely safety signal rather than a therapeutic lead.

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|-------------|-----------------|-----------------|------|
| 1 | Obsolete bundle branch block | 99.62% | L5 | Hold | Mechanistically a safety warning, not a benefit signal |
| 2 | Malignant renovascular hypertension | 99.27% | L4 | Research Question | CCBs are not first-line where renal artery stenosis is present |
| 3 | Malignant hypertensive renal disease | 99.27% | L5 | Hold | No trials or literature |
| 4 | Pulmonary hypertension, unclear multifactorial mechanism | 99.26% | L5 | Hold | Weak theoretical basis; verapamil rarely used in PAH |
| 5 | Pulmonary hypertension owing to lung disease/hypoxia | 99.26% | L5 | Hold | Guidelines advise **against** CCBs in this group (Group 3 PH); literature retrieved is generic hypoxia biology, not verapamil-specific |
| 6 | Braddock syndrome | 99.15% | L5 | Hold | Rare genetic disorder with no known mechanistic link |
| 7 | Periodic paralysis with transient compartment-like syndrome | 99.08% | L5 | Hold | No supporting evidence |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Verapamil is currently **not marketed** in the UK under this Evidence Pack's data, with no marketing authorisations on record (0 licences). No product, dosage form, or approved indication data is available for extraction.

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug interactions) were not available in this Evidence Pack. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Separately, note that the mechanistic analysis underlying the top prediction (Obsolete Bundle Branch Block) flags a **potential AV-conduction risk** with verapamil in patients with bundle branch block — this is a pharmacological caution derived from the repurposing rationale, not from a formal warnings/contraindications database, and should be verified against the current SmPC.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence across all seven predicted indications is weak (L4–L5), with no clinical trials and only tangential literature. The top-ranked prediction is more consistent with a known cardiac safety risk than a therapeutic opportunity, and the drug has no current UK marketing authorisation on record. Only one candidate (malignant renovascular hypertension) reaches a "Research Question" stage, and even that lacks verapamil-specific evidence.

**To proceed, the following is needed:**
- MHRA-approved SmPC warnings and contraindications (currently a blocking data gap preventing formal safety screening)
- Confirmed mechanism-of-action data via DrugBank
- Verapamil-specific literature and/or preclinical data for malignant renovascular hypertension, the only candidate currently at Research Question stage
- Clarification of current UK marketing/licensing status for verapamil products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

