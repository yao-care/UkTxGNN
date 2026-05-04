---
layout: default
title: Acipimox
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 0
---

# Acipimox
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Acipimox: Drug Repurposing Evaluation — No Predictions Generated

## One-Sentence Summary

Acipimox (DrugBank ID: DB09055) is a nicotinic acid analogue historically used as a lipid-lowering agent for dyslipidaemia in several European markets.
The current evidence pack (v4, data cutoff 2026-04-04) contains **no TxGNN repurposing predictions** for this drug, and no supporting clinical trial or literature evidence has been retrieved.
A full repurposing evaluation cannot be completed without resolving the identified data gaps.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Dyslipidaemia / Hyperlipidaemia (nicotinic acid analogue class) |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — pipeline incomplete; no predictions returned |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Drug Background

Detailed mechanism of action data is not currently available in this evidence pack (Data Gap DG002). Based on known pharmacological information, Acipimox is a pyrazine-based nicotinic acid (niacin) analogue that has been used in several European countries — notably Italy and the United Kingdom under the brand name **Olbetam** — for the management of dyslipidaemia, principally reducing plasma triglycerides and free fatty acids.

Its proposed mechanism involves inhibition of lipolysis in adipose tissue via activation of the GPR109A (HM74A) receptor, thereby reducing the hepatic substrate available for very-low-density lipoprotein (VLDL) synthesis. Unlike full-dose niacin, Acipimox was noted for a more favourable tolerability profile with reduced flushing.

These pharmacological properties have made Acipimox of research interest in conditions linked to insulin resistance, metabolic syndrome, and mitochondrial dysfunction — areas that could become the basis of future repurposing hypotheses once TxGNN predictions are generated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — no TxGNN predicted indication is available to anchor an evidence search.

---

## Literature Evidence

Currently no related literature available — no TxGNN predicted indication is available to anchor an evidence search.

---

## UK Market Information

Acipimox currently holds **no active MHRA marketing authorisations** in the United Kingdom. The drug is not marketed in the UK under any licence at the time of this report.

> **Note:** Acipimox was historically available in the UK under the brand name Olbetam (250 mg capsules) for hypertriglyceridaemia and mixed hyperlipidaemia. That authorisation is no longer active. Clinicians considering its use would need to access it via a Specials or unlicensed import route and would require appropriate governance.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> As no safety data was available in the evidence pack (warnings, contraindications, and DDI records all returned no data), prescribers should consult the most recent European product information and relevant literature before clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack for Acipimox is incomplete: the TxGNN model returned no predictions, safety information is absent, and mechanism of action data has not been retrieved. There is presently no evaluable repurposing hypothesis to assess.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Retrieve UK SmPC / MHRA safety information: key warnings, contraindications, and precautions — required before any safety assessment can begin
- **[High — DG002]** Retrieve mechanism of action (MOA) data via DrugBank API (`DB09055`) — required for mechanistic plausibility analysis
- **Re-run TxGNN pipeline** to generate `predicted_indications` — without this, no repurposing evaluation is possible
- **DDI screening** — no drug-drug interaction data was returned; a structured DDI query against DrugBank, CPIC, or BNF interactions database is recommended
- Once predictions are available, conduct a **targeted clinical trial search** (ClinicalTrials.gov, EU CTR, ISRCTN) and **PubMed literature review** for each candidate indication
- Confirm whether any **Specials or named-patient access route** applies for UK clinical use, given the absence of an active MHRA licence

---

*This report was generated as part of the TxGNN UK drug repurposing research programme. Results are for research purposes only and do not constitute medical advice. Any repurposing candidate must undergo appropriate clinical validation before consideration for patient use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

