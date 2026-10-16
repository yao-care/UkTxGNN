---
layout: default
title: Degarelix
parent: Model Prediction Only (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Degarelix: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not stated in the available authorisation data"
monitor_inn: "Degarelix"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "malformation syndrome with odontal and/or periodontal component", "isolated genetic hair shaft abnormality", "allergic urticaria", "cold urticaria", "familial male-limited precocious puberty", "centra precocious puberty 1", "familial isolated trichomegaly"]
---

# Degarelix
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

# Degarelix: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Degarelix is a gonadotropin-releasing hormone (GnRH) receptor antagonist, with a UK marketing authorisation on record but no approved indication text in the data compiled for this report.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **no registered clinical trials** and **no publications** supporting this direction.
This is a model-only prediction with a weak mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available authorisation data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Degarelix is known as a GnRH receptor antagonist: it blocks pituitary GnRH receptors, reducing LH and FSH release and therefore gonadal androgen production.

The link to hypertrichosis is weak. Hypertrichosis is generally not androgen-driven (unlike hirsutism), so suppressing gonadal hormones is not an established way to treat it. The high TxGNN score reflects graph-based network proximity only, with no supporting trials or literature.

Other top-ranked predictions are similarly unsupported. Examples are Ambras-type hypertrichosis universalis congenita, a Dandy-Walker malformation syndrome, isolated hair shaft abnormalities, and urticaria. Only **central precocious puberty** (score 99.67%) is biologically coherent, because GnRH suppression is its established principle of treatment. Even there, no paediatric data exist for degarelix. Practical barriers include the depot formulation and injection-site reactions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0803042R0AAAAAA | Degarelix injection 80 mg vial + diluent | Injection (powder and solvent) | Not stated in the available data |

The data compiled for this report list one valid single-ingredient authorisation. It does not give a PL number, manufacturer or indication text. Please verify details against the MHRA register, the SmPC and the BNF.

---

## Safety Considerations

- **Disease associations flagged by the knowledge graph** (not taken from label text): long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease, gallbladder disease and potassium deficiency disease. These should be checked against the SmPC.
- **Drug Interactions** (100 interactions recorded; main ones shown):
  - **Major:** cisapride and dolasetron (consistent with QT-prolongation concerns).
  - **Moderate:** clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron, famotidine, loperamide, and several laxatives and bowel-preparation agents (bisacodyl, picosulfuric acid, lactulose, lactitol, magnesium citrate, magnesium hydroxide, polyethylene glycol with electrolytes, castor oil, glycerin, mineral oil).
  - **Minor:** metronidazole.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no trials, no literature and a weak mechanistic link to hypertrichosis. Safety data from the product label were also not available for this assessment.

**To proceed, the following is needed:**
- Confirmation of the licensed indication and product details from the MHRA register and SmPC
- Label-based warnings and contraindications, including QT-related risk
- Mechanism of action data
- Preclinical or observational evidence for any androgen-independent role in hair growth
- Consideration of **central precocious puberty** as a separate research question, since it is the most biologically plausible prediction, with paediatric safety and formulation feasibility to be established first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

