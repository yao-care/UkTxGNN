---
layout: default
title: Nefopam
parent: Model Prediction Only (L5)
nav_order: 438
evidence_level: L5
indication_count: 10
monitor_inn: "Nefopam"
predicted_indications: ["immature cataract", "mature cataract", "craniostenosis cataract", "tetanic cataract", "diabetes mellitus type 2 associated cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "diabetic cataract", "lumbar spinal stenosis"]
last_modified_at: 2026-10-30
description: "Nefopam: predicted new indication Immature cataract (evidence level L5). Approved use: Not stated in the licence record compiled for this report"
---

# Nefopam
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

## Nefopam: From a Centrally Acting Analgesic to Immature Cataract
{: .text-alpha }

## One-Sentence Summary

Nefopam is a centrally acting non-opioid analgesic that is currently marketed in the UK as a 30 mg tablet. The TxGNN model predicts it may be effective for **immature cataract**, but **no clinical trials and no publications** support this prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence record compiled for this report |
| Predicted New Indication | Immature cataract |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Licence Records | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not available. From the other information compiled for this report, nefopam is a centrally acting analgesic that inhibits the reuptake of serotonin, noradrenaline and dopamine, and modulates voltage-gated sodium and calcium channels.

No recognised pathway links these actions to lens opacification. Cataract formation is generally driven by oxidative damage, protein modification and, in some subtypes, metabolic or calcium-homeostasis disturbances. Nefopam's calcium channel effects are neuronal and have no known influence on these processes.

The TxGNN model (deep learning) gives a very high score, but near-identical scores appear across many cataract subtypes (for example mature, senile, cortical, nuclear and diabetic cataract). The score comes from the TxGNN model and may reflect similarities the model learned between related diseases, not biological evidence. On the data available, the prediction should be treated as a hypothesis with no supporting mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

For context, among the other predictions for nefopam, only lumbar spinal stenosis has any publications. These concern perioperative pain and dysesthesia, which is symptom control rather than a disease-modifying effect. They do not bear on cataract.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0407010P0AAABAB (as recorded; this is in BNF-style code format, not a PL number) | Nefopam HCl Tab 30mg | Tablet (from product name) | Not stated in the licence record |

This is a single-ingredient product with a valid status. The licence record contains no indication text, so the original approved indication could not be confirmed from the data compiled for this report.

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no results, which means no interaction data are available rather than that none exist.
- **Reported adverse event**: A case report describes status epilepticus attributed to nefopam (PMID 25535527). This is consistent with its known effects on seizure threshold and its anticholinergic and sympathomimetic adverse effects.

Warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no trials or publications on immature cataract, and no plausible mechanistic link. Core safety data are also missing.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a credible biological rationale linking nefopam to lens opacification
- Preclinical evidence (for example lens models) or any clinical study directly addressing cataract
- The SmPC warnings and contraindications, and the licensed indication text, for the UK product
- A route and formulation assessment. Cataract would probably need ocular delivery, while the marketed product is an oral tablet.
- Given the seizure risk, a safety review before any consideration in an older population, in which cataract is most common
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

