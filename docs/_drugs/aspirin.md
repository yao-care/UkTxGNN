---
layout: default
title: Aspirin
parent: Model Prediction Only (L5)
nav_order: 75
evidence_level: L5
indication_count: 7
drugbank_id: DB00945
monitor_inn: "Acetylsalicylic acid"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "trigeminal autonomic cephalalgia", "thrombophilia"]
last_modified_at: 2026-11-20
description: "Aspirin: predicted new indication Atrophoderma vermiculata (evidence level L5). In the UK: 78 NHSBSA BNF presentation codes"
---

# Aspirin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Aspirin: Atrophoderma vermiculata
{: .text-alpha }

## One-Sentence Summary

Aspirin is a long-established cyclooxygenase inhibitor with antiplatelet activity, marketed in the UK in many single-ingredient products.
The TxGNN model predicts it may be relevant to **atrophoderma vermiculata**, a rare atrophic skin disorder affecting hair follicles.
There are currently **no registered clinical trials and no publications** supporting this prediction, so it rests on the computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Atrophoderma vermiculata |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (78 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 78 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for aspirin and extended - release dipyridamole (a combination product containing aspirin): "Aspirin Aspirin inhibits platelet aggregation by irreversible inhibition of platelet cyclooxygenase and thus inhibits the generation of thromboxane A 2, a powerful inducer of platelet aggregation and vasoconstriction." ([DailyMed: Aspirin And Extended - Release Dipyridamole Capsules, 25 Mg / 200 Mg (aspirin and extended - release dipyridamole) prescribing information, Major Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a6e652e1-b2e4-47ba-bed2-c5e902f8b8f1), label version 2026-08-19; accessed 2026-11-19.) Aspirin is generally known to irreversibly inhibit cyclooxygenase enzymes. This reduces prostaglandin and thromboxane production, which gives it antiplatelet, anti-inflammatory and analgesic effects.

Atrophoderma vermiculata is a rare follicular atrophic skin disorder. The data compiled for this report show no clear mechanistic link between aspirin's COX-inhibition or antiplatelet action and this condition. The high TxGNN score (0.9959) reflects a model-derived association only. Without clinical or literature support, the prediction should be treated as a hypothesis, not as a basis for use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

A selection is shown below. Licence indication text is not recorded in the local data, and the list is not exhaustive.

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0407010B0AAAWAW | Acetylsalicylic acid mixture | Aspirin |
| 0209000A0AAA5A5 | Aspirin 100mg/5ml oral liquid | Aspirin |
| 0407010B0AABCBC | Aspirin 150mg suppositories | Aspirin |
| 0209000A0AABHBH | Aspirin 15mg/5ml oral liquid | Aspirin |
| 0209000A0AABJBJ | Aspirin 225mg/5ml oral liquid | Aspirin |
| 0209000A0AAATAT | Aspirin 25mg capsules | Aspirin |
| 0209000A0AABABA | Aspirin 25mg/5ml oral liquid | Aspirin |
| 0407010B0AAAEAE | Aspirin 300mg dispersible tablets | Aspirin |
| 0407010B0AACCCC | Aspirin 300mg effervescent tablets sugar free | Aspirin |
| 0407010B0AAA3A3 | Aspirin 300mg gastro-resistant tablets | Aspirin |
| 0407010B0AACGCG | Aspirin 300mg modified-release tablets | Aspirin |
| 0407010B0AAANAN | Aspirin 300mg orodispersible tablets sugar free | Aspirin |
| 0407010B0AABEBE | Aspirin 300mg suppositories | Aspirin |
| 0407010B0AAAFAF | Aspirin 300mg tablets | Aspirin |
| 0407010B0AAABAB | Aspirin 300mg/5ml oral liquid | Aspirin |
| 0209000A0AABFBF | Aspirin 30mg/5ml oral liquid | Aspirin |
| 0209000A0AACCCC | Aspirin 37.5mg oral powder sachets | Aspirin |
| 0209000A0AABIBI | Aspirin 37.5mg/5ml oral liquid | Aspirin |
| 0209000A0AACDCD | Aspirin 40mg oral powder sachets | Aspirin |
| 0209000A0AABBBB | Aspirin 40mg/5ml oral liquid | Aspirin |

Showing 20 of 78 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

No licence reviewed for this report lists atrophoderma vermiculata as an approved use.

## Safety Considerations

Specific warning, contraindication and interaction data were not available in the data compiled for this report. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no plausible mechanistic link to aspirin's known pharmacology in the data reviewed. The evidence level is L5, which does not support progressing to clinical or regulatory action.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological rationale linking aspirin to atrophoderma vermiculata
- A systematic literature search for case reports or preclinical studies in this condition
- Dermatology expert review of whether the disorder's pathology could respond to COX inhibition
- Review of the safety profile, including bleeding risk, in the relevant patient population (SmPC and BNF)
- Assessment of route and formulation suitability, for example oral versus topical delivery

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "UK regulatory records returned zero marketing authorisations, which is inconsistent with Aspirin's known presence in the UK market and almos" | No longer present after the report was regenerated (2026-11-16: the report was regenerated in 2026-11 and no longer contains this statement; was: Corrected (revised 2026-11-24; earlier version kept in the record)) | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-24 | Removed: "No marketing authorisation records were returned for Aspirin in this Evidence Pack. This is inconsistent with the known UK market: aspirin-c" | No longer present after the report was regenerated (2026-11-16: the report was regenerated in 2026-11 and no longer contains this statement; was: Corrected (revised 2026-11-24; earlier version kept in the record)) | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "**Re-query MHRA Product Licence database** to populate UK marketing authorisation records" | No longer present after the report was regenerated (2026-11-16: the report was regenerated in 2026-11 and no longer contains this statement; was: Corrected) | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "A re-query against the MHRA Product Licence database is strongly recommended before proceeding" | No longer present after the report was regenerated (2026-11-16: the report was regenerated in 2026-11 and no longer contains this statement; was: Corrected) | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-19 | "Currently, detailed mechanism of action data for this drug is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Aspirin And Extended - Release Dipyridamole Capsules, 25 Mg / 200 Mg (aspirin and extended - release dipyridamole) prescribing information, Major Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a6e652e1-b2e4-47ba-bed2-c5e902f8b8f1) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

