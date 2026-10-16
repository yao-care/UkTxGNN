---
layout: default
title: Esomeprazole
parent: Moderate Evidence (L3-L4)
nav_order: 257
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
description: "Esomeprazole: predicted new indication Duodenogastric reflux (evidence level L4). Approved use: Peptic ulcer disease, GORD, oesophagitis, Zollinger-Ellison syndrome"
monitor_inn: "Esomeprazole"
predicted_indications: ["duodenogastric reflux", "duodenal obstruction", "duodenal ulcer (disease)"]
---

# Esomeprazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Esomeprazole: From Acid-Related Upper GI Disorders to Duodenogastric Reflux

## One-Sentence Summary

Esomeprazole is a proton pump inhibitor, originally used for acid-related conditions such as peptic ulcer disease and gastro-oesophageal reflux disease (GORD).
The TxGNN model predicts it may be effective for **duodenogastric reflux** (bile reflux into the stomach), but there are currently **no registered clinical trials** and only **1 general review article** supporting this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, GORD, oesophagitis, Zollinger-Ellison syndrome (the UK licence record has no indication text, so these come from the knowledge-graph indication list) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Esomeprazole suppresses gastric acid by irreversibly blocking the H+/K+-ATPase (proton pump) in gastric parietal cells. Detailed mechanism of action data were not available in the compiled data. The mechanism above is the established class action of proton pump inhibitors.

In duodenogastric reflux, bile and pancreatic secretions flow back into the stomach. Acid suppression may ease symptoms where acid-related mucosal injury coexists. It does not treat the underlying cause, which is usually pyloric or motility dysfunction. The mechanistic link is therefore plausible but indirect.

The very high TxGNN score most likely reflects closeness in the knowledge graph to approved acid-related indications such as GORD and peptic ulcer. It is not disease-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for duodenogastric reflux.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | General update on proton pump inhibitors, which are first-choice drugs for peptic ulcer, H. pylori infection, GORD, NSAID-related GI lesions and Zollinger-Ellison syndrome. It does not address duodenogastric reflux directly. |

---

## UK Market Information

| Reference Code | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0103050E0AAAAAA | Esomeprazole gastro-resistant (E/C) tablets 20 mg | Tablet | Not specified in the compiled record |

The compiled data list one valid single-ingredient authorisation. The reference code is not in the usual PL number format, and the indication text was not captured. Please check the current SmPC and BNF (section 1.3.5, proton pump inhibitors) for licensed indications.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug–disease links, not label text): liver failure, osteoporosis, postmenopausal osteoporosis, bone fracture and chronic atrophic gastritis. These need verifying against the SmPC.
- **Drug Interactions**: The interaction screen found 100 potential interactions, and the first 20 returned are summarised here.
  - **Major**: acalabrutinib, atazanavir.
  - **Moderate** (examples): hydrochlorothiazide, amphotericin B, amikacin, amphetamine, fenofibrate, apalutamide, armodafinil, atorvastatin, bendamustine, bosutinib, bumetanide.
  - **Minor** (examples): acetylsalicylic acid, axitinib, bortezomib, brivaracetam, cyanocobalamin.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model proximity to approved acid-related indications. There are no trials and no disease-specific literature. Esomeprazole would at best relieve coexisting acid-related symptoms and would not treat bile reflux itself.

**To proceed, the following is needed:**
- Clinical studies, or at least observational data, of PPIs in duodenogastric (bile) reflux
- Clear definition of the target outcome (symptom relief versus mucosal protection)
- Mechanism of action data and verified SmPC safety information
- Confirmation of the licensed indications for the UK authorisation

**Note:** A related prediction in the same analysis, **duodenal ulcer** (TxGNN score 99.40%), has far stronger support. It has several completed Phase 3 RCTs and supportive H. pylori trials, giving an evidence level of L1 and a "Proceed with Guardrails" recommendation. It is closely related to esomeprazole's existing peptic ulcer indication, so it is largely an established use rather than true repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

