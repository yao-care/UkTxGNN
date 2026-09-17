---
layout: default
title: Sorafenib
parent: High Evidence (L1-L2)
nav_order: 535
evidence_level: L2
indication_count: 10
---

# Sorafenib
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

# Sorafenib: From Hepatocellular/Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Sorafenib is an oral multi-kinase inhibitor whose established uses (evident from the supporting literature in this pack) include hepatocellular carcinoma and renal cell carcinoma. The TxGNN model predicts it may also be effective for **Liposarcoma**, with **2 clinical trials** and **8 publications** currently identified, though none are subtype-specific to liposarcoma.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available as a formal licence record in this pack (no UK marketing authorisation held). Literature within the pack indicates established use in hepatocellular carcinoma (PMID 40716153) and renal cell carcinoma (multiple RCC trials, e.g. NCT01613846, NCT00378703) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The formal `original_moa` field for sorafenib is a data gap (DG002) in this evidence pack. However, the supporting literature it contains is informative: PMID 15466206 describes sorafenib (BAY 43-9006) as a bi-aryl urea inhibiting Raf-1 and both wild-type and V599E-mutant BRAF, alongside broad activity against receptor tyrosine kinases involved in angiogenesis and tumour progression (VEGFR, PDGFR, FLT3, c-KIT). This dual anti-proliferative (RAF/MEK/ERK) and anti-angiogenic (VEGFR/PDGFR) mechanism is well documented across the pack's evidence for hepatocellular and renal cancers.

Soft tissue sarcomas, including liposarcoma, are recognised as angiogenesis-dependent tumours, and dedifferentiated liposarcoma specifically has been linked to PTEN down-regulation and PI3K pathway activation (PMID 23416162). Since sorafenib's VEGFR/PDGFR-blocking activity is mechanistically relevant to sarcoma vascular dependence, and sorafenib has already shown activity signals in other soft-tissue and bone sarcomas (osteosarcoma, Ewing/Ewing-like sarcoma per the rationale notes), extension to liposarcoma is biologically plausible.

That said, the strongest direct clinical evidence (NCT00217620, a completed Phase 2 trial, and the Phase 2 SARC024 trial) was conducted in broad "advanced soft tissue sarcoma" populations rather than liposarcoma specifically, and SARC024 tested regorafenib (a related but distinct multi-kinase inhibitor), not sorafenib itself. The mechanistic case is reasonable, but subtype-specific clinical confirmation is still lacking.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | "BAY-9006" (sorafenib) tested in advanced soft tissue sarcomas broadly, not liposarcoma-specific; rationale based on VEGFR/PDGFR and angiogenesis blockade |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 protocol testing **regorafenib** (a related but distinct multi-kinase inhibitor, not sorafenib) across selected sarcoma subtypes; indirect reference value only |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | RCT | Cancer | Phase 2 SWOG-directed intergroup trial (S0505) of sorafenib in advanced soft tissue sarcoma; sorafenib targets RAF, VEGFR1-3, PDGFR-B, FLT3 and c-KIT, pathways relevant to STS |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Soft tissue sarcoma treatment increasingly guided by histological subtype; targeted agents alongside doxorubicin/ifosfamide backbone |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology-driven therapy for soft tissue sarcoma; notes trabectedin has "exceedingly high activity in myxoid liposarcoma" specifically, distinct from sorafenib's broader STS role |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Molecular Cancer Therapeutics | Sorafenib inhibited growth and MAPK signalling in both MPNST and dedifferentiated liposarcoma (LS141, DDLS) cell lines |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical/Xenograft | American Journal of Pathology | Novel dedifferentiated liposarcoma xenograft models show PTEN down-regulation as a malignant signature, suggesting susceptibility to PI3K-pathway-adjacent targeted agents |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review (pending classification) | Frontiers in Oncology | Sarcoma PDOX mouse models identify effective combination therapies with the CDK inhibitor palbociclib; supports rationale for targeted-agent combinations in sarcoma |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Pending classification | Annals of Surgical Oncology | Phase I trial of neoadjuvant radiotherapy plus sorafenib in locally advanced extremity soft tissue sarcoma, based on synergy between anti-angiogenic therapy and radiotherapy |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Pending classification | Anti-Cancer Drugs | Case report of response to trabectedin (not sorafenib) in synovial sarcoma with lung metastases; documents that trabectedin's activity is most established in liposarcoma/leiomyosarcoma |

## UK Market Information

Sorafenib does not currently hold a UK marketing authorisation in this evidence pack (market status: **Not marketed**; 0 authorisations on record). No licence or SmPC indication text is available to summarise.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (small-molecule multi-kinase inhibitor of RAF/MEK/ERK and VEGFR/PDGFR/FLT3/c-KIT) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Liver function tests, blood pressure, full blood count, skin assessment (hand-foot skin reaction is a recognised class effect), thyroid function |
| Handling Protection | Please refer to the SmPC and local hazardous medicinal products handling policy |

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: key warnings, contraindications and drug-drug interaction data for sorafenib were flagged as a blocking data gap (DG001) in this evidence pack and could not be summarised here.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for liposarcoib is limited to L2 (one completed Phase 2 trial, graded "B" relevance, conducted in broad soft-tissue sarcoma populations rather than liposarcoma specifically), and a blocking data gap on TFDA/SmPC warnings and contraindications (DG001) prevents a preliminary safety assessment. Sorafenib also holds no current UK marketing authorisation.

**To proceed, the following is needed:**
- SmPC warnings, contraindications and full DDI profile (resolves DG001, currently blocking)
- Confirmed formal mechanism of action record from DrugBank (resolves DG002)
- Liposarcoma-subtype-specific trial data (current trials are broad STS populations, or in the case of SARC024 test a related drug, regorafenib, not sorafenib itself)
- Confirmation of UK regulatory pathway/import status given the drug is not currently marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

