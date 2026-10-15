---
layout: default
title: Duloxetine
parent: Model Prediction Only (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
---

# Duloxetine
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

# Duloxetine: From Major Depressive Disorder to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Duloxetine is an antidepressant used for depressive and anxiety disorders, fibromyalgia and female stress incontinence.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (the data compiled for this report does not include UK licensed indication text, so this is taken from the knowledge graph, which also lists anxiety disorder, fibromyalgia, myofascial pain syndrome and female stress incontinence) |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI). Its efficacy in depression and anxiety is established, but there is no data supporting a mechanistic link to this predicted condition.

Benign paroxysmal torticollis of infancy is a paediatric, migraine-related condition associated with *CACNA1A* (a calcium channel gene). No plausible duloxetine mechanism is supported by the data compiled for this report. The high score (0.998) reflects graph-based proximity only and should be treated as a hypothesis, not evidence. The safety of duloxetine in infants has also not been established.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0403040Y0AAAAAA (appears to be a BNF-style classification code rather than a PL number) | Duloxetine HCl gastro-resistant capsules 30 mg | Capsule (gastro-resistant) | Not available in the compiled data |

Duloxetine falls under BNF section 4.3 (antidepressant drugs). The compiled data does not include NICE-appraised indications.

## Safety Considerations

- **Contraindications and warnings from label text:** not available in the compiled data. Please refer to the SmPC and BNF.
- **Conditions linked to duloxetine by knowledge-graph contraindication edges (not label text):** hypertension, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, epilepsy, bipolar disorder, liver disease (including cirrhosis, fatty liver disease and hepatitis), gallbladder disease, hyperglycaemia, substance abuse/dependence, blood coagulation disease, angle-closure glaucoma, neuroleptic malignant syndrome, serotonin syndrome and syndrome of inappropriate ADH secretion. These need verification against the SmPC.
- **Drug interactions:** 100 interactions are recorded, and 20 were reviewed here.
  - **Major:** bupropion, lorcaserin, diethylpropion, dolasetron and dexfenfluramine.
  - **Moderate:** epinephrine, morphine, acetylsalicylic acid, cimetidine, picosulfuric acid, polyethylene glycol (3350 with electrolytes), difenoxin, diphenoxylate and dronabinol.
  - **Minor:** famotidine, ranitidine, rabeprazole, dexlansoprazole, aluminium hydroxide and calcium carbonate.

Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN graph score alone, with no trials, no publications and no plausible mechanism. It also involves an infant population in which duloxetine safety is unestablished.

**To proceed, the following is needed:**
- Mechanistic evidence linking duloxetine to the pathophysiology of this condition
- Any preclinical or clinical data in paediatric migraine-related or channelopathy disorders
- Paediatric safety and dosing data
- Full SmPC warnings and contraindications

**Note on other predictions:** Among the other predicted indications, **obsessive-compulsive disorder** (score 99.84%) has the strongest support in the compiled data, at evidence level L2. This includes a double-blind augmentation trial in resistant OCD (PMID 27811556), an open-label study (PMID 25637377) and a completed Phase 4 trial (NCT00464698). Evidence is limited by small samples and the absence of a Phase 3 RCT. Agoraphobia has only open-label panic disorder data. OCD may merit a separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

