---
layout: default
title: Epinastine
parent: Model Prediction Only (L5)
nav_order: 253
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Epinastine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis"
monitor_inn: "Epinastine"
predicted_indications: ["rosacea conjunctivitis", "allergic urticaria"]
---

# Epinastine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Epinastine: From Atopic Conjunctivitis to Rosacea Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Epinastine is a topical H1 antihistamine with mast cell stabilising activity, originally used for allergic eye conditions such as atopic, papillary and vernal conjunctivitis.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**, but **no clinical trials and no publications** were found for this indication, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis (no approved indication text is available for the UK products) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (2 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 |
| Recommended Decision | Hold |

<!-- review:begin uk-lic-20261124c-epinastine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Original Indication / Atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis (no approved indication text is available for the UK licence)" Corrected wording only: the text referred to a single UK product, licence or authorisation record, or called the UK market data licence or authorisation data. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902), which lists more than one BNF presentation code for this drug; these are NHS prescribing codes, not MHRA licences, and they carry no indication text. The phrase was changed to the plural or to BNF prescribing codes; the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124c-epinastine-1 -->

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for epinastine: "Epinastine is a topically active, direct H 1 -receptor antagonist and an inhibitor of the release of histamine from the mast cell. Epinastine is selective for the histamine H 1 -receptor and has affinity for the histamine H 2 -receptor." ([DailyMed: epinastine hydrochloride prescribing information, Somerset Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d4ee45c-e58f-4b7c-b389-898f5c27f54d), label version 2025-03-22; accessed 2026-11-19.) Based on known information, epinastine is a topical H1 receptor antagonist (the target is the histamine H1 receptor, HRH1) with mast cell stabilising activity. Its efficacy in allergic conjunctivitis is established, and the eye drops are used to treat itching associated with allergic conjunctivitis.

The link to rosacea conjunctivitis is weak. Rosacea-associated ocular inflammation is driven mainly by meibomian gland dysfunction, innate immune activation and microbial or *Demodex* factors, not classic IgE-mediated histamine release. The high TxGNN score most likely reflects network proximity to other conjunctivitis terms rather than a shared disease mechanism. At best, epinastine might relieve an allergic or itch component.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for rosacea conjunctivitis.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1104020ACAAAAAA | Epinastine 500micrograms/ml eye drops | Epinastine hydrochloride |
| 1104020ACBBAAAA | Relestat 0.5mg/ml eye drops | Epinastine hydrochloride |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Note: the identifier above is as recorded in the compiled data and is not in standard MHRA "PL" format. It should be verified against the MHRA register. Dosage form is inferred from the product name. NICE appraisal and BNF classification details were not available.

## Safety Considerations

- **Drug Interactions**: The only interaction record is a pharmacology entry (epinastine acting on the H1 receptor, its intended target). No drug-drug interactions with severity grading were identified.

Please refer to the SmPC and BNF for warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by model score only (L5), with no trials or publications, and the biology of rosacea-related ocular disease does not fit an antihistamine well. Other predicted indications, such as allergic urticaria (L3, review and histamine skin-test data) and cold urticaria (L4, class-level evidence), have stronger mechanistic rationale, though these would require systemic rather than eye-drop use and are outside the current UK ophthalmic product.

**To proceed, the following is needed:**
- Confirmation of the approved indication, dosage form and authorisation number from the MHRA register and SmPC
- Mechanism of action data (for example from DrugBank)
- Warnings and contraindications from the SmPC/BNF, as safety screening cannot proceed without them
- Any clinical or exploratory studies of epinastine in ocular rosacea or meibomian gland dysfunction
- If broader repurposing is of interest, a focused review of urticaria evidence, noting that no systemic UK formulation is identified in the compiled data

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: epinastine hydrochloride prescribing information, Somerset Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d4ee45c-e58f-4b7c-b389-898f5c27f54d) |
| 2026-11-24 | Corrected: "&#124; Original Indication &#124; Atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis (no approved indication text is available for the UK licence) &#124;" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

