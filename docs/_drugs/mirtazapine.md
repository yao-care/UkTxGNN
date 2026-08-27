---
layout: default
title: Mirtazapine
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 3
---

# Mirtazapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using the Evidence Pack provided, here is the drug repurposing evaluation report.

---

# Mirtazapine: From Depression to Ohdo Syndrome and Variants

## One-Sentence Summary

Mirtazapine is a noradrenergic and specific serotonergic antidepressant (NaSSA), originally established for the treatment of major depressive disorder.
The TxGNN model predicts a possible association with **Ohdo syndrome and variants**, a rare congenital developmental disorder, but this signal is currently supported by **0 clinical trials** and **0 publications**, and the underlying mechanistic rationale is assessed as weak.

*(Note: The Evidence Pack does not contain a populated `original_indications` field or licence-derived indication text for Mirtazapine. The original indication above is stated from established pharmacological knowledge of this molecule for reader orientation, not extracted from the pack — see Data Gaps below.)*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (Major Depressive Disorder) — not present in Evidence Pack; see Data Gaps |
| Predicted New Indication | Ohdo syndrome and variants |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (flagged as Data Gap DG002, High severity). Based on known pharmacology, mirtazapine acts via central α2‑adrenergic antagonism together with 5‑HT2 and 5‑HT3 receptor antagonism and H1 antihistaminergic activity, and its efficacy in depression is well established.

Ohdo syndrome and its variants (including blepharophimosis–intellectual disability syndrome, Ohdo type) are rare congenital disorders caused by mutations in chromatin-modifying and transcriptional-regulation genes such as *KAT6A*, *KAT6B*, *MED12*, *SETD1B*, and *AFF4*. These are structural/developmental gene defects, not neurotransmitter receptor disorders, and there is no established causal or symptomatic-treatment pathway linking mirtazapine's pharmacology to this disease mechanism.

The repurposing rationale accompanying this prediction explicitly assesses the signal as a **likely false positive**: the high TxGNN score most plausibly reflects co-occurrence in the knowledge graph between "intellectual disability / behavioural phenotype" nodes and psychiatric drugs generally, rather than a genuine mechanistic relationship. This is a symptom-level statistical association, not a pharmacological one, and should be treated with corresponding caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No marketing authorisation records are present in the Evidence Pack for Mirtazapine (market status: **Not marketed**; 0 licences on file). This appears inconsistent with mirtazapine's known long-standing UK availability, and should be treated as a data gap requiring verification against the MHRA product database and BNF rather than as a confirmed absence from the UK market.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(All safety fields in the Evidence Pack — key warnings, contraindications, and drug interactions — are recorded as Data Gaps; no interaction search returned results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only, no supporting clinical trials or literature), and the repurposing rationale itself flags the mechanistic link as most likely a knowledge-graph artefact rather than a genuine pharmacological relationship. Combined with a Blocking-severity data gap on TFDA/MHRA label warnings and contraindications (DG001), this candidate does not currently meet the threshold to proceed.
- The two related "Ohdo syndrome" candidates (ranks 1–2, scores 99.42% and 99.11%) and the third candidate, benign paroxysmal torticollis of infancy (rank 3, score 99.11%), are all L5/Hold. The torticollis candidate has a marginally more plausible mechanistic rationale (serotonergic overlap with migraine-spectrum pathophysiology) but still lacks any trial or literature support, and carries additional safety concern given the paediatric/infant population and lack of paediatric safety data.

**To proceed, the following is needed:**
- Resolution of DG001 (Blocking): TFDA/MHRA SmPC warnings and contraindications, required before any S1 safety screening can begin.
- Resolution of DG002 (High): confirmed mechanism-of-action data from DrugBank to properly assess mechanistic plausibility.
- Verification of actual UK marketing/licensing status, given the discrepancy between the Evidence Pack (0 licences, not marketed) and mirtazapine's known clinical use in the UK.
- Independent pharmacological/genetics expert review of whether any plausible biological link exists between mirtazapine's receptor pharmacology and chromatin-modifier-driven developmental syndromes, before further investment in this candidate.
- If pursuing the benign paroxysmal torticollis of infancy candidate instead, dedicated paediatric safety data would be required given the lack of approved paediatric use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

