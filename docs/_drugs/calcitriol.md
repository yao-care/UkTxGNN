---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 7
---

# Calcitriol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Calcitriol: From Calcium and Bone Metabolism Disorders to Hereditary Hypophosphatemic Rickets

## One-Sentence Summary

Calcitriol is the biologically active form of vitamin D3 (1,25-dihydroxyvitamin D3), used globally for calcium and phosphate homeostasis disorders — though no UK marketing authorisations were identified in this Evidence Pack.
The TxGNN model predicts it may be effective for **Hereditary Hypophosphatemic Rickets**, with **7 clinical trials** and **20 publications** currently supporting this direction.
This indication carries **Evidence Level L1** — the strongest category — making it the most actionable repurposing signal in this analysis.

> **Note on TxGNN rankings**: The top-ranked prediction (rank 1, score 99.96%) is "obsolete vitamin D deficiency" — an OMIM/Mondo ontology term that has been formally deprecated and carries no clinical trials or literature. This report therefore focuses on **Hereditary Hypophosphatemic Rickets (rank 7, score 99.28%)**, which holds the highest evidence level (L1) and the only "Proceed with Guardrails" recommendation in the dataset.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No UK marketing authorisation identified in this dataset |
| Predicted New Indication | Hereditary Hypophosphatemic Rickets |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L1 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Calcitriol in this Evidence Pack. Based on established pharmacology, Calcitriol is the biologically active metabolite of vitamin D3, produced in the kidney by the enzyme 1α-hydroxylase acting on 25-hydroxyvitamin D3. It signals through the nuclear vitamin D receptor (VDR), which is widely expressed in intestinal epithelium, renal tubular cells, osteoblasts, and parathyroid cells, and regulates whole-body calcium and phosphate homeostasis.

Hereditary hypophosphataemic rickets — most commonly X-linked hypophosphataemia (XLH), caused by loss-of-function mutations in the *PHEX* gene — is characterised by pathological excess of the hormone fibroblast growth factor 23 (FGF23), secreted by osteocytes. Elevated FGF23 simultaneously suppresses renal 1α-hydroxylase activity (reducing endogenous calcitriol synthesis) and downregulates proximal tubular phosphate co-transporters (NaPi-IIa/IIc), causing chronic renal phosphate wasting. The result is defective skeletal mineralisation presenting as rickets in children and osteomalacia in adults, compounded by inappropriately low calcitriol levels despite hypophosphataemia.

