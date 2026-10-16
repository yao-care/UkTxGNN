---
layout: default
title: Clobazam
parent: Model Prediction Only (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Clobazam: predicted new indication Febrile infection-related epilepsy syndrome (FIRES) (evidence level L5). Approved use: Lennox-Gastaut syndrome"
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Clobazam: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome (FIRES)

## One-Sentence Summary

Clobazam is a benzodiazepine antiseizure medicine, originally used for Lennox-Gastaut syndrome.
The TxGNN model predicts it may be useful for **febrile infection-related epilepsy syndrome (FIRES)**,
but there are currently **no registered clinical trials** and only **2 publications** (a case series and a case report), both on other drugs, so the evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lennox-Gastaut syndrome (from the knowledge graph; no approved indication text available in the UK licence data) |
| Predicted New Indication | Febrile infection-related epilepsy syndrome (FIRES) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (strictly by the rules: model prediction with no direct studies of clobazam; the compiled data grades it L4 on the basis of indirect class-level literature) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold (research question only) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Clobazam is, however, a well-known benzodiazepine that enhances GABA-A receptor signalling (positive allosteric modulation), and this is the basis for its use in Lennox-Gastaut syndrome.

FIRES is a severe, refractory epileptic encephalopathy that typically follows a febrile illness in previously healthy children. Seizures are often resistant to conventional antiseizure medicines, and treatment frequently relies on GABAergic agents such as midazolam, lorazepam and barbiturates. A GABA-A modulator like clobazam is therefore mechanistically plausible.

An important caveat: the retrieved literature concerns other agents (enteral lorazepam and perampanel), not clobazam. The support is indirect, drawn from a related benzodiazepine class.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Case series | Epileptic Disord | Enteral lorazepam as a weaning strategy in midazolam-responsive FIRES (clobazam not studied) |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case report | Cureus | Perampanel may reduce barbiturate dependency in a 13-year-old with FIRES (clobazam not studied) |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 040801060AABTBT | Clobazam Tab 10 mg | Not stated | Not stated |

The licence record compiled for this report has no dosage form or approved indication text, and the number shown does not follow the usual MHRA "PL" format, so it should be verified against the MHRA register. Please check the current SmPC, the BNF classification and any NICE guidance directly.

## Safety Considerations

**Drug Interactions** (100 interactions recorded; examples from the 20 reviewed):

- **Major:** morphine (including liposomal morphine) and eliglustat
- **Moderate:** bupropion, aprepitant, omeprazole, esomeprazole, lansoprazole, cimetidine, clarithromycin, metoclopramide, dronabinol, fenfluramine, dexfenfluramine
- **Minor:** antacids such as magnesium oxide, aluminium hydroxide and calcium carbonate

The concomitant use of opioids with benzodiazepines carries a risk of profound sedation and respiratory depression, which is particularly relevant in critically ill FIRES patients, who often receive multiple sedatives.

Warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold (research question only)**

**Rationale:**
The TxGNN score is high and a GABAergic mechanism is plausible, but there are no trials and no publications evaluating clobazam in FIRES. The only literature covers other drugs. The compiled data classes this as a research question rather than a candidate for clinical adoption.

**To proceed, the following is needed:**
- Clobazam-specific data in FIRES or NORSE (case series, registries or a retrospective cohort)
- Mechanism of action data and the SmPC warnings and contraindications
- Verified UK licence details (MHRA number, dosage form, approved indication)
- A review of interaction risks with the sedatives, anaesthetics and opioids used in intensive care for FIRES
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

