---
layout: default
title: Alfuzosin
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Alfuzosin
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is a selective α₁-adrenergic receptor antagonist, conventionally prescribed for the symptomatic relief of lower urinary tract symptoms associated with benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita**; however, **no clinical trials and no directly relevant published literature** currently support this repurposing direction.
This prediction rests entirely on model inference (Evidence Level L5), and the proposed mechanistic rationale is considered extremely weak given the genetic aetiology of the target condition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign prostatic hyperplasia — symptomatic treatment of lower urinary tract symptoms (based on established pharmacological profile; MHRA licence data not available in this Evidence Pack) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| UK Market Status | Not marketed (no MHRA marketing authorisations on record) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (classified as a high-severity data gap). Based on established pharmacological knowledge, Alfuzosin is a selective α₁-adrenergic receptor antagonist. It acts by competitively blocking α₁ receptors in the smooth muscle of the prostate, bladder neck, and urethra, thereby reducing urethral resistance and improving urine flow in patients with BPH. It has no significant affinity for α₂ receptors and is considered uroselective within the α₁-blocker class.

Ambras Type Hypertrichosis Universalis Congenita is an exceptionally rare congenital disorder characterised by excessive, generalised hair growth across the entire body surface, including the face. It is caused by chromosomal rearrangements affecting the *TRPS1* gene (encoding a GATA-type zinc finger transcription factor at 8q24.12), which dysregulates hair follicle morphogenesis from embryonic development onwards. The theoretical bridge to Alfuzosin rests on the observation that α₁-adrenergic receptors are expressed in arrector pili smooth muscle and dermal papilla vasculature — implying that α₁ blockade could, in principle, modulate follicular microcirculation and hair growth cycling (the anagen–catagen transition).

In practice, however, this mechanistic link is extremely tenuous and unlikely to be clinically actionable. The pathogenesis of Ambras syndrome is driven by a fixed germline genetic defect affecting transcriptional programmes in early hair follicle morphogenesis — a process entirely distinct from the adrenergic regulation of vascular tone in mature follicles. Critically, certain α₁ blockers (notably doxazosin) have been associated with drug-induced hypertrichosis in case reports, suggesting the pharmacological direction may be counterproductive rather than therapeutic. The TxGNN prediction most plausibly reflects indirect node connectivity within the knowledge graph (α₁ receptor → smooth muscle → hair follicle vasculature → hair growth disorder) rather than a biologically coherent repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for this indication.

> **Note:** A separate PubMed search against the third-ranked predicted indication (*malformation syndrome with odontal and/or periodontal component*) returned 20 publications (see below). None of these papers investigate Alfuzosin in the context of periodontal or dental malformation syndromes; they are general periodontology references retrieved by broad disease-keyword matching and do not constitute supporting evidence for drug repurposing. They are listed here for completeness but should not be interpreted as evidence for this candidate.

| PMID | Year | Type | Journal | Note |
|------|------|------|---------|------|
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | Clinical Practice Guideline | J Clin Periodontol | EFP S3 guideline for Stage IV periodontitis treatment — not related to Alfuzosin |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | Review | Diabetologia | Bidirectional relationship between diabetes and periodontitis — not related to Alfuzosin |
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | Systematic Review | Cochrane Database Syst Rev | Periodontal treatment for glycaemic control in diabetes — not related to Alfuzosin |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | Review | Periodontology 2000 | Complications of regenerative periodontal surgery — not related to Alfuzosin |
| [38907216](https://pubmed.ncbi.nlm.nih.gov/38907216/) | 2024 | Review | J Nanobiotechnology | Biomaterial-mediated macrophage immunotherapy in periodontitis — not related to Alfuzosin |
| [39233377](https://pubmed.ncbi.nlm.nih.gov/39233377/) | 2024 | Review | Periodontology 2000 | Sleep disorders as risk factor for periodontal health — not related to Alfuzosin |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | Review | J Dent Res | Role of gingival fibroblasts in periodontitis pathogenesis — not related to Alfuzosin |
| [38362600](https://pubmed.ncbi.nlm.nih.gov/38362600/) | 2024 | Observational | J Dent Res | Oral and gut microbiota changes with periodontal therapy — not related to Alfuzosin |
| [29291254](https://pubmed.ncbi.nlm.nih.gov/29291254/) | 2018 | Cochrane Review | Cochrane Database Syst Rev | Supportive periodontal therapy for dentition maintenance — not related to Alfuzosin |
| [9495612](https://pubmed.ncbi.nlm.nih.gov/9495612/) | 1998 | Observational/Microbiology | J Clin Periodontol | Microbial complexes in subgingival plaque — not related to Alfuzosin |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Data Gap Alert:** MHRA SmPC warning and contraindication data for Alfuzosin were not available in this Evidence Pack (classified as a **Blocking**-severity gap). Drug interaction data returned no records. This gap must be resolved before any clinical feasibility assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications for Alfuzosin carry L5 evidence (model prediction only) with no supporting clinical trials, no relevant literature, no UK marketing authorisation, and mechanistic rationales that range from extremely weak to non-existent. The top-ranked prediction (Ambras Type Hypertrichosis Universalis Congenita) involves a fixed germline genetic disorder with no plausible pharmacological entry point for an α₁-adrenergic blocker. This candidate does not meet the threshold for further investment at this stage.

**To proceed, the following is needed:**

- **Resolve Blocking data gap (DG001):** Obtain MHRA SmPC for Alfuzosin to retrieve approved indication text, warnings, and contraindications — prerequisite for any safety screening
- **Resolve High-severity data gap (DG002):** Confirm full mechanism of action from DrugBank API to enable rigorous mechanistic plausibility scoring
- **Exploratory preclinical scoping:** If continued interest in the hair-disorder cluster, commission a targeted literature review on α₁ receptor expression and function specifically within human hair follicle tissue — current evidence is absent
- **Reconsider candidate prioritisation:** Given that all ten predictions are Hold/L5 and most involve congenital genetic syndromes, consider whether Alfuzosin's known BPH indication offers a stronger repurposing rationale in adjacent genitourinary or smooth muscle conditions (e.g., ureteral spasm, bladder outlet obstruction variants) that may have been missed in the current disease-mapping pipeline
- **Data pipeline review:** The presence of 0 MHRA licences for a drug actively marketed in the UK (Alfuzosin is available as Xatral XL and generics) suggests a potential data ingestion failure in the UK regulatory module that should be investigated and corrected
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

