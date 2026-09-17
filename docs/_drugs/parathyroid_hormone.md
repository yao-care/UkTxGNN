---
layout: default
title: Parathyroid Hormone
parent: Model Prediction Only (L5)
nav_order: 445
evidence_level: L5
indication_count: 10
---

# Parathyroid Hormone
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

# Parathyroid Hormone: From Original Indication Not Recorded to Migraine Disorder

## One-Sentence Summary

Parathyroid hormone (PTH, DrugBank ID DB05829) currently holds no UK marketing authorisation, and this evidence pack does not record its originally licensed indication or mechanism of action. The TxGNN model flags a possible link to **Migraine Disorder**, but this is supported only by indirect genetic and mechanistic literature — no clinical trial directly tests PTH therapy for migraine, and the overall evidence level is **L5 (algorithmic prediction only)**.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in available data |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for parathyroid hormone in this evidence pack, and its original licensed indication is also not recorded, so a mechanistic comparison between old and new indication cannot be made with confidence.

The predicted association with migraine arises from a 2025 genomic study identifying variants in parathyroid hormone-related peptide (PTHrP) receptors as potential genetic drivers of migraine susceptibility, together with a single 1986 paper on the central nervous system effects of parathormone and calcitonin. Both are genetic-association or mechanistic-observation studies, not treatment studies — neither tests PTH replacement therapy or PTH analogues as a migraine treatment.

The reviewing team's own analysis of this evidence explicitly notes the link is at the gene/mechanism level only, with no direct clinical evidence that PTH pharmacotherapy affects migraine outcomes. The high TxGNN score (99.98%) should therefore be read as a knowledge-graph pattern signal rather than clinical support.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07028684](https://clinicaltrials.gov/study/NCT07028684) | N/A | Recruiting | 20 | Studies foot reflexology massage (not PTH pharmacotherapy) for pain, sleep and quality of life in women with migraine; included only because the disease label matches, not because of drug relevance |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24714817](https://pubmed.ncbi.nlm.nih.gov/24714817/) | 2014 | RCT | Braz J Med Biol Res | RCT of add-on vitamin D with amitriptyline in paediatric migraine — evaluates vitamin D, not parathyroid hormone; relevance to PTH is only via the shared calcium/vitamin D axis |
| [40297711](https://pubmed.ncbi.nlm.nih.gov/40297711/) | 2025 | Review/Genetic | Brain Communications | Identifies PTHrP receptor gene variants as candidate genetic drivers of migraine susceptibility; a genomic association study, not a treatment study |
| [29429076](https://pubmed.ncbi.nlm.nih.gov/29429076/) | 2018 | Review | Neuromolecular Medicine | Reviews the bone–brain axis in multiple sclerosis and osteoporosis; touches on PTH's role in bone–neurological crosstalk, not on migraine treatment |
| [11425281](https://pubmed.ncbi.nlm.nih.gov/11425281/) | 2001 | Review | Medical Hypotheses | Reviews magnesium deficiency pathology, including migraine; does not address PTH pharmacotherapy |
| [31261815](https://pubmed.ncbi.nlm.nih.gov/31261815/) | 2019 | Cohort | Medicina (Kaunas) | Evaluates vitamin D status and treatment response in paediatric migraine — again vitamin D, not PTH |
| [3739765](https://pubmed.ncbi.nlm.nih.gov/3739765/) | 1986 | Case/Mechanistic | Acta Neurologica | Historical paper on central nervous system effects of calcitonin and parathormone; no abstract available, direct relevance to migraine treatment is unclear |

## UK Market Information

Parathyroid hormone currently holds no UK marketing authorisation. `taiwan_regulatory.market_status` is recorded as **Not Marketed**, with **0** authorisations on file in this evidence pack.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

No warnings, contraindications, or drug–drug interaction data were available in this evidence pack (flagged internally as a **Blocking** data gap — missing MHRA/SmPC warnings and contraindications prevent the initial safety review stage from starting).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence quality is very low — L5, prediction-only, with no clinical trial directly testing PTH therapy for migraine and no marketing authorisation in the UK. A blocking data gap on safety warnings and contraindications also prevents even a preliminary safety assessment.

**To proceed, the following is needed:**
- Parathyroid hormone's original licensed indication and mechanism of action (DrugBank/SmPC)
- MHRA/SmPC safety data — key warnings, contraindications, drug interactions — to clear the blocking safety data gap
- Direct preclinical or clinical evidence linking PTH pharmacotherapy (not just PTHrP genetics) to migraine outcomes before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

