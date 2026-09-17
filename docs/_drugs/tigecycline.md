---
layout: default
title: Tigecycline
parent: Model Prediction Only (L5)
nav_order: 575
evidence_level: L5
indication_count: 10
---

# Tigecycline
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

# Tigecycline: From Bacterial Infections to Disorder of Tyrosine Metabolism

## One-Sentence Summary

Tigecycline is a glycylcycline-class antibiotic (a tetracycline derivative) used to treat bacterial infections; the specific UK-approved indication text is not included in this Evidence Pack. The TxGNN model predicts a possible association with **Disorder of Tyrosine Metabolism**, but this is currently supported only by **1 clinical trial** and **4 publications**, none of which actually address tyrosine metabolism — the retrieved evidence instead concerns chronic myeloid leukaemia and mitochondrial biology, suggesting the prediction may be a false positive driven by lexical similarity between "tyrosine metabolism" and "tyrosine kinase".

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this Evidence Pack (known to be a glycylcycline-class antibiotic, per literature) |
| Predicted New Indication | Disorder of Tyrosine Metabolism |
| TxGNN Prediction Score | 95.76% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for tigecycline is not available in this Evidence Pack (flagged as data gap DG002, High severity). Based on the literature retrieved, tigecycline is a glycylcycline-class antibiotic that binds the bacterial 30S ribosomal subunit to inhibit protein synthesis. An off-target effect — inhibition of the human mitochondrial ribosome (mitoribosome) — has also been documented, reducing oxidative phosphorylation (OXPHOS) capacity in certain cell types. This off-target activity has been explored in oncology research, particularly in leukaemia stem cells that depend heavily on mitochondrial metabolism.

However, no biochemical or pharmacological relationship has been established between tigecycline's known mechanisms (ribosomal/mitoribosomal protein synthesis inhibition) and disorders of tyrosine metabolism, which arise from defects in tyrosine-degradation enzymes (e.g. fumarylacetoacetase, tyrosine aminotransferase). None of the retrieved clinical trial or literature evidence discusses tyrosine metabolism, tyrosinaemia, or related enzymatic pathways.

The single associated clinical trial (NCT02883036) and three of the four associated publications instead concern chronic myeloid leukaemia (CML) and BCR-ABL/EGFR tyrosine kinase inhibitor resistance, where mitochondrial OXPHOS inhibition by tigecycline is being studied as an adjunct strategy. This strongly suggests the TxGNN association is a lexical/ontological artefact — conflating "tyrosine metabolism" with "tyrosine kinase" — rather than a genuine mechanistic signal. On current evidence, this candidate should not be considered mechanistically plausible.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02883036](https://clinicaltrials.gov/study/NCT02883036) | N/A | Unknown | 100 | In vitro study of mitochondrial biogenesis/metabolic changes with tigecycline in chronic myeloid leukaemia (CML) models. Relevance graded **C (low)** — concerns CML biology, not tyrosine metabolism disorder; likely a coincidental keyword match. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41009505](https://pubmed.ncbi.nlm.nih.gov/41009505/) | 2025 | In Vitro Study | International Journal of Molecular Sciences | Effects of tigecycline on human epidermal melanocytes and fibroblasts; dermatological pigmentary/phototoxic adverse effects — unrelated to tyrosine metabolism disorders. |
| [28920959](https://pubmed.ncbi.nlm.nih.gov/28920959/) | 2017 | Preclinical (cell line) | Nature Medicine | Tigecycline inhibits mitochondrial OXPHOS to eradicate therapy-resistant CML leukaemic stem cells — mechanistically relevant to CML, not tyrosine metabolism. |
| [29404396](https://pubmed.ncbi.nlm.nih.gov/29404396/) | 2018 | Commentary/Review | Molecular & Cellular Oncology | Author commentary on the above CML leukaemic stem cell/mitochondrial OXPHOS study. |
| [31765940](https://pubmed.ncbi.nlm.nih.gov/31765940/) | 2020 | Preclinical | Neoplasia | SIRT1-targeting eradicates EGFR-TKI-resistant lung adenocarcinoma stem cells via mitochondrial OXPHOS regulation; tigecycline discussed as a mitochondrial translation inhibitor, not in the context of tyrosine metabolism. |

---

## UK Market Information

According to this Evidence Pack, tigecycline currently has **no listed UK marketing authorisations** (0 licences; market status: Not marketed).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: this Evidence Pack has a blocking data gap (DG001) for TFDA/MHRA product-label warnings and contraindications, which currently prevents a formal S1 safety pre-assessment.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score (95.76%) is high, but no clinical trial or literature evidence specifically addresses tyrosine metabolism disorders; the associated evidence instead concerns unrelated CML/tyrosine-kinase-inhibitor-resistance research. The mechanistic rationale is unsupported, and the signal is most plausibly a text/ontology-driven false positive (Evidence Level L5, prediction only).

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for tigecycline (data gap DG002)
- UK/MHRA SmPC warnings, contraindications and safety data (data gap DG001, **blocking** — currently prevents any safety pre-assessment)
- Independent biochemical/pharmacological review to confirm or definitively rule out any tyrosine-metabolism hypothesis before further investment
- Note: among the 10 candidates in this Evidence Pack, rank 10 ("monoclonal gammopathy", Evidence Level L4, decision stage S1, recommendation "Research Question") is supported by two independent in vitro studies on tigecycline's anti-myeloma mitochondrial mechanism and may warrant separate evaluation as a more promising repurposing lead than the top-ranked candidate above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

