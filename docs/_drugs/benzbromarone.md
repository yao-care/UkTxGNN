---
layout: default
title: Benzbromarone
parent: Model Prediction Only (L5)
nav_order: 96
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Benzbromarone: predicted new indication Hypouricaemia, renal (evidence level L5). Approved use: Gout"
monitor_inn: "Benzbromarone"
predicted_indications: ["hypouricemia, renal"]
---

# Benzbromarone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Benzbromarone: From Gout and Hyperuricaemia to Renal Hypouricaemia
{: .text-alpha }

## One-Sentence Summary

Benzbromarone is a uricosuric drug, originally used to treat gout and hyperuricaemia.
The TxGNN model predicts it may be relevant to **renal hypouricaemia**, but the data compiled for this report show **no registered clinical trials** and **19 publications**, which are mostly case reports and mechanistic studies. These do not support a therapeutic benefit, and the mechanism points towards possible harm.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; hyperuricaemia |
| Predicted New Indication | Hypouricaemia, renal |
| TxGNN Prediction Score | 99.07% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on known pharmacology, benzbromarone is a uricosuric agent that inhibits the renal urate transporter URAT1 (SLC22A12). This reduces renal urate reabsorption and lowers serum uric acid, which is why it is used in gout and hyperuricaemia.

The prediction is probably a **network association** rather than a therapeutic rationale. Hereditary renal hypouricaemia is caused by loss-of-function variants in URAT1 (SLC22A12) or GLUT9 (SLC2A9). These variants already cause excessive urinary urate excretion and low serum urate. Benzbromarone therefore mimics the disease mechanism rather than correcting it.

Giving a URAT1 inhibitor to patients who already lack URAT1 function would be expected to worsen hypouricaemia. It could also raise the risk of exercise-induced acute renal failure, urate nephropathy and nephrolithiasis. The high TxGNN score most likely reflects shared urate-transport biology. **This should be regarded as a likely contraindication, not a repurposing opportunity.**

In the literature, benzbromarone appears mainly as a **diagnostic probe**. The benzbromarone/pyrazinamide suppression test is used to classify the type of tubular urate transport defect in patients with renal hypouricaemia.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 19 publications identified are mostly case reports and mechanistic studies. None reports benzbromarone as a treatment for renal hypouricaemia. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clin Rheumatol | Narrative update on the causes, diagnosis and clinical relevance of hypouricaemia for rheumatologists |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort | J Am Soc Nephrol | 32 patients with renal hypouricaemia; clinical and genetic analysis of the URAT1 (SLC22A12) gene and urinary urate excretion |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Review | Nihon Rinsho | Concept and classification of urate metabolism abnormalities (hyperuricaemia and hypouricaemia) |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Case report | Am J Kidney Dis | Two brothers with hereditary renal hypouricaemia and exercise-induced acute renal failure |
| [10879667](https://pubmed.ncbi.nlm.nih.gov/10879667/) | 2000 | Case series | Clin Nephrol | Renal hypouricaemia with recurrent exercise-induced acute renal failure and chronic renal dysfunction |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | Case report | Acta Paediatr | Recurrent exercise-induced acute renal failure; the benzbromarone/pyrazinamide test indicated a defect in proximal tubular reabsorption |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | Case series | J Pediatr | Four children with hereditary renal hypouricaemia; benzbromarone did not alter urate clearance ratios |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | Case report | Nephron | Isolated renal urate transport defect; urate clearance rose further after benzbromarone |
| [9144014](https://pubmed.ncbi.nlm.nih.gov/9144014/) | 1997 | Case report | Intern Med | Two cases of renal hypouricaemia with nephrolithiasis; benzbromarone used in a suppression test |
| [14747372](https://pubmed.ncbi.nlm.nih.gov/14747372/) | 2004 | Preclinical | J Am Soc Nephrol | Function and localisation of the URAT1 homologue in mouse kidney |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001040A0AAAAAA | Benzbromarone tablets 100 mg | Tablet | Not stated in the data compiled for this report |

The authorisation number above does not follow the usual MHRA format (PL XXXXX/XXXX), so the licensing details should be verified against the MHRA records. The data compiled for this report do not include NICE appraisals or the BNF classification for this product.

---

## Cytotoxicity

Not applicable. Benzbromarone is not an antineoplastic drug, so this section is omitted.

---

## Safety Considerations

Safety label data (warnings and contraindications) were not available, and no drug interaction records were found. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Based on the mechanism and the published case reports, the following **theoretical concerns** apply specifically to the predicted use:
- Further increased urinary urate excretion in patients who already have excessive renal urate loss.
- Exercise-induced acute renal failure, which is reported repeatedly in renal hypouricaemia.
- Nephrolithiasis, including uric acid stones, which is reported in several of the cases.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5), with no clinical trials and no publications showing therapeutic benefit. The pharmacology of benzbromarone (URAT1 inhibition) runs counter to the disease mechanism, so using it for renal hypouricaemia would be expected to worsen the condition. We do not recommend further development for this indication.

**To proceed, the following is needed:**
- Safety label data (SmPC warnings and contraindications), which is currently a blocking gap.
- Confirmation of the mechanism of action from DrugBank.
- Expert review to determine whether renal hypouricaemia should be recorded as a contraindication, rather than as a repurposing candidate.
- Verification of the UK marketing authorisation details and approved indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

