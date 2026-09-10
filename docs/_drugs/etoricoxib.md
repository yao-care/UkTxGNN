---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
---

# Etoricoxib
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

# Etoricoxib: From NSAID Pain Relief to Migraine Disorder

## One-Sentence Summary

> Etoricoxib is a selective COX-2 inhibitor (NSAID class); the evidence pack does not contain a confirmed original UK-approved indication text.
> The TxGNN model predicts it may be effective for **Migraine Disorder**,
> but this is currently supported by **0 clinical trials** and **0 publications** — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (data gap — DG002); Etoricoxib is pharmacologically a selective COX-2 inhibitor NSAID |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only, no clinical/literature support) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (data gap DG002). Based on general pharmacological knowledge, etoricoxib is a selective cyclo-oxygenase-2 (COX-2) inhibitor within the NSAID class, and its anti-inflammatory/analgesic efficacy in musculoskeletal and acute pain conditions is well established in the literature outside this dataset.

The proposed mechanistic link for migraine is that COX-2 and downstream prostaglandin signalling are theorised to play a role in the neuroinflammatory and vasodilatory components of migraine pathophysiology. However, the evidence pack itself states plainly that this rationale is theoretical: no etoricoxib-specific trial or publication was retrieved for "migraine disorder," "migraine with brainstem aura," or the related susceptibility phenotype. The 20 publications returned for the "susceptibility" variant are genetic/epileptogenesis background studies (e.g., SCN1A, MTHFR C677T polymorphisms) and do not test etoricoxib or any COX-2 inhibitor therapeutically.

By contrast, the pack does contain genuine (if limited) supportive signal for a **related but distinct** indication — "headache disorder" (rank 9) — where case reports and a case series describe etoricoxib benefiting indomethacin-responsive headache syndromes (idiopathic stabbing headache, secondary cough headache) via COX-2 inhibition sparing COX-1-mediated GI toxicity relative to indomethacin. This is a more mechanistically grounded and evidence-backed hypothesis than the top-ranked "migraine disorder" prediction, and is flagged separately below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Migraine Disorder.

---

## Literature Evidence

Currently no related literature available for Migraine Disorder.

---

## UK Market Information

Etoricoxib currently holds no UK marketing authorisation in this evidence pack (0 licenses; market status: not marketed). Where marketed internationally, etoricoxib is classified under NSAIDs, COX-2 selective inhibitors (BNF-equivalent chapter 10.1.1); this classification is provided for context only and is not confirmed against a UK-specific licence in this dataset.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: Key warnings, contraindications and DDI data were all flagged as data gaps in this evidence pack (DG001, Blocking severity — TFDA/MHRA label warnings and contraindications not yet retrieved). This must be resolved before any safety-dependent decision (S1 stage) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Migraine Disorder, TxGNN score 99.90%) has no supporting clinical trials or literature — it is evidence level L5, decision stage S0. A blocking data gap also exists for label-level safety information (DG001), which by itself prevents progression to safety screening (S1).

**To proceed, the following is needed:**
- TFDA/MHRA label warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action data from DrugBank (DG002, High)
- Dedicated clinical or observational data testing etoricoxib specifically in migraine (none currently exist)
- Confirmation of UK marketing/licensing status, since etoricoxib is not currently marketed in this dataset

---

## Other Predicted Indications Considered (For Context)

Of the ten candidates in this evidence pack, only two carry any real supporting evidence — both stronger than the top-ranked migraine prediction:

| Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Basis |
|---|---|---|---|---|---|
| Headache disorder | 99.31% | L4 | S1 | Research Question | 3 case reports + 1 case series describing etoricoxib benefit in indomethacin-responsive headache syndromes (idiopathic stabbing headache, secondary cough headache); PMIDs [35277974](https://pubmed.ncbi.nlm.nih.gov/35277974/), [36893522](https://pubmed.ncbi.nlm.nih.gov/36893522/), [17883876](https://pubmed.ncbi.nlm.nih.gov/17883876/), [18171381](https://pubmed.ncbi.nlm.nih.gov/18171381/) |
| Trigeminal autonomic cephalalgia | 99.15% | L5 | S0 | Hold | No direct evidence; mechanistically adjacent to the headache-disorder signal above (shared indomethacin-responsive subtype rationale) |

Pulmonary hypertension (rank 6) and kyphoscoliotic heart disease (rank 8) also returned trial/literature hits, but all describe COX-2 inhibition as a **risk factor** (sodium/water retention, hyperkalaemia) rather than a therapeutic mechanism, and should not be interpreted as supportive evidence.

If this candidate is pursued further, **headache disorder** — not migraine disorder — is the better-evidenced starting point for a research question at S1.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

