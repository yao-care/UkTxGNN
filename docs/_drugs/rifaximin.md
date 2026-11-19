---
layout: default
title: Rifaximin
parent: Model Prediction Only (L5)
nav_order: 542
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-12
monitor_inn: "Rifaximin"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "burning mouth syndrome", "oral leukoedema", "candidiasis"]
description: "Rifaximin: predicted new indication Oral candidiasis (evidence level L5). In the UK: 8 NHSBSA BNF presentation codes"
---

# Rifaximin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Rifaximin: Oral candidiasis
{: .text-alpha }

## One-Sentence Summary

Rifaximin is a gut-restricted oral antibiotic, originally used to treat hepatic encephalopathy (hepatic coma).
The TxGNN model predicts it may be effective for **oral candidiasis**, but there are **no registered clinical trials** and only **1 publication**, which points towards possible harm rather than benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Oral candidiasis |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (8 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for rifaximin: "Rifaximin is an antibacterial drug. […] Rifaximin is a semi-synthetic derivative of rifampin and acts by binding to the beta-subunit of bacterial DNA-dependent RNA polymerase blocking one of the steps in transcription. This results in inhibition of bacterial protein synthesis and consequently inhibits the growth of bacteria." ([DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b), label version 2025-08-27; accessed 2026-11-19.) Based on known information, rifaximin is a non-absorbed oral antibacterial that acts within the gut. Its efficacy in hepatic encephalopathy relates to reducing gut bacterial load.

On the available evidence, the prediction is **not mechanistically supported**. Rifaximin has no antifungal activity, and oral candidiasis is a fungal infection. The one relevant publication (PMID 34180023) reports that rifaximin use favoured micafungin-resistant *Candida* infections in allogeneic stem cell transplant recipients. This suggests a possible harm signal, such as gut microbiota disruption promoting fungal overgrowth. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top-ranked predictions (commissural lip fistula, osteoradionecrosis of the mandible, oral leukoedema, burning mouth syndrome) also lack clinical or mechanistic support. The broader candidiasis prediction (score 0.9915) likewise has only indirect, observational literature pointing in the opposite direction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort | Annals of Hematology | In allogeneic stem cell transplant recipients, rifaximin prophylaxis (used to reduce gut bacterial infections and GvHD) was associated with micafungin-resistant *Candida* infections. |

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0501070X0AAACAC | Rifaximin 100mg/5ml oral suspension | Rifaximin |
| 0501070X0AAAAAA | Rifaximin 200mg tablets | Rifaximin |
| 0501070X0AAABAB | Rifaximin 550mg tablets | Rifaximin |
| 0501070X0BBABAC | Normix 100mg/5ml granules for oral suspension | Rifaximin |
| 0501070X0BBAAAA | Normix 200mg tablets | Rifaximin |
| 0501070X0BEAAAB | Targaxan 550mg tablets | Rifaximin |
| 0501070X0BDAAAB | Xifaxan 550mg tablets | Rifaximin |
| 0501070X0BCAAAA | Xifaxanta 200mg tablets | Rifaximin |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

