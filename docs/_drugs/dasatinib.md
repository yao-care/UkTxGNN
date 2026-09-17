---
layout: default
title: Dasatinib
parent: High Evidence (L1-L2)
nav_order: 197
evidence_level: L2
indication_count: 10
---

# Dasatinib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Dasatinib: From Chronic Myeloid Leukaemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib is an oral dual BCR-ABL/Src-family tyrosine kinase inhibitor, originally developed for chronic myeloid leukaemia (CML) and Philadelphia chromosome-positive acute lymphoblastic leukaemia.
The TxGNN model predicts possible activity in **Ewing sarcoma**, with **3 clinical trials** and **9 publications** currently associated with this signal.
However, the strongest of these trials already tested dasatinib in this population and reported that it failed as a single agent, so the evidence base is mechanistic rather than clinically confirmatory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myeloid leukaemia (CML) / Philadelphia chromosome-positive ALL |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| UK Market Status | Not marketed (per this evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold (Research Question stage) |

---

## Why is This Prediction Reasonable?

Dasatinib's original approved use is as a dual inhibitor of BCR-ABL and Src-family tyrosine kinases in CML. This dual mechanism is well documented in the literature attached to this evidence pack (e.g. "Targeting ABL and SRC kinases in chronic myeloid leukemia: experience with dasatinib", PMID 17155893), even though the structured `original_moa` field itself is currently a data gap — a supplementary MOA lookup against DrugBank/SmPC is still recommended (see Conclusion).

The link to Ewing sarcoma does not come from disease similarity to CML — it comes from a shared druggable node, Src family kinase signalling. Multiple preclinical studies in this pack show that Ewing sarcoma cell invasion and metastatic behaviour depend on Src activation and invadopodia formation (PMID 31521948, 27566104, 17363602), and dasatinib has demonstrated antiproliferative and antimigratory activity against Ewing sarcoma cell lines in vitro (PMID 18202781). This gives a coherent mechanistic rationale.

Importantly, this rationale has already been tested clinically: a Phase 2 basket trial in advanced sarcomas (NCT00464620, n=366) included Ewing sarcoma, and a 2022 review of that trial (PMID 35655525) states dasatinib "failed as a single agent" in Ewing sarcoma and rhabdomyosarcoma subtypes. This is a meaningful negative signal that tempers the otherwise plausible mechanism, and it is the main reason the evidence level sits at L2 rather than higher despite the very high TxGNN score.

As a side note on model reliability: the same evidence pack also flags dasatinib's *already-approved* indication, myeloid leukaemia, as a top prediction (rank 2, L1 evidence, "Proceed with Guardrails" — because it is standard care). This is a useful sanity check that the underlying knowledge graph correctly reproduces known pharmacology, but it does not independently strengthen the Ewing sarcoma signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Basket trial of dasatinib in advanced sarcomas (including Ewing sarcoma cohort); the most directly relevant trial, but a subsequent review reports dasatinib failed as monotherapy in this subtype. |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Paediatric trial of dasatinib combined with ifosfamide, carboplatin and etoposide; terminated early with only 7 patients enrolled — too small to be informative. |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Recruiting | 41 | Trial of B7-H3 CAR-T cell therapy in relapsed/refractory paediatric solid tumours (including Ewing sarcoma as an eligible tumour type). Note: this trial does not test dasatinib — it is flagged in the source evidence as a likely knowledge-graph co-occurrence artefact and is included here for transparency only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Review | Sarcoma | Reviews FAK-Src targeting in Ewing sarcoma and related tumours; explicitly notes dasatinib monotherapy failed in the Phase 2 basket trial for this indication. |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclinical/Cohort | Cancer Research | Dasatinib inhibits migration/invasion across sarcoma cell lines and induces apoptosis in Src-dependent bone sarcoma cells. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical | Neoplasia | Microenvironmental stress drives tenascin C/Src cooperation, promoting invadopodia formation and invasion in Ewing sarcoma. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical | Neoplasia | Microenvironmental stress induces Src-dependent invadopodia activation and cell migration in Ewing sarcoma. |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclinical | Oncology Reports | In vitro antiproliferative and antimigratory activity of dasatinib in neuroblastoma and Ewing sarcoma cell lines. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | General review of Src signalling's role in sarcoma biology and its feasibility as a drug target. |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Review | Curr Treat Options Oncol | Systemic therapy review for chondrosarcoma; only tangentially related to Ewing sarcoma, does not evaluate dasatinib directly. |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | Preclinical | Cell Commun Signal | Studies the CXCR4 antagonist plerixafor in Ewing sarcoma; does not evaluate dasatinib — included for completeness of the pathway context only. |
| [32999666](https://pubmed.ncbi.nlm.nih.gov/32999666/) | 2020 | Case Report | Case Rep Oncol | Case report of a chromosomal abnormality in CML blast crisis; not related to Ewing sarcoma and appears to be a mismatched result in this evidence set. |

---

## UK Market Information

This evidence pack records no MHRA marketing authorisations for dasatinib (0 licences, status "not marketed"). Given dasatinib is an established oncology product internationally, this most likely reflects an incomplete regulatory data extraction in this pack rather than an actual absence from the UK market — please verify current authorisation and SmPC status directly against the MHRA register or dm+d before relying on this field.

---

## Cytotoxicity

Dasatinib is an antineoplastic agent (targeted kinase inhibitor used in haematological malignancy), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (dual BCR-ABL / Src-family tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question stage)**

**Rationale:**
- The Src-kinase mechanism is biologically coherent and supported by consistent preclinical data, but the one relevant Phase 2 trial that actually tested dasatinib in this population reported it failed as a single agent — this is a stronger constraint than the high TxGNN score alone would suggest, so this remains a research hypothesis rather than a practice-ready signal.

**To proceed, the following is needed:**
- Resolution of the blocking safety data gap (SmPC warnings/contraindications) before any S1 safety screening can occur
- Confirmed mechanism-of-action sourcing (DrugBank/SmPC), since the structured MOA field is currently a data gap
- Verification of current UK MHRA marketing authorisation status, as the "not marketed / 0 licences" result in this pack looks inconsistent with dasatinib's established international market presence
- Ewing-sarcoma-specific (rather than pan-sarcoma basket) trial data, ideally exploring combination regimens given the documented single-agent failure signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

