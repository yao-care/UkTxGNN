---
layout: default
title: Metipranolol
parent: Model Prediction Only (L5)
nav_order: 406
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Metipranolol: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma and ocular hypertension"
---

# Metipranolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Metipranolol: From Open-Angle Glaucoma to Primary Hereditary Glaucoma
{: .text-alpha }

## One-Sentence Summary

Metipranolol is a non-selective beta-blocker eye drop, originally used to treat open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but **no clinical trials or publications** currently address this specific indication.
This prediction most likely reflects an overlap in disease classification with the existing indication rather than a genuinely new use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma and ocular hypertension |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, metipranolol is a non-selective beta-adrenergic blocker that lowers intraocular pressure (IOP) by reducing aqueous humour production.

Primary hereditary glaucoma is closely related to open-angle glaucoma, which is already an established indication. A drug that lowers IOP could plausibly help forms of hereditary glaucoma with raised IOP. However, the prediction rests on the model score and known pharmacology alone, and no evidence specific to hereditary glaucoma was found. This is probably a disease-classification overlap rather than true repurposing.

Two other predictions were also reviewed:
- **Open-angle glaucoma (score 99.35%, evidence level L3):** this is the existing, labelled use. The 18 publications compiled for this report (10 shown in full) mostly support on-label efficacy and tolerability.
- **Closed-angle glaucoma (score 99.26%, evidence level L4):** beta-blockers may serve as an adjunct once the angle has been opened, but they do not address the angle obstruction itself. The only publication found concerns latanoprost, not metipranolol.

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication (or for the other two predictions).

## Literature Evidence

No literature is available for primary hereditary glaucoma. The table below lists the most relevant publications for the closely related existing indication, open-angle glaucoma, as supporting context only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2905641](https://pubmed.ncbi.nlm.nih.gov/2905641/) | 1988 | Review | Drugs | Metipranolol 0.1–0.6% lowered IOP by about 20–29%, comparable to timolol and levobunolol, and was generally well tolerated |
| [8773166](https://pubmed.ncbi.nlm.nih.gov/8773166/) | 1996 | Review | Ann Pharmacother | Compares ocular beta-blockers on systemic adverse effects, local tolerability and cost |
| [10708231](https://pubmed.ncbi.nlm.nih.gov/10708231/) | 2000 | Comparative study | J Glaucoma | 0.3% metipranolol compared with timolol and carteolol on IOP and side effects in 45 patients |
| [2868753](https://pubmed.ncbi.nlm.nih.gov/2868753/) | 1986 | Randomised cross-over | Br J Ophthalmol | Metipranolol 0.3% and timolol 0.25% showed no significant difference in IOP reduction (pilot, 10 patients) |
| [2891739](https://pubmed.ncbi.nlm.nih.gov/2891739/) | 1987 | Double-blind randomised | J Fr Ophtalmol | Metipranolol 0.1% lowered IOP significantly versus placebo, but less than 0.3%, and the effect waned after about 9 hours |
| [7916025](https://pubmed.ncbi.nlm.nih.gov/7916025/) | 1994 | Randomised cross-over | J Ocul Pharmacol | Four metipranolol–pilocarpine fixed-dose combinations compared in 19 patients |
| [2882046](https://pubmed.ncbi.nlm.nih.gov/2882046/) | 1986 | Randomised controlled | Klin Monbl Augenheilkd | Fixed combination of metipranolol 0.1% and pilocarpine 2% lowered IOP better than either alone |
| [2870216](https://pubmed.ncbi.nlm.nih.gov/2870216/) | 1986 | Multicentre long-term study | Klin Monbl Augenheilkd | Average IOP reduction of about 5.9 mmHg (25%) over 16 weeks |
| [2892874](https://pubmed.ncbi.nlm.nih.gov/2892874/) | 1987 | Controlled comparative | J Fr Ophtalmol | Ventilatory and cardiovascular effects of carteolol and metipranolol eye drops studied in asthmatic patients |
| [1359979](https://pubmed.ncbi.nlm.nih.gov/1359979/) | 1992 | Case series | Eye (Lond) | Reviews loss of IOP control in patients with metipranolol-induced adverse reactions |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1106000U0AAADAD | Metipranolol eye drops 0.1% (unit dose) | Eye drops | Not stated in the data compiled for this report |

The number above is a BNF-style product code, not a standard MHRA "PL" licence number. Please verify the licence details with the MHRA.

## Safety Considerations

No label-based warnings, contraindications or drug interaction data were available. The following conditions were flagged as contraindications in the drug–disease knowledge graph (not taken from label text). They are consistent with the known class effects of beta-blockers, and the asthma flag is supported by a small study of ventilatory effects in asthmatic patients (PMID 2892874):

- **Respiratory:** asthma (including intrinsic and allergic), chronic obstructive pulmonary disease, bronchitis, pulmonary emphysema
- **Cardiac:** atrioventricular block
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis
- **Neuromuscular:** myasthenia gravis, neuromuscular junction disease
- **Other:** anaphylaxis

The literature also notes metipranolol-induced adverse reactions, including loss of IOP control in some patients (PMID 1359979).

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for primary hereditary glaucoma has a very high model score but no supporting trials or publications (evidence level L5). It most likely overlaps with the existing open-angle glaucoma indication, so it offers little genuine repurposing value. Closed-angle glaucoma has weak, indirect evidence and would need the angle opened first.

**To proceed, the following is needed:**
- Clarification of whether "primary hereditary glaucoma" is a distinct population from the labelled open-angle glaucoma indication
- Any hereditary-glaucoma-specific clinical data on metipranolol
- Mechanism of action data (for example from DrugBank)
- Current SmPC and BNF warnings and contraindications, and the approved indication text for the UK product
- Confirmation of the MHRA licence number and dosage form
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