Exogenous calcitriol directly bypasses FGF23-mediated suppression of 1α-hydroxylase, restoring VDR signalling, increasing intestinal absorption of both calcium and phosphate, and correcting the functional calcitriol deficiency that underlies the mineralisation defect. Combined with oral phosphate supplementation, this approach has been the internationally recognised standard of care for XLH for over 40 years, supported by Phase 3 and Phase 4 clinical trials and endorsed by current international guidelines (Lancet 2024; Calcified Tissue International 2025). The TxGNN model's high prediction score (99.28%) accurately reflects this well-established mechanistic and clinical relationship.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | Dose optimisation RCT comparing high vs low dose active vitamin D (calcitriol/alfacalcidol) combined with neutral phosphate in children with XLH — primary objective is to establish evidence-based weight-adjusted dosing for the established standard of care |
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Active, Not Recruiting | 20 | Calcitriol monotherapy (without phosphate co-administration) in adults and children with XLH — dose escalated over 3 months; examines effects on serum phosphate, skeletal mineralisation, growth, and nephrocalcinosis risk |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | Active, Not Recruiting | 27 | Randomised controlled trial of INZ-701 (ENPP1 enzyme replacement therapy) in ENPP1 deficiency — calcitriol + phosphate serves as the active comparator arm, providing Phase 3-level effectiveness data for standard therapy |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A | Completed | 260 | Completed observational study (April 2022) investigating FGF23 hypersecretion across hypophosphataemia aetiologies — mechanistically confirms calcitriol deficiency as a direct downstream consequence of FGF23 excess in hereditary rickets |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A | Unknown | 150 | Cross-sectional study of FGF23, Klotho, and sclerostin in kidney stone formers — provides background mechanistic data on phosphate-calcitriol-FGF23 axis relevant to the broader disease biology |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Clinical Study | N Engl J Med | Landmark study in 11 children with vitamin D-resistant rickets: calcitriol + phosphate raised intestinal phosphate absorption and serum calcitriol above normal, outperforming ergocalciferol + phosphate; reduced supplemental phosphate requirements in some patients |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical Study | J Clin Invest | High-dose calcitriol (mean 68.2 ng/day) + phosphorus healed coexistent osteomalacia in 5 XLH patients who had failed conventional vitamin D therapy — established calcitriol's unique role in correcting bone disease beyond rickets |
| [2492895](https://pubmed.ncbi.nlm.nih.gov/2492895/) | 1989 | Clinical Study | Calcified Tissue Int | 17 children with familial hypophosphataemia: axial and appendicular bone mineral density improved at 6-month intervals following calcitriol + phosphate initiation — early quantitative evidence for skeletal mineralisation benefit |
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Review | Lancet | Comprehensive Lancet review of XLH: FGF23-driven suppression of calcitriol synthesis confirmed as the central mechanistic link; calcitriol + phosphate remains foundational first-line therapy alongside emerging anti-FGF23 monoclonal antibody burosumab |
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Clinical Guidelines | Calcified Tissue Int | Current XLH diagnosis and therapy guidelines: active vitamin D (calcitriol) + phosphate is the established standard; discusses transition criteria to burosumab for eligible patients |
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | Systematic review of vitamin D analogues across rickets subtypes: calcitriol and alfacalcidol are the active metabolites of choice in FGF23-mediated hypophosphataemic rickets; pharmacokinetic distinctions discussed |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Clinical Study | Pediatr Endocrinol Rev | 127 XLH patients from 49 European centres: early initiation of calcitriol + phosphate associated with improved height outcomes; documents the pre-burosumab treatment landscape relevant to UK paediatric practice |
| [38988138](https://pubmed.ncbi.nlm.nih.gov/38988138/) | 2024 | Clinical Study | J Bone Miner Res | Detailed case series of hypophosphataemic rickets: biochemical algorithm including FGF23, TmP/GFR, and calcitriol levels confirms the diagnostic and therapeutic pathway; calcitriol supplementation integral to management |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Cohort Study | J Endocrinol Invest | Retrospective cohort documenting growth from birth to adulthood in hereditary hypophosphataemic rickets — quantifies clinical burden including short stature and disproportionate body habitus, supporting early treatment initiation with calcitriol |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Review | Horm Res Paediatr | Historical and scientific review of rickets and vitamin D metabolism from the 17th century to present — contextualises calcitriol's central therapeutic role across all rickets subtypes including hereditary hypophosphataemic forms |

---

## UK Market Information

No marketing authorisations for Calcitriol were identified in this Evidence Pack.

> **Practitioners' note**: Calcitriol (e.g., Rocaltrol®) holds regulatory authorisation in multiple jurisdictions for conditions including hypoparathyroidism and renal osteodystrophy, but no UK MHRA authorisations were retrieved in this dataset. Please verify current authorisation status via the MHRA product licence database and consult the **British National Formulary (BNF, Chapter 9.6.4 — Vitamin D and analogues)** for current UK prescribing guidance. Burosumab (Crysvita®) is separately licensed by the MHRA for XLH in patients aged ≥1 year and may represent an alternative or complementary approach.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|--------------|-------------|---------------------|
| — | No records identified | — | — |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Important clinical alert**: Published literature indicates that excess calcitriol administration can itself induce iatrogenic hypocalcaemia, nephrocalcinosis, and incomplete distal renal tubular acidosis (PMID 10910456). In hereditary hypophosphataemic rickets, nephrocalcinosis is a recognised long-term complication of calcitriol + phosphate therapy, particularly in paediatric patients. Careful dose titration with regular monitoring of serum calcium, serum phosphate, and urinary calcium-to-creatinine ratio is essential. Renal ultrasound surveillance for nephrocalcinosis is strongly recommended.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Calcitriol combined with phosphate supplementation is the internationally established standard of care for hereditary hypophosphataemic rickets, underpinned by 40 years of clinical evidence, Phase 3 and Phase 4 trials, and major guidelines (Lancet 2024; Calcified Tissue International 2025). However, no UK marketing authorisation was identified in this dataset, and detailed safety data — including contraindications, drug interactions, and SmPC-level warnings — requires formal verification before clinical implementation.

**To proceed, the following is needed:**
- Confirm current UK MHRA authorisation status for Calcitriol in hereditary hypophosphataemic rickets via the MHRA product licence database
- Obtain the full SmPC for UK-available calcitriol preparations (if any), including contraindications and drug–drug interactions
- Retrieve formal mechanism of action documentation from DrugBank (DB00136) to complete the mechanistic dossier
- Establish a nephrocalcinosis monitoring protocol: baseline renal ultrasound and urinary calcium/creatinine ratio at treatment initiation, with annual surveillance thereafter
- Define serum calcium, phosphate, and PTH target ranges aligned with UK paediatric metabolic bone disease guidelines
- Assess, in consultation with a specialist metabolic bone disease service, whether burosumab (Crysvita®, MHRA-licensed for XLH) represents a superior or complementary strategy for individual patients — particularly those with existing nephrocalcinosis or who are intolerant of high-dose phosphate
- Consider establishing a formal referral pathway to paediatric endocrinology or metabolic bone disease units for diagnosis confirmation and treatment initiation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

