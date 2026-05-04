---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Atenolol: From Hypertension to Posterolateral Myocardial Infarction

## One-Sentence Summary

Atenolol is a cardioselective beta-1 adrenergic receptor blocker with a long-established history in the management of hypertension, angina pectoris, and cardiac arrhythmias.
The TxGNN model predicts it may be effective for **Posterolateral Myocardial Infarction**, ranking this as its top prediction with a score of **99.87%**; however, the automated evidence search identified **no registered clinical trials** and **no directly relevant publications** for this specific MI subtype.
Mechanistic plausibility is strong and reinforced by the landmark ISIS-1 trial, though critical data gaps in MHRA licence records, mechanism of action, and safety data must be resolved before a complete evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; angina pectoris (BNF Section 2.4 — MHRA licence records not captured in this dataset) |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| UK Market Status | Not captured in dataset (Atenolol is a widely licensed generic in the UK — likely a data collection error) |
| Number of Marketing Authorisations | Not captured (0 returned — data gap) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Atenolol is a selective beta-1 adrenoceptor antagonist. Its primary cardiac effects include reduction in heart rate, myocardial contractility, and myocardial oxygen consumption (MVO₂). In acute myocardial infarction, catecholamine surge drives potentially fatal arrhythmias, infarct extension, and ventricular fibrillation. Beta-1 blockade directly attenuates this sympathetic overdrive, reducing re-infarction risk and cardiovascular mortality — the pharmacological basis that underlies its established class role in acute MI management.

Posterolateral myocardial infarction involves ischaemia in the territory of the left circumflex artery, affecting the posterior and lateral walls of the left ventricle. Unlike inferior MI (which may implicate the right coronary artery and carry higher risk of sinoatrial or atrioventricular nodal dysfunction), posterolateral MI presents no specific anatomical contraindication to beta-blockade. Reducing MVO₂ and suppressing malignant arrhythmias is therefore equally applicable to this subtype.

The prediction aligns closely with the ISIS-1 randomised trial (16,027 patients), which specifically evaluated intravenous followed by oral atenolol in acute MI, demonstrating a statistically significant reduction in cardiovascular mortality at seven days. Although this pivotal study was not retrieved by the automated search pipeline — likely due to pre-1990 database indexing limitations — it provides a robust historical foundation. It is worth noting that beta-blocker use in acute MI is already guideline-endorsed for the drug class; this TxGNN prediction may reflect an existing validated indication rather than a genuinely novel repurposing opportunity.

> **Data gap note:** Detailed mechanism of action data (DrugBank DB00335) was not retrieved by the automated pipeline. The mechanistic analysis above is based on established pharmacological knowledge. A DrugBank API query is recommended to formally populate this field and enable automated mechanistic scoring.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for posterolateral myocardial infarction specifically.

