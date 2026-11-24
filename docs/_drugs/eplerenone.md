---
layout: default
title: Eplerenone
parent: Model Prediction Only (L5)
nav_order: 254
evidence_level: L5
indication_count: 4
monitor_inn: "Eplerenone"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome"]
last_modified_at: 2026-11-24
description: "Eplerenone: predicted new indication Pulmonary hypertension with unclear multifactorial mechanism (evidence level L5). Approved use: Hypertension"
---

# Eplerenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Eplerenone: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism
{: .text-alpha }

## One-Sentence Summary

Eplerenone is a selective mineralocorticoid receptor antagonist.
The TxGNN model predicts it may be useful for **pulmonary hypertension with unclear multifactorial mechanism**, but **no clinical trials and no publications** specifically support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (a relation recorded in the knowledge graph; no licence indication text is available) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 0.9950 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (4 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Eplerenone blocks the mineralocorticoid receptor (MR), the target of aldosterone. Aldosterone/MR signalling is linked to vascular remodelling, fibrosis and inflammation. According to the Mechanism of Action section of the US FDA-approved prescribing information for eplerenone: "Eplerenone binds to the mineralocorticoid receptor and blocks the binding of aldosterone, a component of the renin-angiotensin-aldosterone-system (RAAS). Aldosterone synthesis, which occurs primarily in the adrenal gland, is modulated by multiple factors, including angiotensin II and non-RAAS mediators such as adrenocorticotropic hormone (ACTH) and potassium." ([DailyMed: Inspra (eplerenone) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1a52bedc-8e2c-4116-a296-a87770676b4a), label version 2025-06-23; accessed 2026-11-19.) This description is a general inference.

Eplerenone is linked with hypertension, which is systemic blood-pressure disease. Pulmonary hypertension is a disease of the lung circulation. The two share a vascular element, and MR-driven remodelling could plausibly matter in both. This is a general mechanistic argument, not demonstrated evidence.

The very high TxGNN score (0.9950) is a computational prediction. The disease label "unclear multifactorial mechanism" is also broad, which makes a specific mechanistic argument harder. No similarity analysis between the original and predicted indications has been completed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0202030X0AAAAAA | Eplerenone 25mg tablets | Eplerenone |
| 0202030X0AAABAB | Eplerenone 50mg tablets | Eplerenone |
| 0202030X0BBAAAA | Inspra 25mg tablets | Eplerenone |
| 0202030X0BBABAB | Inspra 50mg tablets | Eplerenone |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The dosage form and approved indication text are not recorded in the data compiled for this report. Please check the current SmPC and BNF entry for licensed indications.

<!-- review:begin uk-lic-20261106-eplerenone-1 -->

> **Review correction (2026-11-24)**: Originally stated: "This is a single-ingredient product with valid status. The dosage form and approved indication text are not recorded in the data compiled for this report." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. The Quick Overview and the BNF code table under UK Market Information show the current number of BNF presentation codes. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-eplerenone-1 -->

---

## Safety Considerations

- **Contraindication-type relations recorded in the knowledge graph** (not taken from label text): liver disease, gallbladder disease, diabetic nephropathy, and impaired renal function disease. Hyperkalaemia risk in renal impairment is a particular consideration.
- **Drug Interactions** (DDInter; 100 interactions in total, 20 reviewed here):
  - **Major**: aprepitant, clarithromycin, clotrimazole, potassium chloride, potassium citrate, potassium bicarbonate.
  - **Moderate**: corticosteroids (hydrocortisone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), acetylsalicylic acid, bupropion, miconazole, dronabinol, nabilone.

Label warnings and contraindications were not available for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials or publications on this disease entry, so the evidence level is L5. Safety concerns include renal impairment and potassium-raising interactions.

**To proceed, the following is needed:**
- A focused literature review for pulmonary hypertension and MR antagonists. A separately listed prediction, pulmonary hypertension owing to lung disease and/or hypoxia, has mainly preclinical papers. These do not directly support this prediction and would need individual appraisal.
- Clarification of which pulmonary hypertension subtype is meant, given the broad "unclear multifactorial mechanism" label.
- Detailed mechanism-of-action data and label-based warnings and contraindications.
- Licensed indication and dosage form details for the UK products.
- A safety plan covering potassium and renal function monitoring and the major interactions above.

<!-- review:begin uk-lic-20261124c-eplerenone-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Licensed indication and dosage form details for the UK authorisation." Corrected wording only: the text referred to a single UK product, licence or authorisation record, or called the UK market data licence or authorisation data. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902), which lists more than one BNF presentation code for this drug; these are NHS prescribing codes, not MHRA licences, and they carry no indication text. The phrase was changed to the plural or to BNF prescribing codes; the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124c-eplerenone-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "This is a single-ingredient product with valid status" | Corrected (revised 2026-11-24; earlier version kept in the record) | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-19 | "Detailed mechanism-of-action data were not available for this report, so t" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Inspra (eplerenone) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1a52bedc-8e2c-4116-a296-a87770676b4a) |
| 2026-11-24 | Corrected: "Licensed indication and dosage form details for the UK authorisation." | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

