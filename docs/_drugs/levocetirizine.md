---
layout: default
title: Levocetirizine
parent: Model Prediction Only (L5)
nav_order: 372
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Levocetirizine"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
description: "Levocetirizine: predicted new indication Rheumatoid arthritis (evidence level L5). In the UK: 5 NHSBSA BNF presentation codes"
---

# Levocetirizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Levocetirizine: Rheumatoid arthritis
{: .text-alpha }

## One-Sentence Summary

Levocetirizine is a selective histamine H1 receptor antagonist, originally used for allergic rhinitis, vasomotor rhinitis and idiopathic urticaria.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**,
but there are currently **no clinical trials** and **no publications** supporting this direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (5 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Levocetirizine is a selective histamine H1 receptor antagonist. This description is based on the known drug class. According to the Mechanism of Action section of the US FDA-approved prescribing information for levocetirizine: "Levocetirizine, the active enantiomer of cetirizine, is an antihistamine; its principal effects are mediated via selective inhibition of H 1 receptors. The antihistaminic activity of levocetirizine has been documented in a variety of animal and human models." ([DailyMed: Xyzal (levocetirizine dihydrochloride) prescribing information, Chattem, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1673f7ff-0c7c-4403-86cf-c05eb1475222), label version 2025-07-22; accessed 2026-11-19.) Its efficacy in allergic and urticarial conditions comes from blocking histamine-driven symptoms.

Histamine is present in rheumatoid synovium and may contribute to vascular permeability and inflammatory signalling. This gives a plausible but unproven link between H1 blockade and rheumatoid arthritis.

The very high TxGNN score (0.9973) is a model prediction only. Allergic conditions and rheumatoid arthritis are quite different diseases, and no studies were identified to show that H1 antagonism alters the course of rheumatoid arthritis. The prediction should be treated as a hypothesis for further investigation.

*Other lower-ranked predictions (colobomatous microphthalmia-rhizomelic dysplasia syndrome, score 0.9959; brachydactyly-syndactyly syndrome, score 0.9952) have no plausible mechanistic link. They are congenital developmental disorders that an antihistamine would not be expected to correct. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.*

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0304010ACAAABAB | Levocetirizine 500micrograms/ml oral solution sugar free | Levocetirizine |
| 0304010ACAAACAC | Levocetirizine 5mg orodispersible tablets sugar free | Levocetirizine |
| 0304010ACAAAAAA | Levocetirizine 5mg tablets | Levocetirizine |
| 0304010ACBBABAB | Xyzal 0.5mg/ml oral solution | Levocetirizine |
| 0304010ACBBAAAA | Xyzal 5mg tablets | Levocetirizine |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The identifier shown is in a non-PL format and should be checked against the MHRA register. The BNF classification (antihistamines, respiratory system chapter) and any NICE-appraised indications should be verified directly.

<!-- review:begin uk-lic-20261106-levocetirizine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The compiled data lists one valid single-ingredient authorisation. The identifier shown is in a non-PL format and should be checked against the MHRA register." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. The Quick Overview and the BNF code table under UK Market Information show the current number of BNF presentation codes. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-levocetirizine-1 -->

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease relationships, not label text): kidney disease, pyoureter, chronic kidney disease, chronic renal failure syndrome, end-stage renal failure. Renal impairment is a recognised consideration for levocetirizine dosing and should be checked against the SmPC.
- **Drug Interactions**: 100 interactions were identified. The examples reviewed are mostly of moderate severity, with central nervous system depressant or additive sedative effects being the most likely concern. Main examples:
  - Opioids and related agents: morphine (including liposomal), fentanyl, dihydrocodeine, opium, loperamide, diphenoxylate, difenoxin
  - Other sedating agents: ethanol, promethazine, chlorpheniramine, dronabinol, nabilone
  - Others: bupropion, metoclopramide, sibutramine, histamine, radioactive iodide (I-123, I-131)
  - Minor: hyaluronidase

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for rheumatoid arthritis is supported only by a computational score. There are no clinical trials or publications, and the mechanistic link is speculative. The evidence is not sufficient to justify moving forward.

**To proceed, the following is needed:**
- Detailed mechanism of action data for levocetirizine
- A systematic literature search on histamine and H1 antagonism in rheumatoid arthritis, including preclinical and observational studies
- Confirmation of the approved indication, dosage form and authorisation details for the UK products from the MHRA register and SmPC
- Review of warnings and contraindications from the SmPC and BNF, with particular attention to renal impairment
- If preclinical rationale emerges, a proof-of-concept study design with appropriate safety monitoring

<!-- review:begin uk-lic-20261124c-levocetirizine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Confirmation of the approved indication, dosage form and authorisation details for the UK product from the MHRA register and SmPC" Corrected wording only: the text referred to a single UK product, licence or authorisation record, or called the UK market data licence or authorisation data. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902), which lists more than one BNF presentation code for this drug; these are NHS prescribing codes, not MHRA licences, and they carry no indication text. The phrase was changed to the plural or to BNF prescribing codes; the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124c-levocetirizine-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "The compiled data lists one valid single-ingredient authorisation" | Corrected (revised 2026-11-24; earlier version kept in the record) | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-20 | "Detailed mechanism of action data is not available in the data compiled for this report, so this description is based on the known drug class" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: Xyzal (levocetirizine dihydrochloride) prescribing information, Chattem, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1673f7ff-0c7c-4403-86cf-c05eb1475222) |
| 2026-11-24 | Corrected: "Confirmation of the approved indication, dosage form and authorisation details for the UK product from the MHRA register and SmPC" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

