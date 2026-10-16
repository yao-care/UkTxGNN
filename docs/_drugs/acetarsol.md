---
layout: default
title: Acetarsol
parent: Model Prediction Only (L5)
nav_order: 16
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Acetarsol: predicted new indication Leishmaniasis, diffuse cutaneous (evidence level L5). Approved use: Amoebiasis (amoebiasis due to Entamoeba histolytica)"
monitor_inn: "Acetarsol"
predicted_indications: ["leishmaniasis, diffuse cutaneous", "mucocutaneous leishmaniasis", "X-linked lymphoproliferative syndrome", "type 2 diabetes nephropathy", "streptococcal pneumonia", "squamous cell lung carcinoma", "Legionnaires' disease", "rete ovarii cystadenoma", "ovarian benign neoplasm", "ovarian papillary cystadenoma"]
---

# Acetarsol
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

# Acetarsol: From Amoebiasis to Diffuse Cutaneous Leishmaniasis

## One-Sentence Summary

Acetarsol is a pentavalent arsenical originally used to treat amoebiasis caused by *Entamoeba histolytica*.
The TxGNN model predicts it may be effective for **diffuse cutaneous leishmaniasis**,
but there are currently **no registered clinical trials and no publications** supporting this prediction, so it rests on computational modelling alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Amoebiasis (amoebiasis due to *Entamoeba histolytica*) |
| Predicted New Indication | Leishmaniasis, diffuse cutaneous |
| TxGNN Prediction Score | 98.67% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

*Note: the approved indication text for the UK product was not available in the data compiled for this report. The original indication shown is taken from the TxGNN knowledge graph.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acetarsol is a pentavalent organic arsenical with antiprotozoal activity against *Entamoeba histolytica*. Its efficacy in amoebiasis is the basis for the prediction, and mechanistically it may be applicable to leishmaniasis.

Amoebiasis and leishmaniasis are both protozoan infections. Arsenicals and other metal-based agents (such as antimonials) have historically been used against protozoan parasites, so a class-level rationale is plausible. The same rationale applies to the second-ranked prediction, mucocutaneous leishmaniasis.

This reasoning is speculative. No trial or literature evidence was available, and the high TxGNN score is a computational prediction only. Arsenic toxicity (for example neuropathy and hepatotoxicity) is a major concern for any repurposing, and safer approved agents already exist for leishmaniasis.

**Other predictions in the top 10** (all L5, all Hold): mucocutaneous leishmaniasis (97.3%), X-linked lymphoproliferative syndrome (96.6%), type 2 diabetes nephropathy (96.5%), streptococcal pneumonia (95.3%), squamous cell lung carcinoma (94.5%), Legionnaires' disease (94.4%), rete ovarii cystadenoma (93.5%), ovarian benign neoplasm (93.4%) and ovarian papillary cystadenoma (93.4%). Apart from the leishmaniasis predictions, no plausible mechanistic link was identified for any of them. Several of the ovarian predictions probably reflect correlated knowledge-graph artefacts rather than biology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0107010B0AAAAAA (BNF code) | Acetarsol suppositories 250 mg | Suppository (per product name) | Not available |

Acetarsol is listed under BNF section 1.7 (local preparations for anal and rectal disorders), as suggested by the 0107 prefix of the code above. The identifier shown is a BNF-style code rather than a standard PL number. Please verify the current MHRA authorisation status before any further evaluation.

## Cytotoxicity

Acetarsol is not classed as an antineoplastic drug, so this section does not apply.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

The data compiled for this report did not include label warnings, contraindications or interaction records. As a pentavalent arsenical, acetarsol carries general arsenic-related concerns (neuropathy, hepatotoxicity, renal injury). Chronic arsenic exposure is also associated with diabetes, kidney injury and lung carcinogenicity. These concerns must be addressed before any new use is considered.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for diffuse cutaneous leishmaniasis is supported only by a model score and a class-level rationale. There are no clinical trials or publications, and the safety profile of arsenicals makes the risk-benefit balance unfavourable compared with existing approved treatments.

**To proceed, the following is needed:**
- Mechanism of action data for acetarsol
- Preclinical evidence (in vitro and in vivo) of activity against *Leishmania* species
- Full safety information from the SmPC and BNF, including contraindications and interactions
- Verification of the UK authorisation details (PL number, dosage form and approved indication)
- Assessment of route compatibility, since the UK product is a rectal suppository and cutaneous or mucocutaneous disease would likely need a different route
- A comparative risk-benefit analysis against current standard treatments for leishmaniasis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

