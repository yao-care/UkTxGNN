---
layout: default
title: Alfacalcidol
parent: Model Prediction Only (L5)
nav_order: 31
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Alfacalcidol: predicted new indication Familial isolated hypoparathyroidism due to impaired PTH secretion (evidence level L5). Approved use: Hyperparathyroidism, osteitis fibrosa, hypoparathyroidism…"
monitor_inn: "Alfacalcidol"
predicted_indications: ["Dahlberg-Borer-Newcomer syndrome", "craniofacial conodysplasia", "acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis"]
---

# Alfacalcidol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Alfacalcidol: From Hyperparathyroidism to Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion

## One-Sentence Summary

Alfacalcidol is an active vitamin D analogue, originally used for conditions such as hyperparathyroidism, hypoparathyroidism, osteitis fibrosa and renal osteodystrophy.
The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion**, with a score of 99.6%, but **no clinical trials and no publications** specific to this condition were found.
The prediction is therefore supported by model output and mechanistic reasoning only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperparathyroidism, osteitis fibrosa, hypoparathyroidism, renal osteodystrophy (from the TxGNN knowledge graph; no approved indication text is available for the UK product) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, alfacalcidol is a 1-alpha-hydroxylated vitamin D prodrug. It is converted in the liver to calcitriol, the active form of vitamin D, and so bypasses the renal 1-alpha-hydroxylase step.

This makes it mechanistically plausible in hypoparathyroidism. Low parathyroid hormone (PTH) reduces renal activation of vitamin D, and an already-activated analogue can compensate for this.

Hypoparathyroidism is already among alfacalcidol's recognised uses. The familial isolated subtype is likely covered by that existing use, so this is probably **not a true repurposing**. The high score is a computational prediction only.

### Other Predictions Considered

Three further predictions were generated, all at low evidence levels:

- **Renal tubular acidosis (score 99.27%, evidence level L4):** The only candidate with relevant published material. Five case reports describe osteomalacia secondary to renal tubular acidosis, including Sjögren's syndrome-associated cases, improving with treatment that included alfacalcidol (for example PMIDs 22740247 and 11518137). Alkali and other agents were given at the same time, so the effect of alfacalcidol alone cannot be separated. The target is the bone complication rather than the tubular defect. It is best framed as a research question.
- **Dahlberg-Borer-Newcomer syndrome (score 99.60%, L5):** The retrieved papers are mostly off-target (Fanconi-Bickel syndrome, FGF23-related hypophosphataemia, general vitamin D reviews, and others). None studies alfacalcidol in this syndrome.
- **Craniofacial conodysplasia (99.55%) and acromesomelic dysplasia, Campailla-Martinelli type (99.53%):** No mechanistic link or supporting evidence. These probably reflect network proximity to other bone disorders.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the lead predicted indication.

---

## Literature Evidence

Currently no related literature available for the lead predicted indication.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0906040B0AAAAAA | Alfacalcidol capsules 250 ng | Capsule | Not available in the compiled data |

This identifier follows the BNF/NHS product-code format rather than the PL number format, so it should be checked against the MHRA register. BNF chemical code 0906040B0 places alfacalcidol in BNF section 9.6.4, vitamin D.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction rests on a model score alone, with no trials or literature. It is probably already covered by the existing hypoparathyroidism use, so it adds little as a repurposing opportunity. Of the alternatives, only renal tubular acidosis has any supporting material, and that consists of uncontrolled case reports.

**To proceed, the following is needed:**
- Confirmation from the current SmPC that familial isolated hypoparathyroidism falls within the licensed hypoparathyroidism indication
- The approved indication text, dosage form and safety information (warnings, contraindications) for the UK product, taken from the SmPC and BNF
- Mechanism of action data for the drug record
- For renal tubular acidosis, a structured review of the case reports and, if warranted, a prospective study to isolate the effect of alfacalcidol on osteomalacia from that of alkali therapy
- Monitoring plans for serum calcium and phosphate, since hypercalcaemia is a recognised risk with active vitamin D analogues
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

