---
layout: default
title: Cycloserine
parent: Model Prediction Only (L5)
nav_order: 196
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cycloserine: predicted new indication Irritable bowel syndrome (evidence level L5). Approved use: Pulmonary tuberculosis"
---

# Cycloserine
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

# Cycloserine: From Pulmonary Tuberculosis to Irritable Bowel Syndrome

## One-Sentence Summary

Cycloserine is a second-line antibiotic originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **irritable bowel syndrome**, but this is a model prediction only, with **no clinical trials** and **no relevant publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis (taken from the knowledge-graph indication record, as no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cycloserine is a D-alanine analogue that inhibits bacterial cell wall synthesis, which explains its use in drug-resistant tuberculosis. It also acts as a partial agonist at the NMDA receptor in the central nervous system.

Neither property offers a clear link to irritable bowel syndrome (IBS). Any effect through the gut microbiome would be speculative, and the data compiled for this report do not support a plausible mechanism. The high TxGNN score most likely reflects patterns in the knowledge graph rather than a demonstrated therapeutic rationale, so it should be treated as a hypothesis only.

Other predicted indications were also reviewed. All remain at L5 with a recommendation of Hold:

| Predicted Indication | TxGNN Score | Comment |
|------|------|------|
| Acne | 99.91% | An antibacterial effect is conceivable, but neuropsychiatric toxicity makes the risk-benefit balance unfavourable against established treatments |
| Gastroparesis | 99.66% | No mechanistic rationale evident |
| Conjunctivitis | 99.27% | Only a 1963 general review of antibiotics; topical agents are the usual choice |
| Insomnia | 99.21% | Literature shows cycloserine can *cause* insomnia and psychosis, which is the opposite of a therapeutic signal |
| Pharyngitis | 99.01% | No supporting data |
| Nasal cavity disease | 99.01% | One unrelated rhinosporidiosis case report |
| Acute laryngopharyngitis | 98.85% | No supporting data |
| Postgastrectomy syndrome | 98.79% | No supporting data |
| Rhinitis | 98.70% | No supporting data |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for irritable bowel syndrome.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501090E0AAABAB (BNF-style product code, not a PL number) | Cycloserine capsules 250 mg | Capsule | Not available in the compiled data |

The BNF classification code (section 5.1.9, antituberculosis drugs) is consistent with its use in tuberculosis.

## Safety Considerations

- **Conditions flagged in the knowledge graph as contraindications** (derived from the knowledge graph, not from label text): epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, pyoureter, psychotic disorder, schizophreniform disorder, mental disorder, schizoaffective disorder, substance abuse/dependence, vitamin B12 deficiency, megaloblastic anaemia and sideroblastic anaemia.
- **Drug interactions** (11 recorded):
  - **Major:** bupropion, ethanol, iohexol, iopamidol
  - **Moderate:** picosulfuric acid, polyethylene glycol 3350 with electrolytes, sodium sulfate, caffeine, dicoumarol, warfarin, lindane
- **Neuropsychiatric effects:** a 2022 case report describes cycloserine-induced insomnia and psychosis during treatment of multidrug-resistant tuberculosis.

Label-based warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials, no supporting literature and no plausible mechanistic link to irritable bowel syndrome. The known neuropsychiatric toxicity and the long list of knowledge-graph contraindications make the risk-benefit balance unfavourable for a non-life-threatening condition such as IBS.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale linking cycloserine to IBS
- Preclinical or early-phase clinical evidence of benefit
- SmPC-based warnings and contraindications (the safety screening could not be completed without them)
- The approved indication text and dosage form for the UK authorisation
- A risk-benefit assessment against established IBS therapies, including a plan for monitoring neuropsychiatric adverse effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

