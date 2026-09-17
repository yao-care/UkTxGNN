---
layout: default
title: Nitazoxanide
parent: Model Prediction Only (L5)
nav_order: 417
evidence_level: L5
indication_count: 10
---

# Nitazoxanide
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

# Nitazoxanide: From Antiprotozoal Therapy to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Nitazoxanide is an antiprotozoal agent traditionally used against parasitic infections such as cryptosporidiosis and giardiasis. The TxGNN model predicts it may be effective for **Polyclonal Hyperviscosity Syndrome**, but this prediction is currently supported by **no clinical trials** and **no relevant literature** — it is a computational (knowledge-graph) signal only, and the evidence pack's own mechanistic assessment flags it as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antiprotozoal therapy (cryptosporidiosis, giardiasis) — inferred from evidence-pack rationale text; structured original indication and MOA fields are marked as data gaps |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 97.82% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for nitazoxanide is not available in this evidence pack (marked as a data gap). Based on the rationale text accompanying the predictions, nitazoxanide acts as a PFOR (pyruvate:ferredoxin oxidoreductase)-dependent electron-transfer inhibitor, a mechanism effective against protozoal pathogens such as *Cryptosporidium* and *Giardia*. Its efficacy in these parasitic infections is well established.

Polyclonal hyperviscosity syndrome, by contrast, arises from excess circulating immunoglobulins (typically IgM or IgG) increasing blood viscosity — an immunological/haematological disorder with no known relationship to antiprotozoal pharmacology. The evidence pack itself explicitly states that there is "no known mechanistic link" between the drug and this condition.

Given the absence of any supporting clinical, preclinical, or literature evidence, and the explicit assessment that the high TxGNN score likely reflects a knowledge-graph embedding artefact rather than genuine biological plausibility, this prediction should be treated as low confidence pending further mechanistic justification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: a single case report (PMID [33642203](https://pubmed.ncbi.nlm.nih.gov/33642203/)) appears under a different candidate indication — monoclonal gammopathy — describing nitazoxanide used to treat an opportunistic cryptosporidiosis infection in myeloma patients, not to treat the gammopathy itself. This is not relevant evidence for polyclonal hyperviscosity syndrome.)*

---

## UK Market Information

Nitazoxanide currently holds no UK marketing authorisations (market status: **Not marketed**; total licences: **0**). No product-level information is available for this drug in the UK market.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: key warnings, contraindications, and drug–drug interaction data are currently flagged as data gaps in this evidence pack — see DG001, a blocking gap for TFDA-equivalent warning/contraindication data, and DG002, a high-severity gap for mechanism-of-action data.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (polyclonal hyperviscosity syndrome) has no supporting clinical trials, no supporting literature, and no plausible mechanistic pathway connecting nitazoxanide's known antiprotozoal action to an immunoglobulin-driven hyperviscosity disorder. The evidence pack explicitly characterises this as a probable false positive arising from knowledge-graph embedding rather than genuine biological signal.

**To proceed, the following is needed:**
- Resolution of DG001 (drug warnings/contraindications) and DG002 (mechanism of action) data gaps
- Any preclinical or in vitro evidence establishing a biological link between nitazoxanide and immunoglobulin/viscosity regulation before further investigation is warranted
- Confirmation of UK regulatory pathway options, given nitazoxanide currently holds no UK marketing authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

