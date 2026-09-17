---
layout: default
title: Reboxetine
parent: High Evidence (L1-L2)
nav_order: 499
evidence_level: L1
indication_count: 10
---

# Reboxetine
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

Using this task as content generation against an already-fully-specified template — no ambiguity requiring brainstorming or debugging skills, so I'm proceeding directly.

One flag before the report: this Evidence Pack lists **10** TxGNN-predicted indications for Reboxetine, not one. The template's `predicted_indications[0]` (*benign paroxysmal torticollis of infancy*) is explicitly annotated in its own `repurposing_rationale` as "TxGNN embedding 雜訊預測" (model noise, no mechanistic plausibility) — L5/Hold. Reporting that as the headline prediction would be misleading. I've built the report around **Melancholia** (rank 5, but the only candidate reaching L1/"Proceed with Guardrails"), and added a supplementary table covering the other 9 candidates for transparency.

---

# Reboxetine: From Major Depressive Disorder to Melancholia

## One-Sentence Summary

Reboxetine is a selective noradrenaline reuptake inhibitor (NRI); the evidence pack contains no UK licensing record for it, but literature within the pack indicates it has been approved in several European countries for major depressive disorder (MDD). Among ten TxGNN-predicted indications reviewed, the model's strongest evidence-backed prediction is **Melancholia** (a recognised MDD subtype), supported by **20 publications** including RCT-based network meta-analyses, though **no dedicated clinical trials** for this specific diagnostic label were found. Several higher-scoring TxGNN predictions (e.g. benign paroxysmal torticollis of infancy, Ohdo syndrome) were reviewed and screened out as implausible model noise with no supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset (data gap in `original_indications`); literature evidence indicates European approval for major depressive disorder |
| Predicted New Indication | Melancholia |
| TxGNN Prediction Score | 99.74% (global rank 3,140) |
| Evidence Level | L1 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured `original_moa` field (data gap). However, the supporting literature is consistent: reboxetine is a highly selective noradrenaline reuptake inhibitor that binds the norepinephrine transporter with low affinity for serotonin/dopamine transporters and 45 other CNS receptors tested, distinguishing it pharmacologically from SSRIs and tricyclics (PMID 14978512).

Melancholia is a clinically recognised subtype of major depressive disorder, characterised by pronounced anhedonia and psychomotor disturbance. Since reboxetine's established efficacy signal sits within the broader MDD literature — supported by large network meta-analyses of antidepressants (PMID 29477251, PMID 19185342, PMID 36253442) — and its noradrenergic mechanism is directly relevant to mood regulation, extension to the melancholic subtype is mechanistically coherent rather than a cross-system inference.

One important caveat must be flagged: the BMJ systematic review by Eyding et al. (PMID 20940209) specifically re-analysed reboxetine trials including **unpublished data** and found that reboxetine's benefit-risk profile was less favourable than the published literature alone suggested — a well-known case of publication bias in this drug's evidence base. Any progression of this indication should explicitly account for that finding rather than rely on published-trial summaries alone.

### Other TxGNN-Predicted Indications (Screened Out)

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Note |
|------|---------|-------------|-----------------|----------|------|
| 1 | Benign paroxysmal torticollis of infancy | 99.92% | L5 | Hold | No mechanistic link; flagged as model noise |
| 2 | Agoraphobia | 99.91% | L3 | Research Question | Small open-label trials only (PMID 11838623, 12415550); no RCT for agoraphobia specifically |
| 3 | Dysthymic disorder | 99.87% | L5 | Hold | Class-level inference only, no direct evidence |
| 4 | Ohdo syndrome and variants | 99.76% | L5 | Hold | Genetic syndrome (KAT6A/KAT6B/MED13L); no plausible link |
| 6 | Neurotic depression | 99.74% | L2 | Research Question | Evidence based on general MDD trials; older diagnostic term, population match uncertain |
| 7 | Blepharophimosis–ID syndrome, Ohdo type | 99.70% | L5 | Hold | Rare genetic syndrome; no link |
| 8 | Neurotic disorder | 99.66% | L5 | Hold | Term too broad/non-specific; theoretical only |
| 9 | Keppen-Lubinsky syndrome | 99.54% | L5 | Hold | KCNJ6-related genetic syndrome; no link |
| 10 | Ligneous conjunctivitis | 99.40% | L5 | Hold | Plasminogen deficiency disorder; no link |

