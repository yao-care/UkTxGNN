---
layout: default
title: Demeclocycline
parent: Model Prediction Only (L5)
nav_order: 201
evidence_level: L5
indication_count: 3
---

# Demeclocycline
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

# Demeclocycline: From Bacterial Infections to Chronic Ethmoidal Sinusitis

## One-Sentence Summary

Demeclocycline is a tetracycline-class antibiotic historically used to treat bacterial infections (and off-label for SIADH-related hyponatraemia), though detailed original-indication and mechanism-of-action data are not available in this dataset. The TxGNN model predicts potential efficacy in **Chronic Ethmoidal Sinusitis**, but this is currently supported by **0 clinical trials** and only **1 tangentially related publication** that does not test any drug intervention.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no marketing authorisation or indication text available in this dataset |
| Predicted New Indication | Chronic Ethmoidal Sinusitis |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available. Based on known information, demeclocycline is part of the tetracycline class of antibiotics, a group with established broad-spectrum antibacterial activity and secondary anti-inflammatory/matrix-metalloproteinase (MMP)-inhibiting properties that have been explored in other tetracyclines (e.g. doxycycline) for chronic sinonasal inflammation.

The predicted link between demeclocycline and chronic ethmoidal sinusitis is plausible only at the class level — tetracyclines are sometimes considered for bacterial or inflammatory sinus disease — but the single literature record returned for this prediction (PMID 9546260) is a histomorphometric study of ethmoid bone in chronic rhinosinusitis patients. It does not evaluate demeclocycline, any tetracycline, or any drug intervention at all. The same paper is also the sole evidence cited for the closely related rank-2 prediction (chronic rhinosinusitis), and the rank-3 prediction (paranasal sinus neoplasm) has no supporting literature or trials whatsoever.

Taken together, this pattern is consistent with a TxGNN disease-term co-occurrence artefact rather than a genuine drug–disease signal. The mechanistic rationale is theoretical and cross-drug (extrapolated from other tetracyclines), not evidence specific to demeclocycline.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9546260](https://pubmed.ncbi.nlm.nih.gov/9546260/) | 1998 | Cohort | The Laryngoscope | Histomorphometric analysis of ethmoid bone in chronic rhinosinusitis patients versus controls, assessing bone synthesis, resorption and inflammatory cell presence; no drug intervention (including demeclocycline) was tested. |

## UK Market Information

Demeclocycline is currently not marketed in the UK — no marketing authorisation is on file in this dataset (0 licences recorded).

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only) with zero supporting clinical trials and a single literature record that does not involve any drug intervention — the link appears to be a term co-occurrence artefact rather than substantive evidence. Combined with the absence of UK marketing authorisation and missing mechanism-of-action and safety data, there is no basis to progress beyond initial screening at this time.

**To proceed, the following is needed:**
- Verified mechanism-of-action data for demeclocycline (currently a data gap)
- Regulatory safety labelling (warnings, contraindications) — currently blocking S1 safety assessment
- Genuine drug-intervention evidence (preclinical or clinical) connecting demeclocycline to chronic ethmoidal sinusitis, rather than co-occurring disease-term literature
- Confirmation of whether any UK-marketed tetracycline formulation could serve as a bridging comparator, given demeclocycline itself is not currently marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

