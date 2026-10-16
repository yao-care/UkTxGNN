---
layout: default
title: Alitretinoin
parent: Model Prediction Only (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Alitretinoin: predicted new indication Acne (evidence level L5). Approved use: Not stated in the UK authorisation data compiled for this report. Ref…"
monitor_inn: "Alitretinoin"
predicted_indications: ["amenorrhea (disease)", "acne (disease)", "atypical coarctation of aorta", "pregnancy associated osteoporosis", "aortic malformation", "postmenopausal osteoporosis", "autosomal dominant neovascular inflammatory vitreoretinopathy", "breast fibrocystic disease", "benign mammary dysplasia", "Worth syndrome"]
---

# Alitretinoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Alitretinoin: From Severe Chronic Hand Eczema to Acne

## One-Sentence Summary

Alitretinoin (9-cis-retinoic acid) is a retinoid that acts on retinoid receptors and is used for severe chronic hand eczema that has not responded to potent topical corticosteroids.
The TxGNN model predicts it may be effective for **acne**, but there are currently **no clinical trials** and only **2 general review articles** supporting this direction, so the evidence is limited to model prediction and biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the UK authorisation data compiled for this report. Reference pharmacology data describes use in severe chronic hand eczema refractory to potent topical corticosteroids |
| Predicted New Indication | Acne (see note below on prediction ranking) |
| TxGNN Prediction Score | 99.92% (acne); the top-ranked prediction, amenorrhoea, scored 99.99% |
| Evidence Level | L4 (acne); L5 for the top-ranked prediction |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

**Note on prediction selection:** The top-ranked TxGNN prediction is amenorrhoea (99.99%), but it has no supporting trials or literature, and any link is more plausibly an adverse effect of retinoids than a therapeutic one. This report therefore focuses on rank 2, acne, the only prediction with any supporting literature and a plausible mechanism. Other predictions are summarised below.

---

## Why is This Prediction Reasonable?

Alitretinoin is a pan-retinoid receptor agonist. It binds all three retinoic acid receptors (RAR-α, -β, -γ) and all three retinoid X receptors (RXR-α, -β, -γ). Detailed mechanism of action data are not otherwise available in the data compiled for this report.

Retinoids are an established treatment class in acne. Isotretinoin, a close isomer, works through RAR-mediated normalisation of keratinocyte differentiation, reduced sebocyte activity and anti-inflammatory effects. Alitretinoin shares this receptor pharmacology (with additional RXR activity), which gives biological plausibility. However, the literature supplied consists of general retinoid dermatology reviews, not alitretinoin-specific acne data. Both its original indication and acne are dermatological conditions, but the link remains theoretical without direct clinical evidence.

**Other TxGNN predictions (all lacking clinical evidence):**

| Predicted Indication | Score | Assessment |
|------|------|------|
| Amenorrhoea | 99.99% | No clear mechanistic link; more likely an adverse-effect relationship |
| Atypical coarctation of aorta | 99.88% | Developmental/teratogenic relationship only; not treatable with a retinoid |
| Pregnancy-associated osteoporosis | 99.83% | Retinoids are contraindicated in pregnancy; no supported mechanism |
| Aortic malformation | 99.79% | Teratogenic rather than therapeutic relationship |
| Postmenopausal osteoporosis | 99.79% | Retinoid excess is associated with reduced bone density; direction of effect potentially unfavourable |
| Autosomal dominant neovascular inflammatory vitreoretinopathy | 99.74% | No mechanism linking alitretinoin to this rare genetic eye disease |
| Breast fibrocystic disease / benign mammary dysplasia | 99.73% | Weak plausibility only; effectively the same entity (redundant predictions) |
| Worth syndrome | 99.70% | No known mechanistic connection |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Review | Clinics in Dermatology | Overview of vitamin A and retinoids in dermatology; lists alitretinoin among oral therapeutic retinoids alongside isotretinoin, acitretin and bexarotene |
| [11586072](https://pubmed.ncbi.nlm.nih.gov/11586072/) | 2001 | Review | Skin Pharmacology and Applied Skin Physiology | Discusses retinoid nuclear receptor biology and which dermatological indications may benefit from retinoids in future |

Neither review provides alitretinoin-specific acne data.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1305010AFAAABAB | Alitretinoin capsule 30 mg | Capsule | Not stated in the data compiled |

One valid single-ingredient authorisation is recorded. Dosage form and approved indication text were not available, so they should be confirmed against the current SmPC and BNF.

---

## Safety Considerations

- **Knowledge-graph contraindication signals:** The TxGNN knowledge graph (not label text) links alitretinoin to contraindication with mycosis fungoides and variants, primary cutaneous T-cell lymphoma, folliculotropic mycosis fungoides, localised pagetoid reticulosis and granulomatous slack skin disease.
- **Teratogenicity:** Retinoids as a class are teratogenic and unsuitable in pregnancy; this is relevant to any new indication in people of childbearing potential.
- **Pharmacological targets:** Alitretinoin interacts with RAR-α/β/γ and RXR-α/β/γ, and the data also list vitamin K epoxide reductase complex subunit 1 (VKORC1). The VKORC1 entry may warrant attention with coumarin anticoagulants, but no interaction severity levels were provided.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne prediction rests on class-level biological plausibility, with no trials and only general review literature. Established retinoids (such as isotretinoin) already exist for acne, so the added value of alitretinoin is unclear. The highest-scoring prediction (amenorrhoea) has no supporting evidence and is more likely an adverse effect.

**To proceed, the following is needed:**
- Alitretinoin-specific preclinical or clinical data in acne
- Confirmed UK approved indication and dosage form from the SmPC
- Full warnings and contraindications from the SmPC and BNF (currently missing)
- Detailed mechanism of action data
- A pregnancy prevention and risk-management plan, given retinoid teratogenicity
- Comparison against existing acne retinoids to justify repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

