---
layout: default
title: Amiodarone
parent: Moderate Evidence (L3-L4)
nav_order: 52
evidence_level: L4
indication_count: 10
---

# Amiodarone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Amiodarone: From Ventricular Fibrillation to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is an antiarrhythmic drug, originally used for ventricular fibrillation.
The TxGNN model predicts it may be effective for **catecholaminergic polymorphic ventricular tachycardia (CPVT)**, but there are **no registered clinical trials** and only **9 publications** (cohorts, a systematic review, a review and case reports). None of them provides direct evidence for amiodarone in this condition, and the literature suggests it is generally less effective than other options.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ventricular fibrillation |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available for this report. Amiodarone is a multichannel-blocking antiarrhythmic, with potassium, sodium and calcium channel effects and beta-adrenergic antagonism. Its efficacy in ventricular fibrillation is established, and mechanistically it may be applicable to other ventricular arrhythmias.

CPVT is a rare inherited arrhythmia driven by calcium-handling abnormalities (RYR2 or CASQ2 variants) that trigger delayed afterdepolarisations during adrenergic stress. Amiodarone's beta-blocking and calcium-channel effects are plausibly relevant. The high TxGNN score is probably driven mainly by the shared ventricular arrhythmia phenotype rather than by a specific mechanistic match.

The link is weak. The retrieved literature indicates amiodarone is generally ineffective in CPVT compared with beta-blockers, flecainide and sympathetic denervation. No direct comparative evidence for amiodarone was found.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic review | Life (Basel) | Clinical characteristics, genetics and arrhythmic outcomes of CPVT patients from China, compared with Western populations |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Retrospective cohort | Rev Cardiovasc Med | Clinical characteristics, genetic basis, healthcare use and costs of CPVT patients in a Chinese city |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | Antiarrhythmic drugs remain important for acute conversion and chronic prevention of ventricular arrhythmias |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case report | Pacing Clin Electrophysiol | Flecainide suppressed defibrillator-induced storming in a 14-year-old with CASQ2-related CPVT |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case report | Turk Pediatri Arsivi | CPVT presenting as sudden cardiac arrest in a 2-year-old |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case report | Medicine | Six-year delayed diagnosis of CPVT with an RYR2 variant in a 9-year-old |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case report | Front Cardiovasc Med | CPVT resolved with right cardiac sympathetic denervation after left denervation in a teenager |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case report | BMJ Case Rep | Young child with out-of-hospital cardiac arrest and recurrent VT/VF requiring 40 shocks; diagnostic dilemma |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case report | Anesth Analg | Neonate with long QT syndrome and refractory ventricular arrhythmias treated with lidocaine, esmolol and amiodarone (not CPVT) |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0203020D0AAAAAA | Amiodarone HCl tablets 100 mg | Not specified | Not specified |

Only one valid single-ingredient authorisation is recorded, and no indication text is available for it. Please check the MHRA record and the BNF classification for current licensed indications.

---

## Safety Considerations

- **Contraindications and cautions (from knowledge-graph drug–disease links, not label text)**:
  - Cardiac conduction and rhythm: long QT syndrome (including familial), torsades de pointes, atrioventricular block, sick sinus syndrome
  - Thyroid: hypothyroidism, myxoedema, congenital hypothyroidism, hyperthyroidism, Graves' disease, thyrotoxicosis
  - Lung: interstitial lung disease, eosinophilic pneumonia, pulmonary eosinophilia, extrinsic allergic alveolitis, hypersensitivity pneumonitis, farmer's lung
  - Liver and gallbladder: liver disease, drug-induced liver injury, gallbladder disease
  - Eye and nerve: optic neuritis, optic nerve disease, visual pathway disease, corneal deposits, peripheral neuropathy, peripheral nervous system disease
  - Metabolic: potassium deficiency
- **Drug Interactions**: 100 interactions were identified. Major-severity examples:
  - Cisapride, clarithromycin, dolasetron and eliglustat
  - Amphotericin B (including its lipid, liposomal and cholesteryl sulfate formulations) and clotrimazole
  - Hydrocortisone and dexamethasone
  - Agalsidase beta

  Moderate examples include famotidine, cimetidine, aprepitant, bisacodyl and budesonide.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The CPVT prediction rests on model score and phenotype similarity alone. There are no trials and no direct amiodarone data, and the literature points to better-established options (beta-blockers, flecainide, sympathetic denervation). The safety burden is substantial, particularly QT prolongation, conduction disease and the DDI load.

**To proceed, the following is needed:**
- Direct comparative or mechanistic evidence for amiodarone in CPVT (preclinical or clinical)
- Mechanism of action data
- Label-based warnings and contraindications, and the licensed indication text for the UK authorisation
- A specialist-led safety monitoring plan (ECG, thyroid, liver and lung monitoring)

**Note:** The data compiled for this report show stronger support for amiodarone in **ventricular tachycardia** (TxGNN score 99.64%, Evidence Level L1). That evidence includes completed Phase 3 trials such as ALPS (3,024 patients) and AVID, and it is a near-label use. It may be a more productive candidate for further evaluation, with guardrails for pulmonary, thyroid, hepatic and ocular toxicity, QT prolongation and bradycardia.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

