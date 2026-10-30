---
layout: default
title: Buprenorphine
parent: Moderate Evidence (L3-L4)
nav_order: 115
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-30
description: "Buprenorphine: predicted new indication Acute intermittent porphyria (evidence level L4). Approved use: Opioid dependence"
monitor_inn: "Buprenorphine"
predicted_indications: ["acute intermittent porphyria", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "continuous spikes and waves during sleep", "benign shuddering attacks", "extrapyramidal and movement disease"]
---

# Buprenorphine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

## Buprenorphine: From Opioid Dependence to Acute Intermittent Porphyria
{: .text-alpha }

## One-Sentence Summary

Buprenorphine is a partial opioid agonist, originally used to treat opioid dependence.
The TxGNN model predicts it may be effective for **acute intermittent porphyria**,
but there are **no registered clinical trials** and only **1 publication** (a 1993 case report on anaesthetic management, which does not show therapeutic benefit).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Opioid dependence (approved indication text not available in the licence record; taken from the drug's known indications: opioid dependence, substance abuse/dependence, morphine dependence) |
| Predicted New Indication | Acute intermittent porphyria |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L4 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, buprenorphine is a partial mu-opioid receptor agonist (and kappa antagonist) whose efficacy in opioid dependence is established.

There is no established mechanistic link between buprenorphine and the pathophysiology of acute intermittent porphyria, which is a heme biosynthesis disorder caused by porbilinogen deaminase (PBGD) deficiency. Opioids are sometimes used to control the severe pain of acute porphyria attacks, which may explain the association the model learned. However, that is symptom relief, not disease modification. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It has no clinical support and should be read with caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case report | Masui (Japanese Journal of Anesthesiology) | Anaesthetic management of a woman with suspected acute intermittent porphyria undergoing gynaecological cancer surgery. It concerns safe perioperative drug use, not therapeutic benefit. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0407020B0AAABAB | Buprenorphine sublingual tablets 200 microgram (sugar-free) | Sublingual tablet | Not available in the data compiled for this report |

Note: the identifier shown is a product code in the compiled data, not a standard MHRA "PL" number. Please verify it against the MHRA register and the BNF.

## Safety Considerations

- **Conditions flagged in the knowledge graph as contraindications or cautions** (not label text, so check against the SmPC): respiratory failure, chronic obstructive pulmonary disease, liver disease (including chronic hepatitis B and C), long QT syndrome and torsades de pointes, orthostatic hypotension, adrenocortical insufficiency (Addison disease), hypothyroidism and myxoedema, paralytic ileus and intestinal obstruction, benign prostatic hyperplasia, urethral stricture, gallbladder disease, raised intracranial pressure (pseudotumour cerebri), and drug dependence or substance-related disorders.
- **Drug interactions** (100 recorded; examples below):
  - **Major:** morphine, alvimopan, bupropion, cisapride, dolasetron
  - **Moderate:** famotidine, cimetidine, loperamide, hyoscyamine, atropine, glycopyrronium, dexamethasone, aprepitant, clarithromycin, clotrimazole, bisacodyl
- **Porphyria-specific note:** the safety of buprenorphine in porphyria is not well established, so any use would need caution.

Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a network score alone. There are no clinical trials, the only publication is a case report on perioperative safety, and no plausible disease-modifying mechanism has been identified.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological link to heme biosynthesis or porphyria attack pathophysiology
- Preclinical or clinical evidence of benefit beyond analgesia
- Porphyria-specific safety review (including porphyrinogenic potential)
- Complete MHRA licence details (approved indications, SmPC warnings and contraindications)

### Other predicted indications (for reference)

All were assessed as **Hold**:

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Lingual-facial-buccal dyskinesia | 0.9932 | L5 | The literature does not test buprenorphine for dyskinesia. Some papers describe opioid-induced myoclonus or hyperexcitability as adverse effects. |
| Chronic tic disorder | 0.9913 | L5 | Prediction only, with no trials or literature. |
| Continuous spikes and waves during sleep | 0.9905 | L5 | Prediction only. Opioids can lower seizure threshold in some settings, a potential safety concern. |
| Benign shuddering attacks | 0.9903 | L5 | Prediction only. The condition is benign and self-limiting, so an opioid would have an unfavourable risk-benefit balance. |
| Extrapyramidal and movement disease | 0.9903 | L5 | Prediction only. A broad category, and the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

