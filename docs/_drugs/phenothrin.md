---
layout: default
title: Phenothrin
parent: Model Prediction Only (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Phenothrin: predicted new indication Aleutian mink disease (evidence level L5). Approved use: Scabies, Norwegian scabies, mite infestation"
monitor_inn: "Phenothrin"
predicted_indications: ["aleutian mink disease", "feline panleukopenia", "variola minor infection", "benign neoplasm of tongue", "epiglottis neoplasm", "benign neoplasm of hypopharynx", "nasal cavity inverting papilloma", "trochlear nerve neoplasm", "spinal accessory nerve neoplasm", "facial nerve neoplasm"]
---

# Phenothrin
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

## Phenothrin: From Scabies to Aleutian Mink Disease
{: .text-alpha }

## One-Sentence Summary

Phenothrin is a synthetic pyrethroid insecticide, originally used to treat scabies, Norwegian scabies and mite infestation.
The TxGNN model predicts it may be effective for **Aleutian mink disease**, but there are **no clinical trials** and **no publications** supporting this prediction, and no plausible mechanistic link has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Scabies, Norwegian scabies, mite infestation (from the knowledge graph; no approved indication text is available for the UK product) |
| Predicted New Indication | Aleutian mink disease |
| TxGNN Prediction Score | 97.21% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, phenothrin is a synthetic pyrethroid that acts on voltage-gated sodium channels in arthropods, which explains its use against scabies mites and other ectoparasites.

Aleutian mink disease is caused by a parvovirus, and phenothrin has no known antiviral activity. The prediction therefore appears to come from network similarity in the knowledge graph (possibly linked to veterinary or antiparasitic associations) rather than from biology. The high score of 97.21% is a model output only and should not be read as evidence of efficacy.

Other top-ranked predictions show the same pattern:
- **Viral diseases** (feline panleukopenia, 97.15%; variola minor, 97.03%): no antiviral activity is known, and variola minor is eradicated, so clinical evaluation is not feasible.
- **Benign neoplasms and nerve tumours** (tongue, hypopharynx, nasal cavity inverting papilloma, trochlear, spinal accessory and facial nerve neoplasms; scores 96.5-96.7%): no antitumour mechanism is documented. The identical scores for the three cranial nerve neoplasms suggest a graph-level artefact rather than independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1310040S0AAABAB | Phenothrin_Alcoholic Lot 0.2% | Not specified | Not specified |

The authorisation number above is in the format supplied in the compiled data and is not a standard MHRA "PL" number. It should be verified against the MHRA register. No NICE appraisal or BNF classification data were available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

No drug interactions were found in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no trials or publications, no plausible mechanism (phenothrin is an arthropod sodium-channel agent, and the predicted diseases are viral or neoplastic), and the safety data are incomplete.

**To proceed, the following is needed:**
- Mechanism of action data for phenothrin, and a credible biological rationale for any predicted indication
- Verification of the UK authorisation record (PL number, dosage form, approved indication) with the MHRA
- Safety information from the SmPC and BNF
- Preclinical or in vitro evidence of activity in the predicted condition before any clinical consideration
- A review of the prediction list for more biologically plausible candidates, such as other ectoparasitic conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

