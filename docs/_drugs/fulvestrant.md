---
layout: default
title: Fulvestrant
parent: Model Prediction Only (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fulvestrant: predicted new indication HIV infectious disease (evidence level L5). Approved use: Not stated in the UK licence data compiled for this report"
---

# Fulvestrant
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

# Fulvestrant: From Breast Cancer to HIV Infectious Disease

## One-Sentence Summary

Fulvestrant is an oestrogen receptor antagonist and degrader. It is marketed in the UK as an injectable product, and its established use is in hormone receptor-positive breast cancer (this is from general knowledge, as the UK licence data compiled for this report contain no indication text).
The TxGNN model predicts it may be effective for **HIV infectious disease**, but there are **no registered clinical trials** and only **2 publications**, both preclinical or indirect.
This is a model-generated hypothesis supported mainly by one in vitro study, and not a validated repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the UK licence data compiled for this report |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (preclinical/mechanistic only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Fulvestrant is generally known as a selective oestrogen receptor antagonist and degrader. Its efficacy in hormone receptor-positive breast cancer is established, and mechanistically it may be applicable wherever oestrogen receptor signalling matters.

For HIV, the rationale is indirect. Oestrogen receptor alpha is expressed in CD4+ T cells and has been hypothesised to influence HIV transcription and latency. A 2026 in vitro study (PMID 42430506) examined how oestrogen receptor ligands, including fulvestrant, and HIV latency-reversing agents affect oestrogen receptor alpha in CD4+ T cells. This suggests fulvestrant could plausibly influence latency reversal, but this has not been tested in patients.

The second publication concerns HTLV-1-associated myelopathy, a different retrovirus, and offers only weak support.

Other predictions in the list (for example simian immunodeficiency virus infection and feline AIDS) appear to reflect the same HIV-related signal in the knowledge graph and are not relevant to human development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for HIV infectious disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42430506](https://pubmed.ncbi.nlm.nih.gov/42430506/) | 2026 | Preclinical/in vitro study | JCI Insight | Examined the effect of oestrogen and fulvestrant, together with HIV latency-reversing agents, on oestrogen receptor alpha in CD4+ T cells |
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Cross-omics cohort analysis | Research Square | Studies HTLV-1-associated myelopathy, not HIV; weak and indirect relevance |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0803041AAAAAAAA | Fulvestrant Inj 250mg/5ml Pfs | Solution for injection (pre-filled syringe) | Not stated in the data compiled |

Only one authorisation was identified. The dosage form and indication fields were not populated in the source data.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Endocrine therapy (oestrogen receptor antagonist/degrader), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): liver disease, gallbladder disease, thrombocytopenia and blood coagulation disease.
- **Drug Interactions**: The interaction query returned 92 entries, but none has a defined severity level. Examples include warfarin, pantoprazole, omeprazole, metformin, simvastatin, dexamethasone and morphine. Given the knowledge-graph coagulation signal, concurrent anticoagulants such as warfarin merit particular attention.

Please refer to the SmPC and BNF for authoritative warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but rests on a single in vitro study, with no clinical trials in HIV. The evidence level is L4 and the idea remains a research question.

**To proceed, the following is needed:**
- Confirmation of the mechanism of action and the approved UK indication from the SmPC and BNF
- Further preclinical work on oestrogen receptor modulation and HIV latency, then early-phase studies if supported
- Review of the safety profile in people living with HIV, including interactions with antiretroviral therapy
- Obtaining the full SmPC warnings and contraindications, which are missing from the data compiled for this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

