---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 10
---

# Mupirocin
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

Using the drug-repurposing evidence pack you provided, here is the evaluation report. Note on judgement call: `predicted_indications[0]` (Pleural Empyema) carries the highest raw TxGNN score, but the evidence pack's own mechanistic rationale argues against its plausibility (Mupirocin is topical-only). I have followed the template literally for the headline indication (as instructed) while being transparent about why the evidence does not support it, and I flag the pack's best-supported alternative (Staphylococcal Scalded Skin Syndrome, rank 9) in the conclusion so the reader isn't misled by the score alone.

---

# Mupirocin: From Topical Staphylococcal Skin Infections to Pleural Empyema

## One-Sentence Summary

Mupirocin is a topical antibacterial agent used against Gram-positive skin and soft-tissue infections (e.g. impetigo) and for nasal *Staphylococcus aureus* decolonisation. The TxGNN model assigns its **highest** repurposing score to **Pleural Empyema** (99.49%), but this prediction is supported by **zero clinical trials** and **zero publications**, and mechanistic review indicates that a topical-only formulation cannot plausibly reach a deep pleural space infection.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Topical antibacterial for Gram-positive skin/soft-tissue infections (e.g. impetigo, nasal *S. aureus* decolonisation) — no formal marketing-authorisation indication text is available in this dataset |
| Predicted New Indication | Pleural Empyema |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for Mupirocin is not available in this dataset (data gap). However, evidence embedded elsewhere in this pack indicates that Mupirocin's established pharmacological target is bacterial **isoleucyl-tRNA synthetase (IleRS)**, which blocks bacterial protein synthesis and underlies its activity against Gram-positive organisms, principally *Staphylococcus aureus* and *Streptococcus pyogenes*.

Pleural empyema is typically a deep, often polymicrobial (including anaerobic and Gram-negative) pleural-space infection requiring systemic antibiotic therapy with adequate pleural penetration, sometimes combined with drainage. Mupirocin, by contrast, is formulated exclusively for topical (skin/nasal) use and has no established systemic pharmacokinetic profile. There is no plausible route by which a topical ointment could reach the pleural cavity in therapeutic concentrations.

Our assessment is that the very high TxGNN score most likely reflects a **generic knowledge-graph association** with *S. aureus* infection (empyema can be staphylococcal in origin) rather than a specific, deliverable treatment pathway. In the absence of any supporting trial or literature evidence, and given the fundamental route-of-administration mismatch, this prediction should currently be treated as a **model artefact rather than a credible repurposing candidate**.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

No marketing authorisations are currently recorded for Mupirocin in this dataset (`total_licenses: 0`, market status: Not Marketed). No product-level dosage form or approved-indication text can therefore be extracted for this evaluation.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: retrieval of the MHRA-approved warnings/contraindications for Mupirocin is flagged in the underlying evidence pack as a **blocking** data gap — see Conclusion below.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The Pleural Empyema prediction has evidence level L5 (model prediction only) — no clinical trials, no literature, and no marketing-authorisation basis in the UK.
- Mupirocin's topical-only formulation makes systemic/deep-tissue delivery to the pleural space mechanistically implausible; the high TxGNN score should not be interpreted as clinical validation.

**To proceed, the following is needed:**
- Retrieval of the MHRA-approved SmPC warnings/contraindications (currently a blocking data gap, per this evidence pack)
- Confirmed mechanism-of-action documentation from DrugBank/product literature
- Any pharmacokinetic data demonstrating systemic or pleural-fluid penetration, if a non-topical formulation exists
- If no systemic formulation exists, this candidate should likely be deprioritised in favour of better-supported signals in the same evidence pack

**Additional note for the reviewing pharmacist:** within this same evidence pack, a different candidate — **Staphylococcal Scalded Skin Syndrome** (rank 9, TxGNN score 95.57%) — is far better supported, with 14 identified publications (including a retrospective cohort directly evaluating topical mupirocin combined with IV antibiotics), an evidence level of L3, and a "Proceed with Guardrails" recommendation. This is mechanistically consistent with Mupirocin's known decolonisation role against toxin-producing *S. aureus* and may warrant a separate, dedicated evaluation report rather than being overshadowed by the Pleural Empyema top-score result.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

