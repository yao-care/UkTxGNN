---
layout: default
title: Famciclovir
parent: Model Prediction Only (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Famciclovir: predicted new indication Post-infectious neuralgia (evidence level L5). Approved use: Herpes zoster"
---

# Famciclovir
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

# Famciclovir: From Herpes Zoster to Post-Infectious Neuralgia

## One-Sentence Summary

Famciclovir is an antiviral medicine originally used to treat herpes zoster (shingles).
The TxGNN model predicts it may be effective for **post-infectious neuralgia** (postherpetic neuralgia), but the evidence is very limited: **1 related clinical trial** is listed, and it tests oxycodone rather than famciclovir, and **no publications** are linked to this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes zoster (from the TxGNN knowledge graph; no approved indication text is available for the UK licence) |
| Predicted New Indication | Post-infectious neuralgia |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only; no study tests famciclovir for this indication) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this report. Based on known information, famciclovir is a prodrug of penciclovir, a guanosine analogue active against herpesviruses. Its efficacy in herpes zoster is established, and mechanistically it may be relevant to the neuralgia that follows zoster.

Postherpetic neuralgia is the most common complication of herpes zoster, the drug's original indication. Early antiviral treatment may reduce the severity of the acute zoster episode and could plausibly lower the risk of the neuralgia that follows. However, this is an inference rather than demonstrated evidence. The only trial linked to this prediction (NCT03120962) tests early oxycodone, not famciclovir, so it provides no direct support for the drug. Because the target condition is a sequela of the existing indication, this is closer to an extension of current use than a true repurposing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | Not applicable | Unknown | 140 | Early oxycodone during acute herpes zoster to prevent postherpetic neuralgia. Famciclovir is not the studied intervention, so this is indirect context only. |

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503021E0AAABAB | Famciclovir Tab 125 mg | Not stated | Not stated |

One single-ingredient product is recorded as valid. The data compiled for this report do not include a dosage form or indication text for this authorisation, and the identifier is not in the standard MHRA PL format, so it should be verified against the MHRA register and the BNF.

---

## Safety Considerations

- **Kidney disease**: The knowledge graph links famciclovir to kidney disease as a contraindication. This comes from graph data rather than label text, so check the SmPC for renal dose adjustment.
- **Pyoureter**: Also listed as a graph-derived contraindication.
- **Drug interactions**: 84 potential interactions were identified, but their severity levels are unclassified. Examples include calcitriol, doxycycline, metformin, morphine, omeprazole, pantoprazole, prednisolone, prednisone, simvastatin and vancomycin. Check these against the BNF interaction guidance.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no study tests famciclovir for postherpetic neuralgia. The only linked trial examines oxycodone, and no publications support the link. Evidence is at model-prediction level.

**To proceed, the following is needed:**
- Clinical data on famciclovir for preventing or treating postherpetic neuralgia (for example, a randomised trial or a systematic review of existing zoster antiviral trials with neuralgia outcomes)
- Mechanism of action data to support the analysis
- Approved indication text, dosage form and SmPC warnings and contraindications for the UK authorisation
- Classification of the interaction severity for the 84 potential interactions
- Renal safety review for patients with kidney disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

