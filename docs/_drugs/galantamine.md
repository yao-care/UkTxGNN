---
layout: default
title: Galantamine
parent: Model Prediction Only (L5)
nav_order: 310
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Galantamine: predicted new indication Psychogenic movement disorders (evidence level L5). Approved use: Alzheimer's disease"
monitor_inn: "Galantamine"
predicted_indications: ["psychogenic movement disorders", "chronic tic disorder", "primary orthostatic tremor", "benign shuddering attacks", "extrapyramidal and movement disease", "tremor-nystagmus-duodenal ulcer syndrome", "lingual-facial-buccal dyskinesia", "benign paroxysmal tonic upgaze of childhood with ataxia", "acute intermittent porphyria"]
---

# Galantamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Galantamine: From Alzheimer's Disease to Psychogenic Movement Disorders
{: .text-alpha }

## One-Sentence Summary

Galantamine is a cholinesterase inhibitor originally used to treat Alzheimer's disease.
The TxGNN model predicts it may be effective for **psychogenic movement disorders**, but **no clinical trials and no publications** currently support this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease (the UK licence record holds no indication text, so this comes from the knowledge-graph indication list) |
| Predicted New Indication | Psychogenic movement disorders |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Galantamine is known as an acetylcholinesterase inhibitor and an allosteric modulator of nicotinic acetylcholine receptors. By raising cholinergic signalling in the brain, it may alter the balance between cholinergic and dopaminergic activity in circuits that control movement. Detailed mechanism-of-action data were not available for this report, so this description draws on general pharmacology and on the abstracts of the literature compiled for the drug's other predicted indications.

The link to psychogenic movement disorders is speculative. These conditions are functional in nature, and no data compiled for this report connect cholinergic modulation to their pathophysiology or treatment. The high TxGNN score reflects network-based similarity in the knowledge graph, not demonstrated clinical benefit. Treat the prediction as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name |
|---------|------|
| 0411000F0AAABAB | Galantamine tablets 8 mg |

The record for this product holds no dosage form, manufacturer or approved indication text. The number is not in the MHRA "PL" format, so the authorisation should be verified against the MHRA register and the BNF entry before any further work.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are graph associations, not label text): familial long QT syndrome, atrioventricular block, liver failure and liver disease, kidney disease, epilepsy, asthma (including intrinsic and allergic forms), chronic obstructive pulmonary disease, peptic ulcer disease, duodenal ulcer, gallbladder disease, bladder neck obstruction and pyoureter.
- **Drug interactions:** 100 interactions were recorded, and the 20 reviewed here included one major and 19 moderate.
  - **Major:** bupropion.
  - **Moderate, anticholinergic agents (pharmacodynamic opposition expected):** atropine, hyoscyamine, glycopyrronium, dicyclomine, clidinium and trospium.
  - **Moderate, others:** the H2 antagonists famotidine, ranitidine and cimetidine, as well as clarithromycin, metronidazole, loperamide, dolasetron, palonosetron, eliglustat, lorcaserin, picosulfuric acid, polyethylene glycol with electrolytes, and sodium sulfate.
- **Movement-disorder signal:** a 2025 systematic review (PMID 40224553) examined movement disorders associated with cholinesterase inhibitors in Alzheimer's dementia. This suggests galantamine could worsen or induce some movement disorders rather than treat them.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials, no publications and no established mechanistic link. Related literature raises the possibility that cholinesterase inhibitors may aggravate movement disorders.

**To proceed, the following is needed:**
- Any clinical or preclinical evidence linking cholinergic modulation to psychogenic movement disorders.
- Confirmed mechanism-of-action data and a verified MHRA authorisation record, including SmPC warnings and contraindications.
- A safety assessment covering cardiac conduction, the interactions above and the possible worsening of movement disorders.

**Note on other predictions from the same analysis:**
- Among the other predicted indications, the best-supported is **lingual-facial-buccal dyskinesia** (tardive dyskinesia). It has a randomised, placebo-controlled crossover trial of galantamine in tardive dyskinesia (PMID 17388711) and several Cochrane reviews and meta-analyses of cholinergic drugs (for example PMIDs 29553158 and 15610922). Their findings for galantamine specifically are not established from the data compiled here. It is better treated as a research question for a separate evaluation than as support for the psychogenic movement disorders prediction.
- The remaining predictions have no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

