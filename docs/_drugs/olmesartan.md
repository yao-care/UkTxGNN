---
layout: default
title: Olmesartan
parent: Model Prediction Only (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Olmesartan: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not stated in the data compiled for this report (olmesartan is an ARB…"
monitor_inn: "Olmesartan"
predicted_indications: ["Prinzmetal angina", "hypotrichosis simplex of the scalp", "migraine disorder", "alopecia", "pulmonary hypertension", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "kyphoscoliotic heart disease", "open-angle glaucoma"]
---

# Olmesartan
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

## Olmesartan: From Hypertension to Prinzmetal Angina
{: .text-alpha }

## One-Sentence Summary

Olmesartan is an angiotensin II receptor blocker (ARB) with a UK marketing authorisation for its tablet formulation. The TxGNN model predicts it may be effective for **Prinzmetal angina**, but **no clinical trials and no publications** were found for this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (olmesartan is an ARB, conventionally used for hypertension) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Olmesartan is an angiotensin II type 1 (AT1) receptor blocker. Detailed mechanism of action data are not available in the data compiled for this report, but the drug class is well characterised: AT1 blockade reduces vascular tone through modulation of the renin-angiotensin-aldosterone system (RAAS).

Prinzmetal (vasospastic) angina is caused by coronary artery spasm. Reduced vascular tone through RAAS modulation could plausibly lessen vasospasm, which is the link the model appears to have found. However, this is a hypothesis only. The high TxGNN score (0.9984) is a model output and is not clinical evidence. No trials or literature were retrieved for this indication.

**Other predictions reviewed**

The model produced ten predictions in total. The most notable are below.

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Migraine disorder | 0.9964 | L4 | Three publications: a 2006 commentary, a 2006 clinical study in hypertensive patients, and a 2019 systematic review of ACE inhibitors and ARBs. Evidence is class-level and indirect. Whether olmesartan works independently of blood pressure lowering is unclear. Suitable as a research question. |
| Pulmonary hypertension | 0.9961 | L4 | Preclinical rat and mouse studies support biological plausibility. No human efficacy data. The one trial retrieved (NCT04330300) is a COVID-19 ACEi/ARB study and is not relevant. Suitable as a research question. |
| Open-angle glaucoma | 0.9940 | L5 | Only a 2009 general review of glaucoma treatment was retrieved, and its relevance to olmesartan is unconfirmed. Hold. |
| Hair disorders (hypotrichosis simplex of the scalp, alopecia, congenital hypotrichosis milia, diffuse alopecia areata) | 99.56–0.9965 | L5 | No plausible mechanism and no evidence. Likely network artefacts. |
| Migraine with brainstem aura, kyphoscoliotic heart disease | 99.47–0.9957 | L5 | Prediction only. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal angina.

---

## Literature Evidence

Currently no related literature available for Prinzmetal angina.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0205052B0AAAAAA | Olmesartan Medoxomil Tablets 10 mg | Tablet | Not stated in the data compiled |

The identifier shown is as supplied and is not in the standard UK PL number format. Authorisation details should be verified against the MHRA register and the BNF.

---

## Safety Considerations

**Drug Interactions**

The interaction screen identified 94 potential interactions. Those listed in the compiled data include:

- **Major:** potassium bicarbonate and potassium chloride (risk of hyperkalaemia, which is a recognised concern with ARBs).
- **Moderate:** hydrocortisone, eluxadoline, exenatide, polyethylene glycol (3350 with electrolytes), and a wide range of insulin preparations (human, aspart, degludec, detemir, glargine, glulisine, lispro and others).

Please refer to the SmPC and BNF for full safety information, including warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Prinzmetal angina prediction is supported only by the TxGNN model score and a plausible but unproven RAAS mechanism. No trials or publications were found, so the evidence level is L5.

**To proceed, the following is needed:**
- A systematic literature search for ARBs and RAAS inhibitors in vasospastic angina
- Confirmation of the licensed indication and product details from the MHRA register and the SmPC
- Detailed mechanism of action data and warnings/contraindications from the SmPC and BNF
- For a more evidence-supported direction, consider prioritising **migraine prevention** (class-level evidence, including candesartan RCTs) or **pulmonary hypertension** (preclinical data) as research questions, with olmesartan-specific data needed in either case
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

