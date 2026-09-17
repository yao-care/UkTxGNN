---
layout: default
title: Nefazodone
parent: Model Prediction Only (L5)
nav_order: 406
evidence_level: L5
indication_count: 2
---

# Nefazodone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Nefazodone: From Antidepressant Therapy to Migraine Disorder

## One-Sentence Summary

> Nefazodone is pharmacologically classified as an antidepressant (5-HT2A receptor antagonist with weak serotonin/noradrenaline reuptake inhibition); no confirmed original indication text is available in the current dataset.
> The TxGNN model predicts it may be effective for **Migraine Disorder**,
> with **0 clinical trials** and **3 review-level publications** currently supporting this direction — evidence is mechanistic and narrative only, not clinical-trial based.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no UK marketing authorisation or licence record on file |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 (mechanism/narrative review only, no RCTs) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory/DrugBank source (flagged as a High-severity data gap, DG002). Based on the repurposing rationale accompanying this prediction, Nefazodone is understood to act as a 5-HT2A receptor antagonist with weak serotonin/noradrenaline reuptake inhibition — a pharmacological profile that partially overlaps with other antidepressant classes (TCAs, SSRIs/SNRIs) already used off-label or on-label for migraine prophylaxis. This overlap provides a plausible theoretical basis for the TxGNN model's prediction.

However, this mechanistic plausibility is undermined by two factors: first, the drug's original indication cannot be confirmed from the available dataset, so the relationship between "original use" and "new indication" cannot be properly assessed; second, Nefazodone is not currently marketed in the UK (market status: not marketed, 0 marketing authorisations), which is consistent with the well-documented hepatotoxicity concerns that led to withdrawal of nefazodone-containing products in numerous markets. Safety concerns therefore outweigh the mechanistic rationale at this stage.

For the secondary prediction (migraine with brainstem aura), the evidence is weaker still — supported only by the TxGNN score (99.60%) with no literature or trial evidence at all. Migraine with brainstem aura is a subtype in which vasoconstrictive agents (e.g. triptans) are relatively contraindicated; if Nefazodone carries meaningful serotonergic activity, its safety profile in this specific subgroup would need particularly careful scrutiny, which cannot be performed given the current absence of evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15115635](https://pubmed.ncbi.nlm.nih.gov/15115635/) | 2004 | Review | Current Pain and Headache Reports | Reviews emerging migraine prophylaxis options; lists nefazodone alongside topiramate, levetiracetam, zonisamide, botulinum toxin and others as an emerging preventive agent |
| [15926007](https://pubmed.ncbi.nlm.nih.gov/15926007/) | 2005 | Review | Neurological Sciences | Broad review of current and emerging migraine preventive therapies, briefly discussing nefazodone in this context |
| [15549532](https://pubmed.ncbi.nlm.nih.gov/15549532/) | 2004 | Review | Neurological Sciences | Review of new migraine preventive drugs; notes that evidence for some agents (including nefazodone) is limited to open, uncontrolled trials rather than double-blind controlled studies |

All three sources are narrative reviews (Tier 3); none report primary controlled-trial data specific to nefazodone in migraine.

---

## UK Market Information

No UK marketing authorisations are on file for Nefazodone. Current market status is **not marketed**, with 0 recorded licences. As no UK product exists, no BNF classification entry or SmPC is currently available for this substance in the UK market.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Note:** A Blocking-severity data gap (DG001) has been identified — MHRA/regulatory warning and contraindication data for Nefazodone are not currently available in this dataset, which **prevents completion of the initial safety assessment (S1 stage)**. Given the drug's non-marketed status in the UK, this gap should be treated as a hard stop for any repurposing evaluation until resolved, particularly given nefazodone's known association with hepatotoxicity signals that have affected its regulatory status in other jurisdictions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to narrative reviews (no clinical trials, no RCTs) and a Blocking-severity safety data gap prevents even an initial safety assessment. The drug is not currently marketed in the UK, and mechanism-of-action data required to assess biological plausibility is also missing (High-severity gap).

**To proceed, the following is needed:**
- MHRA/SmPC warnings, contraindications, and drug interaction data (resolves DG001, Blocking)
- Confirmed mechanism of action from DrugBank or equivalent source (resolves DG002, High)
- Confirmation of the drug's original approved indication(s), to properly assess repurposing rationale
- At minimum, prospective or retrospective clinical evidence (not review-only) specific to nefazodone in migraine before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

