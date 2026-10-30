---
layout: default
title: Erythromycin
parent: Model Prediction Only (L5)
nav_order: 256
evidence_level: L5
indication_count: 5
monitor_inn: "Erythromycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "acute contagious conjunctivitis", "exposure keratitis", "lymphogranuloma venereum", "necrotizing ulcerative gingivitis"]
last_modified_at: 2026-10-30
description: "Erythromycin: predicted new indication punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Erythromycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Erythromycin: Macrolide antibiotic (50S ribosomal subunit inhibitor) → 點狀上皮角膜結膜炎 (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## One-Sentence Summary

Erythromycin is a macrolide antibiotic with antibacterial and anti-inflammatory activity. The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials** and only **1 publication** (a general paediatric review) support this direction, so the evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, erythromycin is a macrolide that inhibits bacterial protein synthesis at the 50S ribosomal subunit and also has anti-inflammatory properties. Topical ophthalmic erythromycin is widely used in eye infections, so applying it to an ocular surface disease is plausible.

The only retrieved publication is a review of chronic blepharokeratoconjunctivitis in children, a related but different ocular surface condition that is often associated with staphylococcal disease. It does not study punctate epithelial keratoconjunctivitis itself, so the support is indirect. Because no cited study directly addresses the predicted disease, the evidence level is capped at L5 (model prediction only), despite the pipeline's preliminary L4 label.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Review | Journal of Pediatric Ophthalmology and Strabismus | Describes history, symptoms, clinical signs and treatment of chronic blepharokeratoconjunctivitis in children; a related condition, not the predicted disease itself |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501050C0AAABAB | Erythromycin Tab E/C 250mg | Not recorded | Not recorded |

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Drug interaction records compiled for this report include the following notable entries:
- **Major**: loperamide, clarithromycin
- **Moderate**: for example famotidine, hydrocortisone, pioglitazone, alosetron, aprepitant, dexamethasone, budesonide, cimetidine

Only a subset of the 100 recorded interactions is shown here; check the BNF interaction guidance before prescribing.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no trials and the sole publication is an indirect review of a related condition. There is no direct evidence for punctate epithelial keratoconjunctivitis.

**To proceed, the following is needed:**
- Studies that directly examine erythromycin (topical or systemic) in punctate epithelial keratoconjunctivitis
- Mechanism of action data and a clear rationale for the anti-inflammatory versus antibacterial role
- Review of the SmPC and BNF safety information, including QT-prolongation risk and interaction management, for any ocular or systemic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

