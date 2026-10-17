---
layout: default
title: Nabumetone
parent: Model Prediction Only (L5)
nav_order: 430
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nabumetone: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, arthropathy"
monitor_inn: "Nabumetone"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "spondyloarthropathy, susceptibility to", "WHIM syndrome", "rheumatoid nodulosis"]
---

# Nabumetone
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

# Nabumetone: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Nabumetone is a non-steroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis, osteoarthritis and related joint disease.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type** (a rare genetic skeletal disorder), but there are currently **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, arthropathy (the licence record held no indication text; these come from the TxGNN knowledge graph) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Nabumetone is understood to be a COX-2-preferential NSAID that reduces prostaglandin-mediated inflammation and pain. Its use in rheumatoid arthritis and osteoarthritis is established.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare genetic skeletal dysplasia caused by loss-of-function mutations in *CDMP1/GDF5*. Nabumetone has no known interaction with the GDF5/BMP signalling pathway. The high score most likely reflects the disease's proximity to musculoskeletal and arthropathy terms in the knowledge graph rather than a causal mechanism. At most, an NSAID might give symptomatic pain relief, not modify the disease.

Of the ten predictions reviewed, the most biologically coherent are indirect and symptomatic:
- **Spondyloarthropathy, susceptibility to** (score 99.94%, L4): NSAIDs are first-line therapy for spondyloarthritis, but the evidence is class-level, not specific to nabumetone, and "susceptibility" denotes a genetic risk entity rather than an active disease.
- **Rheumatoid nodulosis** (score 99.93%, L4): a variant of rheumatoid disease, so symptom control is plausible, but NSAIDs do not alter nodule formation.
- **Pseudoachondroplasia** (score 99.98%, L5): early-onset osteoarthritis could be eased symptomatically, with no evidence of disease modification.

The remaining predictions (brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachyolmia, brachydactyly-syndactyly syndrome, WHIM syndrome) have no plausible mechanistic link to COX inhibition.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010X0AAAAAA | Nabumetone Tab 500mg | Tablet (inferred from the product name) | Not available in the data compiled for this report |

Only one valid single-ingredient authorisation is recorded. The identifier does not follow the usual MHRA "PL XXXXX/XXXX" format, so the entry should be checked against the MHRA product database before being relied on.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug-disease links, not label text): hypertension, kidney disease, liver disease, gallbladder disease, peptic ulcer disease (including active), substance abuse/dependence, blood coagulation disease, myocardial infarction, coronary thrombosis, haemoglobinopathy, cardiovascular disease and heart disease. These are consistent with known NSAID class concerns (gastrointestinal, cardiovascular, renal and bleeding risks) and must be confirmed against the SmPC.
- **Drug interactions** (100 recorded; most relevant shown):
  - Moderate: acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), metformin, sulfonylureas (glimepiride, chlorpropamide), mesalazine, balsalazide, potassium citrate, potassium bicarbonate, vancomycin, and bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate).
  - Minor: ranitidine, cimetidine, linaclotide.
- **Pregnancy and development:** NSAIDs are generally avoided in pregnancy, which complicates any rationale for developmental syndromes.
- **Additional risk:** in WHIM syndrome, NSAID-related platelet and gastrointestinal effects would add risk without a mechanistic benefit.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is supported only by a model score, with no clinical trials, no literature and no plausible mechanistic link to nabumetone. The high score most likely reflects graph proximity rather than biology, and the drug carries recognised NSAID safety risks.

**To proceed, the following is needed:**
- Mechanism of action data for nabumetone
- Label warnings and contraindications from the SmPC and BNF, and the approved indication text and dosage form for the UK authorisation
- For the two L4 candidates (spondyloarthropathy, rheumatoid nodulosis), a search for nabumetone-specific trials and literature, which may justify treating them as research questions
- For pseudoachondroplasia, consideration of a research question on symptomatic NSAID use for secondary arthropathy pain
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

