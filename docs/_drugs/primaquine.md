---
layout: default
title: Primaquine
parent: Model Prediction Only (L5)
nav_order: 518
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Primaquine: predicted new indication Myiasis (evidence level L5). Approved use: Plasmodium vivax malaria"
monitor_inn: "Primaquine"
predicted_indications: ["myiasis", "wound myiasis", "creeping myiasis", "furuncular myiasis", "toxoplasmosis", "nocardiosis", "pneumocystosis"]
---

# Primaquine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Primaquine: From Plasmodium vivax Malaria to Myiasis
{: .text-alpha }

## One-Sentence Summary

Primaquine is an 8-aminoquinoline antimalarial, originally used to treat **Plasmodium vivax malaria**.
The TxGNN model predicts it may be effective for **myiasis** (fly-larvae infestation) with a very high score. However, there are **no clinical trials and no publications** supporting this prediction, and no plausible mechanism is evident, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plasmodium vivax malaria |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, primaquine is an antiprotozoal 8-aminoquinoline. Its efficacy in P. vivax malaria is established, where it acts against liver-stage hypnozoites and mature gametocytes.

On review, the mechanistic case for myiasis is weak. Myiasis is an infestation by dipteran fly larvae, which are insects, not protozoa. Primaquine has no known larvicidal activity. Standard management is larval removal and wound care, with ivermectin-type agents used in some presentations.

The high score most likely reflects proximity to other antiparasitic indications in the knowledge graph, not a pharmacological link. The same pattern applies to the closely related predictions (wound myiasis, creeping myiasis and furuncular myiasis), which also lack clinical or literature support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0504010K0AAAAAA | Primaquine Tab 7.5 mg | Tablet (from product name) | Not stated in the available record |

This single authorisation is a valid single-ingredient product. The identifier is not in the standard MHRA "PL" format, so the authorisation details should be verified against the MHRA register. The BNF lists primaquine among the antimalarials. Myiasis is not an authorised use.

---

## Safety Considerations

- **Contraindications and risk conditions (from drug-disease knowledge-graph links, not label text):** neutropenia, agranulocytosis, G6PD deficiency, haemolytic anaemia, methaemoglobinaemia due to methaemoglobin reductase deficiency, glycogen storage disease, cystinuria, galactosaemia and pyruvate dehydrogenase E3 deficiency.
- **Drug interactions:** 100 interactions were recorded. The 20 reviewed include:
  - **Major:** dolasetron.
  - **Moderate:** clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron, famotidine, alosetron, loperamide, and several laxatives and bowel-preparation agents (e.g. bisacodyl, lactulose, macrogols).
  - **Minor:** metronidazole.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no publications and no plausible antilarval mechanism. Primaquine also carries meaningful haemolytic risk, which is not justified without any supporting benefit.

**To proceed, the following is needed:**
- Any in vitro or in vivo evidence of activity against dipteran larvae
- Detailed mechanism of action data
- Confirmation of the marketing authorisation details, including the approved indication and dosage form

**Other predictions for this drug (for context):** Malaria and pneumocystosis were assessed as L1 with "Proceed with Guardrails". Malaria is essentially primaquine's existing use, not true repurposing. Pneumocystosis is supported by clindamycin–primaquine as a second-line regimen. Both require G6PD testing before use. Toxoplasmosis is a research question (L4) with only incidental literature support. These would be better candidates for a dedicated evaluation than myiasis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

