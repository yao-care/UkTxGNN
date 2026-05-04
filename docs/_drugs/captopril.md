---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 4
---

# Captopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Captopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Captopril is a well-established ACE (angiotensin-converting enzyme) inhibitor, widely used in clinical practice for the treatment of hypertension and heart failure.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**,
with **0 clinical trials** and **1 publication** currently supporting this direction.
A closely related prediction — malignant renovascular hypertension — is supported by 20 publications and carries a stronger evidence level (L3).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No UK marketing authorisation on record in this dataset |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L4 |
| UK Market Status | Not Marketed (per dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Captopril inhibits angiotensin-converting enzyme (ACE), blocking the conversion of Angiotensin I to Angiotensin II. This reduces systemic vascular resistance, suppresses aldosterone secretion, and lowers intraglomerular pressure — all pathophysiologically relevant mechanisms in hypertension-related renal damage. Although detailed MOA documentation is not available from the DrugBank record in this Evidence Pack, the drug's mechanism is well characterised in the wider literature and is directly applicable to renin-angiotensin-aldosterone system (RAAS)-driven disease.

Malignant hypertensive renal disease is characterised by severely elevated blood pressure causing acute end-organ damage to the kidneys, with fibrinoid necrosis of the renal microvasculature and RAAS hyperactivation as central pathophysiological features. By blocking ACE, Captopril directly targets this axis, making the TxGNN prediction mechanistically coherent. The drug's RAAS pathway applicability is further corroborated by the model's rank 2 prediction — malignant renovascular hypertension (TxGNN score 99.28%, L3 evidence, 20 publications) — where the same mechanistic pathway underpins a more evidence-supported therapeutic rationale.

However, a critical caveat applies: in the context of acute kidney injury or bilateral renal artery stenosis, ACE inhibitors carry a well-documented risk of precipitating acute renal failure. Malignant hypertensive renal disease often presents with pre-existing renal impairment, making careful patient selection and close renal function monitoring essential before any clinical application can be considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case Report | Clinical Nuclear Medicine | Positive captopril renography without renal artery stenosis, found to be caused by a chromophobe renal cell carcinoma producing renin-dependent hypertension; blood pressure resolved after nephrectomy, illustrating RAAS involvement in atypical renal hypertensive presentations |

---

## UK Market Information

No UK marketing authorisations are recorded for Captopril within this Evidence Pack dataset. Captopril is a long-established compound and clinicians should verify current authorisation status and approved indications directly via the MHRA product database, the BNF, and available SmPCs.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between Captopril's ACE inhibitory action and malignant hypertensive renal disease is scientifically plausible and internally consistent with the drug's known pharmacology; however, the current evidence base is limited to a single case report (L4), and the inherent risk of acute renal deterioration in this critically ill patient population demands a substantially stronger evidence foundation before clinical repurposing can be considered.

**To proceed, the following is needed:**
- Retrieval and review of the full MHRA SmPC to establish current contraindications, warnings, and renal function thresholds
- Formal MOA documentation from DrugBank (DG002) to support mechanistic narrative in any regulatory submission
- Prospective observational cohort studies or controlled trials specifically in malignant hypertensive renal disease
- Development of a renal safety monitoring protocol addressing acute kidney injury risk, particularly in patients with pre-existing renal impairment or possible bilateral renovascular disease
- Cross-referencing with the rank 2 evidence base (malignant renovascular hypertension, L3, 20 publications) to determine whether a combined or sequenced repurposing strategy is more clinically appropriate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

