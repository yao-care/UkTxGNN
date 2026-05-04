---
layout: default
title: Benzydamine
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 1
---

# Benzydamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Benzydamine: From Oral and Throat Inflammation to Benign Prostatic Hyperplasia

## One-Sentence Summary

Benzydamine is a locally-acting non-steroidal anti-inflammatory agent, widely recognised for its use in the symptomatic relief of pain and inflammation of the mouth and throat.
The TxGNN model predicts it may have potential utility in **Benign Prostatic Hyperplasia (BPH)**, based on an indirect mechanistic link between its anti-inflammatory properties and the chronic inflammatory pathology hypothesised in BPH.
However, this prediction is currently supported by **no clinical trials** and **no published literature** — it represents a purely computational signal at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from UK marketing authorisation data; drug not currently registered in this dataset |
| Predicted New Indication | Benign Prostatic Hyperplasia (BPH) |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on the repurposing rationale provided, Benzydamine is understood to exert anti-inflammatory effects through inhibition of pro-inflammatory cytokines — specifically TNF-α, IL-1β, and IL-6. This places it in a pharmacological class with potential relevance to conditions driven by chronic low-grade inflammation.

Benign prostatic hyperplasia is increasingly understood not merely as a disorder of androgen-mediated cell proliferation, but as a condition in which chronic prostatic inflammation plays a significant pathophysiological role. Histological studies have repeatedly identified inflammatory infiltrates in BPH tissue, and elevated local cytokine levels — including the very mediators that Benzydamine is thought to suppress — have been associated with disease progression and lower urinary tract symptoms (LUTS). This provides an indirect, theoretical mechanistic bridge between the drug and the predicted indication.

That said, Benzydamine is predominantly formulated and used as a topical agent (mouthwash, oromucosal spray) for local, short-duration effects. Its systemic bioavailability and ability to achieve therapeutically relevant concentrations in prostatic tissue following conventional routes of administration have not been established. The TxGNN high score (0.9926) most likely reflects topological proximity within the knowledge graph between inflammation-related and proliferation-related nodes, rather than any direct pharmacological evidence of efficacy in BPH. Caution is therefore warranted in interpreting this signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Benzydamine in Benign Prostatic Hyperplasia.

---

## Literature Evidence

Currently no related literature available for Benzydamine in Benign Prostatic Hyperplasia.

---

## UK Market Information

Benzydamine holds no marketing authorisations in the UK dataset associated with this candidate record. No MHRA-authorised products, approved indications, or dosage form records are available for inclusion.

> **Note for reviewers:** Benzydamine-containing products (e.g., Difflam) may be available in the UK market under separate licence records not captured in this dataset. Practitioners should verify current authorisation status via the MHRA Product Licence Register and the BNF before drawing conclusions about commercial availability.

---

## Safety Considerations

Please refer to the SmPC and BNF for full safety information on Benzydamine. Report suspected adverse reactions via the Yellow Card Scheme at [https://yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produces a high computational score for Benzydamine in BPH; however, there is a complete absence of supporting clinical trial data or published literature, and the drug's established route of administration (topical/oromucosal) is incompatible with the systemic delivery required to reach prostatic tissue. The mechanistic link, while theoretically plausible, is indirect and unvalidated.

**To proceed, the following is needed:**

- **Mechanism of action data (MOA):** Confirm Benzydamine's systemic anti-inflammatory pharmacology and establish whether plasma concentrations achievable via oral or parenteral routes are sufficient to inhibit TNF-α/IL-1β/IL-6 at therapeutically relevant levels in prostatic tissue.
- **Pharmacokinetic assessment:** Evaluate systemic bioavailability across potential repurposing routes (oral tablet/capsule formulation) and model expected prostatic tissue penetration.
- **Preclinical evidence:** Conduct or identify *in vitro* / *in vivo* studies examining Benzydamine's effect on prostatic stromal or epithelial cell proliferation under inflammatory conditions, to upgrade from L5 to at least L4 evidence.
- **Literature scoping review:** Broaden the PubMed search beyond BPH to include prostatitis, LUTS, and related cytokine-mediated urological conditions, to identify any adjacent evidence that might support further investigation.
- **UK regulatory pathway review:** Confirm current MHRA authorisation status for all Benzydamine-containing products in the UK and assess whether any existing licence could support label extension or off-label use evaluation.
- **Safety data completion:** Retrieve the full SmPC (including warnings, contraindications, and drug interactions) before any clinical or translational programme is initiated.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

