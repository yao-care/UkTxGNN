---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Rivaroxaban
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

# Rivaroxaban: From Anticoagulation to Rheumatoid Arthritis

## One-Sentence Summary

Rivaroxaban is a direct oral anticoagulant (DOAC) and selective Factor Xa inhibitor, established in clinical practice for prevention and treatment of venous thromboembolism and stroke prevention in non-valvular atrial fibrillation.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **no clinical trials** and **3 publications** currently identified — none of which directly investigate rivaroxaban as a treatment for RA.
Overall, the evidence base for this predicted repurposing is at the earliest possible stage, and significant data gaps remain in this Evidence Pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack (UK MHRA licensing data not retrieved — see note below) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| UK Market Status | Not available in this Evidence Pack (data gap) |
| Number of Marketing Authorisations | 0 (data gap — see note below) |
| Recommended Decision | Hold |

> **Important data gap**: This Evidence Pack contains no MHRA marketing authorisation records for rivaroxaban. In practice, rivaroxaban is widely marketed in the United Kingdom as **Xarelto®** (Bayer/Janssen-Cilag) under multiple MHRA licences across cardiovascular and thromboembolic indications. The pipeline data source requires correction before any formal regulatory assessment can proceed.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, rivaroxaban is a highly selective, direct inhibitor of coagulation Factor Xa — the convergence point of the intrinsic and extrinsic coagulation pathways. By occupying the active site of Factor Xa, it prevents the conversion of prothrombin to thrombin, thereby interrupting downstream fibrin clot formation without requiring antithrombin as a cofactor, unlike heparins.

The theoretical mechanistic link to rheumatoid arthritis runs as follows: suppression of Factor Xa reduces thrombin generation, which in turn limits the activation of protease-activated receptors PAR-1 and PAR-2 expressed on synovial fibroblasts and infiltrating immune cells. Experimental work has demonstrated that PAR activation in the synovium promotes the release of pro-inflammatory cytokines — in particular IL-6 and TNF-α — which are central mediators of the pannus formation and cartilage destruction characteristic of RA. By blunting this coagulation-driven inflammatory amplification loop, rivaroxaban could theoretically attenuate synovitis.

This connection must be clearly contextualised: it is a molecular-level hypothesis that has not been validated in preclinical RA models or human subjects. The TxGNN prediction score of 0.9957 most likely reflects connections between the Factor Xa → PAR → inflammation pathway nodes within the knowledge graph, rather than any direct clinical evidence. None of the three publications retrieved in the literature search investigate rivaroxaban for RA; they address VTE management, thrombin generation assays in autoimmune disease generally, and DOAC adherence in atrial fibrillation. This repurposing hypothesis requires basic science validation before any clinical development consideration.

---

## Clinical Trial Evidence

Currently no clinical trials investigating rivaroxaban for rheumatoid arthritis have been registered on ClinicalTrials.gov or the WHO ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Laboratory/Methodology Study | La Revue de médecine interne | Thrombin generation assay evaluated as a tool for assessing hypercoagulability in autoimmune diseases, including antiphospholipid syndrome — provides indirect contextual support for the coagulation–inflammation interface, but does not study rivaroxaban in RA |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Comprehensive review of lower extremity venous thromboembolism diagnosis and management — general anticoagulation background only; no relevance to RA |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Retrospective Cohort | PLoS ONE | Real-world adherence comparison of rivaroxaban versus apixaban in non-valvular atrial fibrillation — no relevance to RA |

> **Caveat**: None of the three publications directly support a role for rivaroxaban in treating rheumatoid arthritis. Their retrieval reflects keyword overlap in the database query rather than substantive evidentiary support for this repurposing hypothesis.

---

## UK Market Information

No MHRA marketing authorisation records are available in this Evidence Pack for rivaroxaban. This constitutes a data gap that must be resolved before regulatory review can proceed.

For reference, rivaroxaban (Xarelto®) is established in the UK market across several licensed indications. Clinicians should consult the current MHRA product database, the approved Summary of Product Characteristics (SmPC), and the British National Formulary (BNF — Section 2.8.2, Oral anticoagulants) for authoritative prescribing information.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug-drug interaction records) is available in this Evidence Pack.

Please refer to the current **SmPC** and **BNF** for full safety information on rivaroxaban. Report suspected adverse reactions via the **[Yellow Card Scheme](https://yellowcard.mhra.gov.uk/)**.

Additionally, clinicians should be aware that TxGNN also predicts a potential role for rivaroxaban in HIV infectious disease (ranked 3rd, score 99.17%). The existing literature in that prediction cluster highlights a clinically significant drug-drug interaction: the HIV pharmacokinetic boosters **ritonavir** and **cobicistat** are potent inhibitors of both CYP3A4 and P-glycoprotein, and have been shown to increase rivaroxaban AUC by approximately 2–3 fold, substantially elevating bleeding risk. This interaction is documented in completed clinical trial NCT00786422 (EINSTEIN CYP cohort, Phase 2) and multiple case reports. Any future evaluation of rivaroxaban in inflammatory or immune-mediated indications must account for potential co-prescribing scenarios in immunocompromised patients.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for rivaroxaban in rheumatoid arthritis is at Level 5 — model prediction only, with no supporting clinical trials and no directly relevant publications. The proposed mechanistic link via PAR-mediated synovial inflammation is scientifically interesting but entirely unvalidated. In addition, this Evidence Pack contains critical data gaps (MOA, UK regulatory data, and safety information) that preclude any meaningful safety or regulatory assessment at this stage.

**To proceed, the following is needed:**

- **Resolve the UK regulatory data gap**: Retrieve MHRA marketing authorisation records and the current SmPC for rivaroxaban via the MHRA product database
- **Retrieve full safety information**: Download and parse the SmPC to populate key warnings, contraindications, and DDI data before any safety screen can be completed
- **Preclinical validation**: Commission or identify in vitro studies and animal model data examining Factor Xa inhibition in synovial fibroblast inflammation or established RA models (e.g., collagen-induced arthritis) — this is a prerequisite before forming a clinical hypothesis
- **Mechanistic review**: Formal evaluation of the PAR-1/PAR-2 coagulation–inflammation axis in RA pathogenesis, conducted by a rheumatologist and clinical pharmacologist in collaboration
- **Expert consultation**: Input from a rheumatology specialist to assess whether the coagulation–inflammation hypothesis is scientifically plausible enough to justify any further investment in this repurposing programme

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require rigorous clinical validation before any therapeutic application. All content should be interpreted in conjunction with current MHRA guidance, the approved SmPC, and BNF recommendations.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

