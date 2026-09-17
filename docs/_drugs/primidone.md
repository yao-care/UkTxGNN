---
layout: default
title: Primidone
parent: Model Prediction Only (L5)
nav_order: 481
evidence_level: L5
indication_count: 10
---

# Primidone
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

# Primidone: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Primidone is a broad-spectrum antiepileptic agent, metabolised to phenobarbital and PEMA, though confirmed UK licensing/indication data are not currently available for this drug in this evidence pack. The TxGNN model predicts a possible link to **Trigeminal Nerve Neoplasm** with a **99.99%** prediction score, but **zero clinical trials** and **zero relevant publications** currently support this specific indication — the model's own rationale flags this as a likely knowledge-graph artefact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / seizure disorders (inferred from the drug's pharmacological classification in the evidence pack; no confirmed UK licensing text available) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, formally-sourced mechanism of action data for Primidone is currently a data gap (flagged as a blocking issue in this pack). Based on the mechanistic notes attached to this prediction, Primidone is metabolised to phenobarbital and phenylethylmalonamide (PEMA), acting on GABA-A receptors and voltage-gated sodium channels — the pharmacology of a classic broad-spectrum antiepileptic drug.

There is no known mechanistic connection between this GABA-A/sodium-channel activity and the tumour proliferation pathways implicated in trigeminal nerve neoplasms (e.g. schwannoma). The evidence pack itself notes that the very high TxGNN score most likely reflects lexical/embedding proximity within the knowledge graph — the model may be conflating "trigeminal" as it appears in *trigeminal neuralgia* (a pain condition antiepileptics are sometimes used for) with *trigeminal nerve neoplasm* (a structural tumour), rather than identifying a true pharmacological relationship.

Given the complete absence of supporting clinical trials or literature, and the explicit internal caveat about graph-based confusion, this specific prediction should be treated as low-confidence and not pursued as a repurposing hypothesis without independent mechanistic or preclinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Trigeminal Nerve Neoplasm) has no supporting clinical trials or literature (Evidence Level L5), and the accompanying rationale explicitly identifies this as a probable knowledge-graph artefact rather than a genuine pharmacological signal. Primidone is also not currently marketed in the UK, and core drug-level data — labelling warnings/contraindications and confirmed mechanism of action — are outstanding data gaps (one of them blocking).

**To proceed, the following is needed:**
- TFDA/MHRA product labelling (warnings, contraindications) — currently a blocking data gap preventing any safety pre-assessment
- Confirmed mechanism of action data from DrugBank or an SmPC
- Independent preclinical or mechanistic evidence specifically linking Primidone to trigeminal nerve tumour biology, given the current complete absence of supporting data
- If repurposing work on Primidone continues, consider redirecting attention to the reflex-epilepsy candidates elsewhere in this evidence pack (e.g. audiogenic seizures, startle epilepsy, eating seizures, trigeminal neuralgia), which carry stronger literature support (L3–L4) — though these too currently lack dedicated clinical trials and would need a "Research Question" stage workup before any Go decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

