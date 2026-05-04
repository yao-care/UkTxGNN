---
layout: default
title: Candesartan Cilexetil
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 5
---

# Candesartan Cilexetil
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

# Candesartan Cilexetil: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Candesartan cilexetil is an angiotensin II receptor blocker (ARB) of the sartan class, established as a standard treatment for systemic hypertension and heart failure. The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, with a model confidence score of **99.68%**; however, **no clinical trials or published literature** specifically supporting this repurposed indication were identified, and an important mechanistic safety paradox must be resolved before progression.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no MHRA marketing authorisations recorded in current dataset) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available within this Evidence Pack. Based on established pharmacology, candesartan cilexetil is a prodrug that is hydrolysed to candesartan — a highly selective, competitive antagonist of the AT₁ angiotensin II receptor. By blocking AT₁ receptors, candesartan interrupts the renin-angiotensin system (RAS), reducing vasoconstriction, aldosterone secretion, and sympathetic nervous system activation. Its notable lipophilicity is thought to confer superior tissue penetration compared with other ARBs, potentially achieving more complete local RAS blockade in target organs such as the kidney and vasculature.

Renovascular hypertension arises from renal artery stenosis causing excessive renin release and downstream RAS hyperactivation — precisely the pathway that ARBs are designed to interrupt. The malignant form is characterised by severely elevated blood pressure with acute end-organ damage (hypertensive encephalopathy, papilloedema, acute kidney injury), where aggressive RAS suppression is conceptually appealing. The TxGNN model's high score therefore reflects a plausible mechanistic logic: if RAS hyperactivation drives the hypertensive crisis, then AT₁ blockade should attenuate it.

However, a critical safety paradox must be acknowledged. Bilateral renal artery stenosis — or stenosis affecting a solitary functioning kidney — is a recognised relative contraindication to ACE inhibitors and ARBs in all major guidelines. In this anatomical context, these agents can precipitate acute kidney injury by abolishing the compensatory efferent arteriolar constriction that maintains glomerular filtration pressure. Patients with malignant renovascular hypertension already have compromised renal perfusion; the use of candesartan without prior exclusion of bilateral stenosis carries a substantial risk of precipitating acute renal failure. Renal vascular anatomy must be characterised before any therapeutic trial in this population.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No marketing authorisations for candesartan cilexetil are recorded in the UK dataset within this Evidence Pack. Healthcare professionals should consult the [MHRA Product Licences database](https://products.mhra.gov.uk/) and the [BNF](https://bnf.nice.org.uk/) directly for current licensing and prescribing information.

> **Note for clinicians:** Candesartan cilexetil is a well-established ARB used in UK clinical practice. The absence of MHRA licence records in this dataset reflects a data gap in the current Evidence Pack rather than an absence of authorised products. Please verify current authorisation status via official MHRA channels.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the [Yellow Card Scheme](https://yellowcard.mhra.gov.uk/).

> **Important class-level alert:** As an ARB, candesartan carries a well-established contraindication in the context of bilateral renal artery stenosis or stenosis of the artery supplying a single functioning kidney. This is directly relevant to the predicted indication of malignant renovascular hypertension. Renal function and serum electrolytes (particularly potassium and creatinine) must be monitored closely if use is contemplated. Use in pregnancy is contraindicated. Concomitant use with other agents affecting the RAS (ACE inhibitors, aliskiren) increases the risk of hyperkalaemia, hypotension, and renal impairment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic rationale for ARB therapy in RAS-driven hypertension is pharmacologically coherent, the specific context of *malignant* renovascular hypertension introduces a safety-first paradox: bilateral renal artery stenosis — the most common structural substrate — constitutes a class contraindication to ARBs, and no direct clinical trial or literature evidence supporting candesartan in this precise indication has been identified.

**To proceed, the following is needed:**

- **Renal vascular imaging** to exclude bilateral renal artery stenosis (duplex Doppler ultrasound, CT or MR angiography) prior to any consideration of ARB therapy — this is the single most critical pre-requisite
- **Mechanism of action data** retrieved from DrugBank (DB00796) or published pharmacology literature to complete the mechanistic link analysis
- **Safety profile** including full MHRA SmPC warnings, contraindications, and drug interaction data (DDI query returned no results in this dataset)
- **MHRA licence verification** to confirm current UK marketing authorisation status and approved indications
- **Targeted literature search** using candesartan-specific MeSH terms combined with renovascular hypertension terminology, rather than the prodrug name alone, to ensure complete evidence capture
- **Pilot observational data** or case series in patients with *unilateral* renal artery stenosis and malignant hypertension before any prospective trial design is considered

---

*This report is generated for research purposes only and does not constitute clinical or prescribing advice. Drug repurposing candidates require prospective clinical validation before therapeutic application. All prescribing decisions should be made in accordance with the current BNF, SmPC, and relevant NICE guidance.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

