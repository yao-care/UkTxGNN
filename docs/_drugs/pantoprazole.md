---
layout: default
title: Pantoprazole
parent: Model Prediction Only (L5)
nav_order: 476
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "Pantoprazole"
predicted_indications: ["duodenal obstruction"]
description: "Pantoprazole: predicted new indication Duodenal obstruction (evidence level L5). Approved use: Not recorded in the local data"
---

# Pantoprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Pantoprazole: Duodenal obstruction
{: .text-alpha }

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor, originally used for peptic ulcer disease, gastro-oesophageal reflux disease and Zollinger-Ellison syndrome.
This is largely an on-label use rather than true repurposing, so the prediction mainly confirms existing practice.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal obstruction |
| TxGNN Prediction Score | 0.9921 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, pantoprazole irreversibly inhibits the gastric H+/K+ ATPase (proton pump) in parietal cells. This suppresses acid secretion and allows ulcers to heal.

The predicted indication is essentially the same as the drug's existing use in peptic ulcer disease. Ulcer healing depends on reducing gastric acid exposure, so the mechanism fits directly. Other predicted indications in the data (gastrojejunal ulcer, peptic ulcer perforation, duodenogastric reflux, duodenal obstruction) are weaker. They rest on indirect evidence, or on none, and are outside the scope of this report.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Randomised, double-blind, multicentre comparison of ilaprazole vs pantoprazole triple therapy for 7 days for H. pylori eradication in gastric and/or duodenal ulcer patients |

## Literature Evidence


| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7614102](https://pubmed.ncbi.nlm.nih.gov/7614102/) | 1995 | RCT | Eur J Gastroenterol Hepatol | Double-blind comparison of pantoprazole 40 mg vs omeprazole 20 mg for acute duodenal ulcer healing |
| [7569755](https://pubmed.ncbi.nlm.nih.gov/7569755/) | 1995 | RCT | Scand J Gastroenterol | Multicentre comparison of pantoprazole and ranitidine in acute duodenal ulcer |
| [7781461](https://pubmed.ncbi.nlm.nih.gov/7781461/) | 1995 | RCT | Dig Dis Sci | Double-blind trial (n=276) of pantoprazole 40 mg vs ranitidine 300 mg in acute duodenal ulcer |
| [10638560](https://pubmed.ncbi.nlm.nih.gov/10638560/) | 2000 | Comparative trial | Am J Gastroenterol | Pantoprazole vs ranitidine in duodenal ulcer in a Brazilian population |
| [8882382](https://pubmed.ncbi.nlm.nih.gov/8882382/) | 1996 | Review | Drugs | Pantoprazole 40 mg was superior to ranitidine and equivalent to omeprazole 20 mg in short-term treatment of acute peptic ulcer |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic review/network meta-analysis | Am J Gastroenterol | Compared P-CAB with PPIs for healing grade C/D oesophagitis |
| [38252210](https://pubmed.ncbi.nlm.nih.gov/38252210/) | 2024 | RCT/Meta-analysis | Dig Dis Sci | Pantoprazole and vonoprazan performed well in preventing peptic ulcer recurrence in low-dose aspirin users |
| [19837071](https://pubmed.ncbi.nlm.nih.gov/19837071/) | 2010 | RCT | Gastroenterology | Famotidine was inferior to pantoprazole in preventing recurrence of aspirin-related ulcers or erosions |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Overview of pantoprazole as a proton pump inhibitor |
| [8180294](https://pubmed.ncbi.nlm.nih.gov/8180294/) | 1994 | Review | Aliment Pharmacol Ther | Pooled analysis of five trials: duodenal ulcer healing rates with pantoprazole 40 mg/day were significantly better than ranitidine at 2 and 4 weeks |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0103050R0AAAAAA | Pantoprazole gastro-resistant tablets 40 mg | Gastro-resistant tablet | Not stated in the data compiled for this report |

One valid single-ingredient authorisation is recorded, with no cancelled authorisations. The identifier shown follows a BNF-style coding format rather than a standard PL number, so it should be verified against the MHRA register. In the BNF, pantoprazole is classified among the proton pump inhibitors under gastrointestinal drugs (BNF section 1.3.5).

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): osteoporosis, postmenopausal osteoporosis, bone fracture and pernicious anaemia. These are consistent with known concerns about long-term PPI use, namely fracture risk and reduced vitamin B12 absorption.
- **Drug Interactions**: 100 interactions were identified in total. Examples from the 20 interactions listed:
  - **Major**: acalabrutinib, atazanavir
  - **Moderate**: hydrochlorothiazide, alpelisib, amphotericin B, amikacin, fenofibrate, apalutamide, atorvastatin, bosutinib, bumetanide, among others
  - **Minor**: acetylsalicylic acid, cyanocobalamin, axitinib, bortezomib, brivaracetam

Warnings and contraindications from the product label are not available in the data compiled for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence supports pantoprazole in active peptic ulcer disease: a completed Phase 3 randomised trial (n=323) plus several randomised comparisons against ranitidine and omeprazole. Because this is an existing indication, the main issue is confirming the licence and safety documentation rather than proving efficacy.

**To proceed, the following is needed:**
- Confirmation of the approved indication text, dosage form and PL number from the MHRA register, as these are missing from the licence record
- SmPC warnings and contraindications to complete the safety review, as label-based safety data are missing
- Verification of the NCT02084420 comparator and population, as the trial title is truncated
- Review of long-term use risks (bone health, vitamin B12 status) and the major interactions (atazanavir, acalabrutinib)
- Mechanism of action data from an authoritative source
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

