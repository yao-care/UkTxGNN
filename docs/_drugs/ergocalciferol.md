---
layout: default
title: Ergocalciferol
parent: Model Prediction Only (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ergocalciferol: predicted new indication Top-ranked: familial isolated hypoparathyroidism due to impaired PTH… (evidence level L5). Approved use: Vitamin D deficiency, rickets, osteomalacia…"
monitor_inn: "Ergocalciferol"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "calcium-alkali syndrome"]
---

# Ergocalciferol
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

# Ergocalciferol: From Vitamin D Deficiency and Bone Disorders to Renal Osteodystrophy

## One-Sentence Summary

Ergocalciferol (vitamin D2) is originally used for vitamin D deficiency and related bone and calcium-metabolism disorders such as rickets, osteomalacia and hypoparathyroidism.
The TxGNN model's top-ranked prediction is **familial isolated hypoparathyroidism due to impaired PTH secretion**, but it has no trials or literature behind it. The best-supported prediction in the data compiled for this report is **renal osteodystrophy**, with **1 clinical trial** (Phase 4) and **20 publications**, mostly reviews and small studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin D deficiency, rickets, osteomalacia, hypoparathyroidism and related disorders (the marketing authorisation record carries no indication text) |
| Predicted New Indication | Top-ranked: familial isolated hypoparathyroidism due to impaired PTH secretion. Best evidenced: renal osteodystrophy (rank 7) |
| TxGNN Prediction Score | Rank 1: 99.85%. Renal osteodystrophy: 99.67% |
| Evidence Level | Rank 1: L5. Renal osteodystrophy: L3 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Rank 1: Hold. Renal osteodystrophy: Proceed with Guardrails |

Note: the highest TxGNN scores do not match the strongest evidence. This report therefore covers the full prediction list and highlights renal osteodystrophy as the most actionable candidate.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known pharmacology, ergocalciferol is a prohormone. It is hydroxylated in the liver to 25-hydroxyvitamin D and then in the kidney to active calcitriol, which acts through the vitamin D receptor to increase intestinal calcium and phosphate absorption.

**Renal osteodystrophy (best-supported candidate).** In chronic kidney disease mineral and bone disorder (CKD-MBD), vitamin D deficiency is common and contributes to secondary hyperparathyroidism. Nutritional vitamin D such as ergocalciferol replenishes the 25-hydroxyvitamin D substrate, which supports calcitriol synthesis and may lower parathyroid hormone. The caveat is that efficacy declines as kidney function worsens, because renal 1-alpha hydroxylation is impaired. Activated vitamin D (e.g. calcitriol) is therefore often needed in advanced disease.

**Other predictions:**

| Predicted indication | Assessment |
|------|------|
| Familial isolated hypoparathyroidism (rank 1) | Biologically plausible, since hypoparathyroidism is already among the original indications. No trials or literature specific to this subtype. |
| Hypophosphatemia and hypophosphatemic rickets (ranks 6, 8) | Largely overlaps with existing indications. Older studies combine ergocalciferol with phosphate. Calcitriol is generally preferred, and FGF23-mediated forms respond poorly to vitamin D alone. |
| Vitamin D-dependent rickets (rank 10) | Type I cannot convert 25-OH-D to calcitriol, and type II is receptor-resistant, so ergocalciferol is of limited use. Evidence is limited to reviews and older reports. |
| Renal tubular acidosis (rank 3) | Vitamin D could only be adjunctive for bone complications. The two retrieved papers are only indirectly relevant. |
| Dahlberg-Borer-Newcomer syndrome (rank 5) | The retrieved papers are general vitamin D reviews. The match looks like an ontology artefact. |
| Acromesomelic dysplasia, craniofacial conodysplasia (ranks 2, 4) | No identifiable mechanistic link and no evidence. |
| Calcium-alkali syndrome (rank 9) | Presents with hypercalcaemia, so vitamin D could worsen it. A safety concern rather than a therapeutic opportunity. |

---

## Clinical Trial Evidence

