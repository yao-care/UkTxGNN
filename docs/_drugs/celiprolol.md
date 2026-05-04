---
layout: default
title: Celiprolol
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 0
---

# Celiprolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Celiprolol: Drug Repurposing Evaluation — No Predictions Generated

## One-Sentence Summary

Celiprolol is a third-generation cardioselective beta-1 adrenoceptor blocker with partial beta-2 agonist and vasodilatory properties, not currently marketed in the United Kingdom.
The TxGNN model returned **no predicted new indications** for this compound in the current dataset, likely due to incomplete anchoring data from UK regulatory sources.
This report documents the evaluation status and the critical data gaps that must be resolved before a full drug repurposing assessment can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not established in UK regulatory data (no MHRA licence held) |
| Predicted New Indication | None returned by TxGNN in current dataset |
| TxGNN Prediction Score | N/A |
| Evidence Level | Indeterminate — no TxGNN predictions generated |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Were No Predictions Generated?

TxGNN generates drug repurposing candidates by traversing a biomedical knowledge graph anchored to a drug's known approved indications, targets, and pathways. For Celiprolol, three compounding factors likely explain the absence of predictions:

**1. No UK regulatory anchor.** Celiprolol holds no MHRA marketing authorisation. The knowledge graph may therefore lack the UK-specific indication mappings needed to initiate traversal. Celiprolol is, however, licensed in France (Celectol®) and several other EU member states for mild-to-moderate hypertension and stable angina pectoris — data from these jurisdictions was not included in this Evidence Pack.

**2. Missing mechanism of action data.** The DrugBank MOA field was not retrieved in this pipeline run (Data Gap DG002). Mechanistic nodes — adrenoceptor binding affinities, downstream signalling pathways — are important edges in the TxGNN graph. Without them, the model cannot traverse to candidate disease nodes.

**3. Empty original indications array.** The `original_indications` field returned no entries. TxGNN requires at least one mapped indication as a starting node; with none present, no walk through the graph is possible.

From published literature and regulatory sources outside this Evidence Pack, Celiprolol is known to be a selective β₁-adrenergic antagonist with partial β₂-agonist activity and direct vasodilatory effects. This pharmacological profile distinguishes it from conventional beta-blockers and has motivated research into vascular connective tissue disorders — most notably vascular Ehlers-Danlos syndrome (vEDS), where a landmark 2010 *Lancet* randomised trial (PMID [20870120](https://pubmed.ncbi.nlm.nih.gov/20870120/)) demonstrated a significant reduction in arterial rupture and dissection. This repurposing signal would be a natural candidate for TxGNN to surface if the input data were complete.

---

## UK Market Information

Celiprolol holds **no current MHRA marketing authorisation**. No Product Licences (PL numbers) are on record for this compound in the UK. It was previously available in some markets under the brand name Celectol® but is not approved by the MHRA and is not listed in the British National Formulary (BNF).

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|--------------|-------------|---------------------|
| — | No UK licence held | — | — |

Prescribing in the UK would require either a Specials licence or access via a named-patient basis, subject to MHRA oversight.

---

## Safety Considerations

No safety data was retrievable from this Evidence Pack (DrugBank key warnings, contraindications, and drug–drug interaction records all returned null or were absent from the query). As a beta-adrenoceptor blocking agent, standard class warnings would be expected to apply (e.g., avoid abrupt withdrawal, caution in asthma/COPD, interactions with calcium channel blockers and antiarrhythmics), but these must be confirmed from primary sources before any clinical use.

> Please refer to the European SmPC (available from EMA/national authorities where licensed) and the BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model returned no predicted indications for Celiprolol, and the two blocking data gaps (MOA and approved indication data) prevent the pipeline from functioning as intended. The drug is not marketed in the UK, which further limits direct clinical translation without additional regulatory work.

**To proceed, the following is needed:**

1. **Resolve DG002 — Retrieve MOA from DrugBank API.** Query `DB04846` directly for mechanism of action, targets, and pharmacological action categories. This is the single highest-impact remediation step.
2. **Source EU/French regulatory data.** Import Celiprolol's French ANSM licence (hypertension, stable angina) as `original_indications` to anchor the TxGNN graph walk.
3. **Re-run TxGNN prediction pipeline** once items 1 and 2 are complete; predictions for vascular and cardiovascular indications are anticipated.
4. **Conduct targeted literature review** for vascular Ehlers-Danlos syndrome and Marfan syndrome signals (where published RCT and cohort data already exist) to cross-validate any TxGNN outputs.
5. **Assess MHRA pathway** — if a repurposing candidate is confirmed, determine whether a new Marketing Authorisation Application or a variation to an existing EU authorisation is the appropriate UK regulatory route.

---

> ⚠️ **Disclaimer:** This report is produced for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before therapeutic application. Healthcare professionals should consult current MHRA-approved prescribing information and BNF guidance.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

