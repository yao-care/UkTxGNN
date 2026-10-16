---
layout: default
title: Mesalazine
parent: Model Prediction Only (L5)
nav_order: 396
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Mesalazine: predicted new indication Congenital hypotrichosis with juvenile macular dystrophy (evidence level L5). Approved use: Ulcerative colitis, inflammatory bowel disease…"
---

# Mesalazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Mesalazine: From Ulcerative Colitis to Congenital Hypotrichosis with Juvenile Macular Dystrophy

## One-Sentence Summary

Mesalazine (5-aminosalicylic acid) is an anti-inflammatory drug originally used to treat ulcerative colitis and other inflammatory bowel conditions.
The TxGNN model predicts it may be effective for **congenital hypotrichosis with juvenile macular dystrophy**, but **no clinical trials and no publications** currently support this prediction. The score is a graph-based prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis, inflammatory bowel disease, ulcerative proctosigmoiditis (the licence record held no indication text) |
| Predicted New Indication | Congenital hypotrichosis with juvenile macular dystrophy |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, mesalazine is an aminosalicylate with anti-inflammatory activity (COX/LOX inhibition, PPAR-gamma activation and NF-kB modulation). Its efficacy in ulcerative colitis is well established.

The predicted indication is an ultra-rare genetic disorder caused by CDH3 (cadherin-3) mutations, affecting hair follicle and retinal development. It is a structural defect, not an inflammatory disease. We could identify no plausible mechanistic link between mesalazine's anti-inflammatory action and this condition.

The high score (0.996) should be read as a statistical artefact of the knowledge graph, not as evidence of benefit. For context, the other top-ranked predictions are also weakly supported:

- **Osteoarthritis (rank 2):** only a computational target-identification paper, with no clinical data. Oral mesalazine acts mostly locally in the colon, with low systemic exposure.
- **Rheumatoid arthritis (rank 3):** indirect evidence from sulfasalazine, which releases mesalazine. Its antirheumatic effect is generally attributed to the sulfapyridine moiety or the intact parent compound, not mesalazine. Mesalazine alone has not been shown to work in rheumatoid arthritis.
- **Seborrheic keratosis, osteoarthritis susceptibility, vulvar inverted follicular keratosis and pseudoachondroplasia (ranks 4-7):** no trials, no literature and no plausible mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the predicted indication.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0105010B0AAAIAI (BNF section 1.5.1 code) | Mesalazine 500 mg modified-release tablets | Modified-release tablet | Not recorded in the data compiled |

Mesalazine sits in BNF chapter 1.5 (aminosalicylates for inflammatory bowel disease). The identifier above appears to be a BNF-style product code rather than a standard MHRA PL number, so the PL number should be confirmed against the MHRA register.

---

## Safety Considerations

- **Contraindications and warnings from the labelling:** not available in the data compiled for this report. Please refer to the SmPC and BNF.
- **Conditions linked to mesalazine by the knowledge graph (not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia), pyloric stenosis, lipoid nephrosis and interstitial nephritis. These indicate a need for caution, especially around renal, hepatic and haematological monitoring, and should be verified against the SmPC.
- **Drug interactions (100 recorded; examples):**
  - **Major:** cidofovir; human botulinum neurotoxin A/B immune globulin.
  - **Moderate:** NSAIDs (ketorolac, ibuprofen, celecoxib, bromfenac); nephrotoxic agents (acyclovir, amphotericin B and its lipid formulations, amikacin, bacitracin, capreomycin, cisplatin); azathioprine; sulfonylureas (acetohexamide, chlorpropamide); anisindione.
  - Many of these relate to additive nephrotoxicity or myelosuppression.
- **Pharmacovigilance literature on 5-ASA:** case reports describe 5-ASA-induced colitis and DRESS syndrome with acute renal failure.

Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. There are no trials or publications, and no plausible mechanism links mesalazine to a CDH3-related genetic disorder of hair and retina. The evidence level is L5.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis, supported by preclinical data (for example, cell or animal models of CDH3 deficiency)
- Mechanism of action data for mesalazine
- Complete SmPC warnings and contraindications, and confirmation of the MHRA licence details and approved indication
- Clinical or case-level evidence in the target population, given that the condition is ultra-rare
- If repurposing is pursued, prioritise predictions with clinical rationale, such as inflammatory joint disease, over this lower-plausibility candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

