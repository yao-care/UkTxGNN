---
layout: default
title: Cyclopentolate
parent: Model Prediction Only (L5)
nav_order: 183
evidence_level: L5
indication_count: 3
---

# Cyclopentolate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Cyclopentolate: From Ophthalmic Mydriasis to Cauda Equina Syndrome

## One-Sentence Summary

Cyclopentolate is a short-acting anticholinergic (antimuscarinic) agent used topically in ophthalmology to produce mydriasis and cycloplegia. The TxGNN model predicts a possible link to **Cauda Equina Syndrome**, but this is supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic assessment finds no plausible pharmacological pathway between the two conditions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ophthalmic mydriasis/cycloplegia (not formally recorded in this evidence pack; the drug is not currently UK-marketed) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for cyclopentolate has not been confirmed in this evidence pack (flagged as a High-severity data gap requiring DrugBank API verification). Based on known pharmacology, cyclopentolate is a short-acting antimuscarinic used exclusively as a topical ophthalmic agent to induce pupil dilation and paralysis of accommodation ahead of eye examinations or procedures.

Cauda equina syndrome, by contrast, is a surgical emergency caused by compression of the lumbosacral nerve roots, requiring urgent decompressive surgery. There is no established pharmacological mechanism by which a topical antimuscarinic eye drop would treat or modify the course of this condition.

The model's own rationale is explicit on this point: the high TxGNN score most likely reflects graph-level co-occurrence or proximity between nodes in the knowledge graph, rather than a genuine causal or mechanistic relationship. No clinical trials or literature evidence exist to support this candidate, and no route-of-administration or dosing pathway has been established for systemic or off-label use in this context.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

Cyclopentolate does not currently hold any UK marketing authorisation recorded in this evidence pack (0 licenses on file; market status: not marketed). No product, dosage form, or approved-indication data is therefore available to tabulate.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: UK product labelling/warnings and contraindication data for cyclopentolate were not available in this evidence pack — this is flagged as a Blocking data gap that must be resolved before any safety evaluation can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted association between cyclopentolate and cauda equina syndrome lacks any supporting clinical trial or literature evidence, and the repurposing rationale itself concludes there is no credible pharmacological mechanism linking a topical ophthalmic antimuscarinic to a surgical nerve-compression emergency. The high TxGNN score appears to reflect knowledge-graph proximity rather than causal relevance, and no UK regulatory or safety data are currently available to support further evaluation.

**To proceed, the following is needed:**
- Confirmed mechanism of action data from DrugBank (DG002)
- UK/SmPC warnings, contraindications, and drug interaction data (DG001 — currently blocking any safety evaluation)
- Independent pharmacological or preclinical rationale specifically connecting cyclopentolate to neurological/nerve-root pathology, if this candidate is to be pursued further
- As an alternative research direction, the model's second- and third-ranked predictions (neurogenic bladder and irritable bowel syndrome) carry somewhat stronger class-level rationale, as antimuscarinics are an established drug class for both conditions — though these too remain at evidence level L5 with no supporting trials or literature, and are appropriately flagged as open research questions rather than actionable candidates at this stage.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

