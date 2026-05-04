---
layout: default
title: Bumetanide
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 1
---

# Bumetanide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Bumetanide: From Oedema and Cardiac Fluid Overload to Acute Pulmonary Heart Disease

## One-Sentence Summary

Bumetanide is a potent loop diuretic, classically indicated for oedema and fluid overload associated with congestive heart failure, hepatic cirrhosis, and renal disease. The TxGNN model predicts it may be effective for **Acute Pulmonary Heart Disease**, with **1 partially relevant clinical trial** and **5 publications** currently providing indirect supporting evidence. However, the mechanistic case is nuanced and the quality of direct evidence is limited, warranting careful clinical review before any translational action.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Oedema associated with congestive heart failure, hepatic and renal disease |
| Predicted New Indication | Acute Pulmonary Heart Disease |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L3 |
| UK Market Status | Not currently marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Formal mechanism of action (MOA) data is not available in this evidence pack. Based on published pharmacological literature, Bumetanide is a potent loop diuretic that inhibits the NKCC2 (sodium-potassium-chloride cotransporter 2) on the thick ascending limb of the loop of Henle, promoting rapid natriuresis and diuresis. This action reduces circulating blood volume, lowers cardiac preload, and relieves pulmonary venous congestion — effects that form the pharmacological bridge between its established use in left-sided congestive heart failure and the TxGNN prediction of benefit in acute pulmonary heart disease.

The TxGNN high prediction score (0.9958) most likely reflects the strong association between loop diuretics and cardiac conditions within the knowledge graph. Both congestive heart failure and acute pulmonary heart disease involve elevated filling pressures and fluid congestion, and loop diuretics are a cornerstone of acute decompensated heart failure management. The 1987 interventional study (PMID 3304383) directly demonstrated that intravenous bumetanide reduces pulmonary artery occluded pressure and cardiac index in patients with acute and chronic heart failure, lending mechanistic plausibility.

However, a critical pathophysiological distinction must be highlighted: **acute pulmonary heart disease** (cor pulmonale) is primarily characterised by **acute right ventricular failure**, not the left ventricular failure where loop diuretics are best evidenced. The right ventricle in this setting is highly preload-dependent, and aggressive diuresis risks worsening right ventricular output and systemic perfusion rather than improving it. The TxGNN model does not discriminate between right- and left-sided cardiac pathophysiology, and this mechanistic duality — potentially beneficial in left heart-driven pulmonary congestion, potentially harmful in true right ventricular failure — represents the core clinical uncertainty requiring resolution.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT07375212](https://clinicaltrials.gov/study/NCT07375212) | Phase 4 | Withdrawn | 0 | Pilot study of a single 4 mg intranasal dose of bumetanide to evaluate acute effects on pulmonary artery pressure and blood volume in heart failure patients with implanted remote monitoring devices (CardioMEMS™/Cordella™). The only identified trial directly testing bumetanide in a pulmonary haemodynamic context; however, withdrawn prior to any enrolment — reason unconfirmed (safety concern vs. recruitment difficulty). |
| [NCT05580510](https://clinicaltrials.gov/study/NCT05580510) | Phase 2/3 | Unknown | 160 | Evaluates empagliflozin and sacubitril/valsartan in adult congenital heart disease with reduced ejection fraction. Bumetanide is not a primary study drug and any involvement would be as background therapy only. Low direct relevance; trial status unverifiable. |
| [NCT06885164](https://clinicaltrials.gov/study/NCT06885164) | N/A | Recruiting | 200 | Seismocardiographic wearable remote monitoring study in a heart failure population. Observational/device methodology with no pharmacological evaluation of bumetanide. Provides disease monitoring context only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Clinical Interventional Study | Br J Clin Pharmacol | IV bumetanide (25 µg/kg) prospectively studied in 24 patients with coronary artery disease and either acute exercise-induced or chronic heart failure. Reduced pulmonary artery occluded pressure and cardiac index whilst increasing systemic vascular resistance. The most directly relevant haemodynamic evidence available, though now nearly 40 years old and focused on left heart failure. |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Pharmacological Review | Drugs | Foundational pharmacological review of bumetanide. Documents efficacy in oedema from congestive heart failure, hepatic and renal disease, and acute pulmonary congestion. Confirms rapid diuretic onset within 30 minutes via oral, IV, or IM routes, and principal action at the loop of Henle. |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Review | Am J Ther | Comprehensive review of therapeutic options in acute decompensated heart failure (AHF), encompassing over 1 million annual US hospitalisations. Confirms loop diuretics as the cornerstone of acute symptom management, with discussion of clinical trial outcomes in AHF. |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Comparative Review | Ann Pharmacother | Systematic comparison of all loop diuretics, evaluating pharmacokinetic profiles, comparative safety, efficacy, and cost. Provides context for bumetanide's position relative to furosemide as the class reference agent. |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Epidemiological / Retrospective Cohort | Am J Emerg Med | Large-scale contemporary analysis of heart failure presentations to US emergency departments (2016–2023), covering admission rates, evaluation, and treatment trends. Provides current epidemiological background for acute heart failure management. |

---

## UK Market Information

Bumetanide currently holds **no MHRA marketing authorisations** in the United Kingdom based on the available regulatory dataset. No licensed products, dosage forms, or approved indications were identified.

> **Note for Prescribers**: Any clinical use of bumetanide in the UK would require consideration of unlicensed/off-label prescribing frameworks, named patient access arrangements, or enrolment within a formal clinical trial. Please consult current MHRA guidance on unlicensed medicines and NICE appraisal status before clinical use.

---

## Safety Considerations

Formal safety data — including product warnings, contraindications, and drug interaction profiles — are not available in this evidence pack.

> Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a compelling TxGNN prediction score (99.58%), the mechanistic case for bumetanide in acute pulmonary heart disease is potentially counterproductive: aggressive preload reduction in acute right ventricular failure — the defining pathology of this condition — risks haemodynamic deterioration rather than benefit. The sole bumetanide-specific clinical trial in a pulmonary haemodynamic context (NCT07375212) was withdrawn before enrolling any participants, leaving no prospective evidence to evaluate. Existing literature reflects loop diuretic use in left-sided heart failure and does not adequately address the right ventricular context.

**To proceed, the following is needed:**

- **Clinical clarification**: Define whether the target population represents true cor pulmonale (acute right ventricular failure) or left heart-driven acute pulmonary oedema — the therapeutic strategy differs fundamentally between these.
- **MOA documentation**: Formal confirmation of NKCC2 inhibition mechanism and a structured analysis of haemodynamic implications in right versus left ventricular failure.
- **Withdrawal investigation**: Determine the reason for NCT07375212's withdrawal — if due to a safety signal, this is a blocking concern; if administrative or funding-related, the scientific rationale may remain viable.
- **Prospective haemodynamic study**: A carefully monitored dose-finding study with right heart catheterisation or invasive haemodynamic endpoints would be required before any broader clinical evaluation.
- **Full safety assessment**: SmPC and BNF review covering electrolyte imbalance risk (hypokalaemia, hyponatraemia), renal function monitoring requirements, and drug interaction profile — especially with antiarrhythmics, digoxin, and renin-angiotensin system agents.

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require formal clinical validation before application. All content should be reviewed in conjunction with current MHRA, NICE, and BNF guidance.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

