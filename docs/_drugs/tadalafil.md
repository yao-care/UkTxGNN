---
layout: default
title: Tadalafil
parent: Model Prediction Only (L5)
nav_order: 591
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "Tadalafil"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
description: "Tadalafil: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Not recorded in the local data"
---

# Tadalafil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Tadalafil: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor, originally used for erectile dysfunction, benign prostatic hyperplasia and pulmonary hypertension.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Tadalafil is generally known as a PDE5 inhibitor: it raises cGMP levels and promotes vasodilation, which underlies its use in erectile dysfunction and pulmonary hypertension.

The link to the predicted indication is weak. Ambras syndrome is a rare congenital disorder associated with chromosomal rearrangements affecting TRPS1 regulation. No clear mechanistic connection to PDE5 inhibition has been identified. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, for example the hair-growth effects of other vasodilators such as minoxidil, not biological evidence or a validated pharmacological rationale.

**Other predictions in the same set**

All other predicted indications also have no clinical trials, and only one has any literature:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Hypertrichosis | 0.9998 | L5 | Speculative. Hypertrichosis is a known adverse effect of vasodilators, so the direction of effect is unclear. |
| Malformation syndrome with odontal and/or periodontal component | 0.9997 | L5 | No identifiable mechanism. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |
| Syndrome with a Dandy-Walker malformation as major feature | 0.9997 | L5 | No credible mechanism for a structural developmental anomaly. |
| Isolated genetic hair shaft abnormality | 0.9996 | L5 | No established mechanism. Likely phenotypic proximity to hypertrichosis. |
| Familial isolated trichomegaly | 0.9965 | L5 | No supported role for PDE5 inhibition. |
| Kyphoscoliotic heart disease | 0.9943 | L5 | Indirect but most biologically coherent, given the pulmonary hypertension and right heart strain. Vasodilators may worsen ventilation-perfusion matching in hypoxia-driven disease. |
| Migraine with brainstem aura | 0.9908 | L5 | The only evidence is a case report suggesting tadalafil may provoke aura, which is a possible adverse effect rather than a benefit. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (Ambras type hypertrichosis universalis congenita), currently no related literature is available.

The only publication identified across the predicted indications relates to migraine with brainstem aura:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) | 2006 | Case report | Cephalalgia | Tadalafil associated with typical migraine aura without headache, suggesting a possible adverse effect rather than a therapeutic benefit |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0704050R0AAAAAA | Tadalafil Tab 10 mg | Tablet (10 mg) | Not stated in the data compiled |

The identifier shown is a BNF-style code rather than a standard MHRA PL number, and the dosage form is inferred from the product name. Please verify both against the MHRA register and the BNF.

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text)**

The knowledge graph links tadalafil to the following conditions as contraindications. These should be checked against the SmPC:
- **Cardiovascular:** acute coronary syndrome, myocardial infarction, coronary thrombosis, aortic stenosis and aortic valve disease, hypertrophic cardiomyopathy, hypotensive disorder
- **Cerebrovascular:** stroke, cerebrovascular disorder, cerebral infarction
- **Penile conditions:** priapism, Peyronie disease, penile fibromatosis, balanitis xerotica obliterans
- **Haematological:** sickle cell anaemia, hemoglobinopathy, plasma cell myeloma, leukaemia, blood coagulation disease
- **Other:** liver failure, epilepsy, hearing loss disorder, functional visual loss

**Drug interactions**

The interaction screen returned 100 interactions in total, and 20 are listed in the data compiled for this report. Most are of moderate severity. Examples include:
- Aprepitant, dexamethasone, clarithromycin, cimetidine, miconazole and clotrimazole (moderate)
- SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin and ertugliflozin (moderate)
- Lorcaserin, sapropterin and troglitazone (moderate)
- Papaverine (minor)

Interactions with pantoprazole, glimepiride, doxycycline, morphine, metformin and omeprazole are of unknown severity.

**Signal from the migraine report:** the case report suggests tadalafil may provoke migraine aura, so caution is warranted in patients with migraine.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no clinical trials or publications and no plausible mechanistic link. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a therapeutic effect. None of the other predicted indications has stronger support. Kyphoscoliotic heart disease is the most biologically coherent, but it is still prediction-only. The migraine signal points towards harm.

**To proceed, the following is needed:**
- Mechanism of action data, to allow proper analysis of any mechanistic link
- Licence details: approved indication text, dosage form, and a verified MHRA PL number
- Warnings and contraindications from the SmPC and BNF, as the safety screen cannot proceed without them
- For kyphoscoliotic heart disease, a literature review and a clearly framed hypothesis that accounts for hypoxia-driven pulmonary hypertension
- Preclinical or mechanistic studies before any clinical consideration of hypertrichosis-related indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

