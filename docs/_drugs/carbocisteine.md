---
layout: default
title: Carbocisteine
parent: Model Prediction Only (L5)
nav_order: 134
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-06
description: "Carbocisteine: predicted new indication Gout (evidence level L5). Approved use: Not stated in the available authorisation data (the product is classe…"
monitor_inn: "Carbocisteine"
predicted_indications: ["gout"]
---

# Carbocisteine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Carbocisteine: From an Unspecified Original Indication to Gout
{: .text-alpha }

## One-Sentence Summary

Carbocisteine is a mucolytic agent marketed in the UK as a 375 mg capsule. The data compiled for this report do not state its approved indication.
The TxGNN model predicts it may be effective for **gout**, but there are currently **no clinical trials** and **no publications** supporting this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available authorisation data (the product is classed as a mucolytic) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (11 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Carbocisteine is a mucolytic, and it is generally thought to act as a thiol-based agent with antioxidant and anti-inflammatory properties. Its original indication is not recorded in the data compiled for this report, so the relationship between the original and predicted indications cannot be assessed directly.

A plausible but unproven hypothesis is that these antioxidant and anti-inflammatory effects could modulate oxidative stress and inflammation relevant to gouty inflammation, for example neutrophil activity and NLRP3-related signalling. **No evidence in the compiled data supports this.** There is also no established link to urate-lowering mechanisms such as xanthine oxidase inhibition or URAT1 inhibition.

The high TxGNN score (0.9967) is therefore a computational signal that needs verification, not evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0307000J0AAABAB | Carbocisteine 125mg/5ml oral solution | Carbocisteine |
| 0307000J0AAACAC | Carbocisteine 250mg/5ml oral solution | Carbocisteine |
| 0307000J0AAAHAH | Carbocisteine 250mg/5ml oral solution sugar free | Carbocisteine |
| 0307000J0AAAAAA | Carbocisteine 375mg capsules | Carbocisteine |
| 0307000J0AAAJAJ | Carbocisteine 750mg capsules | Carbocisteine |
| 0307000J0AAAGAG | Carbocisteine 750mg/10ml soln 10ml sachets sugar free | Carbocisteine |
| 0307000J0AAAIAI | Carbocisteine 750mg/5ml oral solution sugar free | Carbocisteine |
| 0307000J0BBABAC | Mucodyne 250mg/5ml syrup | Carbocisteine |
| 0307000J0BBAAAA | Mucodyne 375mg capsules | Carbocisteine |
| 0307000J0BBADAB | Mucodyne Paediatric 125mg/5ml syrup | Carbocisteine |
| 0307000J0BBAEAC | Mucodyne Paediatric 250mg/5ml syrup | Carbocisteine |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

The identifier above appears to be a BNF-style product code, not a standard PL marketing authorisation number. It should be verified against the MHRA register. The BNF chemical code (03.07) places carbocisteine among the mucolytics in the respiratory system chapter.

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph (PrimeKG) links carbocisteine with a contraindication for **active peptic ulcer disease**. This comes from the graph, not from label text, and should be checked against the SmPC.

No drug interaction records were found in the data compiled for this report.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for this prediction is a model score. There are no clinical trials or publications, the mechanism of action is missing, and the approved indication and label safety data could not be obtained. The evidence level is L5.

**To proceed, the following is needed:**
- The approved indication, dosage form and manufacturer from the MHRA authorisation and SmPC, and verification of the product identifier
- Label warnings and contraindications, including confirmation of the peptic ulcer signal, to allow safety screening
- Mechanism of action data to test whether antioxidant or anti-inflammatory effects are relevant to gout
- A systematic search for preclinical or clinical studies of carbocisteine in gout or crystal-induced inflammation
- A comparison with established gout treatments (urate-lowering therapy, anti-inflammatory therapy) to define any plausible role
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

