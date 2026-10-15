---
layout: default
title: Gamolenic Acid
parent: Model Prediction Only (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
---

# Gamolenic Acid
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

# Gamolenic Acid: From an Unspecified Original Indication to Insomnia

## One-Sentence Summary

Gamolenic acid (GLA) is an omega-6 fatty acid marketed in the UK as an 80 mg capsule. The data compiled for this report do not state its original approved indication.
The TxGNN model predicts it may be effective for **insomnia**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, GLA is converted to dihomo-gamma-linolenic acid and then to prostaglandin E1 (PGE1), which has anti-inflammatory effects.

A link between this pathway and sleep regulation is speculative. Possible routes would be modulation of neuroinflammation or neuronal membrane lipid composition, but nothing in the data compiled for this report supports either. The high score is the only support for the prediction.

Other predictions follow the same pattern:
- **Sleep disorder (initiating and maintaining sleep)** (98.87%) is essentially the same clinical entity as insomnia, so it likely reflects the same signal rather than independent support.
- **Anxiety** (98.87%), **anxiety disorder** (97.14%) and **agoraphobia** (97.27%) overlap with one another and are likewise unsupported by trials or literature.
- **Rheumatoid arthritis** (97.61%) is the most biologically plausible. GLA is metabolised to PGE1 and 15-HETrE, which have anti-inflammatory effects and may reduce pro-inflammatory leukotriene production. This is consistent with GLA's known pharmacology, but the data compiled here contain no trials or literature, so it remains L5. It is flagged as a research question.
- Predictions for **alcohol withdrawal delirium**, **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, **benign paroxysmal torticollis of infancy** and **acute encephalopathy with biphasic seizures and late reduced diffusion** (all about 97%) have no plausible GLA mechanism and are most likely knowledge-graph artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1305010I0AAABAB | Gamolenic Acid Cap 80mg | Capsule (80 mg) | Not stated in the compiled data |

The identifier above is a classification-style code rather than a standard MHRA PL number, so it should be verified against the MHRA register. The approved indication, manufacturer and NICE appraisal status should also be checked against the SmPC and BNF.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction has a high model score but no supporting trials, no literature and no mechanism of action data, so it remains at evidence level L5. Safety information is also missing, so the candidate cannot progress to safety screening.

**To proceed, the following is needed:**
- Confirm the original approved indication and the full SmPC (warnings, contraindications, interactions) from the MHRA and BNF.
- Obtain mechanism of action data (for example from DrugBank).
- Run a targeted literature and trial registry search (PubMed, ClinicalTrials.gov, ISRCTN, EU CTR) for GLA in insomnia and sleep disorders.
- Run a separate targeted search for existing GLA randomised trials in rheumatoid arthritis, the most biologically plausible alternative. Such evidence may exist outside the compiled data and could raise the evidence level.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

