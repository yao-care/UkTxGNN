---
layout: default
title: Rifaximin
parent: Moderate Evidence (L3-L4)
nav_order: 542
evidence_level: L4
indication_count: 6
---

# Rifaximin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Rifaximin: From Hepatic Encephalopathy to Oral Candidiasis

## One-Sentence Summary

Rifaximin is a gut-restricted oral antibiotic, originally used to treat hepatic encephalopathy (hepatic coma).
The TxGNN model predicts it may be effective for **oral candidiasis**, but there are **no registered clinical trials** and only **1 publication**, which points towards possible harm rather than benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic encephalopathy / hepatic coma (from the knowledge graph; no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Oral candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rifaximin is a non-absorbed oral antibacterial that acts within the gut. Its efficacy in hepatic encephalopathy relates to reducing gut bacterial load.

On the available evidence, the prediction is **not mechanistically supported**. Rifaximin has no antifungal activity, and oral candidiasis is a fungal infection. The one relevant publication (PMID 34180023) reports that rifaximin use favoured micafungin-resistant *Candida* infections in allogeneic stem cell transplant recipients. This suggests a possible harm signal, such as gut microbiota disruption promoting fungal overgrowth. The high TxGNN score is most likely an artefact of the knowledge graph.

Other top-ranked predictions (commissural lip fistula, osteoradionecrosis of the mandible, oral leukoedema, burning mouth syndrome) also lack clinical or mechanistic support. The broader candidiasis prediction (score 99.15%) likewise has only indirect, observational literature pointing in the opposite direction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort | Annals of Hematology | In allogeneic stem cell transplant recipients, rifaximin prophylaxis (used to reduce gut bacterial infections and GvHD) was associated with micafungin-resistant *Candida* infections. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501070X0AAAAAA (BNF-style code; not a PL number) | Rifaximin tablets 200 mg | Tablet | Not available |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): *Clostridium difficile* colitis; perinatal necrotising enterocolitis.
- **Drug Interactions**: 69 interactions were identified. Most are of moderate severity. One is major: live cholera vaccine (*Vibrio cholerae* CVD 103-HgR). Examples of moderate interactions include warfarin, ciclosporin, tolvaptan, cabozantinib, daclatasvir, ledipasvir, apalutamide and darolutamide.
- **Fungal infection signal**: the available literature suggests rifaximin exposure may be associated with resistant *Candida* infections in vulnerable patients. This should be treated as a safety concern.

Please also refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials, rifaximin has no antifungal activity, and the only directly relevant publication suggests a possible harm signal rather than benefit.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale for an antifungal or anti-candidal effect
- Prospective or well-controlled studies, if any link between rifaximin, gut-oral axis effects and oral candidiasis is to be explored
- Review of the safety signal for resistant *Candida* infection in immunocompromised patients
- Complete UK authorisation details (PL number, dosage form, approved indication) and SmPC warnings and contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

