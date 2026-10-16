---
layout: default
title: Betahistine
parent: Model Prediction Only (L5)
nav_order: 100
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Betahistine: predicted new indication Restless legs syndrome (evidence level L5). Approved use: Meniere disease"
monitor_inn: "Betahistine"
predicted_indications: ["restless legs syndrome", "active cochlear Meniere disease", "active cochleovestibular Meniere disease", "active vestibular Meniere disease", "otosclerosis", "peripheral vertigo", "age-related hearing impairment", "vertigo, benign recurrent, 2", "autosomal recessive hyperinsulinism due to Kir6.2 deficiency", "hyperinsulinemic hypoglycemia, familial"]
---

# Betahistine
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

# Betahistine: From Meniere Disease to Restless Legs Syndrome

## One-Sentence Summary

Betahistine is a histamine analogue originally used to treat Meniere disease and endolymphatic hydrops.
The TxGNN model's top-ranked prediction is **restless legs syndrome**, but this is a model prediction only, with **no clinical trials** and **no publications** supporting it.
The better-supported predicted indications are vertigo-related conditions (for example peripheral vertigo, with 18 publications retrieved), but these sit close to the existing marketed use rather than being truly new.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Meniere disease; endolymphatic hydrops (no indication text is available in the UK authorisation data) |
| Predicted New Indication | Restless legs syndrome |
| TxGNN Prediction Score | 98.51% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available in the data compiled for this report. From the literature, betahistine is a weak histamine H1 receptor agonist and a more potent H3 receptor antagonist (inverse agonist). This increases histamine turnover and is thought to improve inner-ear microcirculation and promote vestibular compensation.

For **restless legs syndrome (RLS)**, the link is speculative. RLS pathophysiology is generally linked to dopaminergic and iron-related mechanisms, and no trials or publications connecting betahistine to RLS were found. The high model score should therefore be treated as a hypothesis only.

Several other predictions are far more plausible, but mostly because they overlap with the existing label:

- **Meniere disease subtypes** (active cochlear, cochleovestibular and vestibular): these are subtypes of the approved indication, not new indications. Preclinical work supports H3-heteroreceptor involvement and a pericyte/precapillary arteriole mechanism that increases cochlear blood flow.
- **Peripheral vertigo and BPPV-related vertigo**: mechanistic and clinical literature exists, but the largest Meniere trial (BEMED) reported no significant benefit over placebo, so the evidence is mixed.
- **Otosclerosis, age-related hearing impairment, and two hyperinsulinism conditions**: indirect or no mechanistic rationale; the hyperinsulinism predictions are probably graph-model artefacts.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked prediction (restless legs syndrome), nor for any of the other predicted indications in the data compiled for this report.

---

## Literature Evidence

No literature was found for restless legs syndrome. The table below shows the most relevant publications for the best-supported related prediction, **peripheral vertigo** (rank 6), which is largely within existing marketed use.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26797774](https://pubmed.ncbi.nlm.nih.gov/26797774/) | 2016 | RCT | BMJ | BEMED long-term, multicentre, double-blind, placebo-controlled, dose-defining trial in Meniere's disease; betahistine did not significantly reduce vertigo attacks versus placebo |
| [36827524](https://pubmed.ncbi.nlm.nih.gov/36827524/) | 2023 | Systematic review | Cochrane Database Syst Rev | Systemic pharmacological interventions for Meniere's disease, including betahistine, diuretics, antivirals and corticosteroids |
| [27327415](https://pubmed.ncbi.nlm.nih.gov/27327415/) | 2016 | Systematic review | Cochrane Database Syst Rev | Betahistine versus placebo for symptoms of vertigo from different causes |
| [23778722](https://pubmed.ncbi.nlm.nih.gov/23778722/) | 2014 | Meta-analysis | Eur Arch Otorhinolaryngol | Meta-analysis of 12 double-blind, placebo-controlled studies in vestibular vertigo or Meniere's disease |
| [12582782](https://pubmed.ncbi.nlm.nih.gov/12582782/) | 2003 | RCT | Eur Arch Otorhinolaryngol | Double-blind trial (144 patients) of betahistine versus placebo in Meniere's disease or paroxysmal positional vertigo |
| [41487075](https://pubmed.ncbi.nlm.nih.gov/41487075/) | 2026 | RCT | J Otolaryngol Head Neck Surg | EGb 761 versus betahistine in dizziness/vertigo of unclear cause |
| [37000080](https://pubmed.ncbi.nlm.nih.gov/37000080/) | 2023 | Systematic review and meta-analysis | Medicine | Epley's manoeuvre plus betahistine in posterior canal BPPV |
| [41038567](https://pubmed.ncbi.nlm.nih.gov/41038567/) | 2025 | Systematic review | Acta Otorrinolaringol Esp | Cinnarizine/dimenhydrinate combination versus betahistine for vertigo |
| [26245698](https://pubmed.ncbi.nlm.nih.gov/26245698/) | 2015 | Review | Acta Otolaryngol | Betahistine reported as effective and safe in Meniere's disease, BPPV, vestibular neuronitis and other peripheral vertigo |
| [24177346](https://pubmed.ncbi.nlm.nih.gov/24177346/) | 2013 | Review/commentary | J Vestib Res | Mechanisms of betahistine in vertigo relief and vestibular compensation |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0406000B0AAAAAA | Betahistine HCl Tab 8 mg | Not stated | Not stated |

The data compiled for this report show one valid single-ingredient authorisation. The identifier shown is not in standard MHRA PL format, and dosage form, manufacturer and approved indication are not recorded. Please verify details against the MHRA register, the BNF and the current SmPC.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, restless legs syndrome, rests on a model score alone (L5), with no trials, no literature and only a speculative mechanistic link. The better-supported indications (vertigo, BPPV, Meniere subtypes) largely overlap with the existing use and have mixed evidence, including the null BEMED result. Of those, peripheral vertigo (L3) could be considered for "Proceed with Guardrails" as a label-adjacent question rather than a new repurposing indication.

**To proceed, the following is needed:**
- Mechanism of action data to be formally confirmed (for example from DrugBank)
- Any preclinical or clinical rationale linking histaminergic modulation to RLS before further investment
- For vertigo-related indications: a defined vertigo subtype, standardised outcome measures, and careful interpretation of the BEMED null result
- Complete UK authorisation details (dosage form, indication, MHRA licence number) and SmPC safety information, including warnings, contraindications and interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

