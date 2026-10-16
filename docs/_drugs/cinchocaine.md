---
layout: default
title: Cinchocaine
parent: Model Prediction Only (L5)
nav_order: 169
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Cinchocaine: predicted new indication Bronchitis (evidence level L5). Approved use: Dermatitis"
---

# Cinchocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cinchocaine: From Dermatitis to Bronchitis

## One-Sentence Summary

Cinchocaine (dibucaine) is an amide-type local anaesthetic, originally used for dermatitis-related symptom relief.
The TxGNN model predicts it may be effective for **bronchitis**, but **no clinical trials** and **no publications** currently support this direction. This is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; no approved indication text is available for the UK product) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known pharmacology, cinchocaine is an amide-type local anaesthetic that blocks voltage-gated sodium channels. Its topical use for local pain and itch is the likely basis for its dermatological association.

For bronchitis, an airway anaesthetic effect could plausibly dampen cough reflex or airway irritation. However, there is no evidence that it acts on the underlying infectious or inflammatory process. The high TxGNN score is a network-based computational prediction and is not supported by any trial or publication.

**Other predicted indications (all L5, all Hold)**

All were predicted with scores above 99.6%, with no clinical trials or literature:

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Acrodermatitis chronica atrophicans | 99.76% | Late Lyme disease skin manifestation, treated with antibiotics; at most symptomatic relief |
| 3 | Neonatal dermatomyositis | 99.72% | Immune-mediated; neonatal systemic absorption is a safety concern |
| 4 | Secondary childhood interstitial lung disease with connective tissue disease | 99.72% | No plausible mechanism; paediatric safety bar is high |
| 5 | Acne keloid | 99.67% | Topical symptom relief is conceivable; no evidence on inflammation or scarring |
| 6 | Hydroa vacciniforme, familial | 99.66% | No photoprotective or disease-modifying mechanism |
| 7 | Amyopathic dermatomyositis | 99.65% | Would not address immune pathology |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0107010G0AAAAAA | Cinchocaine HCl ointment 1.1% | Ointment | Not stated in the data compiled for this report |

Note: the identifier shown is a BNF-style classification code (BNF section 1.7, anorectal preparations), not a PL marketing authorisation number. The product is a topical ointment.

## Safety Considerations

- **Knowledge-graph contraindication signals** (these come from drug–disease network links, not from SmPC text): epilepsy, kidney disease, liver disease, gallbladder disease, pyoureter, sudden cardiac arrest, heart conduction disease, cardiovascular disease, heart disease, respiratory failure, myasthenia gravis (including adult-onset), neuromuscular junction disease, and butyrylcholinesterase deficiency.
- **Drug interactions**: no interactions were found in the data compiled for this report.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN score, with no clinical trials or publications (evidence level L5). The proposed mechanism for bronchitis is weak, and the route of administration is unresolved: the only UK product is a topical ointment, which is not suited to airway use.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- SmPC warnings and contraindications for the UK product, to complete safety screening
- Confirmation of the approved indication and licence details for the UK product
- A route-compatibility assessment (topical ointment versus the route required for bronchitis)
- Preclinical or clinical evidence, starting with a literature search, before any further evaluation
- If any indication is pursued, the more biologically plausible option is topical symptom relief in a dermatological condition such as acne keloid. Paediatric uses (neonatal dermatomyositis, childhood interstitial lung disease) would need a particularly high safety bar.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

