---
layout: default
title: Tazarotene
parent: Model Prediction Only (L5)
nav_order: 595
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Tazarotene: predicted new indication Seborrhoeic dermatitis (evidence level L5). Approved use: Psoriasis, parapsoriasis, acne"
monitor_inn: "Tazarotene"
predicted_indications: ["seborrheic dermatitis", "seborrheic keratosis", "vulvar inverted follicular keratosis"]
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tazarotene: From Psoriasis to Seborrhoeic Dermatitis

## One-Sentence Summary

Tazarotene is a topical retinoid, originally used to treat psoriasis, parapsoriasis and acne.
The TxGNN model predicts it may be effective for **seborrhoeic dermatitis**, but there are currently **no clinical trials** and **no publications** supporting this specific prediction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis, parapsoriasis, acne (from the knowledge graph; no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Seborrhoeic dermatitis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on general pharmacology, tazarotene is a topical retinoid prodrug that is converted to tazarotenic acid. This binds selectively to retinoic acid receptors beta and gamma (RARβ and RARγ), normalising keratinocyte differentiation and reducing hyperproliferation and inflammation.

These effects are relevant to psoriasis and acne, and could plausibly help with the scaling and inflammatory component of seborrhoeic dermatitis. However, that condition is also driven by *Malassezia* yeast colonisation and the skin's inflammatory response to it, which retinoid activity does not directly address. The very high TxGNN score is a computational prediction only, so the mechanistic link is inferred rather than demonstrated. Topical retinoid irritation (redness, peeling) could also aggravate a condition that commonly affects sensitive facial skin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for seborrhoeic dermatitis.

*Other predicted indications (for context):*
- **Seborrhoeic keratosis** (TxGNN score 99.51%, evidence level L4): a 2023 systematic review of topical treatments for seborrhoeic keratoses ([PMID 36215682](https://pubmed.ncbi.nlm.nih.gov/36215682/)) and a 2004 comparative study of cryosurgery versus topical calcipotriene, tazarotene and imiquimod ([PMID 15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/)) provide indirect evidence. Only titles and short abstracts were available, so the tazarotene-specific results need confirming from the full texts. This is best treated as a research question.
- **Vulvar inverted follicular keratosis** (TxGNN score 99.38%, evidence level L5): no trials or literature. A retinoid effect is speculative, and local irritation on thin genital skin is a particular concern.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1305020T0AAAAAA | Tazarotene Aq Gel 0.05% | Gel (aqueous) | Not stated in the available data |

The authorisation is recorded as a single-ingredient product with valid status. Manufacturer and approved indication text are not available in the data compiled for this report, so the UK licensed indications should be checked against the current SmPC and BNF.

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
- The current SmPC for the UK product (indications, contraindications, warnings), as this information was not available
- A tolerability and safety plan for sensitive facial skin, and for women of childbearing potential
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

