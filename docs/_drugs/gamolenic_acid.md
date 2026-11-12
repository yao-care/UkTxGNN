---
layout: default
title: Gamolenic Acid
parent: Model Prediction Only (L5)
nav_order: 311
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-06
monitor_inn: "Gamolenic acid"
predicted_indications: ["insomnia (disease)"]
description: "Gamolenic Acid: predicted new indication Insomnia (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Gamolenic Acid
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

## Gamolenic Acid: Insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Gamolenic acid (GLA) is an omega-6 fatty acid marketed in the UK as an 80 mg capsule. The data compiled for this report do not state its original approved indication.
The TxGNN model predicts it may be effective for **insomnia**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (23 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 23 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, GLA is converted to dihomo-gamma-linolenic acid and then to prostaglandin E1 (PGE1), which has anti-inflammatory effects.

A link between this pathway and sleep regulation is speculative. Possible routes would be modulation of neuroinflammation or neuronal membrane lipid composition, but nothing in the data compiled for this report supports either. The high score is the only support for the prediction.

Other predictions follow the same pattern:
- GLA is metabolised to PGE1 and 15-HETrE, which have anti-inflammatory effects and may reduce pro-inflammatory leukotriene production. This is consistent with GLA's known pharmacology, but the data compiled here contain no trials or literature, so it remains L5. It is flagged as a research question.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1305010I0AAAAAA | Gamolenic acid 40mg capsules | Gamolenic acid |
| 1305010I0AAAMAM | Gamolenic acid 67.5mg/5ml oral solution | Gamolenic acid |
| 1305010I0AAABAB | Gamolenic acid 80mg capsules | Gamolenic acid |
| 1305010I0BWAAAA | AaciGam 40mg capsules | Gamolenic acid |
| 1305010I0BWABAB | AaciGam 80mg capsules | Gamolenic acid |
| 1305010I0BMACAI | Boots Evening Primrose Oil One A Day capsules | Gamolenic acid |
| 1305010I0BMADAM | Boots Evening Primrose Oil liquid | Gamolenic acid |
| 1305010I0BUAAAA | Gam-O 40mg capsules | Gamolenic acid |
| 1305010I0BUABAB | Gam-O 80mg capsules | Gamolenic acid |
| 1305010I0BVAAAA | Gamolen 40mg capsules | Gamolenic acid |
| 1305010I0BVABAB | Gamolen 80mg capsules | Gamolenic acid |
| 1305010I0AAAPAP | Gamolenic acid 37mg / Vitamin E 10unit capsules | Gamolenic acid |
| 1305010I0AAAQAQ | Gamolenic acid 74mg / Vitamin E 10unit capsules | Gamolenic acid |
| 091200000AAEPEP | Gamolenic acid 90mg / Vitamin E 10unit capsules | Other health supplement preparations |
| 1305010I0AAAIAI | Gamolenic acid 90mg / Vitamin E 15unit capsules | Gamolenic acid |
| 1305010I0AAANAN | Gamolenic acid 95mg / Vitamin E 15unit capsules | Gamolenic acid |
| 1305010I0BGAAAA | Gamophase 40mg capsules | Gamolenic acid |
| 1305010I0BJAAAA | Lamberts Evening Primrose Oil capsules | Gamolenic acid |
| 1305010I0BIAAAA | Lin-Gam 40mg capsules | Gamolenic acid |
| 091200000BFNQEP | Lloydspharmacy Evening Primrose Oil 1000mg capsules | Other health supplement preparations |

Showing 20 of 23 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

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
- Such evidence may exist outside the compiled data and could raise the evidence level.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

