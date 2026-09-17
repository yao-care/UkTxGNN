---
layout: default
title: Lormetazepam
parent: High Evidence (L1-L2)
nav_order: 353
evidence_level: L1
indication_count: 10
---

# Lormetazepam
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Lormetazepam: From Insomnia (Undocumented Original Use) to Confirmed Insomnia Indication

## One-Sentence Summary

> Lormetazepam is a benzodiazepine hypnotic; this Evidence Pack has no recorded original indication or mechanism-of-action data (data gap), but based on established pharmacology it is already used in parts of Europe (as Noctamid) for **insomnia**.
> The TxGNN model's top signal also points to **Insomnia (disease)**, with **3 clinical trials** and **4 publications** identified — this is best read as a confirmation of an established use rather than a genuine repurposing hypothesis.
> Note: the Evidence Pack also flagged several lower-confidence signals (anxiety, alcohol withdrawal delirium, various "abuse" categories) that are largely unsupported (Hold) and are not covered further in this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this dataset (data gap — closest real-world match: insomnia, marketed in parts of Europe as Noctamid) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this dataset (flagged as a High-severity data gap). Based on known pharmacology, lormetazepam is a benzodiazepine that acts as a positive allosteric modulator of the GABA-A receptor, producing sedative-hypnotic effects — the same class mechanism underlying agents such as diazepam and flunitrazepam.

Insomnia is not truly a "new" indication for lormetazepam: it is the drug's established, originally-approved use in several European markets (brand name Noctamid), and the Evidence Pack's empty `original_indications` field appears to be a data-capture gap rather than a genuine absence of prior approved use. In other words, the TxGNN signal here largely reconfirms known pharmacology rather than proposing a novel therapeutic hypothesis.

This still has practical value for a UK context: lormetazepam currently holds **no UK marketing authorisation** (0 licenses, "Not marketed"), so the clinical trial and literature evidence assembled here is directly relevant to any future licensing assessment for the insomnia indication specifically in the UK market, even though it would not represent a novel therapeutic use elsewhere.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00679900](https://clinicaltrials.gov/study/NCT00679900) | Phase 3 | Completed | 283 | Randomised, double-blind comparison of eplivanserin 5 mg/day vs lormetazepam 1 mg/day in chronic primary insomnia with sleep-maintenance difficulties; assessed next-day residual sleepiness and safety, including rebound insomnia/withdrawal. |
| [NCT00788515](https://clinicaltrials.gov/study/NCT00788515) | Phase 3 | Terminated | 33 | Randomised, double-blind comparison of volinanserin 2 mg/day vs lormetazepam 1 mg/day in chronic primary insomnia; study terminated early, limiting statistical power. |
| [NCT06473415](https://clinicaltrials.gov/study/NCT06473415) | N/A | Recruiting | 50 | Observational EEG study of continuous lormetazepam infusion on sleep/sedation patterns in ICU patients — an indirect, non-randomised signal from a critical-care rather than outpatient insomnia population. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT | J Int Med Res | Double-blind comparison in 100 outpatients: lormetazepam 1 mg significantly outperformed diazepam 5 mg on sleep-onset latency and duration of uninterrupted sleep. |
| [2873832](https://pubmed.ncbi.nlm.nih.gov/2873832/) | 1986 | Cohort | Br J Clin Pract | Cohort study of long-term nitrazepam users transferred to lormetazepam (no abstract available; title indicates a switching/tolerability study). |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatr Scand Suppl | Review of hypnotic classes for insomnia subtypes, discussing benzodiazepine pharmacokinetic/pharmacodynamic profiles including agents like lormetazepam. |
| [11215344](https://pubmed.ncbi.nlm.nih.gov/11215344/) | 2001 | Review | MMW Fortschr Med | Review discussing antidepressants as an alternative sleep aid to benzodiazepines (no abstract available). |

---

## UK Market Information

Lormetazepam currently holds **no UK marketing authorisation** (0 licenses recorded; market status: Not marketed). No product-level data (PL number, product name, dosage form, approved indication text) is available in this dataset.

---

## Safety Considerations

Key warnings, contraindications, and drug–drug interaction data are not available in this Evidence Pack (flagged as a **Blocking**-severity data gap — TFDA/MHRA-equivalent product labelling has not yet been sourced). As a class, benzodiazepines carry known risks of dependence, withdrawal/rebound insomnia, sedation, and next-day psychomotor impairment, as reflected in several of the literature items above — but drug-specific warning text should not be inferred from this alone.

> Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 3 RCT (n=283) plus supporting Phase 3 and mechanistic/observational data give reasonable (L1) confidence that lormetazepam is effective for insomnia — but this reflects an already-established use rather than a novel repurposing opportunity, and the drug has no current UK licence or sourced safety labelling.

**To proceed, the following is needed:**
- MHRA-equivalent SmPC (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank — currently a High-severity data gap (DG002)
- A UK-specific licensing pathway assessment, since lormetazepam has 0 current UK marketing authorisations
- Clarification of the `original_indications` data gap to confirm this is a labelling-confirmation exercise rather than a true repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

