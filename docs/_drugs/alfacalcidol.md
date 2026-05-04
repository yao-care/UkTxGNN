---
layout: default
title: Alfacalcidol
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 5
---

# Alfacalcidol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Alfacalcidol: From Hypoparathyroidism to Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion

## One-Sentence Summary

Alfacalcidol is a synthetic active vitamin D analogue used in the management of calcium and bone metabolism disorders, including hypoparathyroidism, where it bypasses renal 1α-hydroxylation to directly provide the physiologically active form of vitamin D without requiring intact parathyroid hormone (PTH) signalling.
The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion** — a rare, genetically defined subtype of hypoparathyroidism characterised by deficient PTH production — with a prediction score of **99.61%**.
Currently, **no clinical trials** and **no publications** specifically addressing this precise genetic subtype in the context of alfacalcidol therapy have been identified, placing this prediction in the category of a mechanistically well-grounded but clinically unvalidated research question.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypoparathyroidism and related calcium/bone metabolism disorders (established clinical use; no MHRA licence data available in this dataset) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L4 — mechanistic basis only; no direct clinical studies identified |
| UK Market Status | Not Marketed (no MHRA authorisations recorded in this dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Alfacalcidol (1α-hydroxycholecalciferol) is a prodrug that undergoes rapid hepatic 25-hydroxylation to form calcitriol (1,25-dihydroxyvitamin D₃), the biologically active form of vitamin D. Crucially, unlike nutritional cholecalciferol, alfacalcidol bypasses the renal 1α-hydroxylation step — the rate-limiting conversion step that is ordinarily upregulated by PTH. This pharmacological property renders alfacalcidol functionally independent of intact parathyroid gland activity, making it inherently well-suited to any condition in which PTH production or secretion is impaired.

In familial isolated hypoparathyroidism due to impaired PTH secretion, a genetic defect (variants in genes such as *GCM2*, *SOX3*, or related loci) directly reduces or abolishes PTH production from the parathyroid glands. The resultant PTH deficiency leads to decreased renal 1α-hydroxylase (CYP27B1) activity, diminished calcitriol synthesis, persistent hypocalcaemia, hyperphosphataemia, and disordered skeletal mineralisation. Since alfacalcidol does not require PTH-mediated renal activation to exert its downstream effects on intestinal calcium and phosphate absorption, it can directly substitute for the absent vitamin D activation that the deficient PTH can no longer drive. The mechanistic fit is therefore highly direct and biologically coherent.

General hypoparathyroidism — including both post-surgical and idiopathic forms — is already a well-recognised clinical indication for alfacalcidol in international practice. The TxGNN model's prediction essentially constitutes an extension of this established therapeutic principle to the specific genetic subtype defined by impaired PTH secretion. While the mechanistic reasoning is compelling, no dedicated clinical trials or publications have been identified for this precise disease entity; the evidence remains an extrapolation from broader hypoparathyroidism treatment experience and from alfacalcidol's established pharmacodynamic profile.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available specifically for this indication.

---

## Safety Considerations

Detailed safety data, including key warnings, contraindications, and drug–drug interactions, are not available in the current dataset.

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic link between alfacalcidol and familial isolated hypoparathyroidism due to impaired PTH secretion is strong, biologically coherent, and directly derived from the drug's established mode of action, no clinical trials or disease-specific publications have been identified for this rare genetic subtype. In the absence of any direct clinical evidence, this candidate cannot progress beyond a mechanistically reasoned research question at this time.

**To proceed, the following is needed:**

- Genetic confirmation and patient identification: case series or registry data in patients with molecularly confirmed familial isolated hypoparathyroidism due to impaired PTH secretion (e.g., *GCM2*, *SOX3* variant carriers)
- Clinical outcome data: observational or retrospective data documenting serum calcium normalisation, bone density, and quality-of-life outcomes with alfacalcidol in this specific subtype
- Long-term safety monitoring plan: a structured protocol addressing hypercalcaemia, hypercalciuria, nephrocalcinosis, and renal function impairment — known risks with active vitamin D analogues in hypoparathyroid patients receiving supplemental calcium
- Mechanism of action (MOA) data: retrieval from DrugBank (DB01436) to formally document the pharmacological rationale and strengthen the evidence dossier
- UK regulatory review: verification of current MHRA authorisation status and approved indications via the MHRA Product Licence database and the BNF (vitamin D and analogues section), particularly given the absence of licence data in this dataset

---

> **Note on alternative candidates with stronger evidence:** Amongst the five predicted indications evaluated in this pack, **renal tubular acidosis** (rank 5, TxGNN score 99.27%) carries substantially stronger clinical evidence (Evidence Level L3), supported by multiple published case reports and a case series documenting alfacalcidol's benefit in osteomalacia secondary to Fanconi syndrome and Sjögren's syndrome-associated distal renal tubular acidosis. That candidate carries a **"Proceed with Guardrails"** recommendation and may warrant prioritisation for clinical translation ahead of the rank 1 prediction.

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require prospective clinical validation before therapeutic application. For clinical decision-making, refer to the current BNF, MHRA guidance, and relevant NICE technology appraisals.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

