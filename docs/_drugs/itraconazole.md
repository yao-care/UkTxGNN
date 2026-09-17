---
layout: default
title: Itraconazole
parent: Model Prediction Only (L5)
nav_order: 321
evidence_level: L5
indication_count: 1
---

# Itraconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

Using no specialised skill here — this is a direct documentation/report-generation task governed entirely by the prompt's explicit template, not a coding or debugging task.

# Itraconazole: From Fungal Infections to Pneumocystosis

## One-Sentence Summary

Itraconazole is a triazole antifungal agent originally used to treat fungal infections; the evidence pack does not specify its original UK-approved indication text.
The TxGNN model predicts it may be effective for **Pneumocystosis**, with a prediction score of **99.34%**,
but this is currently supported only by **0 clinical trials** and **20 publications**, none of which are direct interventional trials for this indication — and one mechanistic study reports findings that directly contradict the plausibility of this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (itraconazole is a triazole/azole antifungal; no `taiwan_regulatory.licenses` or `drug.original_indications` data available) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 (mechanistic/observational evidence only; no disease-specific clinical trials; one RCT identified is for general antifungal prophylaxis, not pneumocystosis) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for itraconazole in this evidence pack. Based on general pharmacological knowledge, itraconazole is a triazole antifungal that inhibits fungal lanosterol 14α-demethylase (a CYP51 enzyme), blocking ergosterol synthesis in the fungal cell membrane. This mechanism underlies its efficacy against a range of fungal pathogens.

Pneumocystis jirovecii (formerly *P. carinii*) was historically classified as a fungal organism, which superficially supports the plausibility of an azole-class antifungal being repurposed for pneumocystosis. Additionally, several of the retrieved publications describe itraconazole use in the same immunocompromised patient populations (HIV/AIDS, transplant recipients) in which pneumocystosis is a common opportunistic infection, suggesting an epidemiological rather than direct therapeutic overlap.

**Important caveat**: one of the retrieved publications (PMID 12606318) directly characterises the lanosterol 14α-demethylase enzyme of *Pneumocystis carinii* and reports that the organism is **intrinsically resistant to azole antifungal medications**, due to structural differences at key resistance-conferring sites. This finding is mechanistically at odds with the TxGNN prediction and should be treated as a significant caution flag rather than supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | Double-blind, placebo-controlled Phase 3 trial of itraconazole capsules for prevention of deep fungal infections in HIV-infected patients — general antifungal prophylaxis, not pneumocystosis-specific |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | Mechanism Study | Am J Respir Cell Mol Biol | Characterises *Pneumocystis carinii* lanosterol 14α-demethylase; reports the organism is **intrinsically resistant to azole antifungals** — directly contradicts the repurposing rationale |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Reviews therapy/prophylaxis of *Pneumocystis carinii* and other protozoan/fungal opportunistic infections, including antifungal mechanisms and dosing |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | Reviews primary/secondary prophylaxis of HIV-related opportunistic infections, including *Pneumocystis* pneumonia |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Curr Clin Top Infect Dis | Reviews prophylaxis/treatment of infections, including PCP, in bone marrow transplant recipients |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Semin Respir Infect | Reviews infections, including PCP, after lung transplantation |
| [7877856](https://pubmed.ncbi.nlm.nih.gov/7877856/) | 1994 | Review | Pathol Biol | Notes prior pneumocystosis as a predisposing factor for aspergillosis in AIDS patients |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case Report | Frontiers in Immunology | Case of *Talaromyces marneffei* and *Pneumocystis jirovecii* coinfection in a child with STAT1 mutation |
| [19080136](https://pubmed.ncbi.nlm.nih.gov/19080136/) | 2008 | Observational | Zhonghua Nei Ke Za Zhi | Study of pathogens and drug resistance in pulmonary infections, including PCP, among AIDS patients |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Observational | Indian J Med Microbiol | Compares respiratory fungal pathogen profiles, including PCP, in immunocompetent vs immunocompromised hosts |

---

## UK Market Information

Itraconazole is currently **not marketed** in the UK per this evidence pack, with no marketing authorisations recorded (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No disease-specific clinical trials support this indication, MOA and safety data are unavailable, the drug is not currently marketed in the UK, and — most importantly — a mechanistic study in the evidence pack indicates that *Pneumocystis* is intrinsically resistant to azole antifungals, directly challenging the biological plausibility of the TxGNN prediction.

**To proceed, the following is needed:**
- Resolution of the contradictory mechanistic evidence on azole resistance in *Pneumocystis* (PMID 12606318) before further evaluation
- Detailed mechanism of action data (MOA) for itraconazole
- MHRA/SmPC-sourced safety data (key warnings, contraindications, DDIs)
- Any UK regulatory status update, given the drug is currently unmarketed
- Disease-specific interventional or observational studies evaluating itraconazole for pneumocystosis, rather than general antifungal prophylaxis in overlapping patient populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

