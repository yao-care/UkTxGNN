---
layout: default
title: Phenol
parent: Model Prediction Only (L5)
nav_order: 490
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Phenol: predicted new indication Acne keloid (evidence level L5). Approved use: Dermatitis"
monitor_inn: "Phenol"
predicted_indications: ["acrodermatitis chronica atrophicans", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "neonatal dermatomyositis", "amyopathic dermatomyositis", "acne keloid", "hydroa vacciniforme, familial", "severe nonproliferative diabetic retinopathy", "dry eye syndrome"]
---

# Phenol
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

# Phenol: From Dermatitis to Acne Keloid

## One-Sentence Summary

Phenol is a topical antiseptic and caustic agent, originally associated with the treatment of dermatitis.
The TxGNN model predicts it may be relevant to **acne keloid** (acne keloidalis), but there are **no registered clinical trials** and only **1 indirectly related publication** (a non-randomised report on phenol peeling for wrinkles and acne scars).
This is a model prediction with very limited supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis |
| Predicted New Indication | Acne keloid (the highest-ranked prediction, acrodermatitis chronica atrophicans, has no supporting evidence and no plausible mechanism, so the best-supported prediction is used for this report) |
| TxGNN Prediction Score | 99.94% (acne keloid); the top-ranked prediction scored 99.95% |
| Evidence Level | L4 (acne keloid); L5 for the top-ranked prediction |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, phenol is a protein-denaturing, caustic and antiseptic agent. At higher concentrations it is used as a chemical peeling agent.

Phenol peels cause controlled injury to the epidermis and papillary dermis, followed by remodelling and new collagen formation. This is plausibly relevant to acne scarring. A 2007 report (PMID 17204096) describes a modified phenol peel (Exoderm) used on facial wrinkles, acne scars and other skin problems in Asian patients.

However, this evidence concerns acne scars in general, not acne keloidalis, which is a chronic inflammatory folliculitis with scarring. Caustic injury in keloid-prone tissue could also worsen scarring. The link to the original dermatitis indication is therefore only loose.

Other predictions in the list (for example acrodermatitis chronica atrophicans, dermatomyositis, interstitial lung disease, diabetic retinopathy and dry eye) have no plausible pharmacological rationale. The high scores likely reflect network proximity in the knowledge graph rather than biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17204096](https://pubmed.ncbi.nlm.nih.gov/17204096/) | 2007 | Clinical series (uncontrolled) | The Journal of Dermatology | Modified phenol peel (Exoderm) evaluated for facial wrinkles, acne scars and other skin problems in Asian patients. It was designed to reduce side effects such as arrhythmia, prolonged erythema, hypopigmentation, hypertrophic scarring and keloid. Indirect evidence only. |

For dry eye syndrome (score 99.04%), 20 publications were retrieved, but none evaluated phenol. They concern dry eye pathophysiology or other compounds and are not evidence for phenol.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1203040K0AAAGAG | Phenol 0.71% | Not specified | Not specified |

The data compiled for this report do not include the authorisation's dosage form or approved indication text. The authorisation number is not in standard MHRA PL format, so it should be verified.

---

## Safety Considerations

Contraindications recorded in the knowledge graph (not taken from label text) include: epilepsy, liver disease, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, neutropenia, agranulocytosis, sudden cardiac arrest, heart conduction disease and heart block, respiratory failure, peripheral vascular disease, active peptic ulcer disease, herpes simplex, herpes zoster, cytomegalovirus infection, common wart, anogenital human papillomavirus infection, cancer and lymphoma. Dermatitis also appears on this list, which conflicts with the original indication and needs clarification.

Other concerns raised in the data:
- Phenol is caustic and irritant to tissue, so ocular use would be a safety concern.
- Its tissue-destructive properties and systemic toxicity are a concern for use in neonates.
- Modified phenol peels have been associated with arrhythmia, prolonged erythema, hypopigmentation and hypertrophic scarring or keloid.

No drug interaction data were found. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions are driven by the model alone. Only one indirectly related, uncontrolled report exists (acne scars, not acne keloidalis), and there are no trials. The mechanistic link is weak, and the safety signals (caustic injury in keloid-prone skin, cardiac and systemic toxicity) are significant. Acne keloid may be treated as a research question rather than a candidate for development.

**To proceed, the following is needed:**
- Mechanism of action data and the licensed product's SmPC (warnings, contraindications, dosage form, approved indication)
- Verification of the UK authorisation details
- Controlled studies of phenol in acne keloidalis, with scarring outcomes and safety monitoring
- Review of the knowledge-graph contraindications against the original dermatitis indication
- Route and formulation compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

