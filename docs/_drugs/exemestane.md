---
layout: default
title: Exemestane
parent: Model Prediction Only (L5)
nav_order: 256
evidence_level: L5
indication_count: 10
---

# Exemestane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Exemestane: From Breast Cancer to Antithrombin Deficiency Type 2

## One-Sentence Summary

Exemestane is a steroidal, irreversible aromatase inhibitor originally used for postmenopausal, oestrogen receptor-positive breast cancer. The TxGNN model's top-ranked prediction associates it with **Antithrombin Deficiency Type 2**, but this candidate currently has **no clinical trials** and **no publications** supporting it, and the evidence pack's own mechanistic review found **no plausible biological link** between the two conditions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal, oestrogen receptor-positive breast cancer *(derived from evidence-pack rationale text; no original_indications data recorded)* |
| Predicted New Indication | Antithrombin Deficiency Type 2 |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap). Based on information recoverable from the evidence pack's own rationale text, exemestane is a steroidal, irreversible aromatase inhibitor that blocks peripheral conversion of androgens to oestrogens, producing a systemic reduction in oestrogen levels — the basis of its established use in postmenopausal, oestrogen receptor-positive breast cancer.

For the top-ranked candidate, **antithrombin deficiency type 2**, no such mechanistic bridge exists. This is an inherited disorder caused by mutations in the antithrombin (SERPINC1) gene affecting coagulation regulation — a pathway that does not intersect with aromatase inhibition or oestrogen metabolism. The evidence pack's own mechanistic assessment explicitly states there is no known biological link and that exemestane has no antithrombin-modulating activity. The high TxGNN score most likely reflects network-embedding similarity within the knowledge graph rather than a causally plausible mechanism, and it is not corroborated by any clinical or literature evidence.

It is worth noting that among the ten candidates in this evidence pack, **breast fibrocystic disease** (rank 10) has the strongest mechanistic rationale — as an oestrogen-dependent benign breast condition, it aligns directly with exemestane's original oncology indication — though it too currently lacks supporting clinical trials or literature and is flagged only as a "Research Question."

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## UK Market Information

No MHRA marketing authorisations are recorded for exemestane in the available regulatory data (market status: not marketed; 0 licences on file).

## Cytotoxicity

Exemestane is an endocrine (hormonal) anticancer agent used in breast cancer, rather than a conventional cytotoxic chemotherapy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/endocrine therapy — steroidal, irreversible aromatase inhibitor (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by a TxGNN model prediction (L5, decision stage S0) with no clinical trials, no literature, and no biological rationale — the evidence pack's own mechanistic review found no plausible link between aromatase inhibition and antithrombin deficiency type 2. A blocking data gap (missing UK product labelling/warnings) also means this drug cannot yet enter a formal safety review for any indication.

**To proceed, the following is needed:**
- UK product labelling (SmPC warnings, contraindications, DDI data) to close the blocking safety data gap
- Verified mechanism of action data to confirm or refute the biological rationale
- If pursuing repurposing further, consider prioritising **breast fibrocystic disease** instead, which has a mechanistically coherent rationale aligned with exemestane's original indication, and seek supporting preclinical or observational evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

