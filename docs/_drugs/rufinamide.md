---
layout: default
title: Rufinamide
parent: Model Prediction Only (L5)
nav_order: 558
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Rufinamide: predicted new indication Febrile infection-related epilepsy syndrome (evidence level L5). Approved use: Lennox-Gastaut syndrome"
monitor_inn: "Rufinamide"
predicted_indications: ["perioral myoclonia with absences", "trigeminal nerve neoplasm", "renal-hepatic-pancreatic dysplasia"]
---

# Rufinamide
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

## Rufinamide: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome
{: .text-alpha }

## One-Sentence Summary

Rufinamide is an antiseizure medication, originally used as add-on treatment for seizures in Lennox-Gastaut syndrome.
The TxGNN model predicts it may be effective for **febrile infection-related epilepsy syndrome (FIRES)**,
but **no clinical trials and no publications** were found for this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lennox-Gastaut syndrome |
| Predicted New Indication | Febrile infection-related epilepsy syndrome |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Published reviews describe rufinamide as a triazole derivative thought to prolong the inactive state of voltage-gated sodium channels, which limits repetitive neuronal firing. Its efficacy in Lennox-Gastaut syndrome, a severe drug-resistant epileptic encephalopathy, is established.

FIRES is also a severe, drug-resistant epilepsy. It follows a febrile illness and causes frequent, prolonged seizures. A drug that suppresses seizure activity in refractory epileptic encephalopathies could plausibly help control FIRES seizures. This is the main basis for the prediction.

There are two important limits. First, FIRES is driven largely by neuroinflammation, which rufinamide does not address. At best it would offer symptomatic seizure control. Second, the link rests on the model score alone, with no direct clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Reference Code | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0408010AFAAABAB (BNF-style code; PL number not provided) | Rufinamide 200 mg tablets | Tablet | Not stated in the data compiled; BNF chapter 4.8.1 (antiepileptic drugs) |

Only one authorisation (single-ingredient, valid) was identified. The licensed indication text, manufacturer and MHRA PL number were not available and should be checked against the current SmPC. The licensed UK indication is adjunctive treatment of seizures in Lennox-Gastaut syndrome. FIRES is not a licensed indication.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these come from drug-disease links in the model's knowledge graph, not from product label text): liver failure, liver disease, gallbladder disease, leukopenia, anxiety disorder, neurotic disorder and dysthymic disorder. Hepatic and haematological status, and psychiatric history, would need careful review in any repurposing study.
- **Drug interactions**: 100 interactions were identified, all at the level of Moderate among those listed. Examples include:
  - corticosteroids (hydrocortisone, prednisone, betamethasone, triamcinolone)
  - opioids and related agents (morphine, diphenoxylate, difenoxin)
  - bupropion, pioglitazone, metoclopramide and ondansetron
  - cannabinoids (dronabinol, nabilone)
  - vitamin D analogues (cholecalciferol, calcifediol, calcitriol)

  Corticosteroid interactions are especially relevant because immunotherapy is commonly used in FIRES.

Please also refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no trials or publications for FIRES, and the evidence level is L5 (model prediction only). Rufinamide does not target the immune-mediated pathology of FIRES.

**To proceed, the following is needed:**
- Case series, registry data or early-phase studies of rufinamide in FIRES
- Confirmed mechanism of action data
- Review of the licensed UK indication, dosing and safety against the current SmPC
- A safety plan covering hepatic and haematological monitoring, and interactions with corticosteroids and other antiseizure drugs

**Note on other predictions:** The other candidates in the list also lack trials, and several raise concerns. Perioral myoclonia with absences and atypical childhood epilepsy with centrotemporal spikes carry a risk that sodium channel blockers worsen seizures. Trigeminal nerve neoplasm and renal-hepatic-pancreatic dysplasia look like model artefacts. "Childhood onset epileptic encephalopathy" has the most literature, but this largely reflects the already-licensed Lennox-Gastaut indication. The literature does not directly support extension to other encephalopathies. Small uncontrolled studies in non-LGS encephalopathies (PMIDs 20666837 and 32334364) could be reviewed as a more evidence-based lead than FIRES.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

