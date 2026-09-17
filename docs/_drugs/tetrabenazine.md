---
layout: default
title: Tetrabenazine
parent: Model Prediction Only (L5)
nav_order: 567
evidence_level: L5
indication_count: 10
---

# Tetrabenazine
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

# Tetrabenazine: From Huntington's Disease Chorea to Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)

## One-Sentence Summary

Tetrabenazine is a VMAT2 (vesicular monoamine transporter 2) inhibitor internationally used to reduce chorea associated with Huntington's disease. The TxGNN model predicts a possible association with **Polycystic Kidney Disease 3, with or without Polycystic Liver Disease**, but this candidate is currently supported by **0 clinical trials** and **20 background publications that describe the disease itself rather than Tetrabenazine-specific evidence**, placing it at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this Evidence Pack (`original_indications` is empty); internationally used for Huntington's disease-associated chorea, as referenced within the supporting trial evidence for this candidate |
| Predicted New Indication | Polycystic Kidney Disease 3, with or without Polycystic Liver Disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is not available in this Evidence Pack (`original_moa: [Data Gap]`). However, the accompanying rationale for this candidate notes that Tetrabenazine is a known VMAT2 inhibitor, which depletes presynaptic monoamine neurotransmitters (dopamine, serotonin, noradrenaline). This pharmacology underlies its established use in hyperkinetic movement disorders such as Huntington's disease-associated chorea.

Polycystic kidney disease and polycystic liver disease, in contrast, are driven by an entirely different pathophysiological pathway — mutations in genes such as *PKD1*, *PKD2*, and *PKHD1* leading to primary cilia dysfunction and progressive cyst formation in the kidney and liver. There is no established pharmacological or molecular link between central monoamine depletion and renal/hepatic cystogenesis.

Consistent with this, the Evidence Pack's own mechanistic assessment for this candidate explicitly finds no plausible pathway connecting VMAT2 inhibition to ciliopathy-driven cyst formation. All 20 supporting literature items describe the natural history, genetics, diagnosis, or clinical management of polycystic kidney/liver disease itself — none mention Tetrabenazine or VMAT2 pathways. This pattern is consistent with disease-keyword co-occurrence noise in the underlying knowledge graph rather than a genuine drug-repurposing signal, and the same weak-evidence pattern (L4–L5, "Hold") recurs across the other nine predicted indications for this candidate in the wider evidence set.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Guideline | Am J Gastroenterol | ACG clinical guideline on focal liver lesions, including management of polycystic liver disease |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | J Hepatol | EASL clinical practice guidelines on the management of cystic liver diseases |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | Comprehensive review of ADPKD pathophysiology, genetics, and extrarenal manifestations |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | Review of the ADPKD/polycystic liver disease clinical course; notes tolvaptan (not Tetrabenazine) as an approved treatment |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | J Am Soc Nephrol | Genetic complexity and gene overlap between ADPKD and autosomal dominant polycystic liver disease |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Adv Kidney Dis Health | Genetic spectrum of *PKD1*/*PKD2* mutations and resulting phenotypes |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Review | Annu Rev Pathol | Mechanistic understanding and treatment advances in polycystic liver disease |
| [36200122](https://pubmed.ncbi.nlm.nih.gov/36200122/) | 2022 | Review | Hepat Med | Overview of pathophysiology, diagnosis, and treatment of polycystic liver disease |
| [28375157](https://pubmed.ncbi.nlm.nih.gov/28375157/) | 2017 | Basic Science | J Clin Invest | Whole-exome sequencing identifies effectors of polycystin-1 function in isolated polycystic liver disease |
| [37266470](https://pubmed.ncbi.nlm.nih.gov/37266470/) | 2023 | Case Report | Maedica | Case report of ADPKD/adult polycystic liver disease associated with advanced gastric cancer |

**Note:** None of the above literature mentions Tetrabenazine, VMAT2, or any pharmacological intervention relevant to this drug. All items describe the natural history, genetics, or clinical management of polycystic kidney/liver disease itself.

---

## UK Market Information

Tetrabenazine currently holds no marketing authorisation on record in this Evidence Pack (market status: Not Marketed; 0 licenses).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- This candidate sits at evidence level L5 (model prediction only), with zero drug-specific clinical trials and literature limited entirely to disease background rather than Tetrabenazine-specific data. The Evidence Pack's own mechanistic assessment finds no plausible pathway linking VMAT2 inhibition to renal/hepatic cystogenesis, and this lack of support is consistent across the broader set of predicted indications for this drug.

**To proceed, the following is needed:**
- MHRA/SmPC-sourced key warnings and contraindications (currently a Blocking data gap, DG001)
- Confirmed mechanism-of-action data via DrugBank (currently a High-severity data gap, DG002)
- Drug-specific preclinical or mechanistic studies linking the VMAT2 pathway to ciliopathy/cystogenesis, should this hypothesis be pursued further
- Clarification of Tetrabenazine's current UK licensing/marketing status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

