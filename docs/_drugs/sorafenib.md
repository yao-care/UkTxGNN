---
layout: default
title: Sorafenib
parent: Model Prediction Only (L5)
nav_order: 573
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-06
monitor_inn: "Sorafenib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "female breast carcinoma", "renal pelvis carcinoma", "vulva sarcoma", "dermatofibrosarcoma protuberans"]
description: "Sorafenib: predicted new indication Liposarcoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Sorafenib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Sorafenib: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Sorafenib is an oral multikinase inhibitor that blocks RAF, VEGFR, PDGFR and KIT signalling. The TxGNN model predicts it may be effective for **liposarcoma**, but no study has tested sorafenib in liposarcoma itself. The available support comes from **1 Phase 2 trial in soft tissue sarcoma generally** and a small set of related publications, so the evidence level is **L5**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (2 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Sorafenib is known to be a multikinase inhibitor acting on RAF, VEGFR, PDGFR and KIT. Through these targets it may suppress MAPK signalling and tumour angiogenesis.

Soft tissue sarcomas, including liposarcoma, can depend on these pathways. Laboratory work in dedifferentiated liposarcoma cell lines and xenograft models points to biological plausibility. However, those studies concern nerve sheath tumour cells and model development, not sorafenib treatment of liposarcoma in patients. Benefit specific to liposarcoma has not been shown.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Single-arm trial of sorafenib in advanced soft tissue sarcomas. Not liposarcoma-specific and has no randomised comparator. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 trial (SWOG S0505) | Cancer | Sorafenib in advanced soft tissue sarcomas. Not specific to liposarcoma. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Ann Surg Oncol | Neoadjuvant radiotherapy plus sorafenib in extremity soft tissue sarcoma. |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Mol Cancer Ther | Sorafenib inhibited growth and MAPK signalling in malignant peripheral nerve sheath tumour cells. |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical | Am J Pathol | Dedifferentiated liposarcoma xenograft models showing PTEN down-regulation and response to PI3K pathway inhibition. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | Histology-driven therapy for soft tissue sarcomas. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magy Onkol | Medical treatment of soft tissue sarcomas by histological subtype. |

---

## UK Market Information

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0801050AJAAAAAA | Sorafenib 200mg tablets | Sorafenib |
| 0801050AJBBAAAA | Nexavar 200mg tablets | Sorafenib |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC; typically full blood count, liver function, blood pressure |
| Handling Protection | Please refer to the SmPC and local cytotoxic handling policy |

---

## Safety Considerations

- **Drug Interactions** (100 interactions recorded; examples):
  - Major: dolasetron
  - Moderate: famotidine, loperamide, dexamethasone, clarithromycin, levofloxacin, palonosetron, naltrexone and several laxatives (bisacodyl, lactulose, lactitol, sodium picosulfate, polyethylene glycol)
  - Minor: dapagliflozin, metronidazole, naloxegol

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study tests sorafenib in liposarcoma itself. The trials enrol soft tissue sarcoma in general, and the preclinical work involves other tumour types or models. The high TxGNN score (0.9982) is not backed by direct evidence, so the evidence level is L5.

**To proceed, the following is needed:**
- Liposarcoma-specific clinical data, such as subgroup analyses from the existing soft tissue sarcoma trials
- Mechanism of action data for sorafenib
- Preclinical testing of sorafenib in liposarcoma models
- Review of the SmPC warnings, contraindications and interactions for the intended population

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

