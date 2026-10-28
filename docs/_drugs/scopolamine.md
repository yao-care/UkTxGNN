---
layout: default
title: Scopolamine
parent: Model Prediction Only (L5)
nav_order: 563
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
monitor_inn: "Scopolamine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "atopic conjunctivitis", "rosacea conjunctivitis", "vernal conjunctivitis"]
description: "Scopolamine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Scopolamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Scopolamine: Cauda equina syndrome
{: .text-alpha }

## One-Sentence Summary

Scopolamine (hyoscine) is a non-selective muscarinic antagonist, originally used for motion sickness, peptic ulcer disease, irritable bowel syndrome and ophthalmic conditions such as cycloplegia and uveitis.
The TxGNN model predicts it may be effective for **cauda equina syndrome** (the top-ranked of six predictions), but there are currently **no clinical trials and no publications** supporting this direction; the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

Other predictions in the same list, all at evidence level L5 with a Hold recommendation:

| Rank | Predicted Indication | TxGNN Score |
|------|------|------|
| 2 | Neurogenic bladder (term flagged obsolete in the ontology) | 0.9998 |
| 3 | Papillary conjunctivitis | 0.9998 |
| 4 | Atopic conjunctivitis | 0.9980 |
| 5 | Rosacea conjunctivitis | 0.9940 |
| 6 | Vernal conjunctivitis | 0.9908 |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known pharmacology, scopolamine is a non-selective muscarinic antagonist. Its efficacy in motion sickness and in smooth-muscle and secretory conditions is established, and mechanistically it may modulate autonomic function of the bladder and bowel.

For cauda equina syndrome, the link is theoretical only. The condition is a structural, compressive neurological emergency treated surgically. An antimuscarinic could at most address secondary symptoms such as detrusor overactivity, not the underlying disease. The high TxGNN score is therefore a network-based model prediction with no supporting trial or literature data.

Among the other predictions, **neurogenic bladder** has the most biologically plausible rationale: muscarinic antagonism reduces detrusor overactivity, the established mechanism of agents such as oxybutynin and tolterodine. However, scopolamine penetrates the central nervous system (sedation, confusion, cognitive effects), making it less suitable than peripherally selective agents. The conjunctivitis predictions (papillary, atopic, rosacea, vernal) have weak rationales. These conditions are driven by mechanical irritation, allergic/Th2 inflammation or meibomian gland dysfunction, not cholinergic signalling, and antimuscarinics may worsen dry eye. A cycloplegic effect might at most relieve ciliary spasm or photophobia symptomatically in vernal disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0406000A0AAADAD (as recorded in the compiled data; not a standard PL number) | Hyoscine skin patch 1 mg/72 hrs | Transdermal patch | Not recorded in the compiled data |

Only one authorisation, a single-ingredient product, is recorded. Dosage form and indication text are not captured in the compiled record; please verify against the current MHRA record, SmPC and BNF.

## Safety Considerations

**Contraindications / cautions flagged in the knowledge graph** (drug–disease edges, not label text; verify against the SmPC):
- Cardiovascular and respiratory: hypertension, chronic obstructive pulmonary disease
- Neurological and psychiatric: epilepsy, anxiety and neurotic disorders, dysthymic disorder, psychotic and schizophreniform disorders, schizoaffective disorder, mental disorder
- Hepatic and renal: liver failure, liver disease, hepatic coma, kidney disease, pyoureter
- Gastrointestinal and pancreatic: gastric ulcer, pancreatitis, gallbladder disease
- Metabolic: diabetes mellitus, diabetic ketoacidosis, porphyria (including inherited porphyria)
- Haematological: thrombocytopenia, neutropenia, agranulocytosis
- Ophthalmic and urological: open-angle glaucoma, benign prostatic hyperplasia

**Drug Interactions:** 100 interactions were identified; most of those shown are Moderate, a few Minor. Main examples:
- Other anticholinergic or antimuscarinic agents (additive effects): aclidinium, hyoscyamine, amitriptyline, amantadine, acetylcholine
- Sedating antihistamines: chlorpheniramine, acrivastine, phenyltoloxamine
- CNS depressants (additive sedation): opioids (fentanyl, alfentanil, codeine, dihydrocodeine, tramadol), ethanol
- Others: botulinum toxin type A, phenylephrine, acebutolol, loperamide
- Minor: acetaminophen, hydrochlorothiazide

Label warnings and contraindications were not available in the compiled data. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six predictions are supported only by the TxGNN model, with no clinical trials or publications. Mechanistic plausibility is weak for cauda equina syndrome and the conjunctivitis conditions, and modest for neurogenic bladder, where better-suited peripheral antimuscarinics already exist.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- Label warnings and contraindications from the SmPC and BNF, which are required before any safety screening
- A systematic literature and trial registry search, prioritising neurogenic bladder, to see whether any evidence exists
- Complete MHRA authorisation details (dosage form, indication, PL number) and clarification of whether any non-patch formulation would suit the target route
- For neurogenic bladder, a comparison against peripherally selective antimuscarinics, with attention to central nervous system adverse effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

