---
layout: default
title: Flumethasone
parent: Model Prediction Only (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Flumethasone: predicted new indication Alopecia areata (evidence level L5). Approved use: Inflammatory skin conditions (e.g. atopic eczema, contact dermatitis…"
monitor_inn: "flumethasone"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "hereditary hypotrichosis with recurrent skin vesicles", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "primary cutaneous B-cell lymphoma", "alopecia universalis onychodystrophy vitiligo"]
---

# Flumethasone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Flumethasone: From Inflammatory Skin Conditions to Alopecia Areata
{: .text-alpha }

## One-Sentence Summary

Flumethasone is a corticosteroid, originally used for inflammatory and immune-mediated skin conditions such as eczema, dermatitis and cutaneous lupus erythematosus.
The TxGNN model predicts it may be effective for **alopecia areata**, but there are currently **no registered clinical trials** and **no publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inflammatory skin conditions (e.g. atopic eczema, contact dermatitis, seborrhoeic dermatitis, discoid lupus erythematosus, primary cutaneous T-cell lymphoma); the licence records compiled for this report contain no indication text |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (2 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, flumethasone is a corticosteroid, and its efficacy in inflammatory skin disease is established. Mechanistically, it may be applicable to alopecia areata.

Alopecia areata is an autoimmune, T-cell-mediated disease of the hair follicle. Topical and intralesional corticosteroids are an established therapy class for it, so a glucocorticoid anti-inflammatory and immunosuppressive effect is biologically plausible.

However, the very high score probably reflects similarity to other corticosteroids rather than flumethasone-specific data. No trial or literature data for flumethasone itself were available, so this remains a hypothesis.

Other predicted indications were considered, and none has supporting evidence:
- **Alopecia mucinosa, Quinquaud's folliculitis decalvans and primary cutaneous B-cell lymphoma** have a plausible anti-inflammatory or lympholytic rationale, but only as adjunctive or symptomatic therapy.
- **Telogen effluvium, hereditary hypotrichosis with recurrent skin vesicles, atrichia with papular lesions, and the rare syndromic alopecias** (including alopecia with antibody deficiency, and alopecia with intellectual disability and hypergonadotropic hypogonadism) have little or no pharmacological rationale. In antibody deficiency, immunosuppression could be harmful.
- **Alopecia universalis with onychodystrophy and vitiligo** involves autoimmune components, but alopecia universalis responds poorly to topical steroids.

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1201010F0AAAAAA | Flumetasone 0.02% / Clioquinol 1% ear drops | Flumetasone pivalate |
| 1201010F0BBAAAA | Locorten Vioform ear drops | Flumetasone pivalate |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The numbers above are as recorded in the data compiled for this report and are not in standard PL format. The products are ear preparations, so any use for scalp or skin conditions would be outside the marketed route and would need a route-compatibility assessment.

<!-- review:begin uk-lic-20261106-flumethasone-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Both authorisations are valid single-ingredient records. The numbers above are as recorded in the data compiled for this report and are not in standard PL format." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 2 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-flumethasone-1 -->

---

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** The knowledge graph links flumethasone to contraindication-type associations with pituitary hormone deficiency and hypogonadotropic hypogonadism conditions, and with skin atrophy, telangiectasia, capillary disease and hereditary haemorrhagic telangiectasia. Skin atrophy is a recognised effect of topical corticosteroids and is relevant to any prolonged use on the scalp or skin. These associations need verification against the product label.

No drug interaction data were found.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for alopecia areata is biologically plausible at the corticosteroid class level, but there are no flumethasone-specific trials or publications (Evidence Level L5). The only UK products are ear preparations, and the label-based safety information has not been obtained.

**To proceed, the following is needed:**
- Product label (SmPC) warnings and contraindications, which are required before safety screening can proceed
- Mechanism of action data for flumethasone
- A literature and trial search for flumethasone, or comparison with established topical corticosteroids, in alopecia areata
- Route and formulation assessment, since the marketed products are ear drops
- Verification of the knowledge-graph contraindication associations against the label

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Both authorisations are valid single-ingredient records" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

