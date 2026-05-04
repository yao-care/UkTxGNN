---
layout: default
title: Chloroxylenol
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
---

# Chloroxylenol
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

# Chloroxylenol: From Antimicrobial Agent to Osteoarthritis

## One-Sentence Summary

Chloroxylenol (PCMX) is a phenol-based antimicrobial agent widely used as a topical antiseptic and disinfectant ingredient (e.g. in surgical scrubs and household antiseptic products), but it currently holds no MHRA marketing authorisation for any therapeutic indication in the United Kingdom.
The TxGNN model predicts it may be effective for **Osteoarthritis**, with a prediction score of **98.27%**; however, this prediction is supported by **no clinical trials** and **no directly relevant published literature**.
Critically, the only related study identified in evidence gathering demonstrates cartilage toxicity from chronic chloroxylenol exposure — a negative mechanistic signal that directly contradicts a therapeutic role in joint disease.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical antimicrobial / antiseptic agent (no UK marketing authorisation on record) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.27% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for chloroxylenol is not currently available in this evidence pack. Based on established pharmacological knowledge, chloroxylenol is a halogenated phenolic compound that exerts broad-spectrum antimicrobial activity primarily through disruption of bacterial cell membranes and enzyme inactivation. Like other phenolic compounds, it may in principle possess weak antioxidant properties, and phenolics as a chemical class have been theorised to modulate inflammatory pathways (e.g. NF-κB inhibition). The TxGNN model most likely connected chloroxylenol to osteoarthritis via knowledge graph nodes linking phenolic compounds to proteoglycan or collagen degradation pathways relevant to cartilage biology.

The relationship between the antimicrobial/antiseptic indication and osteoarthritis is mechanistically tenuous. Osteoarthritis is a degenerative joint condition driven by cartilage breakdown, subchondral bone remodelling, and low-grade synovial inflammation. There is no established pharmacological bridge between topical antisepsis and systemic or intra-articular chondroprotection. The prediction score, whilst high in absolute terms, reflects the model's graph-traversal confidence rather than biological plausibility validated by experimental data.

Of particular concern, the sole identified study involving chloroxylenol and cartilage biology (PMID [39489103](https://pubmed.ncbi.nlm.nih.gov/39489103/)) reports **toxic** effects on endochondral ossification in amphibian tadpoles following chronic exposure. This constitutes a **negative mechanistic signal**: rather than protecting cartilage, chloroxylenol appears to impair the very process of cartilage-to-bone formation that is relevant in joint tissue homeostasis. This finding should be treated as a meaningful counter-signal against pursuing this repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The following paper was retrieved during evidence collection for related musculoskeletal indications. It is included here as the only available literature signal — noting that its findings are adverse rather than supportive.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39489103](https://pubmed.ncbi.nlm.nih.gov/39489103/) | 2024 | Animal Toxicology Study (in vivo) | Aquatic Toxicology | Chronic exposure to chloroxylenol (PCMX) at environmentally relevant concentrations (1.43–143 µg/L) inhibited endochondral ossification and impaired body condition in *Rana chensinensis* tadpoles — indicating cartilage developmental toxicity, not a therapeutic effect |

> **⚠️ Interpretive note:** This study demonstrates harm to cartilage tissue, not benefit. It should be interpreted as a negative mechanistic signal for any osteoarthritis or joint disease repurposing hypothesis.

---

## UK Market Information

Chloroxylenol holds **no MHRA marketing authorisations** in the United Kingdom. It is present as an active ingredient in certain topical antiseptic consumer products, but these are regulated as biocidal products or general sale cosmetics rather than licensed medicinal products. There are no BNF entries for chloroxylenol as a monotherapy medicinal product. No NICE technology appraisals cover this compound.

---

## Safety Considerations

Detailed clinical safety data (prescribing warnings, formal contraindications, and drug–drug interaction profiles) are not available in this evidence pack.

Please refer to the Summary of Product Characteristics (SmPC) and the British National Formulary (BNF) for full safety information when evaluating any potential therapeutic application. Report suspected adverse reactions via the **[Yellow Card Scheme](https://yellowcard.mhra.gov.uk/)** (MHRA).

> **Additional signal of concern:** One environmental toxicology study (PMID 39489103) documents adverse effects on cartilage and bone development. Systemic safety in humans has not been characterised for any therapeutic dosing regimen.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications for chloroxylenol are graded L5 (model prediction only), with zero supporting clinical trials and no substantive therapeutic literature. The single identified relevant study documents cartilage toxicity rather than benefit, directly contradicting the osteoarthritis repurposing hypothesis. Furthermore, four predictions sharing identical TxGNN scores (ranks 7–10, all hepatic diseases) are consistent with knowledge graph clustering artefacts rather than genuine independent predictions, raising questions about signal reliability across this candidate profile. Chloroxylenol currently has no UK marketing authorisation, and no established therapeutic dose, route, or formulation exists from which a clinical programme could be derived.

**To proceed, the following would be needed at minimum:**

- **Mechanism of action clarification**: Systematic review of chloroxylenol's known molecular targets and whether any interact with pathways relevant to osteoarthritis (e.g. MMP inhibition, NF-κB, RANKL/OPG axis)
- **Toxicology safety review**: Full characterisation of systemic toxicity at therapeutic-range exposures in mammalian models, particularly addressing the chondrotoxicity signal from PMID 39489103
- **Pharmacokinetic data**: Joint penetration and bioavailability data to assess whether systemic or intra-articular concentrations relevant to any anti-inflammatory effect are achievable without toxicity
- **Preclinical proof-of-concept study**: A mammalian in vivo model of osteoarthritis (e.g. DMM mouse model) demonstrating efficacy before any human application is considered
- **Regulatory pathway scoping**: A pre-submission meeting with the MHRA to discuss the feasibility of a new therapeutic indication given the absence of existing authorisations

> *This report is produced for research purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

