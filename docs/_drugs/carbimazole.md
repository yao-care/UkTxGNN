---
layout: default
title: Carbimazole
parent: Model Prediction Only (L5)
nav_order: 133
evidence_level: L5
indication_count: 2
monitor_inn: "Carbimazole"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia"]
last_modified_at: 2026-11-06
description: "Carbimazole: predicted new indication Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (evidence level L5). Approved use: Not recorded in the local data"
---

# Carbimazole
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

## Carbimazole: Antithyroid thionamide prodrug (thyroid hormone synthesis inhibitor) → Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta
{: .text-alpha }

---

## One-Sentence Summary

Carbimazole is an antithyroid medicine that is converted in the body to methimazole and reduces thyroid hormone production.
The TxGNN model predicts it may be relevant to **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta**, but there are **no clinical trials** and only **1 case report** in the data compiled for this report, and that report does not support use in this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (19 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Carbimazole is known to act as a prodrug of methimazole, which inhibits thyroid peroxidase and so lowers the synthesis of thyroid hormones.

In resistance to thyroid hormone beta, the defect lies in the hormone receptor. Patients typically have raised thyroid hormones with a non-suppressed TSH. In theory, lowering hormone synthesis could reduce circulating hormone levels. In practice, it would also remove negative feedback and increase TSH, which risks goitre enlargement and worsening hypothyroidism in tissues that are already resistant to the hormone.

The mechanistic rationale is therefore weak and potentially harmful. The high TxGNN score most likely reflects shared thyroid-hormone-axis terms rather than a true therapeutic link. Antithyroid drugs are generally not recommended in this condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Case report / differential diagnosis | BMJ Case Reports | A young man with persistently raised free thyroxine and non-suppressed TSH was treated intermittently with carbimazole for about 10 years under a diagnosis of hyperthyroidism. The report discusses the differential diagnosis of this biochemical pattern; it does not show benefit of carbimazole in thyroid hormone resistance. |

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0602020D0AAAVAV | Carbimazole 1.25mg/5ml oral liquid | Carbimazole |
| 0602020D0AAAIAI | Carbimazole 1.5mg/5ml oral liquid | Carbimazole |
| 0602020D0AAAYAY | Carbimazole 10mg tablets | Carbimazole |
| 0602020D0AAAGAG | Carbimazole 10mg/5ml oral solution | Carbimazole |
| 0602020D0AAAWAW | Carbimazole 10mg/5ml oral suspension | Carbimazole |
| 0602020D0AAAZAZ | Carbimazole 15mg tablets | Carbimazole |
| 0602020D0AAARAR | Carbimazole 2.5mg capsules | Carbimazole |
| 0602020D0AAATAT | Carbimazole 2.5mg/5ml oral liquid | Carbimazole |
| 0602020D0AABABA | Carbimazole 2.5mg/ml oral solution sugar free | Carbimazole |
| 0602020D0AAABAB | Carbimazole 20mg tablets | Carbimazole |
| 0602020D0AAAFAF | Carbimazole 20mg/5ml oral liquid | Carbimazole |
| 0602020D0AAAUAU | Carbimazole 2mg/5ml oral liquid | Carbimazole |
| 0602020D0AAAXAX | Carbimazole 30mg/5ml oral suspension | Carbimazole |
| 0602020D0AAAPAP | Carbimazole 4mg/5ml oral liquid | Carbimazole |
| 0602020D0AAAAAA | Carbimazole 5mg tablets | Carbimazole |
| 0602020D0AAAKAK | Carbimazole 5mg/5ml oral liquid | Carbimazole |
| 0602020D0AAAQAQ | Carbimazole 60mg/5ml oral liquid | Carbimazole |
| 0602020D0BBABAB | NeoMercazole 20 tablets | Carbimazole |
| 0602020D0BBAAAA | NeoMercazole 5 tablets | Carbimazole |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials, the single retrieved publication is a case report that does not demonstrate benefit, and the mechanism suggests possible harm through raised TSH and goitre growth.

**To proceed, the following is needed:**
- Mechanism of action data and a clear mechanistic case that addresses receptor-level resistance
- Controlled or observational data in patients with thyroid hormone receptor beta mutations
- A safety assessment covering TSH rise, goitre and hypothyroidism in this population
- Full SmPC warnings and contraindications for review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

