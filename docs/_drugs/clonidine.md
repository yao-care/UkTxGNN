---
layout: default
title: Clonidine
parent: Model Prediction Only (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Clonidine: predicted new indication Faciodigitogenital syndrome (evidence level L5). Approved use: Hypertension, open-angle glaucoma, ADHD"
monitor_inn: "Clonidine"
predicted_indications: ["faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "trichotillomania", "Tourette syndrome", "obesity disorder", "hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "migraine disorder", "manic bipolar affective disorder"]
---

# Clonidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Clonidine: From Hypertension to Faciodigitogenital Syndrome

## One-Sentence Summary

Clonidine is an alpha-2 adrenergic agonist originally used for hypertension, open-angle glaucoma and attention deficit hyperactivity disorder (ADHD).
The TxGNN model predicts it may be effective for **faciodigitogenital syndrome**, a rare genetic developmental syndrome.
There are **no clinical trials** and **no publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, open-angle glaucoma, ADHD (from the knowledge-graph indication records; the licence text in the compiled data is blank) |
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 99.999% (model rank 34) |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Clonidine is an alpha-2 adrenergic agonist that reduces noradrenergic tone, and its efficacy in hypertension and ADHD is established.

On the evidence available, **the prediction is not mechanistically supported**. Faciodigitogenital syndrome is a rare genetic developmental disorder, and alpha-2 adrenergic agonism has no known link to its pathophysiology. The score is very high (0.99999), but with no trials and no literature it is most likely an artefact of the knowledge graph rather than a genuine repurposing signal.

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
| 0205020E0AAACAC (as recorded; a BNF-style product code rather than a PL number) | Clonidine HCl Tab 100mcg | Tablet (taken from the product name) | Not stated in the data compiled |

This is a single-ingredient product with valid status. The compiled data give no indication text, so check the current SmPC and BNF entry for the licensed indications.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** The TxGNN knowledge graph links clonidine to a number of conditions as potential contraindications. They should be checked against the SmPC before any use. Examples:
  - Cardiovascular: hypotensive disorder, myocardial infarction, myocardial ischaemia, heart conduction disease, sudden cardiac arrest
  - Metabolic and endocrine: type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, gout, hypercalcaemia
  - Organ-related and other: liver failure, anuria, respiratory failure, pancreatitis, systemic lupus erythematosus, anxiety disorder
- **Drug interactions:** The interaction screen returned 100 interactions. The 20 shown were all of moderate severity, mainly:
  - corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
  - glucose-lowering drugs (SGLT2 inhibitors, sulfonylureas, insulins)
  - others, such as bupropion, morphine and dronabinol

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support, no identifiable mechanistic link, and the condition is a rare genetic syndrome unrelated to clonidine's pharmacology. It is best treated as a likely computational artefact.

**To proceed, the following is needed:**
- Any human or credible preclinical evidence linking alpha-2 agonism to this syndrome
- Detailed mechanism of action data
- Label-based warnings and contraindications from the SmPC

**Note:** Other predicted indications for clonidine in the same dataset have more support. Tourette syndrome has guideline and meta-analysis backing and is closer to established off-label use. Obesity-related hypertension, migraine and mania have limited, mostly small studies. These would be better starting points for any repurposing work.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

