---
layout: default
title: Amiodarone
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Amiodarone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Amiodarone: From Ventricular Arrhythmia to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is a broad-spectrum Class III antiarrhythmic agent, widely used for the treatment and prevention of life-threatening ventricular and supraventricular arrhythmias.
The TxGNN model predicts it may be effective for **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)** — a rare inherited arrhythmia syndrome — with **no registered clinical trials** and **10 publications** currently identified in support of this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No UK marketing authorisation records found in current dataset |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 (observational studies and case series only; no dedicated RCT) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Amiodarone is a multi-channel antiarrhythmic agent with a uniquely broad pharmacological profile. Its primary mechanism involves blockade of IKr/IKs potassium channels, prolonging the action potential duration (APD) and effective refractory period (ERP). It additionally blocks fast sodium channels (INa) and L-type calcium channels (ICa-L), and exerts non-competitive beta-adrenoceptor blockade — encompassing properties of all four Vaughan-Williams classes simultaneously. Formal mechanism of action data from DrugBank was not available in this evidence pack (a flagged data gap); the above is derived from published pharmacological literature cited within the evidence.

CPVT is a rare inherited ion channelopathy in which mutations in the *RYR2* gene (~60% of cases) or *CASQ2* gene (~3–5%) cause excessive intracellular calcium release during exercise or adrenergic stimulation. This triggers delayed afterdepolarisations (DADs), which generate triggered activity manifesting as bidirectional or polymorphic ventricular tachycardia. Amiodarone's ICa-L blockade and non-competitive beta-blockade theoretically suppress this DAD-driven mechanism, offering a plausible pharmacological rationale for the TxGNN model's prediction.

However, amiodarone's targeting is notably less precise than flecainide, which directly inhibits the pathological RYR2 calcium release channel via INa blockade and has emerged as the preferred second-line agent in contemporary CPVT management (supported by PMID 22553997). The existing literature consistently positions amiodarone as a third-line adjunct or acute rescue agent — deployed when beta-blockers and flecainide have failed, or to terminate ICD shock storms. No dedicated randomised controlled trial of amiodarone in CPVT has been conducted, and it does not currently feature as a recommended therapy in major CPVT treatment guidelines.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | Overview of antiarrhythmic pharmacotherapy for ventricular arrhythmias; reviews amiodarone's role as an adjunctive option in CPVT when first-line agents fail |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Retrospective Cohort | Life (Basel) | Systematic review of CPVT patients in China; describes clinical characteristics, genetic basis (RYR2/CASQ2), and treatment outcomes including antiarrhythmic drug use |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Retrospective Cohort | Rev Cardiovasc Med | CPVT clinical characteristics, genetic basis, and healthcare resource utilisation from a Chinese cohort; real-world management data across drug classes |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case Series | Pacing Clin Electrophysiol | Flecainide suppressed ICD-triggered arrhythmic storm in a CPVT patient with a CASQ2 mutation; contextualises amiodarone's comparatively limited targeted efficacy |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case Report | BMJ Case Rep | Young child with out-of-hospital cardiac arrest due to refractory VT/VF; amiodarone administered during resuscitation requiring 40 defibrillation shocks before CPVT diagnosis was made |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case Report | Anesth Analg | Neonate with refractory ventricular arrhythmia (long QT/VT overlap); multimodal pharmacotherapy including amiodarone, esmolol, and lidocaine alongside ventricular pacing described |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case Report | Front Cardiovasc Med | CPVT in a teenager ultimately resolved only by bilateral cardiac sympathetic denervation after left-sided procedure failed; illustrates treatment-refractory severity when pharmacotherapy is exhausted |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case Report | Turk Pediatri Arsivi | CPVT presenting as sudden cardiac arrest in a 2-year-old; highlights diagnostic challenges and acute management trajectory in paediatric CPVT |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case Report | Medicine | Six-year delayed CPVT diagnosis (RYR2 c.7580T>G mutation) in a 9-year-old child; discusses antiarrhythmic management including role of amiodarone |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Case Report | Rev Esp Cardiol | Arrhythmic storm induced by ICD shocks in a CPVT patient; amiodarone used as acute rescue therapy to interrupt the hyperadrenergic cycle |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Amiodarone's multi-channel pharmacology offers a mechanistically plausible — but imprecise — rationale for CPVT management. The available evidence consists entirely of case reports and observational cohorts (Evidence Level L3), with no dedicated clinical trials registered and no recognised guideline endorsement for this indication. Amiodarone's current role in CPVT is limited to third-line or emergency rescue use, where its benefit is largely empirical and overshadowed by flecainide's more targeted RYR2 inhibition.

**To proceed, the following is needed:**
- Completion of the formal mechanism of action data gap (DrugBank, DG002) to support mechanistic analysis
- Retrieval of UK SmPC safety data including warnings, contraindications, and drug interactions (DG001), particularly given amiodarone's known pulmonary toxicity (1–2%/year), thyroid dysfunction, hepatotoxicity, and CYP2C9/CYP3A4-mediated interactions
- Prospective registry or observational data specifically evaluating amiodarone in CPVT patients refractory to beta-blockers and flecainide, to characterise real-world efficacy and tolerability
- Paediatric-specific pharmacokinetic and safety assessment, as CPVT predominantly presents in childhood and adolescence (enzyme immaturity, thyroid development susceptibility)
- Clarification of UK regulatory status — no MHRA marketing authorisation records were identified in this dataset, which should be verified against the current BNF and MHRA register before any clinical planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

