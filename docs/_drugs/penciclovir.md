---
layout: default
title: Penciclovir
parent: Model Prediction Only (L5)
nav_order: 449
evidence_level: L5
indication_count: 10
---

# Penciclovir
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

# Penciclovir: From Herpes Simplex/Varicella-Zoster Virus Infection to Fascioliasis

## One-Sentence Summary

Penciclovir is a guanosine analogue whose antiviral activity depends on phosphorylation by viral (HSV/VZV) thymidine kinase, and it is conventionally used against herpes simplex and varicella-zoster virus infections.
The TxGNN model predicts it may be effective for **Fascioliasis** (liver fluke infection), but this is currently supported by **0 clinical trials** and **0 publications**, and the drug's own repurposing rationale flags the mechanism as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes simplex virus (HSV) / varicella-zoster virus (VZV) infection (inferred from mechanism of action data in the evidence pack; no formal indication text supplied) |
| Predicted New Indication | Fascioliasis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism of action (MOA) data for Penciclovir is not available in this evidence pack. Based on the mechanistic description accompanying the prediction, Penciclovir is a guanosine nucleoside analogue that requires phosphorylation by virus-specific thymidine kinase (HSV/VZV) before it can inhibit viral DNA polymerase and halt viral replication. This mechanism is entirely dependent on a viral enzyme system that herpesviruses possess but that is absent in helminth/trematode parasites.

Fascioliasis is caused by the liver fluke *Fasciola hepatica*, a trematode with a metabolic and enzymatic profile that has no known overlap with viral thymidine kinase-dependent nucleoside activation. The evidence pack's own repurposing rationale explicitly states that there is "no reasonable mechanistic support" for antiparasitic activity, and suggests the high TxGNN score more likely reflects indirect or noisy connections within the knowledge graph rather than a genuine biological relationship.

Given the absence of any supporting mechanism, clinical trial, or published literature, this prediction should be treated as a hypothesis-generating signal only, not as a basis for further pharmacological reasoning at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## UK Market Information

Penciclovir is recorded as **not marketed** in this evidence pack, with **0 marketing authorisations** on file. No licence records are currently available for this compound.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there are zero clinical trials, zero publications, no marketing authorisation in the UK, and the accompanying mechanistic rationale explicitly states there is no biological plausibility linking Penciclovir's viral thymidine kinase-dependent mechanism to fascioliasis. This is a Stage S0, Evidence Level L5 candidate with no independent corroboration.

**To proceed, the following is needed:**
- Verified MOA data from DrugBank (currently a blocking/high-severity data gap)
- TFDA/MHRA label warnings, contraindications and drug interaction data (currently a blocking data gap for safety triage)
- Independent preclinical or mechanistic evidence exploring any activity against *Fasciola hepatica* or related trematodes
- Confirmation of current UK/international marketing status for Penciclovir formulations
- Re-evaluation once any clinical trial or peer-reviewed literature becomes available for this drug-disease pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

