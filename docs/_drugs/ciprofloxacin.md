---
layout: default
title: Ciprofloxacin
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Ciprofloxacin
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

# Ciprofloxacin: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

> Ciprofloxacin is a broad-spectrum fluoroquinolone antibiotic, originally developed for the treatment of bacterial infections.
> The TxGNN model predicts it may be effective for **Diffuse Scleroderma**,
> but this is currently supported by **no registered clinical trials** and only **2 publications**, one of which addresses a secondary gastrointestinal complication rather than the disease itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (broad-spectrum fluoroquinolone antibiotic); specific licensed indication text is not available in the current dataset |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold (flagged internally as a "Research Question" — early-stage hypothesis, not yet actionable) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for ciprofloxacin is not available in this evidence pack. Based on general pharmacological knowledge, ciprofloxacin is a fluoroquinolone antibiotic that works by inhibiting bacterial DNA gyrase and topoisomerase IV, thereby blocking bacterial DNA replication. Its efficacy against a wide range of gram-negative and some gram-positive bacterial infections is well established.

Diffuse scleroderma, however, is an autoimmune connective tissue disorder characterised by microvascular injury and progressive skin/organ fibrosis — a pathology driven by immune dysregulation and fibroblast activity, not bacterial infection. There is no well-established mechanistic pathway linking DNA gyrase inhibition to antifibrotic activity, and the supporting literature itself does not propose one; one source tested ciprofloxacin empirically for a possible antifibrotic effect, while the other only addresses a secondary gut complication (bacterial overgrowth) that can occur in some scleroderma patients, using antibiotics to manage that complication rather than the underlying fibrotic disease.

In short, this prediction should be read as a data-driven hypothesis surfaced by the model rather than one grounded in a confirmed mechanistic rationale. It may warrant a research question, but the mechanistic case for repurposing is currently weak.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Randomised, double-blind controlled trial (small) | The Journal of Dermatology | Tested whether oral ciprofloxacin reduces the severity of skin fibrosis in scleroderma patients; the available abstract describes the study design but the outcome is not stated in the excerpt provided. |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Cohort/diagnostic study | British Journal of Rheumatology | Investigated small bowel bacterial overgrowth (a gastrointestinal complication of systemic sclerosis) and antibiotic treatment outcomes; addresses a secondary complication, not the fibrotic disease itself. |

---

## UK Market Information

Currently no marketing authorisation records are available for ciprofloxacin in this dataset (0 licences recorded; market status: Not Marketed). This should be verified directly against the MHRA product register and BNF before any regulatory conclusions are drawn, as ciprofloxacin is a long-established generic antibiotic and this may reflect a gap in the current dataset rather than an actual absence from the UK market.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(No structured safety data — warnings, contraindications, or drug interactions — were available in this evidence pack; this is flagged as a Blocking data gap below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence base is limited to L4 (mechanism/small clinical study level): there are no registered clinical trials for ciprofloxacin in diffuse scleroderma, and only two publications, one of which is only indirectly relevant (a gut complication, not the fibrotic disease itself).
- No established mechanistic pathway connects ciprofloxacin's antibacterial action to an antifibrotic effect, so the biological rationale for this specific prediction remains unconfirmed.
- Critical safety data (SmPC warnings, contraindications, drug interactions) and UK marketing authorisation status are both missing from this evidence pack — the missing safety/label data is flagged as a **Blocking** severity data gap in the source pack, meaning safety review cannot proceed until it is resolved.

**To proceed, the following is needed:**
- MHRA/SmPC-sourced warnings, contraindications and interaction data for ciprofloxacin (currently a Blocking data gap)
- Confirmed mechanism of action data, ideally including any proposed antifibrotic pathway (currently a High-severity data gap)
- Verification of current UK marketing authorisation status, since ciprofloxacin is a well-established generic and the "Not Marketed" status recorded here should be reconciled with the MHRA register
- A dedicated, adequately powered clinical trial in diffuse scleroderma before this candidate can move beyond the research-question stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

