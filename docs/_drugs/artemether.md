---
layout: default
title: Artemether
parent: Model Prediction Only (L5)
nav_order: 72
evidence_level: L5
indication_count: 8
monitor_inn: "artemether"
predicted_indications: ["acquired angioedema", "angioedema", "hereditary angioedema", "nephrogenic syndrome of inappropriate antidiuresis", "acute contagious conjunctivitis", "scleroderma (disease)", "conjunctivitis", "renin-angiotensin-aldosterone system-blocker-induced angioedema"]
last_modified_at: 2026-11-25
description: "Artemether: predicted new indication Acquired angioedema (evidence level L5). In the UK: 2 NHSBSA BNF presentation codes"
---

# Artemether
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Artemether: Antimalarial artemisinin derivative → Acquired angioedema
{: .text-alpha }

## One-Sentence Summary

Artemether is an artemisinin-derivative antimalarial that is listed in the UK BNF prescribing codes. The TxGNN model predicts it may be relevant to **acquired angioedema**, with a prediction score of 0.9990. However, the data compiled for this report contain **no clinical trials and no publications** supporting this prediction.

<!-- review:begin uk-lic-20261125-artemether-1 -->

> **Review correction (2026-11-25)**: Originally stated: "Artemether is an artemisinin-derivative antimalarial that is marketed in the UK." Corrected wording only: the text said the drug or product is marketed, available or sold in the UK. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902): a BNF presentation code shows that an NHS prescribing code exists, not that the product is currently marketed or on sale, and MHRA licence status is not included. The wording was changed to the UK BNF prescribing codes (or the unsupported premise was removed); forms named are those in the BNF code list, and the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261125-artemether-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acquired angioedema |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (2 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of artemether as: Ferriprotoporphyrin IX inhibitor ([ChEMBL CHEMBL566534 (artemether): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL566534), CC BY-SA 3.0; accessed 2026-11-19.) Artemether is an artemisinin derivative, a class used as antimalarial therapy, but no mechanism has been identified that would connect it to acquired angioedema.

Acquired angioedema is a bradykinin- or complement-pathway-related swelling disorder. No known action of artemether on these pathways was identified. The high TxGNN score (0.9990) is a computational output only. With no supporting trials or literature, it most likely reflects network proximity in the model rather than biology, and it should not be read as clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0504010AAAAAAAA | Artemether 20mg / Lumefantrine 120mg tablets | Artemether with lumefantrine |
| 0504010AABBAAAA | Riamet tablets | Artemether with lumefantrine |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The identifiers shown are BNF-style codes rather than MHRA PL numbers.

<!-- review:begin uk-lic-20261106-artemether-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Both listed records are valid single-ingredient entries according to the local data. The identifiers shown are BNF-style codes rather than MHRA PL numbers." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. The Quick Overview and the BNF code table under UK Market Information show the current number of BNF presentation codes. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-artemether-1 -->

## Cytotoxicity

Not applicable: artemether is not an antineoplastic agent, so this section is omitted in substance.

## Safety Considerations

- **Contraindication-type associations:** The data compiled for this report record associations between artemether and long QT syndrome (including familial long QT syndrome), torsades de pointes and potassium deficiency. These are database associations, not label wording, and should be checked against the SmPC.
- **Drug Interactions:** 95 interactions were identified. Examples rated **Major**: clarithromycin, cobicistat, amprenavir, apalutamide, atazanavir and boceprevir. Examples rated **Moderate**: dexamethasone, miconazole, troglitazone, deferasirox, fostamatinib, bosentan, armodafinil, bexarotene and brigatinib. Many involve enzyme inhibition or induction, and QT-related risk should be considered.

For full warnings and contraindications, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for acquired angioedema is supported only by a model score, with no trials, no publications and no plausible mechanistic link. The evidence level is therefore L5.

**To proceed, the following is needed:**
- Mechanistic evidence linking artemether to bradykinin or complement pathways, or relevant preclinical data
- Any clinical or observational reports in angioedema
- Complete SmPC-based safety data, with particular attention to QT prolongation and interacting drugs
- Mechanism of action data for artemether

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "Both listed records are valid single-ingredient entries according to the local data" | Corrected (revised 2026-11-24; earlier version kept in the record) | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-19 | "Detailed mechanism-of-action data for artemether are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL566534 (artemether): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL566534) |
| 2026-11-25 | Corrected: "Artemether is an artemisinin-derivative antimalarial that is marketed in the UK." | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

