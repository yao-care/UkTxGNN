---
layout: default
title: Glimepiride
parent: Model Prediction Only (L5)
nav_order: 315
evidence_level: L5
indication_count: 9
monitor_inn: "Glimepiride"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-11-12
description: "Glimepiride: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Glimepiride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Glimepiride: Classic stiff person syndrome
{: .text-alpha }

## One-Sentence Summary

Glimepiride is a sulfonylurea medicine originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but **no clinical trials and no publications** in the data compiled for this report support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (14 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug in the data compiled for this report. Glimepiride is a sulfonylurea, a class known to close ATP-sensitive potassium (KATP) channels on pancreatic beta cells and so stimulate insulin release.

Classic stiff person syndrome is an autoimmune neurological disorder, usually linked to anti-GAD65 antibodies and impaired GABAergic signalling. No clear mechanistic link to glimepiride has been identified. The high score probably reflects network associations, such as the frequent co-occurrence of diabetes and GAD autoimmunity, rather than a therapeutic mechanism.

The other top-ranked predictions are similarly weak:
- **Focal stiff limb syndrome** (score 0.9975): a focal variant of the stiff person spectrum. The prediction probably comes from network proximity to stiff person syndrome.
- **Opsismodysplasia** (0.9974): a skeletal dysplasia involving INPPL1/SHIP2 and insulin signalling. The link is speculative.
- **Thiamine-responsive dysfunction syndrome** (0.9973): can involve diabetes, but treatment is thiamine, and a sulfonylurea would at most address the hyperglycaemia.
- **Lipodystrophy-type conditions** (drug-induced localised, centrifugal, pressure-induced and idiopathic; 0.9956 to 0.9962): probably linked through metabolic and insulin-injection network context, with no known therapeutic effect of glimepiride.
- **Pancreatic agenesis** (0.9955): glimepiride needs functional beta cells, so it would be expected to be ineffective where they are absent.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction. The only publication retrieved for any of the top predictions concerns pancreatic agenesis (PMID [12720536](https://pubmed.ncbi.nlm.nih.gov/12720536/), 2003, *European Journal of Endocrinology*). It is a study of endosonographic imaging pitfalls in suspected insulinomas and is not relevant to treatment.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0601021A0AAABAB | Glimepiride 1mg tablets | Glimepiride |
| 0601021A0AAAAAA | Glimepiride 2mg tablets | Glimepiride |
| 0601021A0AAAGAG | Glimepiride 2mg/5ml oral liquid | Glimepiride |
| 0601021A0AAACAC | Glimepiride 3mg tablets | Glimepiride |
| 0601021A0AAADAD | Glimepiride 4mg tablets | Glimepiride |
| 0601021A0AAAHAH | Glimepiride 6mg/5ml oral suspension | Glimepiride |
| 0601021A0BBABAB | Amaryl 1mg tablets | Glimepiride |
| 0601021A0BBAAAA | Amaryl 2mg tablets | Glimepiride |
| 0601021A0BBACAC | Amaryl 3mg tablets | Glimepiride |
| 0601021A0BBADAD | Amaryl 4mg tablets | Glimepiride |
| 0601021A0BCAAAB | Niddaryl 1mg tablets | Glimepiride |
| 0601021A0BCABAA | Niddaryl 2mg tablets | Glimepiride |
| 0601021A0BCACAC | Niddaryl 3mg tablets | Glimepiride |
| 0601021A0BCADAD | Niddaryl 4mg tablets | Glimepiride |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The list is complete.

<!-- review:begin uk-lic-20261106-glimepiride-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The data compiled for this report show one single-ingredient authorisation (valid). The list is complete." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 14 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-glimepiride-1 -->

## Safety Considerations

**Contraindications or conditions of concern recorded in the knowledge graph** (these are graph relations, not label text): kidney disease, liver disease, gallbladder disease, congestive heart failure, hypopituitarism and other pituitary hormone deficiencies, hypogonadotropic hypogonadism (including Kallmann syndrome), osteoporosis (including postmenopausal), thymus gland disease and infectious disease.

**Drug interactions:** 100 interactions were identified. Examples from the first 20 listed:
- **Moderate:** phenylephrine, acebutolol, acetazolamide, famotidine, ranitidine, acitretin, formoterol, pseudoephedrine, ketorolac, epinephrine, ibuprofen, ethinylestradiol, hydrocortisone, albiglutide, salbutamol, ethanol, nitazoxanide, hydrochlorothiazide
- **Minor:** topical hydrocortisone, topical alclometasone

Label-based warnings and contraindications were not available. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications and no plausible mechanism, so the evidence level is L5. The high TxGNN score appears to reflect network proximity rather than pharmacology.

**To proceed, the following is needed:**
- Mechanism of action data for glimepiride and a credible mechanistic hypothesis for stiff person syndrome
- Preclinical or clinical studies that directly address stiff person syndrome
- Label-based safety information (SmPC/BNF warnings and contraindications)
- Licence indication text and dosage form details for the UK authorisation

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The data compiled for this report show one single-ingredient authorisation (valid)" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

