---
layout: default
title: Amorolfine
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Amorolfine
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

# Amorolfine: From Onychomycosis to Drug-Induced Osteoporosis

## One-Sentence Summary

Amorolfine is a morpholine-class topical antifungal agent, established for the treatment of onychomycosis (fungal nail infections) via a nail lacquer formulation. The TxGNN model predicts it may be effective for **Drug-Induced Osteoporosis**, however this prediction is currently supported by **no clinical trials** and **no published literature**, placing the evidence at the lowest possible confidence level (L5). This finding is most likely a model artefact and warrants a **Hold** decision at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Onychomycosis (topical antifungal; no UK marketing authorisation data returned in this dataset) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.9978% |
| Evidence Level | L5 |
| UK Market Status | Not marketed (per dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Amorolfine is a morpholine antifungal that exerts its effect by inhibiting two sequential enzymes in the **fungal ergosterol biosynthesis pathway**: Δ14-reductase and Δ7–Δ8-isomerase. This causes depletion of ergosterol — the principal sterol in fungal cell membranes — and accumulation of aberrant sterols (notably ignosterol), leading to membrane disruption and fungal cell death. Detailed MOA data from DrugBank was not available in this evidence pack, but the above is well-established in the pharmacological literature.

The mechanistic link proposed by TxGNN is **highly speculative**. The theoretical basis rests on the fact that the ergosterol and mammalian cholesterol biosynthesis pathways share upstream sterol precursors. It has been hypothesised that sterol synthesis inhibition could, in principle, interfere with bone metabolism-related steroid hormones. However, Amorolfine's target enzyme (fungal Δ14-reductase) is functionally and structurally distinct from any human enzyme involved in bone metabolism or steroid hormone synthesis, and there is no established role for this target in mammalian physiology.

Crucially, Amorolfine is formulated exclusively as a **topical nail lacquer** with negligible systemic absorption. Even if a hypothetical mechanistic link to bone metabolism were to exist, the drug cannot reach bone tissue at clinically relevant concentrations following topical application. There is no clinical, preclinical, or mechanistic evidence in the published literature to support Amorolfine in drug-induced osteoporosis. This prediction almost certainly reflects a knowledge graph artefact resulting from shared pathway nodes, rather than a genuine repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No UK marketing authorisation records were returned for Amorolfine in this dataset. Clinicians should be aware that amorolfine (Loceryl® nail lacquer 5%) has historically been available in the UK as both a Prescription-Only Medicine (POM) and, subsequently, as a Pharmacy (P) medicine for mild to moderate onychomycosis not involving the lunula. Clinicians are advised to consult the current **MHRA Product Licence register** and the **British National Formulary (BNF) Section 13.10.2** (Antifungal preparations) for up-to-date authorisation status and prescribing guidance.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

> **Note regarding pregnancy:** The repurposing rationale in this evidence pack flags that animal studies have shown reproductive toxicity for amorolfine. This is a relevant safety signal to document should any systemic reformulation ever be considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction of amorolfine for drug-induced osteoporosis is biologically implausible given the drug's fungal-specific mechanism of action, its exclusively topical formulation with negligible systemic absorption, and the complete absence of supporting clinical trials or published literature (Evidence Level L5). This is not a viable repurposing candidate under current evidence.

**To proceed, the following would be needed:**

- **MOA data gap closure:** Retrieve full DrugBank entry for DB09056 to confirm target profile and any off-target human enzyme interactions that might theoretically link to sterol metabolism in bone
- **Pharmacokinetic assessment:** Obtain or model systemic bioavailability data to determine whether therapeutically relevant concentrations at bone could ever be achieved (even with a hypothetical systemic reformulation)
- **Preclinical evidence:** Commission or identify *in vitro* or *in vivo* studies examining amorolfine's effects on mammalian sterol synthesis or osteoblast/osteoclast biology, should any plausible mechanism emerge
- **Regulatory data retrieval:** Download and parse current MHRA product information and SmPC to complete the safety assessment (currently blocking)
- **Reformulation feasibility:** If mechanistic evidence were ever to emerge, a systemic oral or parenteral formulation would be required, entailing a full new drug development programme — a substantial barrier to repurposing

> **Research disclaimer:** This report is intended for research purposes only and does not constitute medical advice. Any drug repurposing candidate identified by the TxGNN model requires rigorous clinical validation before consideration for patient use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

