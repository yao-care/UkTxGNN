---
layout: default
title: Nicotinamide
parent: Model Prediction Only (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nicotinamide: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Acne, pellagra, beriberi"
monitor_inn: "Nicotinamide"
predicted_indications: ["zinc, elevated plasma", "isolated congenital adermatoglyphia", "Beare-Stevenson cutis gyrata syndrome", "Werner syndrome", "pyogenic arthritis-pyoderma gangrenosum-acne syndrome", "demodicidosis of sebaceous gland", "dyspepsia", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "inherited cutis laxa", "syndromic oculocutaneous albinism"]
---

# Nicotinamide
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

# Nicotinamide: From Acne to Elevated Plasma Zinc

## One-Sentence Summary

Nicotinamide (vitamin B3) is used for acne and for niacin-deficiency conditions such as pellagra.
The TxGNN model predicts it may be effective for **elevated plasma zinc** with a high score, but there are **0 registered clinical trials** and only **2 loosely related publications**, neither of which tests nicotinamide against zinc levels. The prediction rests on model output alone.

> Note: the data compiled for this report show that the more credible repurposing signal among the model's top ten predictions is **Werner syndrome** (a randomised trial of the related compound nicotinamide riboside). It is described under "Why is This Prediction Reasonable?" and in the conclusion.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, pellagra, beriberi (from the knowledge graph; no approved indication text is available for the UK product) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 97.83% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Nicotinamide is the amide form of vitamin B3 and a precursor of NAD+, a cofactor central to cellular redox balance and energy metabolism. Its efficacy in deficiency states (pellagra) and in acne, where anti-inflammatory activity is thought to contribute, is established.

For **elevated plasma zinc**, no biological rationale links nicotinamide to zinc handling. The two retrieved papers cover COVID-19 metabolic and thrombotic risk factors and antioxidant enzymes in hypertensive rat kidney. Neither tests nicotinamide's effect on zinc levels. Any connection would be indirect, through general redox or metabolic pathways, and is speculative. The high model score should therefore be read with caution.

**Other predictions of note (for context):**

- **Werner syndrome** (score 88.6%, evidence level L2): Werner syndrome is a rare progeroid disorder in which NAD+ depletion and impaired mitophagy are reported. Preclinical studies show NAD+ augmentation restores mitophagy and limits accelerated-ageing features. A 2025 double-blind, randomised crossover placebo-controlled trial tested **nicotinamide riboside**, a related NAD+ precursor, not nicotinamide itself. The trial is not registered in the data provided, so phase and size are unconfirmed, and a small sample is likely given the rarity of the disease. This is the strongest mechanistic and clinical signal among the predictions.
- **Mitochondrial oxidative phosphorylation disorders** (score 84.7%, L4): plausible through NAD+ biosynthesis, but supported only by indirect reviews and mechanistic papers.
- **Pyogenic arthritis-pyoderma gangrenosum-acne (PAPA) syndrome** and **demodicidosis of sebaceous gland**: probably driven by overlap with acne; no supporting evidence.
- **Dyspepsia**: the retrieved literature is off-target, and gastrointestinal upset is a known adverse effect of high-dose niacin-related compounds, so the direction of effect may be opposite.
- Isolated congenital adermatoglyphia, Beare-Stevenson cutis gyrata syndrome, inherited cutis laxa and syndromic oculocutaneous albinism: prediction only, with no trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for elevated plasma zinc.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32938758](https://pubmed.ncbi.nlm.nih.gov/32938758/) | 2020 | Review | Open Heart | Discusses hyperinsulinaemia, magnesium, vitamin D and thrombosis in COVID-19; does not examine nicotinamide and zinc levels |
| [15361776](https://pubmed.ncbi.nlm.nih.gov/15361776/) | 2004 | Preclinical (animal) | Journal of Hypertension | Antioxidant enzymes in the kidneys of spontaneously hypertensive rats on an antioxidant-rich diet; not relevant to plasma zinc |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1306010N0AAAAAA | Nicotinamide Gel 4% | Topical gel (per product name) | Not stated in the data compiled for this report |

The identifier shown is a BNF-style product code rather than a standard MHRA "PL" number, and no manufacturer or indication text was available. Please check the MHRA product listing and the BNF before relying on this entry.

---

## Safety Considerations

**Knowledge-graph contraindication signals** (derived from drug-disease links in the knowledge graph, not from label text, so they should be checked against the SmPC and BNF):

- Kidney, liver and gallbladder disease
- Peptic ulcer disease
- Diabetes mellitus and diabetic ketoacidosis
- Gout
- Blood coagulation disease and haemophilia
- Acute coronary syndrome and hypotensive disorder
- Thyroid disease (including goitre and Hashimoto thyroiditis)
- Iron-metabolism disorders (hereditary haemochromatosis, haemosiderosis) and Wilson disease
- Sickle cell anaemia, rhabdomyolysis, primary hyperoxaluria, dermatitis herpetiformis, bronchitis and others

**Drug interactions:** 64 interactions were identified. The ones listed below are from the first 20 returned, and all are rated Moderate except carbamazepine (Minor):

- Antidiabetic agents: metformin, pioglitazone, chlorpropamide, acarbose, and the DPP-4 inhibitors, SGLT2 inhibitors and GLP-1 agonists alogliptin, linagliptin, canagliflozin, dapagliflozin, empagliflozin, albiglutide and dulaglutide
- Antineoplastics: methotrexate, clofarabine, brentuximab vedotin, and asparaginase products
- Others: efavirenz, cannabidiol, carbamazepine (Minor)

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication of elevated plasma zinc has no trials, no relevant literature and no plausible mechanism, so it rests on model output alone (L5). The Werner syndrome prediction is worth exploring separately as a research question, but its trial used nicotinamide riboside rather than nicotinamide.

**To proceed, the following is needed:**
- Mechanism of action data for nicotinamide, and any evidence linking it to zinc metabolism
- SmPC warnings and contraindications for the UK product, and confirmation of its MHRA authorisation number, dosage form and indication
- For Werner syndrome: full review of the 2025 nicotinamide riboside RCT, a check on whether nicotinamide itself has been tested, and a comparison of the safety and pharmacology of the two NAD+ precursors
- A review of the knowledge-graph contraindication signals against the label before any new-use proposal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