Only the renal osteodystrophy prediction has a registered trial. The other nine predictions have none.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01799317](https://clinicaltrials.gov/study/NCT01799317) | Phase 4 | Unknown | 60 | Tests whether vitamin D2 (ergocalciferol) combined with doxercalciferol, or doxercalciferol alone, corrects the mineralisation defect in children with secondary hyperparathyroidism on peritoneal dialysis. Phosphate is controlled with sevelamer. Results are not available. |

---

## Literature Evidence

The table shows the most relevant publications for renal osteodystrophy, the best-supported prediction. Study types follow the classification in the compiled data.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27401037](https://pubmed.ncbi.nlm.nih.gov/27401037/) | 2016 | Randomised controlled trial (open-label) | Eur J Pharmacol | Ergocalciferol (n=104) vs calcitriol (n=100) in stage 3-5 CKD over about 33 months, assessing control of CKD-MBD. Ergocalciferol raised 25-hydroxyvitamin D levels significantly. |
| [3877585](https://pubmed.ncbi.nlm.nih.gov/3877585/) | 1985 | Clinical comparison | Clin Nephrol | Calcitriol vs ergocalciferol in 18 children with chronic renal failure, assessing bone histology, biochemistry and height velocity. Aluminium deposition and osteomalacia were seen in some patients. |
| [30274806](https://pubmed.ncbi.nlm.nih.gov/30274806/) | 2019 | Review | Nefrologia | Native vitamin D (ergocalciferol, cholecalciferol, calcifediol) in pre-dialysis CKD. Its role remains unclear. |
| [28873969](https://pubmed.ncbi.nlm.nih.gov/28873969/) | 2017 | Clinical practice recommendations | Nephrol Dial Transplant | Recommendations on native vitamin D therapy in children with CKD stages 2-5 and on dialysis. Few studies provide firm evidence. |
| [30297082](https://pubmed.ncbi.nlm.nih.gov/30297082/) | 2018 | Expert workshop report | Am J Kidney Dis | Vitamin D deficiency is common in CKD stages 3-4, but its management remains controversial. |
| [21947120](https://pubmed.ncbi.nlm.nih.gov/21947120/) | 2011 | Review | Nat Rev Nephrol | Mineral and bone disorders in children with CKD, and the need for tight bone and mineral control. |
| [16898852](https://pubmed.ncbi.nlm.nih.gov/16898852/) | 2006 | Review | Paediatr Drugs | Minimising bone abnormalities in children with renal failure. |
| [20671739](https://pubmed.ncbi.nlm.nih.gov/20671739/) | 2010 | Review | Kidney Int Suppl | Role of vitamin D, calcimimetics and minerals in kidney bone disease and mortality. |
| [23713880](https://pubmed.ncbi.nlm.nih.gov/23713880/) | 2014 | Review | Curr Vasc Pharmacol | Native vitamin D and calcifediol for replenishing vitamin D in CKD and ESRD. |
| [12091645](https://pubmed.ncbi.nlm.nih.gov/12091645/) | 2002 | Guideline | Nephrol Dial Transplant | European best practice guidance on bone disease after renal transplantation, including vitamin D treatment during steroid therapy. |

Evidence for the other predictions is limited to reviews, case reports and small older studies. Examples are [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) (1980, small clinical study of phosphate with ergocalciferol or calcitriol in vitamin D-resistant rickets, N Engl J Med) and [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) (2024, review of rickets types and vitamin D treatment, Nutrients). Familial isolated hypoparathyroidism, acromesomelic dysplasia, craniofacial conodysplasia and calcium-alkali syndrome have no related literature.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0906040N0AAEWEW (BNF-style product code, as recorded in the data) | Ergocalciferol tablets 12.5 microgram | Tablet (not stated in the record) | Not stated in the record |

Only one valid single-ingredient authorisation is recorded. The record does not give a PL number, manufacturer, dosage form or indication text. Please check the current MHRA and BNF entries.

---

## Safety Considerations

**Contraindications flagged by the knowledge graph (not label text).** These are drug-disease associations from a knowledge graph and need verification against the SmPC. They include:
- Hypercalcaemia, nephrocalcinosis and phosphorus metabolism disorders
- Hyperparathyroidism and osteitis fibrosa
- Sarcoidosis
- Kidney, liver and gallbladder disease
- Hypertension and atrial fibrillation
- Diabetes mellitus and diabetic ketoacidosis
- Primary hyperoxaluria and Wilson disease
- Iron metabolism disorders, including haemochromatosis and haemosiderosis
- Blood coagulation disorders and sickle cell anaemia
- Hyperlipidaemia
- Breast and prostate cancer

Hypercalcaemia and nephrocalcinosis also appear among the original indications, so that overlap in the knowledge graph needs clinical interpretation.

**Drug interactions.** The interaction screen found 55 interacting drugs. The first 20 returned include:
- **Major:** other vitamin D products, namely cholecalciferol, calcifediol, calcitriol and doxercalciferol. Duplicate vitamin D therapy risks hypercalcaemia.
- **Moderate:** thiazide-type diuretics (hydrochlorothiazide, chlorothiazide, chlortalidone), barbiturates (amobarbital, butalbital), carbamazepine, rifabutin, bile acid sequestrants (cholestyramine, colesevelam, colestipol), magnesium oxide, sevelamer, digoxin, and topical calcipotriol and calcitriol.
- **Minor:** cimetidine.

**Safety points from the literature.** Tertiary hyperparathyroidism has been reported with phosphate therapy in familial hypophosphatemic rickets. Calcium and phosphate monitoring is important, particularly in CKD.

Label warnings could not be retrieved. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (renal osteodystrophy only). Hold for all other predictions.**

**Rationale:**
- Renal osteodystrophy has a registered Phase 4 trial, an RCT comparing ergocalciferol with calcitriol in CKD, and consistent supporting reviews. No confirmed Phase 2/3 RCT exists, so the evidence is graded L3. Guardrails on dosing and calcium and phosphate monitoring are essential.
- The top-ranked prediction (familial isolated hypoparathyroidism) has the highest score but no supporting evidence (L5) and largely overlaps existing indications. Calcium-alkali syndrome carries a likely safety concern. Hypophosphatemia, hypophosphatemic rickets and vitamin D-dependent rickets are mostly on-label overlaps with limited, mainly historical evidence. They are best treated as research questions.

**To proceed, the following is needed:**
- Results and full design of NCT01799317, and verification of the 2016 RCT (PMID 27401037) endpoints and outcomes
- Current UK authorisation details (PL number, dosage form, approved indications) and the SmPC warnings and contraindications
- Mechanism of action data
- A monitoring plan covering serum calcium, phosphate, PTH and 25-hydroxyvitamin D, with dose limits and a strategy for avoiding duplicate vitamin D therapy
- A review of how efficacy changes with CKD stage, and where activated vitamin D should replace ergocalciferol
- Review against NICE guidance and BNF recommendations for CKD-MBD
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

