---
layout: default
title: Amylmetacresol
parent: Model Prediction Only (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-06
description: "Amylmetacresol: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Amylmetacresol"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "ciliary body disease", "panuveitis (disease)", "iris disease", "infectious anterior uveitis", "uveitis", "ciliary body cancer", "benign neoplasm of ciliary body"]
---

# Amylmetacresol
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

## Amylmetacresol: From Throat Infection Relief to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Amylmetacresol is a topical antiseptic, used in throat lozenges. The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are **no clinical trials and no publications** supporting this prediction. It is a model output only, with no plausible pharmacological rationale evident.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the licence record contains no indication text) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (25 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 25 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Amylmetacresol is a topical antiseptic used in throat lozenges, usually for the relief of sore throat. Its use in the oropharynx involves minimal systemic exposure.

Cauda equina syndrome is a compressive neurological emergency that is treated surgically. No mechanistic link to an antiseptic lozenge has been established, and no plausible pharmacological rationale is evident. The high score (0.9999) reflects a model prediction only, not clinical or literature support.

The other top-ranked predictions are similarly unsupported. They include obsolete neurogenic bladder, irritable bowel syndrome and a cluster of ocular conditions (ciliary body disease, panuveitis, iris disease, infectious anterior uveitis, uveitis, ciliary body cancer and benign ciliary body neoplasm). The ocular cluster in particular looks like a model artefact from correlated disease terms rather than independent signals. The only weak, speculative rationale is for infectious anterior uveitis: amylmetacresol shows in vitro antibacterial and antiviral activity in the oropharyngeal setting, but it is not formulated or validated for intraocular use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1203030A0AAAEAE | Amylmetacresol 600microgram lozenges | Amylmetacresol |
| 1203030A0AAADAD | Amylmetacresol 600microgram lozenges sugar free | Amylmetacresol |
| 1203030A0BCAAAD | Antiseptic Throat Drops Blackcurrant sugar free | Amylmetacresol |
| 1203030A0BCABAE | Antiseptic Throat Drops Cherry Menthol | Amylmetacresol |
| 1203030A0BCACAE | Antiseptic Throat Drops Orange and Menthol with Vitamin C | Amylmetacresol |
| 1203030A0BCAFAE | Boots Sore Throat Relief 600microgram loz orange & menthol | Amylmetacresol |
| 1203030A0BCADAE | Boots Sore Throat Relief 600microgram lozenges cherry | Amylmetacresol |
| 1203030A0BCAEAE | Boots Sore Throat Relief 600microgram lozenges lemon | Amylmetacresol |
| 1203030A0BCAGAD | Boots Sore Throat Relief 600microgram lozenges sugar free | Amylmetacresol |
| 1203030A0AAACAC | Dichlorobenzyl alc 230microg/Amylmetacresol 120microg loz | Amylmetacresol |
| 1203030A0AAAAAA | Dichlorobenzyl alcohol 1.2mg / Amylmetacresol 600microg loz | Amylmetacresol |
| 1203030AAAAAAAA | Dichlorobenzyl alcohol 1.2mg/Amylmetacresol 600microg loz SF | Dichlorobenzyl alcohol/amylmetacresol |
| 1203030A0AAABAB | Generic Strepsils Orange with Vitamin C 100mg lozenges | Amylmetacresol |
| 1203030A0BIAAAC | Lloydspharmacy Antiseptic Throat lozenges | Amylmetacresol |
| 1203030A0BBAIAA | Strepsils Children 6+ lozenges | Amylmetacresol |
| 1203030A0BBAGAA | Strepsils Cool lozenges | Amylmetacresol |
| 1203030A0BBABAA | Strepsils Honey and Lemon lozenges | Amylmetacresol |
| 1203030A0BBAJAA | Strepsils Menthol 1.2mg/600microgram lozenges | Amylmetacresol |
| 1203030A0BBACAB | Strepsils Orange with Vitamin C 100mg lozenges | Amylmetacresol |
| 1203030A0BBAEAA | Strepsils Strawberry lozenges sugar free | Amylmetacresol |

Showing 20 of 25 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

Dosage form and indication details were not available in the data compiled for this report, so the lozenge form is inferred from the product name.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

No drug interaction records were found for this drug in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score. There are no trials, no publications, no mechanistic data and no plausible pharmacological link between a throat antiseptic and cauda equina syndrome. The other top-ranked predictions are similarly unsupported.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- Confirmed original indication and licence details (dosage form, indication text) from the MHRA/BNF records
- Warnings, contraindications and interaction data from the SmPC and BNF
- Preclinical or mechanistic evidence showing a credible biological rationale for the predicted indication
- Assessment of route compatibility, since a lozenge acts locally in the oropharynx and the predicted conditions are neurological, gastrointestinal or ocular
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

