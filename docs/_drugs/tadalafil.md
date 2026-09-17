---
layout: default
title: Tadalafil
parent: Model Prediction Only (L5)
nav_order: 551
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Tadalafil: From Unspecified Original Indication to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

The Evidence Pack does not specify Tadalafil's original approved indication or mechanism of action (both flagged as data gaps), so this evaluation is based solely on the TxGNN prediction output. The model's top-ranked prediction is **Ambras Type Hypertrichosis Universalis Congenita**, a rare congenital hair-overgrowth syndrome, but there are **no supporting clinical trials and no supporting literature**, and the evidence pack's own mechanistic analysis flags this as a likely knowledge-graph artefact rather than a genuine biological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Evidence Pack (data gap) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Tadalafil is not available in this Evidence Pack. Based on general pharmacological knowledge referenced within the pack's own rationale text, Tadalafil is a PDE5 inhibitor acting on the cGMP/vascular smooth muscle pathway.

Ambras type hypertrichosis universalis congenita is a rare genetic disorder involving chromosomal rearrangement and abnormal hair follicle development. There is no known biological pathway connecting PDE5 inhibition to hair follicle morphogenesis or growth regulation. The Evidence Pack's own repurposing rationale explicitly states that this high score is most likely explained by a shared node in the knowledge graph (possibly via a skin or genotype-related node) producing a **false-positive link**, rather than genuine mechanistic plausibility.

Given the complete absence of clinical trial or literature support, and the explicit acknowledgement within the pack that no mechanistic pathway exists, this prediction should be treated as a model-generated hypothesis only, not as a candidate ready for further clinical consideration.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Tadalafil currently holds no marketing authorisations recorded in this Evidence Pack (market status: **Not Marketed**, 0 authorisations). No product, dosage form, or approved indication data is available for tabulation.

## Safety Considerations

- **Literature-derived signal (caution, not direct SmPC data)**: One case report (PMID [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/), *Cephalalgia*, 2006) describes Tadalafil associated with typical migraine aura without headache. This is a lower-ranked predicted association (rank 8, "migraine with brainstem aura") in this same Evidence Pack, and it points in the direction of a **risk signal**, not a treatment benefit — it should not be interpreted as supporting evidence for a new indication.
- Formal safety data — key warnings, contraindications, and drug–drug interactions — is not available in this Evidence Pack (DDI query returned no results). Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication has no supporting clinical trial or literature evidence, and the Evidence Pack's own mechanistic analysis describes it as a likely false-positive link arising from knowledge-graph structure rather than genuine biology. In addition, a Blocking-severity data gap (missing regulatory warnings/contraindications) means this candidate cannot yet enter the initial safety assessment stage (S1).

**To proceed, the following is needed:**
- Regulatory warnings, contraindications, and full SmPC/BNF safety information (currently missing — Blocking data gap)
- Confirmed mechanism of action via DrugBank or equivalent source (currently missing — High-priority data gap)
- Original approved indication(s) and UK marketing authorisation history for Tadalafil
- If further repurposing signals are explored from this batch, the mechanistically more plausible but still low-evidence candidate — kyphoscoliotic heart disease/PAH-related right heart strain (rank 7, flagged as "Research Question") — would warrant closer review before this hypertrichosis signal, given its class-effect rationale via pulmonary vasodilation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

