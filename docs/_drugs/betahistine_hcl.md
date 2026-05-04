---
layout: default
title: Betahistine Hcl
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 0
---

# Betahistine Hcl
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

# Betahistine HCl: Evidence Pack Incomplete — Repurposing Assessment Pending

---

## One-Sentence Summary

Betahistine hydrochloride is a histamine analogue antivertigo agent, used in many countries for vertigo and Ménière's disease.
This Evidence Pack, however, contains **no TxGNN repurposing predictions** and carries a **blocking data gap** on safety information,
meaning a full drug repurposing evaluation cannot be completed at this stage and the assessment must be placed on **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vertigo / Ménière's Disease *(derived from general clinical knowledge; not recorded in Evidence Pack)* |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — Model prediction only; no candidates returned |
| UK Market Status | Not Marketed *(per Evidence Pack; 0 MHRA licences recorded)* |
| Number of Marketing Authorisations | 0 *(per Evidence Pack)* |
| Recommended Decision | **Hold** |

---

## Why No Prediction Could Be Generated

The TxGNN pipeline returned an empty `predicted_indications` array. Based on the Evidence Pack, three likely root causes exist:

**1. Missing DrugBank ID**
The DrugBank identifier for this entry is `null`. The TxGNN knowledge graph uses DrugBank IDs as primary drug nodes. Without a valid mapping, the model cannot locate the drug within the graph and therefore cannot generate repurposing candidates. The likely correct DrugBank accession for betahistine is **DB00772**, but this has not been confirmed by the pipeline.

**2. Missing Mechanism of Action (Data Gap DG002 — High Severity)**
No MOA data is present in the Evidence Pack. From established clinical pharmacology, betahistine acts as a **partial H1 receptor agonist** and a **potent H3 receptor antagonist**, with downstream effects on histaminergic neurotransmission and cochlear microvascular blood flow. This mechanistic profile has not been formally sourced through the pipeline, which may limit graph traversal in the knowledge graph step.

**3. Input Ingredient Mismatch**
The query was submitted as `"BETAHISTINE HCL"` (salt form). Many drug databases index by INN (`betahistine`). Normalising the query to the free base INN may improve matching rates.

---

## UK Market Information

No MHRA marketing authorisation data is recorded in this Evidence Pack (0 licences, status: Not Marketed).

> **Important note for UK clinicians:** This almost certainly reflects a **data retrieval error** rather than the true regulatory position. Betahistine-containing medicinal products (e.g., *Serc®* 8 mg and 16 mg tablets) are well established in European prescribing practice and are listed in the **BNF under Section 4.6 — Drugs used in nausea and labyrinthine disorders**. UK prescribers should consult the [MHRA Product Licences database](https://products.mhra.gov.uk/) directly to verify current authorisation status. Prescribing information and the Summary of Product Characteristics (SmPC) are available via the [electronic Medicines Compendium (eMC)](https://www.medicines.org.uk/emc/).

---

## Safety Considerations

> Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** at [https://yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

No warnings, contraindications, or drug interaction data are present in this Evidence Pack. The safety data gap (DG001) is rated **Blocking severity**, which formally prevents progression through the standard safety pre-screening stage until resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned no repurposing candidates for Betahistine HCl, most likely due to an unresolved DrugBank ID and an incomplete regulatory data pull. No safety evaluation is possible while the blocking data gap (DG001) remains open. There is insufficient information in this Evidence Pack to support any repurposing recommendation.

**To proceed, the following steps are required:**

1. **Confirm the DrugBank ID** — Map `BETAHISTINE HCL` to `DB00772` (betahistine) via the DrugBank API or normaliser, and update the Evidence Pack metadata
2. **Re-run the TxGNN prediction pipeline** — Once the DrugBank ID is confirmed and the INN is normalised to `betahistine`, re-submit to the KG and DL prediction modules
3. **Retrieve MHRA licensing data** — Query the MHRA Product Licences database to recover UK marketing authorisation records and correct the market status entry
4. **Resolve DG001 (Blocking) — Safety data** — Download and parse the betahistine SmPC from the eMC to extract warnings, contraindications, and special precautions
5. **Resolve DG002 (High) — MOA data** — Query the DrugBank API using the confirmed accession number to retrieve pharmacodynamic and mechanistic information
6. **Re-issue a full Evidence Pack** — Once the above five items are complete, generate a v5 Evidence Pack and re-run the standard evaluation workflow

---

*This report was generated on 2026-04-05 based on Evidence Pack v4 (candidate ID: TW-UNKNOWN-multi). The findings are for research reference only and do not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

