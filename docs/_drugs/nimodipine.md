---
layout: default
title: Nimodipine
parent: Model Prediction Only (L5)
nav_order: 446
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Nimodipine: predicted new indication Homozygous familial hypercholesterolaemia (evidence level L5). Approved use: Subarachnoid haemorrhage (aneurysmal)"
monitor_inn: "Nimodipine"
predicted_indications: ["homozygous familial hypercholesterolemia", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Nimodipine
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

## Nimodipine: From Subarachnoid Haemorrhage to Homozygous Familial Hypercholesterolaemia
{: .text-alpha }

## One-Sentence Summary

Nimodipine is a calcium channel blocker originally used to treat subarachnoid haemorrhage, including aneurysmal subarachnoid haemorrhage.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolaemia**, but there are currently **no clinical trials** and **no publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Subarachnoid haemorrhage (aneurysmal) |
| Predicted New Indication | Homozygous familial hypercholesterolaemia |
| TxGNN Prediction Score | 0.9929 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (5 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, nimodipine is a dihydropyridine L-type calcium channel blocker with selectivity for the cerebral vasculature. Its efficacy in subarachnoid haemorrhage is linked to its effects on cerebral vessels.

The link to the predicted new indication is weak. Homozygous familial hypercholesterolaemia is caused by loss-of-function variants in genes such as *LDLR* (or *APOB*, *PCSK9*, *LDLRAP1*), which impair LDL clearance. Calcium channel blockade does not address this defect. Any association would be speculative, for example through possible vascular or atherosclerosis-related effects. The high TxGNN score (0.9929) is a computational prediction only and is not backed by any trial or literature evidence.

A second prediction, nephrogenic syndrome of inappropriate antidiuresis (score 0.9905), is also at the same early stage. It has no mechanistic support and no trials or literature, and its very small patient population would make generating evidence difficult.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0206020M0AAAAAA | Nimodipine 10mg/50ml solution for infusion vials | Nimodipine |
| 0206020M0AAABAB | Nimodipine 30mg tablets | Nimodipine |
| 0206020M0AAACAC | Nimodipine 30mg/5ml oral suspension | Nimodipine |
| 0206020M0BBAAAA | Nimotop 0.02% solution for infusion 50ml vials | Nimodipine |
| 0206020M0BBABAB | Nimotop 30mg tablets | Nimodipine |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The authorisation identifier above is not in standard MHRA PL format and the approved indication text is not available, so it should be verified against the MHRA register, the SmPC and the BNF.

<!-- review:begin uk-lic-20261106-nimodipine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The data compiled for this report lists one valid single-ingredient authorisation. The authorisation identifier above is not in standard MHRA PL format and the approved indication text is not available, so it should be verified against the MHRA register, the SmPC and the BNF." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 5 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-nimodipine-1 -->

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The TxGNN knowledge graph links nimodipine to liver disease, gallbladder disease and hypotensive disorders. These should be checked against the SmPC.
- **Drug Interactions**: 100 interactions were identified. The sample reviewed included:
  - **Major**: clarithromycin, dolasetron
  - **Moderate**: bupropion, aprepitant, morphine, acetylsalicylic acid (aspirin), cimetidine, miconazole, magnesium sulfate, canagliflozin, dapagliflozin, empagliflozin, kanamycin, neomycin, dronabinol, nabilone, and calcium salts (phosphate, acetate, carbonate, chloride)

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5). There are no trials or publications, and no plausible mechanistic link between L-type calcium channel blockade and the genetic LDL-clearance defect in homozygous familial hypercholesterolaemia.

**To proceed, the following is needed:**
- Mechanism of action data and a credible hypothesis linking nimodipine to LDL metabolism
- Preclinical or mechanistic studies supporting the link
- A systematic literature and trial registry search (including ISRCTN and EU CTR)
- Full UK licence details (PL number, dosage form, approved indication) and SmPC warnings and contraindications
- Review of the established treatments for this condition to judge any realistic added value

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The data compiled for this report lists one valid single-ingredient authorisation" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

