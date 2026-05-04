---
layout: default
title: Capreomycin
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Capreomycin
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

# Capreomycin: From Tuberculosis to Gout

## One-Sentence Summary

Capreomycin is a second-line antimycobacterial antibiotic with an established role in the treatment of multidrug-resistant tuberculosis (MDR-TB).
The TxGNN model predicts it may be effective for **Gout**, ranking it first across 10 predicted indications with a prediction score of 99.91%.
However, **no clinical trials** and **no published literature** currently support this repurposing direction, placing this prediction at the lowest evidence level (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multidrug-resistant tuberculosis (MDR-TB) — second-line agent |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Capreomycin is a cyclic polypeptide antibiotic that inhibits bacterial protein synthesis by binding to the prokaryotic 70S ribosomal subunit (interacting with both 30S and 50S subunits to inhibit translocation). It is active almost exclusively against *Mycobacterium* species and is reserved as a second-line injectable agent for drug-resistant tuberculosis.

Gout is a metabolic disorder characterised by hyperuricaemia, monosodium urate crystal deposition in joints and soft tissues, and recurrent episodes of acute inflammatory arthritis. This pathophysiological process — rooted in purine metabolism dysregulation and uric acid handling — is entirely distinct from mycobacterial infection. There is no established mechanistic link between ribosomal protein synthesis inhibition and uric acid metabolism or neutrophil-driven crystal-induced inflammation. The repurposing rationale notes that Capreomycin's known nephrotoxicity could theoretically impair renal uric acid excretion, but this represents an adverse-effect pathway rather than a therapeutic mechanism, and would be expected to *worsen* hyperuricaemia rather than ameliorate it.

Established, well-tolerated therapies for gout (allopurinol, febuxostat for urate-lowering; colchicine and NSAIDs for acute flares) already address the key unmet needs, substantially reducing the motivation for repurposing. The high TxGNN score (99.91%) most likely reflects structural connectivity within the knowledge graph — for example, shared disease-node neighbourhoods with other inflammatory or musculoskeletal conditions — rather than genuine mechanistic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Capreomycin holds **no MHRA marketing authorisations** and is **not currently marketed** in the United Kingdom. It does not appear in the BNF as an active licensed product for UK prescribing. Any future repurposing effort would require a de novo regulatory pathway — either a full Marketing Authorisation Application (MAA) submitted to the MHRA, or consideration under the Innovative Licensing and Access Pathway (ILAP) — in addition to clinical evidence generation.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Note for clinical reviewers:** Although formal safety data was not available in this Evidence Pack, Capreomycin's established toxicity profile from its TB indication includes **nephrotoxicity** (tubular damage, electrolyte wasting) and **ototoxicity** (vestibular and cochlear). These risks are particularly pertinent when evaluating any chronic-use indication such as gout, and must be formally characterised before any further development is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score to gout (99.91%), there is no clinical trial evidence, no supporting literature, and no plausible mechanistic pathway linking Capreomycin's mode of action to the pathophysiology of gout. The known toxicity profile — including nephrotoxicity — is particularly unfavourable for a condition in which long-term treatment is often required and renal function is already a key determinant of uric acid clearance. All ten predicted indications in this pack are L5 / Hold, indicating a systemic absence of translational evidence for this candidate.

**To proceed, the following would be needed:**

- Detailed mechanism of action data (MOA) to identify any indirect pathway between protein synthesis inhibition and uric acid metabolism or inflammatory signalling
- Preclinical (in vitro or in vivo) data demonstrating any measurable effect on serum uric acid levels, xanthine oxidase activity, or NLRP3 inflammasome activation
- A compelling clinical unmet need justification, given the availability of multiple safe and effective standard-of-care therapies for gout
- Complete safety data (SmPC, key warnings, contraindications, DDI profile) to enable a full risk–benefit assessment
- A regulatory strategy to address the complete absence of MHRA marketing authorisation in the United Kingdom

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application to patient care. This report was produced using the TxGNN drug repurposing prediction platform (Evidence Pack v4, data cut-off: 5 April 2026).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

