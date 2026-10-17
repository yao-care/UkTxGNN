---
layout: default
title: Cyclizine
parent: Model Prediction Only (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cyclizine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Cyclizine"
predicted_indications: ["acute laryngopharyngitis", "headache disorder", "trigeminal autonomic cephalalgia", "IgE responsiveness, atopic"]
---

# Cyclizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Cyclizine: From Allergic and Upper Respiratory Conditions to Allergic Urticaria

## One-Sentence Summary

Cyclizine is a first-generation H1-antihistamine, originally used for allergic rhinitis, conjunctivitis, common cold symptoms and motion sickness.
The TxGNN model predicts it may be effective for **allergic urticaria**,
but there are currently **no clinical trials** and **no publications** supporting this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, conjunctivitis (atopic, papillary, vernal), nasopharyngitis, motion sickness (knowledge-graph-derived; no approved indication text is available in the UK licence record) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cyclizine is a first-generation H1-antihistamine, and its efficacy in allergic rhinitis and allergic conjunctivitis is the basis of its established allergic indications.

Urticaria is a histamine-mediated condition, so H1 receptor blockade is biologically plausible. Allergic urticaria is closely related to the existing allergic indications (rhinitis, conjunctivitis), which likely explains the high model score.

However, H1-antihistamines are already standard therapy for urticaria, and second-generation, non-sedating agents are generally preferred. No cyclizine-specific evidence was available, so the prediction is plausible but unsupported by clinical data. It is also not a clearly novel mechanism; it largely extends an existing one.

### Other Predicted Indications (Overview)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Nasal cavity disease | 99.96% | L5 | Broad term; overlaps with existing rhinitis indications |
| 3 | Acute laryngopharyngitis | 99.95% | L5 | Related to existing pharyngitis and common cold indications; symptomatic benefit only |
| 4 | Cold urticaria | 99.84% | L5 | H1 blockade plausible; second-generation agents preferred |
| 5 | Rosacea conjunctivitis | 99.75% | L5 | Weak antihistamine link |
| 6 | Headache disorder | 99.49% | L4 | Only indirect literature (see below) |
| 7 | Trigeminal autonomic cephalalgia | 99.43% | L5 | No clear mechanistic rationale |
| 8 | Rhinitis | 99.35% | L5 | Already covered by the existing label |
| 9 | Recalcitrant atopic dermatitis | 99.28% | L5 | May relieve itch and sleep disturbance only |
| 10 | IgE responsiveness, atopic | 98.83% | L5 | General association; H1 blockade does not modify IgE responsiveness |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was retrieved for allergic urticaria. For the sixth-ranked prediction (headache disorder), two papers were retrieved, but they are only indirectly relevant:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3926322](https://pubmed.ncbi.nlm.nih.gov/3926322/) | 1985 | RCT | Cephalalgia | Randomised parallel trial (114 patients) comparing naproxen sodium with an ergotamine/caffeine/cyclizine combination for acute migraine; cyclizine was only a component of the comparator, so cyclizine alone was not evaluated |
| [20420788](https://pubmed.ncbi.nlm.nih.gov/20420788/) | 2010 | Cohort | Int J Clin Pharmacol Ther | Pharmacy database analysis of migraine prescribing patterns and costs, focused on triptans; does not evaluate cyclizine |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0406000F0AAACAC | Cyclizine HCl tablets 50 mg | Tablet (as indicated by product name) | Not available in the licence record |

The listed identifier follows a BNF-style code format rather than a standard MHRA "PL" number, so it should be verified against the MHRA register. BNF classification and NICE appraisal information should be checked directly.

## Safety Considerations

**Contraindications and conditions flagged by the knowledge graph (not label text):** the TxGNN knowledge graph links cyclizine to caution or contraindication in conditions including:
- Cardiovascular: hypertension, coronary artery disease, myocardial infarction, atherosclerosis, hypotensive disorder
- Neurological and ocular: epilepsy, ocular hypertension
- Hepatic, renal and gastrointestinal: liver disease, kidney disease, pancreatitis, gallbladder disease, peptic ulcer disease, inflammatory bowel disease, *Clostridium difficile* colitis, necrotizing enterocolitis
- Endocrine and metabolic: diabetes mellitus, diabetic ketoacidosis, hypothyroidism, adrenocortical insufficiency (Addison disease)
- Other: benign prostatic hyperplasia, pyoureter, hemoglobinopathy

These come from knowledge-graph edges, not product labelling, and should be confirmed against the SmPC.

**Drug Interactions:** 100 interactions were recorded; the main ones in the data reviewed are:
- **Major:** potassium chloride, potassium citrate
- **Moderate (additive anticholinergic effects):** atropine, hyoscyamine, glycopyrronium, dicyclomine, trospium, scopolamine, propantheline, methscopolamine, mepenzolate
- **Moderate (other):** morphine, opium, loperamide, eluxadoline, metoclopramide, prucalopride, dronabinol, nabilone

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by the TxGNN model score (L5), with no trials or cyclizine-specific literature. Established, better-tolerated second-generation antihistamines already serve urticaria, and many top predictions merely overlap with existing allergic indications rather than representing true repurposing.

**To proceed, the following is needed:**
- Cyclizine-specific clinical or observational evidence in urticaria (or a comparison against non-sedating antihistamines)
- Official SmPC warnings and contraindications (currently unavailable, and this blocks safety screening)
- Mechanism of action data
- Approved indication text and verified MHRA authorisation details for the UK product
- Assessment of the safety burden of a sedating, anticholinergic agent in chronic urticaria use, including the knowledge-graph-flagged conditions above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

