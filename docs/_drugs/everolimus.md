---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
---

# Everolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using the drug-repurposing evaluation report template directly (no additional skill needed for this content-generation task, since it's a one-off report from a supplied JSON evidence pack following an already-detailed spec).

A note before the report: the evidence pack's `original_indications` and `taiwan_regulatory.licenses` arrays are both empty, so the "original indication" and "UK marketing authorisation" fields cannot be populated from this pack — I've flagged that as a gap rather than guessing at licence numbers (everolimus is in fact marketed in the UK under other brand names for other indications, but that's outside this evidence pack's dataset, so I haven't asserted specific licence details).

---

# Everolimus: From Established mTOR-Inhibitor Oncology Use to Liposarcoma

## One-Sentence Summary

> Everolimus is an mTOR inhibitor already used across a range of oncology indications, although this evidence pack does not itself record its original licensed indication.
> The TxGNN model predicts it may be effective for **Liposarcoma** (specifically dedifferentiated liposarcoma, in combination with a CDK4/6 inhibitor),
> with **1 clinical trial** and **4 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (no licences on file) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| UK Market Status | Not marketed (per this evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on generally established pharmacological knowledge, everolimus is an mTOR inhibitor (rapalog class), a mechanism already exploited across multiple oncology settings; the specific licensed indication(s) held for everolimus are not captured in this dataset.

Dedifferentiated liposarcoma (DDL) is characterised by activation of the Akt–mTOR and MAPK signalling pathways, and frequently by co-occurring MDM2/CDK4 amplification. This provides a direct biological rationale for mTOR-pathway blockade in this tumour type. Critically, the supporting evidence is for **everolimus in combination with the CDK4 inhibitor ribociclib**, not everolimus monotherapy — the two agents have shown synergistic growth inhibition in preclinical tumour models, which is why the Phase II trial below tests the doublet rather than everolimus alone.

The mechanistic link is therefore reasonably strong for the dedifferentiated liposarcoma subtype specifically, but should not be extrapolated to other liposarcoma subtypes without their own supporting data (see, for example, ovarian myxoid liposarcoma among the lower-ranked predictions, which has no clinical or literature support and is driven by a FUS–DDIT3 fusion with no established mTOR link).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Two-centre, two-arm study of ribociclib + everolimus in advanced dedifferentiated liposarcoma (Arm A) and leiomyosarcoma (Arm B), in patients with ≥1 prior systemic therapy; ribociclib 300 mg/day (3 weeks on/1 off) plus everolimus, assessing anti-tumour activity of the doublet. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | RCT (Phase 2, combination) | Clinical Cancer Research | Published results of the ribociclib + everolimus Phase II trial (SAR-096) in advanced dedifferentiated liposarcoma and leiomyosarcoma; rationale based on synergistic growth inhibition of CDK4/6 and mTOR blockade in tumour models. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review (PDOX model) | Frontiers in Oncology | Review of patient-derived orthotopic xenograft sarcoma models identifying effective combination therapies with the CDK inhibitor palbociclib, supporting a CDK/mTOR-pathway rationale in sarcoma. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Mechanistic/preclinical | Tumour Biology | Immunohistochemical and in-vitro analysis of 99 dedifferentiated liposarcoma specimens showing Akt/mTOR and MAPK pathway activation, with antitumour effects observed from an mTOR inhibitor in vitro. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical (different combination) | Anticancer Research | Broad-spectrum preclinical activity of eribulin in liposarcoma models, combined with mechanistically differing anticancer agents; indirect supporting context rather than direct everolimus evidence. |

---

## UK Market Information

Currently no UK marketing authorisation is recorded for everolimus in this evidence pack (0 licences on file, market status "Not marketed"). This should be verified directly against the MHRA products database and BNF before any regulatory or prescribing decision is made, as it may reflect a gap in this dataset rather than confirmed absence of authorisation.

---

## Cytotoxicity

Everolimus is an oncology agent (mTOR inhibitor) and the predicted indication (liposarcoma) is malignant, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor / rapalog) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence currently comes from a single, still-active (not yet fully completed) Phase 2 combination trial and four supporting publications (L2, decision stage S2 — research question), and it supports everolimus **only in combination with ribociclib**, not as monotherapy. A Blocking-severity data gap on TFDA/MHRA label warnings and contraindications means an initial safety review (S1) cannot even be started, and no UK marketing authorisation or safety data are on file.

**To proceed, the following is needed:**
- SmPC-level safety data: key warnings, contraindications, and drug interactions for everolimus (currently a Blocking gap)
- Confirmed mechanism of action and current UK licensed indication(s) for everolimus (currently a High-severity gap)
- Verification of UK marketing authorisation status directly against the MHRA products database, given the discrepancy between this pack's "not marketed" status and everolimus's known use under other brand names
- Maturation and full publication of NCT03114527 (SAR-096) results, since the trial is still active/not recruiting rather than completed
- Explicit confirmation that any repurposing pathway pursued is for the **ribociclib + everolimus combination** in dedifferentiated liposarcoma, not everolimus alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

