---
layout: default
title: Amifampridine
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Amifampridine
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

# Amifampridine: From Lambert-Eaton Myasthenic Syndrome to Glaucoma

---

## One-Sentence Summary

Amifampridine (3,4-diaminopyridine) is a voltage-gated potassium channel (VGKC) blocker with established use in Lambert-Eaton Myasthenic Syndrome (LEMS), a rare paraneoplastic neuromuscular disorder in which presynaptic acetylcholine release is impaired by autoantibodies.
The TxGNN model predicts it may have utility in **Glaucoma**, with a prediction confidence of **99.71%**; however, this is currently supported by **no clinical trials** and **no published literature** specific to this indication.
The evidence base rests entirely on model prediction alone, and the proposed mechanistic link is considered highly indirect — independent preclinical validation is required before this direction can be taken further.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Lambert-Eaton Myasthenic Syndrome (LEMS) — not recorded in UK MHRA dataset; based on established pharmacological use |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| UK Market Status | Not currently marketed |
| Number of UK Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this dataset. Based on established pharmacological knowledge, Amifampridine acts by blocking presynaptic voltage-gated potassium channels (VGKCs). This prolongs the presynaptic action potential duration, increases calcium influx at the neuromuscular junction, and ultimately enhances acetylcholine (ACh) release into the synaptic cleft. This mechanism underlies its proven efficacy in LEMS, where autoantibodies directed against P/Q-type voltage-gated calcium channels (VGCCs) reduce ACh vesicle exocytosis, resulting in proximal muscle weakness, depressed tendon reflexes, and autonomic dysfunction.

For glaucoma, VGKCs are known to be expressed in the trabecular meshwork and ciliary body epithelium — tissues that govern intraocular pressure (IOP) through aqueous humour secretion and outflow. In principle, modulation of potassium channel activity at these sites could theoretically influence IOP dynamics. However, the mechanistic link is highly indirect: Amifampridine's established pharmacological action operates specifically at presynaptic motor nerve terminals in the peripheral neuromuscular junction, not at the intraocular smooth muscle or epithelial secretory cells relevant to glaucoma pathophysiology.

Critically, there is no preclinical evidence — no animal model or in vitro study — to support Amifampridine's relevance to glaucoma. The high TxGNN score most likely reflects knowledge graph topological adjacency, where ion channel biology and neurological disease nodes are proximate within the graph, rather than true biological plausibility. This prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Amifampridine currently holds no MHRA marketing authorisations in the United Kingdom, and no licensed products are recorded in this dataset.

> **Note for prescribers:** In the European Union, amifampridine phosphate (Firdapse®) holds a centralised EMA marketing authorisation for the symptomatic treatment of LEMS in adults. UK clinicians should verify the current MHRA status independently via the MHRA product database. Access for the LEMS indication may be possible through unlicensed routes (e.g., specials manufacturer licence or named-patient supply) where appropriate. There is no UK-approved indication for any ophthalmic or glaucoma use.

---

## Safety Considerations

All safety data — including key warnings, contraindications, and drug interaction information — was not available from the sources queried at the time of this report.

> Please refer to available international prescribing information (e.g., the EMA-approved Firdapse SmPC) and the BNF for safety guidance. Suspected adverse reactions should be reported via the **MHRA Yellow Card Scheme** at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk). Given the absence of a UK marketing authorisation, prescribers should seek specialist advice before initiating treatment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial, published literature, or preclinical evidence linking Amifampridine to glaucoma. The high TxGNN prediction score appears to reflect knowledge graph topology rather than validated biological plausibility, and the proposed mechanistic pathway (VGKC blockade → aqueous humour dynamics → IOP reduction) is highly speculative and unsubstantiated.

**To proceed, the following would be needed:**

- **Mechanistic gap analysis:** Obtain full MOA data from DrugBank (DB11640) to enable rigorous assessment of whether VGKC blockade has any plausible downstream effect on intraocular structures
- **Preclinical feasibility study:** In vitro investigation of VGKC subtype expression and pharmacological sensitivity in trabecular meshwork and ciliary body epithelial cells
- **Animal model data:** IOP measurement in a glaucoma rodent model following systemic or topical Amifampridine administration
- **Ocular formulation assessment:** Evaluate whether topical ocular delivery is pharmacokinetically feasible, given that systemic VGKC blockade could carry significant cardiovascular and neurological risks
- **Safety data retrieval:** Obtain full contraindication, warning, and DDI profile from the EMA SmPC or MHRA records before any human study design is considered
- **Regulatory context:** Clarify current UK MHRA licensing status and whether Firdapse holds or is eligible for a UK Orphan Medicinal Product designation

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application. Data cut-off: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

