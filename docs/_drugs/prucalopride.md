---
layout: default
title: Prucalopride
parent: Model Prediction Only (L5)
nav_order: 528
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Prucalopride: predicted new indication Hypoalphalipoproteinemia (evidence level L5). Approved use: Constipation disorder"
monitor_inn: "Prucalopride"
predicted_indications: ["hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "duodenal ulcer (disease)", "oral candidiasis", "obsolete familial combined hyperlipidemia", "amyloidosis (disease)", "strongyloidiasis", "HIV infectious disease", "primary amyloidosis", "acquired amyloid peripheral neuropathy"]
---

# Prucalopride
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

## Prucalopride: From Constipation Disorder to Hypoalphalipoproteinemia
{: .text-alpha }

## One-Sentence Summary

Prucalopride is a selective 5-HT4 receptor agonist (a prokinetic) originally used to treat constipation.
The TxGNN model predicts it may be effective for **hypoalphalipoproteinemia**, but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation disorder |
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, prucalopride is a selective 5-HT4 receptor agonist that enhances gastrointestinal motility, and its efficacy in constipation is established.

For hypoalphalipoproteinemia (low HDL cholesterol), no credible mechanistic link could be identified. HDL metabolism and lipoprotein regulation are not known to involve 5-HT4 signalling in the gut. The high TxGNN score appears to be a knowledge-graph prediction artefact rather than a pharmacologically grounded signal.

Other top-ranked predictions show the same pattern. Homozygous familial hypercholesterolaemia, oral candidiasis, strongyloidiasis and HIV infection have no plausible mechanism and no supporting studies. The only predictions with even an indirect rationale are the amyloidosis-related ones (amyloidosis, primary amyloidosis), where a prokinetic could in theory relieve gut dysmotility symptoms. That would be symptom management, not treatment of the underlying disease. Duodenal ulcer has only a weak, speculative link, as prucalopride does not reduce acid secretion or address *H. pylori*.

## Clinical Trial Evidence

Currently no related clinical trials registered for hypoalphalipoproteinemia.

## Literature Evidence

Currently no related literature available for hypoalphalipoproteinemia.

For context, the only publications retrieved across the top-ranked predictions concern amyloidosis-related gut dysmotility. Neither tested prucalopride:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34231480](https://pubmed.ncbi.nlm.nih.gov/34231480/) | 2021 | Cohort | Turk J Gastroenterol | Specific GI motility disorders (gastroparesis, chronic intestinal pseudo-obstruction, colonic inertia) are often misdiagnosed as functional GI disorders in the early stage |
| [40376135](https://pubmed.ncbi.nlm.nih.gov/40376135/) | 2025 | Case report | Cureus | Amyloidosis presenting as chronic intestinal pseudo-obstruction in a 61-year-old man after multiple non-diagnostic laparotomies |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0106070A0AAABAB (BNF-style product code, not a PL number) | Prucalopride tablets 2 mg | Tablet | Not stated in the data compiled for this report |

One valid single-ingredient product is recorded. Dosage form and approved indication text were not available, so please confirm details against the current SmPC.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** ulcerative colitis, inflammatory bowel disease, intestinal perforation.
- **Drug Interactions:** 98 interactions are recorded. Examples include:
  - **Moderate:** aclidinium, atropine, benzatropine, biperiden, clidinium, glycopyrronium, hyoscyamine (anticholinergics, which may oppose the prokinetic effect), and the hormonal agents levonorgestrel, norethisterone and ethinylestradiol.
  - **Minor:** nifedipine, diltiazem, amiodarone, captopril, carvedilol, spironolactone, afatinib, alpelisib, cobicistat and conivaptan.

Please also refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hypoalphalipoproteinemia is supported only by a model score. There are no trials or publications, and no plausible link between 5-HT4 agonism and HDL metabolism. None of the other top-ranked predictions has direct evidence either.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking 5-HT4 agonism to lipoprotein metabolism, or a decision to deprioritise this prediction
- Mechanism of action data (MOA) for prucalopride from DrugBank
- Label-based warnings and contraindications from the SmPC and BNF, as the safety screen cannot proceed without them
- Authorisation details (PL number, dosage form, approved indication) for the UK product
- If a different direction is of interest, a focused review of prokinetic use for amyloid-related GI dysmotility, which is the only indirectly plausible signal, as symptom management rather than a new disease indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

