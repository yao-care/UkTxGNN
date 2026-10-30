---
layout: default
title: Cocaine
parent: Model Prediction Only (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Cocaine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the UK authorisation data"
monitor_inn: "Cocaine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "rhinitis", "irritable bowel syndrome", "anaphylaxis", "neurocirculatory asthenia", "atopic conjunctivitis", "food-dependent exercise-induced anaphylaxis", "pharyngitis"]
---

# Cocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Cocaine: From Local Anaesthesia to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Cocaine is a topical local anaesthetic and monoamine reuptake inhibitor, used in nasal, oral and laryngeal surgery.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are **no registered clinical trials** and only **1 publication** (a case report that does not involve cocaine treatment).
This prediction rests on model output alone and is not supported by direct evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the UK authorisation data; the drug is described as a local anaesthetic for nasal, oral and laryngeal surgery |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (2 of 2) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, cocaine is a local anaesthetic and a blocker of monoamine reuptake (including dopamine and noradrenaline). Its anaesthetic efficacy in mucosal surgery is established.

Cauda equina syndrome is a compressive neurological emergency, usually caused by disc herniation, and it requires urgent surgical decompression. We could not identify a credible mechanistic link between cocaine and this condition. The single publication retrieved is a case report of lumbosacral disc pathology that does not involve cocaine. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predicted indications were also reviewed. All are rated Hold. The most evidence-rich (rhinitis, anaphylaxis, pharyngitis) are dominated by reports of cocaine causing harm, not treating disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31528422](https://pubmed.ncbi.nlm.nih.gov/31528422/) | 2019 | Case report/Review | Surgical Neurology International | Case report and literature review of distal cauda equina syndrome from lumbosacral disc pathology. It describes the diagnostic challenge of the condition and does not involve cocaine treatment. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1502010G0AAAAAA | Cocaine mouthwash 5% | Mouthwash | Not specified in the data compiled; BNF section 15.2 (local anaesthesia) |
| 1502010F0AAATAT | Cocaine hydrochloride mouthwash 2% | Mouthwash | Not specified in the data compiled; BNF section 15.2 (local anaesthesia) |

Note: the identifiers above are NHS BNF product codes, not MHRA "PL" numbers, and the data compiled do not give approved indication text. Please verify the licensing details against the MHRA register and the SmPC.

## Safety Considerations

- **Knowledge-graph contraindications** (from drug-disease contraindication links in the TxGNN knowledge graph, not from product label text): epilepsy, sudden cardiac arrest, heart conduction disease, thyrotoxicosis, hyperthyroidism and Graves disease.
- **Pharmacological interactions** (target-level data, no severity grading): cocaine acts on the 5-HT3A and 5-HT3AB receptors and on the dopamine transporter (DAT; rat data). These are pharmacological targets rather than clinically graded drug-drug interactions.
- **Harm signals from the retrieved literature:** cocaine-induced rhinitis, septal and palatal necrosis, mucosal burns of the upper aerodigestive tract, bronchospasm and hypersensitivity reactions. Its sympathomimetic cardiovascular toxicity (arrhythmia, hypertension, vasospasm) is a major barrier to any new use.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for cauda equina syndrome has no clinical trials, no supporting literature and no plausible mechanism. The evidence level is L5 (model prediction only). The broader profile of predicted indications shows more evidence of harm than benefit, and cocaine's cardiovascular and mucosal toxicity argue against repurposing.

**To proceed, the following is needed:**
- Mechanism of action data, with a credible rationale linking cocaine to the proposed condition
- Product-level warnings, contraindications and approved indication text from the SmPC/BNF
- Preclinical or clinical evidence of benefit in cauda equina syndrome, and a comparison with current standard care (surgical decompression)
- A formal benefit-risk assessment addressing cardiovascular toxicity, abuse liability and controlled-drug status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

