---
layout: default
title: Telithromycin
parent: Model Prediction Only (L5)
nav_order: 599
evidence_level: L5
indication_count: 10
monitor_inn: "Telithromycin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "septicemic plague", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-11-12
description: "Telithromycin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Streptococcal infection, streptococcal pneumonia…"
---

# Telithromycin
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

## Telithromycin: From Streptococcal Infection to Polyclonal Hyperviscosity Syndrome
{: .text-alpha }

## One-Sentence Summary

Telithromycin is a ketolide antibiotic, with relations recorded in the knowledge graph for streptococcal infection, streptococcal pneumonia, Mycoplasma pneumoniae pneumonia and chlamydial pneumonia.
The TxGNN model (deep learning) predicts it may be effective for **polyclonal hyperviscosity syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** directly studying this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal infection, streptococcal pneumonia, Mycoplasma pneumoniae pneumonia and chlamydial pneumonia (relations recorded in the knowledge graph; no licence indication text is available) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (2 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Telithromycin is a ketolide antibiotic that inhibits bacterial protein synthesis at the 50S ribosomal subunit. Detailed mechanism of action data is not available in the data compiled for this report, so this description reflects general knowledge of the drug class.

Polyclonal hyperviscosity syndrome is driven by an excess of polyclonal immunoglobulins in the blood. No known pathway connects an antibacterial ketolide to this process. The high TxGNN score (0.9990) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

On present evidence, the prediction is not mechanistically supported and should be regarded as a hypothesis only.

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
| 0501050T0AAAAAA | Telithromycin 400mg tablets | Telithromycin |
| 0501050T0BBAAAA | Ketek 400mg tablets | Telithromycin |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The code resembles a BNF-style classification code rather than a standard PL number, so the authorisation details should be verified against the MHRA register.

<!-- review:begin uk-lic-20261106-telithromycin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The listed record is a single-ingredient product and is shown as valid. The code resembles a BNF-style classification code rather than a standard PL number, so the authorisation details should be verified against the MHRA register." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 2 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-telithromycin-1 -->

---

## Safety Considerations

No label-derived warnings or contraindications were available in the data compiled for this report. The following items come from other sources.

- **Contraindication relations recorded in the knowledge graph (not label text):** long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease, drug-induced liver injury, gallbladder disease, potassium deficiency disease, diarrhoeal disease, *Clostridium difficile* colitis, perinatal necrotising enterocolitis, myasthenia gravis (including adult-onset), and neuromuscular junction disease.
- **Drug interactions (100 recorded; examples):**
  - Major: loperamide, triamcinolone, budesonide, dolasetron, eliglustat.
  - Moderate: famotidine, rabeprazole, hydrocortisone, dexamethasone, betamethasone, clarithromycin, alosetron, aprepitant, bisacodyl, saxagliptin.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a TxGNN model (deep learning) score alone, which may reflect similarities the model learned between related diseases, not biological evidence. No trial or publication addresses polyclonal hyperviscosity syndrome, there is no plausible mechanism, and the drug carries significant safety concerns (QT prolongation, hepatotoxicity, myasthenia gravis).

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological link to immunoglobulin-driven hyperviscosity
- Preclinical or clinical studies directly addressing the predicted disease
- Verified UK licence details, including approved indication text and the MHRA authorisation number
- Label-based warnings and contraindications from the SmPC and BNF
- A benefit-risk assessment given the safety signals above

**Other predictions reviewed:** The remaining top-ranked predictions (hyperamylasaemia, congenital analbuminaemia, blood group incompatibility, premalignant haematological disease, monoclonal gammopathy and others) also have no trials or literature and no supporting mechanism, so all are L5 and Hold. Septicaemic plague is biologically plausible for an antibacterial, but the only retrieved item is a review of a different ketolide (cethromycin), so it remains a research question rather than supported evidence.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The listed record is a single-ingredient product and is shown as valid" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

