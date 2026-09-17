---
layout: default
title: Pyrazinamide
parent: Model Prediction Only (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide: From Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

Pyrazinamide is a core component of standard first-line antituberculosis combination therapy. The TxGNN model's top-ranked prediction for this drug is **Infectious Otitis Media**, but currently **0 clinical trials** and **0 publications** directly support this specific term — it is a pure knowledge-graph prediction. Related, more narrowly defined middle-ear diagnoses (e.g. *middle ear disease*, *chronic otitis media*) do have case-report-level literature describing tuberculous otitis media, which lends indirect mechanistic plausibility but does not constitute direct evidence for this top-ranked candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (as a component of standard anti-TB combination therapy — no formal indication text available in this evidence pack) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| UK Market Status | Not marketed (per this evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the information available in this evidence pack, Pyrazinamide is described as a component of standard antituberculous combination therapy, and its efficacy in tuberculosis has been established through decades of clinical use; mechanistically, this could extend to tuberculous infections of the middle ear.

Infectious Otitis Media, the top-ranked prediction, has no clinical trial or literature evidence directly attached to it in this evidence pack — the model's own rationale explicitly notes this is a "purely predictive association" based on TxGNN score alone, with the underlying hypothesis (a tuberculous infection pathway) inferred rather than demonstrated. It is worth noting, however, that several lower-ranked but mechanistically adjacent predictions from the same drug — *middle ear disease* (rank 2), *chronic otitis media* (rank 4), *suppurative otitis media* (rank 5), and *infectious otitis interna* (rank 10) — are supported by case reports and small case series describing tuberculous otitis media (TOM), a rare but recognised form of extrapulmonary tuberculosis. These related indications reached evidence level L4 (decision stage S1, "Research Question"), whereas Infectious Otitis Media itself remains at L5.

Because tuberculous otitis media is a genuine, if rare, clinical entity typically treated with standard multi-drug anti-TB regimens (including pyrazinamide), the overall disease-class signal is biologically plausible. However, the specific term "Infectious Otitis Media" is broad and not restricted to tuberculous aetiology; without direct evidence, it cannot be distinguished from bacterial otitis media of non-tuberculous origin, for which pyrazinamide has no established activity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although Infectious Otitis Media carries the highest TxGNN prediction score among candidates for this drug, it has zero supporting clinical trials or publications (Evidence Level L5). This is a pure model-generated association and does not meet the threshold for progression beyond initial screening.

**To proceed, the following is needed:**
- Product safety information (warnings, contraindications) — currently a Blocking data gap; required before any S1 safety pre-assessment can proceed
- Mechanism of action data from DrugBank — currently a High-severity data gap affecting mechanistic-relevance analysis
- Direct clinical or literature evidence specific to "Infectious Otitis Media" (as distinct from the better-evidenced related terms *middle ear disease* and *chronic otitis media*, which warrant separate evaluation as Research Questions at L4/S1)
- Confirmation of actual UK marketing authorisation status against the MHRA product register — pyrazinamide is a well-established first-line anti-TB agent, so the "0 licences / not marketed" status recorded here may reflect incomplete regulatory data collection rather than genuine non-availability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