> **Important context:** This reflects a limitation of the automated retrieval rather than a true evidence gap. The following trial, identified in the context of the chronic pulmonary heart disease prediction (rank 9), is noted here for completeness as it evaluates beta-blocker therapy in a broad post-MI population:
>
> | Trial Number | Phase | Status | Enrolment | Key Findings |
> |-------------|-------|--------|-----------|--------------|
> | [NCT03278509](https://clinicaltrials.gov/study/NCT03278509) | Phase 4 | Active, not recruiting | 5,000 | REDUCE-SWEDEHEART: evaluates whether long-term oral beta-blockade reduces death or new MI in patients with preserved LVEF after MI — primary endpoint results pending |
>
> A dedicated manual search for the ISIS-1 trial and subsequent acute MI beta-blocker studies (COMMIT, CAPRICORN) is strongly recommended to supplement the automated evidence base.

---

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction from the automated search.

> **Important context:** As with the clinical trials section, this reflects an automated retrieval gap rather than a true absence of evidence. Beta-blocker use in acute MI represents one of the most extensively studied topics in cardiology. A manual PubMed search using terms such as "atenolol myocardial infarction" or "beta-blocker acute MI" is required to capture the relevant evidence base before any evaluation decision is made.

---

## All Predicted Indications — Summary

The TxGNN model generated 9 predictions for Atenolol. The complete list is summarised below to support prioritisation:

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|----------|
| 1 | Posterolateral Myocardial Infarction | 99.87% | L5 | Hold |
| 2 | Posteroinferior Myocardial Infarction | 99.87% | L4 | Research Question |
| 3 | Malignant Renovascular Hypertension | 99.85% | L4 | Hold |
| 4 | Malignant Hypertensive Renal Disease | 99.85% | L5 | Hold |
| 5 | Pulmonary Hypertension — Lung Disease/Hypoxia (Group 3) | 99.84% | L5 | Hold ⚠️ |
| 6 | Pulmonary Hypertension — Unclear/Multifactorial (Group 5) | 99.84% | L5 | Hold ⚠️ |
| 7 | Septal Myocardial Infarction | 99.84% | L4 | Hold |
| 8 | Braddock Syndrome | 99.80% | L5 | Hold |
| 9 | Chronic Pulmonary Heart Disease (Cor Pulmonale) | 99.04% | L3 | Research Question |

**Key observations:**

- **Ranks 1, 2, 7 — MI subtypes:** Mechanistically coherent with Atenolol's established cardiovascular profile. The apparent absence of subtype-specific trial data reflects how acute MI trials historically enrol patients by clinical presentation and ECG criteria rather than anatomical territory. The ISIS-1 trial data is directly applicable but was not captured automatically.

- **Rank 2 — Posteroinferior MI (L4):** One directly relevant randomised crossover study identified ([PMID 3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/)). Caution warranted: inferior MI may involve the right coronary artery, and atenolol may worsen conduction abnormalities (AV block, sinus bradycardia) in this subtype.

- **Rank 9 — Chronic Pulmonary Heart Disease (L3):** The strongest evidence base among all predictions (1 related Phase 4 trial, 15 publications). Atenolol's high beta-1 selectivity theoretically enables cardiac protection in COPD comorbidity whilst minimising bronchospasm risk, but right ventricular function must be carefully evaluated before use.

- **Ranks 5 & 6 — Pulmonary Hypertension ⚠️:** These carry a plausible safety concern. Even selective beta-1 blockade may exhibit beta-2 spillover at higher doses, potentially causing pulmonary vasoconstriction and worsening right heart afterload. The 20 publications retrieved for Group 3 PH were confirmed as false-positive results upon manual review — all relate to general hypoxia biology (HIF-1α, tumour hypoxia, neurodegeneration) and are entirely unrelated to Atenolol's use in pulmonary hypertension.

- **Rank 8 — Braddock Syndrome:** A rare SETBP1-related neurodevelopmental disorder. No mechanistic link to beta-1 blockade has been established. The high TxGNN score likely reflects knowledge graph topological proximity rather than genuine biological relevance. Not recommended for further evaluation.

---

## UK Market Information

MHRA marketing authorisation records for Atenolol were not retrieved by the automated pipeline (0 licences returned). This is inconsistent with Atenolol's well-established status as a licensed generic medicine in the United Kingdom, and is considered a data collection error rather than reflecting actual market status.

Atenolol is listed in the **British National Formulary (BNF), Section 2.4 — Beta-adrenoceptor blocking drugs**, and is available from multiple generic manufacturers. Based on established knowledge, the following are the principal UK-licensed presentations:

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|--------------|-------------|---------------------|
| PL not retrieved — data gap | Atenolol 25 mg tablets (generics) | Tablet | Hypertension; angina pectoris; arrhythmias |
| PL not retrieved — data gap | Atenolol 50 mg tablets (generics) | Tablet | Hypertension; angina pectoris; arrhythmias; adjunct in thyrotoxicosis |
| PL not retrieved — data gap | Atenolol 100 mg tablets (generics) | Tablet | Hypertension; angina pectoris |
| PL not retrieved — data gap | Tenormin® (original brand) | Tablet / IV injection | Hypertension; angina; arrhythmias; acute MI (early intervention) |

> **Action required:** Re-run the MHRA/product licence database query for Atenolol (INN) to retrieve PL numbers, full SmPC references, and confirmed approved indications before proceeding with any evaluation stage.

---

## Safety Considerations

Safety data (SmPC warnings, contraindications, drug–drug interactions) were not retrieved by the automated pipeline. This is classified as a Blocking severity data gap (DG001), meaning the safety screening stage (S1) cannot formally commence until this information is obtained.

Please refer to the **Atenolol SmPC** and **BNF Section 2.4** for full prescribing information. Report suspected adverse reactions via the **Yellow Card Scheme** at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk/).

