---
layout: default
title: Capsaicin
parent: Model Prediction Only (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Capsaicin: predicted new indication Otitis externa (evidence level L5). Approved use: Neuralgia"
monitor_inn: "Capsaicin"
predicted_indications: ["otitis externa", "post-bacterial disorder", "postinfectious vasculitis", "infective urethral stricture", "post-infectious syndrome", "Chagas cardiomyopathy", "papillary conjunctivitis", "infection-related hemolytic uremic syndrome", "tinea corporis", "rosacea conjunctivitis"]
---

# Capsaicin
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

## Capsaicin: From Neuralgia to Otitis Externa
{: .text-alpha }

## One-Sentence Summary

Capsaicin is a TRPV1 agonist, originally used to treat neuralgia and postherpetic neuralgia.
The TxGNN model predicts it may be effective for **otitis externa**, but there are currently **no clinical trials** and **no publications** supporting this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neuralgia; postherpetic neuralgia |
| Predicted New Indication | Otitis externa |
| TxGNN Prediction Score | 98.76% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, capsaicin is a TRPV1 agonist. Topical use is thought to desensitise nociceptive nerve fibres and reduce the pain messenger substance P, which underlies its use in neuralgia.

In theory, the same desensitisation could relieve pain from an inflamed ear canal, which is the only plausible link between neuralgia and otitis externa. However, no supporting mechanistic or clinical evidence was found. Capsaicin is a strong irritant, and applying it to inflamed or broken skin or inside the ear canal is a real safety concern. The prediction should therefore be regarded as a hypothesis only.

The same model also ranked several other conditions highly (for example post-infectious syndrome, papillary conjunctivitis and tinea corporis). None has trial evidence. The only one with indirect literature is post-infectious syndrome (TRPV1 sensitisation in post-infectious irritable bowel syndrome), which is graded L4 and is a research question rather than a candidate for use.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1003020AAAAAAAA | Capsaicin cream 0.075% | Not stated | Not stated |

The authorisation number is in a format that does not look like a standard MHRA "PL" number, and the dosage form and indication are not recorded. The UK authorisation status and indication should be verified against the MHRA register, the SmPC and the BNF.

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** the TxGNN knowledge graph links capsaicin to a number of conditions, including hypertension, liver failure and liver disease, kidney disease, epilepsy, diabetes mellitus and diabetic ketoacidosis, blood coagulation disorders, haemophilia, stroke and cerebrovascular disorders, myocardial infarction and other heart disease, anaemia, respiratory failure, gastritis, and gastro-oesophageal reflux disease. These are model-derived associations and should be verified against the SmPC.
- **Pharmacological targets:** capsaicin acts on TRPV1 (human). Activity at Kv1.1, Kv1.2, Kv1.7 and Kv3.1 (mouse and rat) and CFTR (human) has also been recorded. These are target interactions, not clinical drug-drug interactions, and none has an established clinical significance in the data compiled.
- **Site-specific concerns:** capsaicin is a potent irritant. Application to the ear canal, broken or inflamed skin, or the eyes is a particular concern for the predicted indication.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for otitis externa is supported by model score only (L5), with no clinical trials or literature, a speculative mechanism, and a clear local irritancy concern at the proposed site.

**To proceed, the following is needed:**
- Detailed mechanism of action data (for example from DrugBank)
- Verification of the UK authorisation details (product form, indication, MHRA number) and of SmPC and BNF warnings and contraindications
- Preclinical or early clinical data showing that capsaicin is tolerable and effective for ear canal pain, including local tolerability
- Assessment of suitable formulations and routes, as none has been established for the ear
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

