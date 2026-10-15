---
layout: default
title: Diltiazem
parent: Model Prediction Only (L5)
nav_order: 229
evidence_level: L5
indication_count: 1
---

# Diltiazem
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Diltiazem: From Hypertension and Cardiac Arrhythmia to Susceptibility to Ischaemic Stroke (Obsolete Term)

## One-Sentence Summary

Diltiazem is a calcium channel blocker originally used for hypertension, atrial fibrillation, Prinzmetal angina and ventricular tachycardia.
The TxGNN model predicts it may be effective for **susceptibility to ischaemic stroke** (an obsolete ontology term),
but **no clinical trials or publications** were found in the data compiled for this report, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension, atrial fibrillation, Prinzmetal angina, ventricular tachycardia (from the knowledge graph; no approved indication text is available for the UK product) |
| Predicted New Indication | Obsolete susceptibility to ischaemic stroke |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. From general pharmacology, diltiazem is a non-dihydropyridine calcium channel blocker. It lowers blood pressure, slows the heart rate and dilates blood vessels.

Several of its established uses relate to stroke risk factors. Hypertension is the leading modifiable risk factor for stroke, and atrial fibrillation is a major cause of cardioembolic stroke. Blood pressure lowering and heart rate control could therefore plausibly reduce stroke susceptibility. Vasodilation of cerebral and coronary vessels is another possible link.

These links are indirect inferences. No trial or publication in the data compiled for this report supports them, and the high TxGNN score is a model output, not clinical evidence. The disease term is also labelled "obsolete", which suggests a deprecated ontology entry. It may map to a broader or different current term, such as ischaemic stroke or stroke susceptibility, and should be reconciled before further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0107010AAAAAJAJ (BNF code, not a PL number) | Diltiazem HCl cream 2% | Cream | Not stated in the data compiled |

The data compiled for this report show one valid single-ingredient product and no cancelled authorisations. A 2% diltiazem cream is a topical product, so its use differs from oral or intravenous diltiazem for the cardiovascular indications above. The route of administration for the predicted new indication has not yet been assessed.

## Safety Considerations

**Contraindications and cautions suggested by the knowledge graph** (derived from drug-disease links, not from label text, so they must be verified against the SmPC):

- **Cardiac conduction and rhythm:** atrioventricular block, sick sinus syndrome (including familial), Wolff-Parkinson-White syndrome, Lown-Ganong-Levine syndrome, ventricular tachycardia (including catecholaminergic and infant forms)
- **Haemodynamic and structural heart disease:** hypotension, aortic stenosis (including supravalvular), aortic valve disease, hypertrophic cardiomyopathy, renal artery obstruction
- **Organ function:** kidney disease, liver disease, gallbladder disease
- **Haematological:** neutropenia, agranulocytosis
- **Angioedema:** acquired, hereditary (including C1 inhibitor deficiency), non-histaminic, and renin-angiotensin-aldosterone system blocker-induced forms
- **Other:** pyoureter, connective tissue disease, bone disease, cartilage disease

**Drug interactions:** 100 interactions were identified in total, and the first 20 are summarised here. One is rated **Major**: loperamide. The others shown are rated **Moderate**:
- Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide (including nasal)
- Calcium products: calcium phosphate, acetate, carbonate, chloride, citrate, glubionate and glucoheptonate
- Others: pioglitazone, bupropion, aprepitant, morphine, acetylsalicylic acid, canagliflozin

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (Evidence Level L5), and the target disease term is obsolete. The only UK authorisation identified is a topical cream, with no approved indication text available. The case for the prediction is currently theoretical.

**To proceed, the following is needed:**
- Reconcile the obsolete disease term with a current ontology term, such as ischaemic stroke or stroke susceptibility
- Mechanism of action data (for example from DrugBank) to support the mechanistic-link analysis
- A targeted literature and trial search on diltiazem and stroke prevention or outcomes
- SmPC and BNF warnings and contraindications for the relevant UK formulations, as the safety screening data are incomplete
- Confirmation of the UK marketing authorisation details (PL number, dosage form, approved indication) and of routes of administration suitable for the proposed use
- Assessment of the interaction and contraindication profile in patients at stroke risk, who often have conduction disease, hypotension or are on multiple medicines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

