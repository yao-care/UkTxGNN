---
layout: default
title: Fexofenadine
parent: Model Prediction Only (L5)
nav_order: 286
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Fexofenadine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis…"
monitor_inn: "Fexofenadine"
predicted_indications: ["rosacea conjunctivitis"]
---

# Fexofenadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Fexofenadine: From Allergic Rhinitis to Rosacea Conjunctivitis

## One-Sentence Summary

Fexofenadine is a selective peripheral H1-receptor antagonist (antihistamine), originally used for allergic rhinitis, allergic conjunctivitis and idiopathic urticaria.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**, but there are currently **no clinical trials** and **no publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis, idiopathic urticaria (the licence record held no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fexofenadine is an oral, non-sedating, peripheral H1-receptor antagonist. Its efficacy in allergic and atopic conjunctivitis and in allergic skin and nasal conditions is established.

The possible link is histamine-mediated inflammation, which may contribute to ocular surface symptoms in rosacea-associated conjunctivitis. Fexofenadine already treats several conjunctivitis types with an allergic basis, which is probably why the model scores this indication so highly.

There are important reasons for caution. The main pathology of ocular rosacea is thought to involve meibomian gland dysfunction, tear film instability, innate immune and inflammatory pathways (for example matrix metalloproteinases and cytokines), and possibly *Demodex* colonisation. None of these is clearly histamine-driven. Because fexofenadine is oral and systemic, delivery to the ocular surface and benefit in a non-allergic, lipid- and tear-film-driven condition are uncertain. A high TxGNN score is a computational prediction, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0304010E0AAAAAA (BNF-style product code, not a PL number) | Fexofenadine HCl tablets 120 mg | Tablet | Not stated in the data compiled for this report |

The record shows one valid single-ingredient product and no cancelled products. Fexofenadine falls under antihistamines in the BNF (chapter 3, respiratory system; the code prefix 0304 matches this). Please check the MHRA register and the SmPC for the licensed indications and the PL number.

## Safety Considerations

**Contraindications flagged in the knowledge graph (not taken from label text):** the TxGNN knowledge graph links fexofenadine to the following conditions as contraindications. These should be treated as signals to verify against the SmPC, not confirmed label contraindications.
- Cardiovascular: hypertension/hypertensive disorder, coronary artery disease, coronary atherosclerosis, arteriosclerosis, atherosclerosis
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis
- Renal and urological: kidney disease, pyoureter, benign prostatic hyperplasia
- Ocular: angle-closure (closed-angle) glaucoma

**Drug Interactions:** the interaction query returned 100 records. The main ones in the data reviewed are:
- **Moderate:** antacids containing aluminium or magnesium (aluminium hydroxide, magnesium hydroxide, magaldrate, magnesium carbonate), eliglustat, eluxadoline and rolapitant
- **Minor:** clarithromycin, miconazole and clotrimazole
- **Severity not classified:** calcitriol, doxycycline, cimetidine, famotidine, levocarnitine, epinephrine, dolasetron, dicyclomine, chlorhexidine and acetylsalicylic acid

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for this indication is a high model score. There are no clinical trials or publications, the proposed histamine link is weak for the likely disease mechanisms of ocular rosacea, and the route of delivery is uncertain.

**To proceed, the following is needed:**
- Curated mechanism of action and target data to test the histamine-pathway hypothesis
- A literature and trial search specifically on antihistamines in ocular rosacea
- Label warnings and contraindications from the current SmPC and BNF, which are missing from the data compiled for this report
- The approved indication text and PL number for the UK authorisation
- Evaluation of route and formulation (oral versus topical ocular) and of similarity to the original allergic indications
- Early-phase or pilot data in ocular rosacea patients, ideally comparing against standard care (lid hygiene, topical or oral antibiotics)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

