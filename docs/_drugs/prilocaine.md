---
layout: default
title: Prilocaine
parent: Model Prediction Only (L5)
nav_order: 479
evidence_level: L5
indication_count: 10
---

# Prilocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Prilocaine: From Local Anaesthesia to Papillary Conjunctivitis

## One-Sentence Summary

Prilocaine is an amide-type local anaesthetic, originally used to provide local and regional anaesthesia (for example dental and nerve blocks, and topical anaesthesia as the EMLA cream component).
The TxGNN model predicts it may be effective for **Papillary Conjunctivitis**,
but currently **no clinical trials** and **no publications** support this specific direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local and regional anaesthesia (amide-type local anaesthetic) |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for prilocaine is not available in DrugBank for this evidence pack. Based on the pharmacological information referenced across the wider evidence base, prilocaine is an amide-type local anaesthetic that blocks voltage-gated Na⁺ channels in peripheral sensory neurones, producing local and regional anaesthesia. It is used for infiltration and nerve-block anaesthesia and, in combination with lidocaine, as the topical anaesthetic cream EMLA.

Papillary conjunctivitis is an allergic or mechanically driven inflammatory condition of the conjunctival surface, mediated by immune and vascular pathways rather than peripheral nerve conduction. There is no established pharmacological pathway connecting Na⁺ channel blockade to conjunctival papillary inflammation. The model's own repurposing rationale states this prediction "應屬 KG embedding 相似性而非藥理連結" (likely reflects knowledge-graph embedding similarity rather than a genuine pharmacological connection), and no clinical trial or literature evidence was found to support the association. This prediction should be treated as exploratory only.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## UK Market Information

Prilocaine currently holds no active marketing authorisation recorded in this evidence pack (market status: Not Marketed; 0 licences on file). No product-level dosage form or indication data is therefore available.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score, there is no clinical trial or literature evidence, and no plausible mechanistic link, connecting prilocaine to papillary conjunctivitis. The model's own analysis flags this as a probable embedding artefact rather than a genuine pharmacological signal.

**To proceed, the following is needed:**
- Confirmed mechanism of action data from DrugBank (currently a data gap, DG002)
- TFDA/MHRA product label warnings and contraindications (currently blocking, DG001 — required before any S1 safety screening)
- Preclinical or in vitro evidence linking Na⁺ channel blockade to conjunctival inflammatory pathways, if this indication is to be pursued further

**Note:** among the other TxGNN-ranked candidates in this evidence pack, **neuralgia** (rank 5, evidence level L3, decision stage S2, "Proceed with Guardrails") is substantially better supported — it has a coherent mechanistic rationale (prilocaine as an EMLA component for postherpetic neuralgia) and multiple relevant clinical trials and publications, including an RCT (PMID 2616182, tier 1). This may be a more productive candidate for further evaluation than the top-ranked prediction reported here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

