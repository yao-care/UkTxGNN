---
layout: default
title: Clobazam
parent: Model Prediction Only (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
monitor_inn: "Clobazam"
predicted_indications: ["febrile infection-related epilepsy syndrome", "perioral myoclonia with absences", "photosensitive occipital lobe epilepsy", "cryptogenic late-onset epileptic spasms", "atypical childhood epilepsy with centrotemporal spikes", "childhood onset epileptic encephalopathy", "benign occipital epilepsy", "early-onset epileptic encephalopathy and intellectual disability due to GRIN2A mutation", "restless legs syndrome", "polymicrogyria with optic nerve hypoplasia"]
last_modified_at: 2026-11-06
description: "Clobazam: predicted new indication febrile infection-related epilepsy syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Clobazam
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

## Clobazam: GABA-A positive allosteric modulator (benzodiazepine) → febrile infection-related epilepsy syndrome
{: .text-alpha }

## One-Sentence Summary

Clobazam is a benzodiazepine-class anti-seizure medicine that acts on GABA-A receptors. The TxGNN model predicts it may be effective for **febrile infection-related epilepsy syndrome**, but there are **no registered clinical trials** and only **2 publications** (a case series and a case report), both on other agents rather than clobazam itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | febrile infection-related epilepsy syndrome |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (39 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 39 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Clobazam is, however, a well-known GABA-A positive allosteric modulator. Febrile infection-related epilepsy syndrome (FIRES) is a severe, refractory epileptic encephalopathy in which GABAergic agents such as midazolam, lorazepam and barbiturates are used to control seizures.

The mechanistic link is therefore plausible at class level. However, the retrieved literature concerns other agents (enteral lorazepam and perampanel), not clobazam. The support for clobazam in FIRES is indirect and comes from the related benzodiazepine class.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Case series | Epileptic Disorders | Enteral lorazepam used as a weaning substitute in midazolam-dependent FIRES patients; clobazam not studied |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case report | Cureus | Perampanel may reduce barbiturate dependency in a 13-year-old boy with FIRES; clobazam not studied |

---

## UK Market Information

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 040801060AACLCL | Clobazam 1.25mg/5ml oral liquid | Clobazam |
| 040801060AABZBZ | Clobazam 1.5mg/5ml oral liquid | Clobazam |
| 040801060AACFCF | Clobazam 100mg/5ml oral liquid | Clobazam |
| 040801060AABTBT | Clobazam 10mg tablets | Clobazam |
| 040801060AAA4A4 | Clobazam 10mg/5ml oral liquid | Clobazam |
| 040801060AACSCS | Clobazam 10mg/5ml oral suspension sugar free | Clobazam |
| 040801060AABYBY | Clobazam 12.5mg/5ml oral liquid | Clobazam |
| 040801060AACHCH | Clobazam 120mg/5ml oral liquid | Clobazam |
| 040801060AAA7A7 | Clobazam 15mg/5ml oral liquid | Clobazam |
| 040801060AAA8A8 | Clobazam 1mg/5ml oral liquid | Clobazam |
| 040801060AAAGAG | Clobazam 2.5mg capsules | Clobazam |
| 040801060AABABA | Clobazam 2.5mg/5ml oral liquid | Clobazam |
| 040801060AACTCT | Clobazam 20mg tablets | Clobazam |
| 040801060AABSBS | Clobazam 20mg/5ml oral liquid | Clobazam |
| 040801060AABUBU | Clobazam 250micrograms/5ml oral liquid | Clobazam |
| 040801060AAA3A3 | Clobazam 25mg/5ml oral liquid | Clobazam |
| 040801060AABNBN | Clobazam 2mg/5ml oral liquid | Clobazam |
| 040801060AABLBL | Clobazam 3.5mg/5ml oral liquid | Clobazam |
| 040801060AABPBP | Clobazam 3.75mg/5ml oral liquid | Clobazam |
| 040801060AACBCB | Clobazam 32.5mg/5ml oral liquid | Clobazam |

Showing 20 of 39 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

Please consult the BNF and the current SmPC for licensed indications and formulations.

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 recorded interactions. Examples include:
  - **Major**: morphine (including liposomal morphine) and eliglustat
  - **Moderate**: bupropion, aprepitant, omeprazole, esomeprazole, lansoprazole, cimetidine, clarithromycin, metoclopramide, fenfluramine, dexfenfluramine and dronabinol
  - **Minor**: antacids containing magnesium or aluminium salts, and calcium carbonate

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (0.9982), and a GABAergic rationale exists. However, no trial or publication studies clobazam in FIRES. The evidence is therefore model prediction only (L5).

**To proceed, the following is needed:**
- Clobazam-specific clinical data in FIRES (for example case series or registry data)
- Detailed mechanism of action data
- Label-level warnings and contraindications from the SmPC and BNF
- A safety plan covering interactions, particularly with opioids, given the major interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

