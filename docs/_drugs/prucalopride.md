---
layout: default
title: Prucalopride
parent: Model Prediction Only (L5)
nav_order: 528
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
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
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (4 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for prucalopride: "Prucalopride, a selective serotonin type 4 (5-HT 4 ) receptor agonist, is a gastrointestinal (GI) prokinetic agent that stimulates colonic peristalsis (high-amplitude propagating contractions [HAPCs]), which increases bowel motility. Prucalopride was devoid of effects mediated via 5-HT 2A, 5-HT 2B, 5-HT 3, motilin or CCK-A receptors in vitro at concentrations exceeding 5-HT 4 receptor affinity by 150-fold or greater." ([DailyMed: Motegrity (prucalopride) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bca1e4c6-4b2b-4876-8ab3-654629c4ff1b), label version 2025-07-17; accessed 2026-11-19.) Based on known pharmacology, prucalopride is a selective 5-HT4 receptor agonist that enhances gastrointestinal motility, and its efficacy in constipation is established.

For hypoalphalipoproteinemia (low HDL cholesterol), no credible mechanistic link could be identified. HDL metabolism and lipoprotein regulation are not known to involve 5-HT4 signalling in the gut. The high TxGNN score appears to be a TxGNN model (deep learning) prediction artefact rather than a pharmacologically grounded signal.

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

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0106070A0AAAAAA | Prucalopride 1mg tablets | Prucalopride |
| 0106070A0AAABAB | Prucalopride 2mg tablets | Prucalopride |
| 0106070A0BBAAAA | Resolor 1mg tablets | Prucalopride |
| 0106070A0BBABAB | Resolor 2mg tablets | Prucalopride |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Dosage form and approved indication text were not available, so please confirm details against the current SmPC.

<!-- review:begin uk-lic-20261106-prucalopride-1 -->

> **Review correction (2026-11-24)**: Originally stated: "One valid single-ingredient product is recorded. Dosage form and approved indication text were not available, so please confirm details against the current SmPC." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. The Quick Overview and the BNF code table under UK Market Information show the current number of BNF presentation codes. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-prucalopride-1 -->

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
- Authorisation details (PL number, dosage form, approved indication) for the UK products
- If a different direction is of interest, a focused review of prokinetic use for amyloid-related GI dysmotility, which is the only indirectly plausible signal, as symptom management rather than a new disease indication

<!-- review:begin uk-lic-20261124c-prucalopride-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Authorisation details (PL number, dosage form, approved indication) for the UK product" Corrected wording only: the text referred to a single UK product, licence or authorisation record, or called the UK market data licence or authorisation data. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902), which lists more than one BNF presentation code for this drug; these are NHS prescribing codes, not MHRA licences, and they carry no indication text. The phrase was changed to the plural or to BNF prescribing codes; the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124c-prucalopride-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "One valid single-ingredient product is recorded" | Corrected (revised 2026-11-24; earlier version kept in the record) | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Motegrity (prucalopride) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bca1e4c6-4b2b-4876-8ab3-654629c4ff1b) |
| 2026-11-24 | Corrected: "Authorisation details (PL number, dosage form, approved indication) for the UK product" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