## Clinical Trial Evidence

Currently no related clinical trials registered for the Melancholia indication specifically.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/) | 2018 | Network Meta-analysis | Lancet | Ranked efficacy/acceptability of 21 antidepressants for acute MDD treatment |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Systematic Review/NMA | Molecular Psychiatry | Efficacy, acceptability, tolerability and safety of antidepressants in maintenance-phase MDD |
| [19185342](https://pubmed.ncbi.nlm.nih.gov/19185342/) | 2009 | Network Meta-analysis | Lancet | Multiple-treatments meta-analysis of 12 new-generation antidepressants for major depression |
| [20940209](https://pubmed.ncbi.nlm.nih.gov/20940209/) | 2010 | Systematic Review/Meta-analysis | BMJ | Reboxetine vs placebo/SSRI including unpublished trial data; found efficacy overestimated in published literature — key publication-bias caveat |
| [14978512](https://pubmed.ncbi.nlm.nih.gov/14978512/) | 2004 | Review | CNS Drug Reviews | Pharmacological and clinical profile of reboxetine; high NE transporter selectivity |
| [10901157](https://pubmed.ncbi.nlm.nih.gov/10901157/) | 2000 | Cohort/Safety study | Acta Psychiatr Scand Suppl | n=1,503 reboxetine vs n=1,027 comparator: no significant cardiovascular effects, low DDI potential, no cognitive/motor impairment, no increased suicidal ideation |
| [33549697](https://pubmed.ncbi.nlm.nih.gov/33549697/) | 2021 | Systematic Review/Meta-analysis | Prog Neuropsychopharmacol Biol Psychiatry | GI side-effect rates across second-generation antidepressants in MDD |
| [22859791](https://pubmed.ncbi.nlm.nih.gov/22859791/) | 2012 | Systematic Review | Nephrol Dial Transplant | Antidepressant pharmacokinetics/efficacy/safety in CKD stage 3–5 (ERBP recommendations) |
| [25911132](https://pubmed.ncbi.nlm.nih.gov/25911132/) | 2015 | Review (RCT-based) | J Affect Disord | Evidence-based dose-equivalence recommendations for antidepressants |
| [10651558](https://pubmed.ncbi.nlm.nih.gov/10651558/) | 2000 | Case Report | NEJM | Reboxetine-associated hyponatremia |

## UK Market Information

No UK marketing authorisations are currently recorded for reboxetine in this dataset (`taiwan_regulatory.total_licenses = 0`); market status is recorded as **Not marketed**. This should be independently verified against the current MHRA product database, as it conflicts with the drug's known European regulatory history discussed in the literature above.

## Safety Considerations

Official structured safety data (key warnings, contraindications, DDI) are not available in this evidence pack (all flagged as data gaps; DDI query returned no results). Please refer to the current SmPC and BNF for authoritative safety information, and report suspected adverse reactions via the Yellow Card Scheme.

From the literature evidence base itself, two signals are worth noting for any repurposing assessment:
- A case report of reboxetine-associated **hyponatremia** (PMID 10651558)
- The BMJ re-analysis (PMID 20940209) indicating reboxetine's benefit-risk profile is less favourable once unpublished trial data are included, relative to published-literature-only assessments

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Melancholia specifically; all other predicted indications in this pack are Hold or Research Question)

**Rationale:**
Melancholia is the only one of ten TxGNN-predicted indications reaching L1 evidence, underpinned by a large RCT/network meta-analysis literature base for antidepressant efficacy in MDD and a coherent noradrenergic mechanism. However, the drug-specific BMJ re-analysis flagging publication bias, the complete absence of official UK safety/label data, and the lack of melancholia-specific (vs general MDD) trials mean this cannot proceed without further work.

**To proceed, the following is needed:**
- Current MHRA/SmPC data for reboxetine (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Re-assessment of efficacy incorporating unpublished trial data per Eyding et al. 2010
- Independent verification of UK market/licensing status (dataset conflicts with known European approval history)
- Melancholia-subtype-specific trial evidence, as current literature is MDD-general rather than subtype-specific
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

