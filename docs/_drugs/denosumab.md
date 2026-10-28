---
layout: default
title: Denosumab
parent: Model Prediction Only (L5)
nav_order: 214
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Denosumab: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Osteoporosis (including postmenopausal and drug-induced osteoporosis)"
monitor_inn: "Denosumab"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Denosumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Denosumab is a RANKL-neutralising monoclonal antibody, originally used to treat osteoporosis, including postmenopausal and drug-induced osteoporosis.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but this is a model prediction only, with **no clinical trials** and **no publications** supporting it directly.
A closely related prediction, **diabetic retinopathy**, has **2 publications**, neither of which tests denosumab in this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (including postmenopausal and drug-induced osteoporosis) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Denosumab is a monoclonal antibody that neutralises RANKL. In osteoporosis, this reduces bone resorption. Detailed mechanism of action data are not available in the data compiled for this report, so the following reasoning is hypothetical.

One plausible but unverified link is that RANKL/RANK/OPG signalling may influence vascular inflammation, endothelial dysfunction and vascular calcification. These processes are relevant to diabetic microvascular disease. No retinal-specific evidence was identified, so this link is speculative.

The original indication (bone metabolism) and the predicted indication (diabetic eye disease) are not closely related. The similarity between them has not been assessed. The very high TxGNN score reflects a model-derived association, not clinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No publications were found for severe nonproliferative diabetic retinopathy. For the broader **diabetic retinopathy** prediction (score 0.9923), two publications were identified. Neither tests denosumab as a treatment for retinopathy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Likely observational cohort with systematic review and meta-analysis (design not confirmed) | Diabetes, Obesity & Metabolism | In osteoporosis patients, denosumab was associated with a lower incidence of type 2 diabetes, less foot ulceration and lower all-cause mortality than bisphosphonates. The study also examined microvascular outcomes (including retinopathy), but the retinopathy result cannot be confirmed from the available data. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Likely observational or cross-sectional (design not confirmed) | Cureus | Evaluated use of the FRAX fracture risk tool in adults with type 2 diabetes. Unrelated to retinopathy treatment. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0606020Z0AAAAAA (BNF-style code) | Denosumab injection 60 mg/1 mL pre-filled syringe | Not specified | Not specified |

The identifier above looks like a BNF classification code, not a standard MHRA PL number. Authorisation details should be checked against the MHRA register.

---

## Safety Considerations

- **Drug Interactions:** 100 potential interactions were identified in the interaction database. The entries listed are all of moderate severity. Examples include:
  - Corticosteroids: hydrocortisone, prednisolone, prednisone, methylprednisolone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Immunosuppressants and immunomodulators: tacrolimus, mercaptopurine, dupilumab, levamisole
  - Radiopharmaceuticals and related agents: ibritumomab tiuxetan, tositumomab, iobenguane (I-131)
  - Corticotropin and tetracosactide

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no registered trials, and the two publications identified do not test denosumab in diabetic retinopathy. The mechanistic link is speculative, so the evidence does not support repurposing at this stage.

**To proceed, the following is needed:**
- Full-text review of PMID 38899553 to determine whether retinopathy was an outcome and what the result was
- Mechanism of action data and preclinical evidence for RANKL/RANK/OPG involvement in retinal disease
- Safety review based on the SmPC and BNF, as warnings and contraindications were not available for this report
- Confirmation of MHRA authorisation details, including licence number, dosage form and approved indication
- Assessment of route compatibility, as intravitreal and systemic delivery have not been evaluated
- Any registered or planned clinical studies in diabetic retinopathy, to move beyond L5 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

