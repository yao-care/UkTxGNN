---
layout: default
title: Fenoprofen
parent: Model Prediction Only (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fenoprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis"
monitor_inn: "Fenoprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "pseudoachondroplasia", "spondyloarthropathy, susceptibility to", "WHIM syndrome", "ankylosing spondylitis"]
---

# Fenoprofen
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

# Fenoprofen: From Rheumatoid Arthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Fenoprofen is a non-steroidal anti-inflammatory drug (NSAID) used for rheumatoid arthritis and osteoarthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
There are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on the computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis (the UK authorisation record has no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available for this report. Fenoprofen is known to be a non-selective cyclooxygenase (COX-1 and COX-2) inhibitor. It reduces prostaglandin-mediated inflammation and pain, and its efficacy in inflammatory joint disease is well established.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare skeletal dysplasia caused by loss-of-function variants in the *CDMP1/GDF5* gene, which disrupt cartilage and bone development. Fenoprofen does not act on this pathway, and an anti-inflammatory drug would not be expected to correct a developmental defect in chondrogenesis.

The high score most likely reflects shared skeletal and joint features in the knowledge graph rather than a true biological link. The prediction should therefore be treated as a hypothesis-generating signal with no supporting mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010G0AAABAB | Fenoprofen Tab 300 mg | Tablet | Not recorded |

This authorisation number is not in the standard MHRA "PL" format, so the record should be checked against the MHRA register before use. Current NICE appraisals or BNF classification for this product should also be checked directly.

## Safety Considerations

**Contraindications and cautions suggested by the knowledge graph.** These come from drug-disease relationships in the TxGNN knowledge graph, not from product label text, and need confirming against the SmPC. The main groupings are:
- **Cardiovascular and cerebrovascular:** hypertension, congestive heart failure, myocardial infarction, coronary thrombosis, stroke, cerebral infarction, thrombotic disease and general cardiovascular or heart disease.
- **Renal:** kidney disease, kidney papillary necrosis and acute papillary necrosis.
- **Gastrointestinal and hepatic:** active peptic ulcer disease and drug-induced liver injury.
- **Haematological:** blood coagulation disease, anaemia (including macrocytic anaemia) and haemoglobinopathy.
- **Sensory:** vision disorder, blindness, hearing disorder and auditory system disease.
- **Other:** substance abuse or dependence, and pyoureter.

**Drug interactions.** The interaction screening returned 100 interactions in total, of which 20 were available for review. Most are Moderate, with some Minor.
- **Moderate:** acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), metformin, sulfonylureas (chlorpropamide, glimepiride), mesalazine, balsalazide, potassium citrate and bicarbonate, and bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate).
- **Minor:** H2-receptor antagonists (famotidine, ranitidine, cimetidine) and linaclotide.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, literature or mechanistic support. It conflicts with the underlying biology of a genetic skeletal disorder, and it is probably an artefact of the graph. The knowledge-graph safety signals in cardiovascular, renal and gastrointestinal disease would also need careful weighing in any new patient group.

**To proceed, the following is needed:**
- A plausible biological rationale linking COX inhibition to *GDF5*-related skeletal development, supported by preclinical data
- Mechanism of action data for fenoprofen
- Confirmation of the UK authorisation record, including the approved indication text, dosage form and SmPC safety information

**Note on other predictions:** Of the ten top-ranked predictions for fenoprofen, only **ankylosing spondylitis** (model rank 10, score 99.94%) has any supporting literature. This includes two small double-blind cross-over trials from 1980 and a 1981 randomised comparison of NSAIDs. It is classed as L3 with a "Research Question" recommendation. However, it is a symptomatic extension within the NSAID class rather than true repurposing, and well-established alternatives exist. If a lead indication is wanted for further assessment, this is the more defensible candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

