---
layout: default
title: Azelaic Acid
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 0
---

# Azelaic Acid
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

# Azelaic Acid: Drug Repurposing Evaluation — No Predictions Generated

## One-Sentence Summary

Azelaic acid is a naturally occurring dicarboxylic acid widely used topically for acne vulgaris, rosacea, and hyperpigmentation disorders.
The TxGNN model did not generate any repurposing predictions for this compound in the current pipeline run, most likely due to incomplete input data preventing knowledge graph traversal.
No evidence review of a predicted new indication can therefore be performed at this stage; a **Hold** decision is recommended pending data remediation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne vulgaris; rosacea; melasma (topical) |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no predictions available |
| UK Market Status | Not confirmed (data extract shows 0 MHRA licences; independent verification strongly recommended) |
| Number of Marketing Authorisations | 0 (per data extract — likely incomplete; see UK Market Information below) |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The TxGNN knowledge graph pipeline requires at least one mapped disease indication as a starting node before it can propagate scores to candidate repurposing diseases. In this evidence pack, the `original_indications` field is empty, indicating that the drug's current therapeutic categories were not successfully extracted or mapped prior to the prediction run. Two data gaps were formally flagged:

- **DG001 (Blocking):** UK SmPC warnings and contraindications are absent, preventing a safety pre-screen and halting progress to the S1 safety evaluation stage.
- **DG002 (High):** Mechanism of action data is unavailable, limiting mechanistic plausibility analysis and reducing the quality of knowledge graph edge weighting.

The absence of predictions therefore reflects a **pipeline data completeness issue**, not a judgement on azelaic acid's repurposing potential.

**What is known about azelaic acid from the literature:** It is a C9 saturated dicarboxylic acid (nonanedioic acid) found naturally in wheat, rye, and barley. Its pharmacological activity spans inhibition of thioredoxin reductase, tyrosinase, and mitochondrial oxidoreductases, producing antimicrobial, anti-inflammatory, antiproliferative, and keratolytic effects. These mechanistically diverse properties have historically prompted investigation beyond dermatology — including in inflammatory, pigmentation, and neoplastic contexts — suggesting that meaningful repurposing candidates are likely to emerge once the pipeline is re-run with complete drug-level data.

---

## UK Market Information

The current data extract records **zero MHRA marketing authorisations** for azelaic acid. This is almost certainly a data extraction gap rather than a true reflection of the UK market. Two topical azelaic acid products have been historically authorised and dispensed in the United Kingdom:

| Product | Manufacturer | Formulation | Indication (known) |
|---------|-------------|-------------|---------------------|
| Skinoren | LEO Pharma | 20% cream | Acne vulgaris |
| Finacea | Almirall | 15% gel | Rosacea (papulopustular) |

Independent verification against the [MHRA Product Licence Register](https://products.mhra.gov.uk/), the **BNF** (section 13.6.1 — Drugs used in acne), and published NICE guidance is strongly recommended before drawing any conclusions from the market status field in this evidence pack.

---

## Safety Considerations

All safety fields in this evidence pack are absent. Please refer to the **SmPC** (available via the MHRA or the electronic Medicines Compendium) and the **BNF** for full safety information. Report suspected adverse reactions via the **Yellow Card Scheme** at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model returned no repurposing predictions for azelaic acid in this pipeline run, and two data gaps — one blocking and one high-severity — prevent a meaningful repurposing evaluation. The report cannot proceed to evidence synthesis without a predicted indication to evaluate.

**To proceed, the following is needed:**

- **Resolve UK regulatory data (DG001):** Re-extract MHRA marketing authorisation records, parse the SmPC PDF for approved indications, warnings, and contraindications, and correct the market status field
- **Resolve MOA data gap (DG002):** Query the DrugBank API for DB00548 to populate the mechanism of action and pharmacological categories
- **Populate original indications:** Map extracted SmPC indications (acne, rosacea) to TxGNN disease vocabulary nodes to enable knowledge graph traversal
- **Re-run TxGNN prediction pipeline:** With complete drug-level data, re-execute both the KG-based and deep learning prediction workflows
- **Conduct full evidence review:** Once predictions are available, search ClinicalTrials.gov, PubMed, and ICTRP (including EU CTR) for the top-ranked predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

