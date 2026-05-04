---
layout: default
title: Auranofin
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 2
---

# Auranofin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Auranofin: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Auranofin is an oral gold compound classically used in the treatment of rheumatoid arthritis, known for its immunomodulatory and thioredoxin reductase (TrxR)-inhibiting properties.
The TxGNN model predicts it may be effective for **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**, an extremely rare congenital developmental disorder affecting the eyes and skeleton.
There is currently **no supporting clinical trial or published literature evidence** for this indication, placing this prediction at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis (based on established drug profile; no UK marketing authorisation on record) |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Auranofin is an orally bioavailable organogold compound whose primary mechanism centres on the inhibition of thioredoxin reductase (TrxR), a selenocysteine-containing enzyme critical to cellular redox homeostasis. By disrupting the thioredoxin system, Auranofin promotes an accumulation of reactive oxygen species (ROS), shifts the intracellular redox balance, and triggers apoptotic pathways. It also suppresses NF-κB signalling and modulates downstream inflammatory cascades, which accounts for its established disease-modifying efficacy in rheumatoid arthritis. There is growing research interest in repurposing Auranofin for oncology and infectious disease indications on the basis of these same redox-disrupting properties. Detailed mechanism of action data was not available in the current evidence pack; the above is drawn from published pharmacological literature.

Colobomatous microphthalmia-rhizomelic dysplasia syndrome is an exceptionally rare condition caused by embryonic-stage genetic mutations — likely involving developmental signalling pathways such as BMP, WNT, or Hedgehog — that result in fixed structural malformations: ocular coloboma/microphthalmia and rhizomelic (proximal limb) shortening. These are irreversible structural defects established during organogenesis, not inflammatory, redox-driven, or immune-mediated processes susceptible to pharmacological modulation in postnatal life.

The mechanistic overlap between Auranofin's TrxR-inhibitory and immunomodulatory pharmacology and this syndrome's pathophysiology is therefore extremely tenuous. The TxGNN knowledge graph model may have identified an indirect network connection via shared immune or oxidative stress nodes within the biological graph — for instance, through NF-κB as a tangential link to BMP downstream signalling — but this is a graph topological association rather than a direct biological rationale. No mechanistic basis currently supports the hypothesis that TrxR inhibition could alter or ameliorate the structural consequences of these developmental mutations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Safety data for Auranofin (key warnings, contraindications, and drug interactions) was not retrievable within the current evidence pack. As Auranofin holds no UK marketing authorisation, no MHRA-approved Summary of Product Characteristics (SmPC) is available domestically. Please consult the BNF, available international SmPCs (e.g., US label for Ridaura®), and primary pharmacological literature for safety profiling. Any suspected adverse reactions observed in clinical or research settings should be reported via the **MHRA Yellow Card Scheme** at [https://yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score of 99.56%, this score reflects network-based topological proximity rather than biological plausibility. Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a congenital structural condition with no mechanistic correspondence to Auranofin's pharmacology, and there is a complete absence of supporting clinical, preclinical, or mechanistic evidence for this repurposing direction.

**To proceed, the following is needed:**

- **Mechanistic evidence**: Identification of a credible biological pathway linking TrxR inhibition or NF-κB modulation to the pathophysiology of this specific syndrome (e.g., relevant in vitro cellular or genetic models)
- **Preclinical data**: In vitro and/or in vivo studies in relevant disease models demonstrating measurable pharmacological effect
- **Regulatory clarification**: Confirmation of Auranofin's approved status across relevant jurisdictions (US, EU) and retrieval of the full SmPC for safety baseline assessment
- **Safety profiling**: Complete characterisation of key warnings, contraindications, and clinically significant drug interactions before any further development steps are undertaken
- **MOA documentation**: Retrieval of Auranofin's full mechanism of action profile from DrugBank (DB00995) to support any future mechanistic plausibility analysis

> ⚠️ **Research Disclaimer**: This report is produced for research purposes only and does not constitute medical advice. All drug repurposing candidates identified by TxGNN require clinical validation before any therapeutic application. This content should not be used to inform prescribing decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

