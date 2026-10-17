---
layout: default
title: Cetirizine
parent: Model Prediction Only (L5)
nav_order: 149
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Cetirizine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Allergic rhinitis (other indications include vasomotor rhinitis…"
monitor_inn: "Cetirizine"
predicted_indications: ["acute laryngopharyngitis", "recalcitrant atopic dermatitis"]
---

# Cetirizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Cetirizine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Cetirizine is a second-generation H1-receptor antihistamine, originally used for allergic rhinitis, conjunctivitis and idiopathic urticaria.
The TxGNN model predicts it may be effective for **allergic urticaria**,
with **1 clinical trial** and **18 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (other indications include vasomotor rhinitis, atopic, papillary and vernal conjunctivitis, and idiopathic urticaria) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (see note under Conclusion) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, cetirizine is a selective H1-receptor antagonist and the carboxylated metabolite of hydroxyzine. It has minimal sedative effects at the standard 10 mg dose.

In urticaria, histamine released from mast cells drives wheal and flare formation, so blocking H1 receptors addresses the underlying pathophysiology directly. Cetirizine is already listed for idiopathic urticaria, so allergic urticaria is a close extension of its existing use rather than a new therapeutic area.

Other lower-ranked predictions were also generated (cold urticaria, nasal cavity disease, acute laryngopharyngitis, rosacea conjunctivitis, recalcitrant atopic dermatitis). Only cold urticaria has meaningful supporting literature (small clinical studies showing wheal reduction with cetirizine, typically as a first-line antihistamine). The others rest on model prediction or indirect evidence and are not assessed further here.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Multicentre, randomised, double-blind pilot comparing IV cetirizine 10 mg with IV diphenhydramine 50 mg in acute urticaria in emergency, urgent care and allergy settings. A feasibility study, not powered for efficacy. |

## Literature Evidence

The publications retrieved are mostly narrative reviews of antihistamines in urticaria and allergic rhinitis. No randomised controlled trial of cetirizine in allergic urticaria was identified. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Review | Drugs | Cetirizine is effective and well tolerated in seasonal/perennial allergic rhinitis and chronic idiopathic urticaria in adults. |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Potent peripheral H1 antagonist; controlled trials support use in allergic rhinitis, pollen-induced asthma and chronic urticaria. |
| [11702618](https://pubmed.ncbi.nlm.nih.gov/11702618/) | 2001 | Evidence-based review | Am J Clin Dermatol | Antihistamines remain the mainstay of urticaria treatment. |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Reviews efficacy and safety of first- and newer-generation antihistamines in allergic rhinitis and chronic idiopathic urticaria. |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | Non-sedating antihistamines are the mainstay of treatment for most chronic idiopathic urticaria. |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Review | Allergy | Overview of clinical studies of cetirizine in allergic rhinitis and chronic urticaria. |
| [14512923](https://pubmed.ncbi.nlm.nih.gov/14512923/) | 2003 | Small clinical study | J Am Acad Dermatol | Cetirizine plus zafirlukast in acquired cold urticaria (related indication). |
| [1364168](https://pubmed.ncbi.nlm.nih.gov/1364168/) | 1992 | Comparative study | J Investig Allergol Clin Immunol | Randomised crossover comparison of loratadine, cetirizine, cyproheptadine and ketotifen in 7 patients with cold urticaria. |
| [17225008](https://pubmed.ncbi.nlm.nih.gov/17225008/) | 2007 | Experimental study | Acta Derm Venereol | Cetirizine 10 mg reduced cold-induced wheals by about 50% in 6 patients; histamine is an essential mediator. |
| [11034010](https://pubmed.ncbi.nlm.nih.gov/11034010/) | 2000 | Case report | J Clin Gastroenterol | Cetirizine-induced cholestasis (safety signal). |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0304010I0AAAAAA | Cetirizine HCl Tablets 10 mg | Tablet | Indication text not available |

One single-ingredient authorisation is recorded as valid. The identifier shown is a classification-style code rather than a standard MHRA PL number, so please verify it against the MHRA register. Dosage form and indication details were not provided; the tablet form is inferred from the product name.

## Safety Considerations

The following contraindication-type associations come from the TxGNN knowledge graph, not from product label text, and should be treated as signals to verify against the SmPC:

- **Cardiovascular:** hypertension, coronary artery disease, atherosclerosis
- **Renal:** kidney disease, chronic kidney disease, end-stage renal failure
- **Hepatic and biliary:** liver disease, gallbladder disease (a published case report describes cetirizine-induced cholestasis)
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease
- **Genitourinary and ocular:** benign prostatic hyperplasia, angle-closure glaucoma

**Drug interactions:** The interaction screen returned 100 entries. Those shown are mostly moderate, with several of unknown severity. Moderate-level interactions include bupropion, dronabinol, loperamide, metoclopramide, morphine, nabilone, opium, sibutramine, difenoxin and diphenoxylate. Many involve additive central nervous system effects, but the data do not state the mechanism.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cetirizine has a well-established H1-antagonist mechanism, is already used for idiopathic urticaria, and has a completed Phase 3-labelled trial (IV formulation) in acute urticaria. That trial was a small (n=36) feasibility pilot, not an efficacy-powered RCT, so the L1 grade rests mainly on the strength of class and label evidence and should be read with caution. The remaining predictions are weaker: cold urticaria is a research question (L3), and the other four are on hold (L4–L5).

**To proceed, the following is needed:**
- Complete UK authorisation details (verified PL number, dosage form and approved indications) from the MHRA register
- Review of SmPC warnings and contraindications, which are missing from the data compiled for this report, and reconciliation with the knowledge-graph signals above
- Mechanism of action data from DrugBank
- Confirmation of whether the IV formulation in the trial is relevant to UK practice, as only a tablet authorisation is recorded
- Efficacy-powered randomised evidence, or a guideline and NICE/BNF check, specifically for allergic urticaria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

