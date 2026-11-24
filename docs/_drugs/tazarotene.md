---
layout: default
title: Tazarotene
parent: Model Prediction Only (L5)
nav_order: 595
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Tazarotene"
predicted_indications: ["seborrheic dermatitis", "seborrheic keratosis", "vulvar inverted follicular keratosis"]
description: "Tazarotene: predicted new indication Seborrheic dermatitis (evidence level L5). In the UK: 4 NHSBSA BNF presentation codes"
---

# Tazarotene
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

## Tazarotene: Seborrheic dermatitis
{: .text-alpha }

## One-Sentence Summary

Tazarotene is a topical retinoid, originally used to treat psoriasis, parapsoriasis and acne.
The TxGNN model predicts it may be effective for **seborrhoeic dermatitis**, but there are currently **no clinical trials** and **no publications** supporting this specific prediction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 0.9979 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (4 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for tazarotene: "Tazarotene is a retinoid prodrug which is converted to its active form, the carboxylic acid of tazarotene, by deesterification. Tazarotenic acid binds to all three members of the retinoic acid receptor (RAR) family: RARα, RARβ, and RARγ, but shows relative selectivity for RARβ, and RARγ and may modify gene expression." ([DailyMed: Tazorac (tazarotene) prescribing information, Almirall, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e4e4b81-420e-4492-8a74-80b692a80057), label version 2026-11-04; accessed 2026-11-19.) Based on general pharmacology, tazarotene is a topical retinoid prodrug that is converted to tazarotenic acid. This binds selectively to retinoic acid receptors beta and gamma (RARβ and RARγ), normalising keratinocyte differentiation and reducing hyperproliferation and inflammation.

These effects are relevant to psoriasis and acne, and could plausibly help with the scaling and inflammatory component of seborrhoeic dermatitis. However, that condition is also driven by *Malassezia* yeast colonisation and the skin's inflammatory response to it, which retinoid activity does not directly address. The very high TxGNN score is a computational prediction only, so the mechanistic link is inferred rather than demonstrated. Topical retinoid irritation (redness, peeling) could also aggravate a condition that commonly affects sensitive facial skin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for seborrhoeic dermatitis.

*Other predicted indications (for context):*
- **Seborrhoeic keratosis** (TxGNN score 0.9951, evidence level L4): a 2023 systematic review of topical treatments for seborrhoeic keratoses ([PMID 36215682](https://pubmed.ncbi.nlm.nih.gov/36215682/)) and a 2004 comparative study of cryosurgery versus topical calcipotriene, tazarotene and imiquimod ([PMID 15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/)) provide indirect evidence. Only titles and short abstracts were available, so the tazarotene-specific results need confirming from the full texts. This is best treated as a research question.
- **Vulvar inverted follicular keratosis** (TxGNN score 0.9938, evidence level L5): no trials or literature. A retinoid effect is speculative, and local irritation on thin genital skin is a particular concern.

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1305020T0AAAAAA | Tazarotene 0.05% gel | Tazarotene |
| 1305020T0AAABAB | Tazarotene 0.1% gel | Tazarotene |
| 1305020T0BBAAAA | Zorac 0.05% gel | Tazarotene |
| 1305020T0BBABAB | Zorac 0.1% gel | Tazarotene |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Manufacturer and approved indication text are not available in the data compiled for this report, so the UK licensed indications should be checked against the current SmPC and BNF.

<!-- review:begin uk-lic-20261106-tazarotene-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The authorisation is recorded as a single-ingredient product with valid status. Manufacturer and approved indication text are not available in the data compiled for this report, so the UK licensed indications should be checked against the current SmPC and BNF." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. The Quick Overview and the BNF code table under UK Market Information show the current number of BNF presentation codes. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-tazarotene-1 -->

---

## Safety Considerations

- **Knowledge-graph contraindications** (not label text): photoparoxysmal response, photosensitivity disease and sunburn.
- **Drug interactions:** 25 potential interactions were identified, none with an assigned severity level. Those listed include doxycycline, minocycline, adapalene, tretinoin, omeprazole, cetirizine, montelukast, fluticasone, salbutamol, citalopram, levothyroxine, rofecoxib, hydroxyzine, diclofenac, etodolac, duloxetine, clobetasol, tacrolimus, cyclobenzaprine and doxepin. Concurrent use with other retinoids (adapalene, tretinoin) and photosensitising agents (such as tetracyclines) warrants particular attention.
- **Other considerations:** tazarotene is contraindicated in pregnancy, and local irritation is common, which matters especially on the face and genital skin.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for seborrhoeic dermatitis is supported only by a model score, with no trials or publications, and the mechanism does not address the fungal component of the disease. Possible skin irritation is an added concern.

**To proceed, the following is needed:**
- Mechanism of action data and a fuller review of retinoid effects in seborrhoeic dermatitis
- A systematic literature search for tazarotene in seborrhoeic dermatitis, and any registered trials
- Review of the full texts of PMID 36215682 and PMID 15090020 to see whether seborrhoeic keratosis is a stronger candidate
- The current SmPC for the UK products (indications, contraindications, warnings), as this information was not available
- A tolerability and safety plan for sensitive facial skin, and for women of childbearing potential

<!-- review:begin uk-lic-20261124c-tazarotene-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The current SmPC for the UK product (indications, contraindications, warnings), as this information was not available" Corrected wording only: the text referred to a single UK product, licence or authorisation record, or called the UK market data licence or authorisation data. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902), which lists more than one BNF presentation code for this drug; these are NHS prescribing codes, not MHRA licences, and they carry no indication text. The phrase was changed to the plural or to BNF prescribing codes; the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124c-tazarotene-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "The authorisation is recorded as a single-ingredient product with valid status" | Corrected (revised 2026-11-24; earlier version kept in the record) | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available from the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tazorac (tazarotene) prescribing information, Almirall, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e4e4b81-420e-4492-8a74-80b692a80057) |
| 2026-11-24 | Corrected: "The current SmPC for the UK product (indications, contraindications, warnings), as this information was not available" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