The following is provided from established pharmacological knowledge as an interim reference only — it does not substitute for the formal SmPC review:

**Key Warnings:**
- Abrupt withdrawal may precipitate rebound angina, myocardial infarction, or arrhythmia — always taper the dose gradually
- May cause bronchospasm even at therapeutic doses in patients with obstructive airways disease; this is particularly relevant to the chronic pulmonary heart disease prediction (rank 9) where COPD is frequently comorbid
- May mask tachycardia as a warning sign of hypoglycaemia; use with caution in insulin-dependent diabetes

**Contraindications:**
- Cardiogenic shock or uncontrolled heart failure
- Second- or third-degree atrioventricular block (in the absence of a functioning pacemaker)
- Sick sinus syndrome; severe sinus bradycardia
- Severe peripheral arterial occlusive disease; Prinzmetal's angina
- Uncontrolled phaeochromocytoma (without concurrent alpha-blockade)
- Metabolic acidosis

**Drug Interactions:**
- **Verapamil / diltiazem:** Concurrent use substantially increases the risk of severe bradycardia and atrioventricular block; generally avoid co-administration
- **Clonidine:** Atenolol should not be withdrawn before clonidine when stopping both drugs — rebound hypertension risk
- **NSAIDs:** May attenuate the antihypertensive effect of atenolol
- **Insulin and oral hypoglycaemics:** Glycaemic response may be altered; symptoms of hypoglycaemia (particularly tachycardia) may be masked

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction linking Atenolol to posterolateral myocardial infarction is mechanistically coherent and well-grounded in established cardiovascular pharmacology, but two critical issues prevent progression: first, this is likely an existing guideline-endorsed indication for the beta-blocker class rather than a genuinely novel repurposing opportunity; second, two data gaps of Blocking and High severity are present in this evidence pack (MHRA licence data and mechanism of action), which prevent the mandatory safety screening stage (S1) from proceeding.

**To proceed, the following is needed:**

- **Resolve data gap DG001 (Blocking — Safety):** Download and parse the Atenolol SmPC from the MHRA product database to obtain confirmed warnings, contraindications, and UK-approved indications. This is a prerequisite for any further evaluation stage.
- **Resolve data gap DG002 (High — Mechanism):** Query DrugBank API for DB00335 to retrieve the full mechanism of action, pharmacodynamic data, and drug categories. This is required for automated mechanistic plausibility scoring.
- **Re-run MHRA licence query:** Correct the erroneous zero-licence dataset to confirm UK marketing authorisation status, approved indications, and PL numbers.
- **Manual literature search:** Conduct a targeted PubMed search for "atenolol myocardial infarction" to retrieve the ISIS-1 trial and contemporaneous evidence base, which was not captured by the automated pipeline due to pre-1990 indexing limitations.
- **Clarify novelty of the primary prediction:** Confirm whether posterolateral MI (or acute MI broadly) is already covered under Atenolol's existing UK marketing authorisation. If so, this prediction has no repurposing value and attention should be redirected to genuinely unexplored indications.
- **Prioritise chronic pulmonary heart disease (rank 9) for future research planning:** This indication offers the most scientifically novel and actionable research question within the predictions (L3 evidence, 15 supporting publications, 1 relevant Phase 4 trial). A prospective pilot study in COPD patients with comorbid hypertension or ischaemic heart disease should specify right ventricular function criteria (suggested exploratory threshold: RV EF ≥ 35%) to manage the risk of right heart decompensation.
- **Flag pulmonary hypertension predictions (ranks 5–6) as potential harm signals:** The retrieved literature for these indications was confirmed as false-positive on manual review. These should be explicitly excluded from further consideration pending a specific safety review of beta-blockade in pulmonary hypertension subtypes.

---

*This report is generated for research purposes only. All predictions require prospective clinical validation before any prescribing decisions are made. This report does not constitute medical advice. Data cutoff: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

