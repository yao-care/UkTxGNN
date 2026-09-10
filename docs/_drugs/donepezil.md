---
layout: default
title: Donepezil
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 8
---

# Donepezil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Donepezil: From Alzheimer's Disease to Movement and Tic Disorder Spectrum

## One-Sentence Summary

Donepezil is a cholinesterase inhibitor originally used for Alzheimer's disease/dementia. This evidence pack contains **8 TxGNN-predicted candidate indications** spanning movement disorders and tic disorders, headed by **psychogenic movement disorders** (TxGNN score 99.23%), but this lead candidate has **zero supporting clinical trials or literature** — it is a model-only prediction. Across all 8 candidates combined, evidence remains sparse and inconsistent: no clinical trials were found for any candidate, and only 3 of 8 have any literature at all.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease / dementia (cholinesterase inhibitor) — derived from literature cited in this pack, as formal DrugBank/regulatory records were not available |
| Predicted New Indication (lead candidate) | Psychogenic movement disorders |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| UK Market Status | Not marketed *(0 licences on record — see caveat below)* |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

**Note on market status:** this evidence pack records donepezil as having zero UK marketing authorisations, which is inconsistent with donepezil's long-established UK availability (e.g. as Aricept). This most likely reflects an incomplete regulatory-data capture in this pipeline run (consistent with the blocking data gap DG001, below) rather than genuine unavailability. It should not be relied upon as confirmation of market status.

### Other TxGNN-Predicted Candidates in This Pack

This candidate record ("multi") groups 8 predicted indications for donepezil. For completeness, all are summarised here rather than in isolation:

| Rank | Disease | TxGNN Score | Evidence Level | Trials | Literature | Decision |
|------|---------|------|------|------|------|------|
| 1 | Psychogenic movement disorders | 99.23% | L5 | 0 | 0 | Hold |
| 2 | Chronic tic disorder | 99.19% | pending (≈L3, see below) | 0 | 5 | pending |
| 3 | Primary orthostatic tremor | 99.17% | L5 | 0 | 0 | Hold |
| 4 | Extrapyramidal and movement disease | 99.16% | L4 | 0 | 4 | Hold |
| 5 | Benign shuddering attacks | 99.16% | L5 | 0 | 0 | Hold |
| 6 | Tremor-nystagmus-duodenal ulcer syndrome | 99.15% | L5 | 0 | 1 (unrelated case report) | Hold |
| 7 | Benign paroxysmal tonic upgaze of childhood with ataxia | 99.12% | L5 | 0 | 0 | Hold |
| 8 | Lingual-facial-buccal dyskinesia (tardive dyskinesia spectrum) | 99.02% | pending (≈L3, Cochrane reviews present) | 0 | 20 | pending |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data was not available for this record (data gap DG002). Based on the literature captured in this pack itself, donepezil is consistently described as an acetylcholinesterase inhibitor (AChEI), the standard-of-care drug class for Alzheimer's disease (e.g. PMID 12611743, PMID 40224553). Cholinergic signalling is known to modulate basal ganglia and striatal circuits, which underlie both tic disorders and extrapyramidal movement disorders — this provides a plausible pharmacological bridge between donepezil's approved use in dementia and the movement/tic-disorder candidates predicted here.

However, the strength of this rationale varies sharply by candidate. For the **lead candidate, psychogenic movement disorders**, there is no mechanistic or clinical literature at all in this pack — the prediction rests solely on knowledge-graph embedding similarity, with no verifiable hypothesis. For **extrapyramidal and movement disease**, the literature is genuinely bidirectional: some reports describe donepezil ameliorating tardive movement disorders and Lewy body dementia psychosis, while a 2025 systematic review flags AChEIs as a possible *cause* of movement disorders as an adverse effect — the same mechanism argued to help may also harm, so no consistent treatment hypothesis emerges. The two candidates with the richest literature — **chronic tic disorder** and **lingual-facial-buccal dyskinesia** (essentially tardive dyskinesia) — are better supported, including small open-label trials and two Cochrane systematic reviews of cholinergic drugs (including donepezil) for tardive dyskinesia, but these have not yet been formally scored for evidence tier in this pack.

Overall, the mechanistic plausibility (cholinergic modulation of movement circuits) is real, but it is not uniformly supported across the 8 candidates, and for the top-ranked candidate specifically there is no evidence beyond the model score.

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 8 predicted indications. ClinicalTrials.gov and WHO ICTRP searches returned zero results across all candidate diseases queried in this pack.

## Literature Evidence

*No literature exists for ranks 1, 3, 5, and 7. Literature for the remaining candidates is presented below, grouped by indication.*

### Chronic tic disorder (rank 2)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18343255](https://pubmed.ncbi.nlm.nih.gov/18343255/) | 2008 | Open-label trial | Clinical Therapeutics | 18-week dose-escalating open-label study in children/adolescents with tics and ADHD; striatal cholinergic dysfunction proposed as relevant to both conditions |
| [10440471](https://pubmed.ncbi.nlm.nih.gov/10440471/) | 1999 | Case report | J Clin Psychopharmacol | Donepezil reported for Tourette's disorder and ADHD |
| [16986157](https://pubmed.ncbi.nlm.nih.gov/16986157/) | 2006 | Case report | Movement Disorders | Donepezil reported as possibly effective in Tourette's syndrome |
| [16045972](https://pubmed.ncbi.nlm.nih.gov/16045972/) | 2005 | Preclinical (mice) | Pharmacol Biochem Behav | Donepezil, nicotine and haloperidol effects on serotonergic system; proposed model for tic symptoms in Tourette's syndrome |
| [14643839](https://pubmed.ncbi.nlm.nih.gov/14643839/) | 2003 | Preclinical (mice) | Pharmacol Biochem Behav | Donepezil attenuates DOI-induced head-twitch response, proposed as a Tourette's syndrome model |

### Extrapyramidal and movement disease (rank 4)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40224553](https://pubmed.ncbi.nlm.nih.gov/40224553/) | 2025 | Systematic Review | Brain Circulation | Reviews movement disorders **associated with (i.e. caused by)** AChEIs in Alzheimer's dementia — an adverse-effect signal, not an efficacy signal |
| [15669896](https://pubmed.ncbi.nlm.nih.gov/15669896/) | 2005 | Case Series | J Clin Psychiatry | Donepezil reported beneficial for elderly patients with tardive movement disorders |
| [12671528](https://pubmed.ncbi.nlm.nih.gov/12671528/) | 2003 | Open-label add-on trial | Clin Neuropharmacol | Donepezil as add-on treatment for psychotic symptoms in Alzheimer's dementia (12 inpatients) |
| [14676467](https://pubmed.ncbi.nlm.nih.gov/14676467/) | 2004 | Narrative Review | Dement Geriatr Cogn Disord | Reviews pharmacologic management of dementia with Lewy bodies, including motor and psychotic features |

### Lingual-facial-buccal dyskinesia / tardive dyskinesia spectrum (rank 8) — top 10 of 20

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15610922](https://pubmed.ncbi.nlm.nih.gov/15610922/) | 2004 | Meta-analysis of RCTs | Prog Neuropsychopharmacol Biol Psychiatry | Systematic review/meta-analysis of cholinergic drugs (incl. donepezil) for neuroleptic-induced tardive dyskinesia |
| [29553158](https://pubmed.ncbi.nlm.nih.gov/29553158/) | 2018 | Cochrane Systematic Review | Cochrane Database Syst Rev | Cholinergic medication for antipsychotic-induced tardive dyskinesia |
| [12137608](https://pubmed.ncbi.nlm.nih.gov/12137608/) | 2002 | Cochrane Systematic Review | Cochrane Database Syst Rev | Earlier Cochrane review of cholinergic medication for neuroleptic-induced tardive dyskinesia |
| [17914039](https://pubmed.ncbi.nlm.nih.gov/17914039/) | 2007 | RCT | New England Journal of Medicine | Landmark RCT of donepezil for agitation in Alzheimer's disease (efficacy on behavioural, not dyskinesia, endpoints — tangential relevance) |
| [19142126](https://pubmed.ncbi.nlm.nih.gov/19142126/) | 2009 | Clinical report | J Clin Psychopharmacol | Effect of donepezil on tardive dyskinesia |
| [15689723](https://pubmed.ncbi.nlm.nih.gov/15689723/) | 2005 | Case report | J Am Acad Child Adolesc Psychiatry | Donepezil and tardive dyskinesia |
| [10634264](https://pubmed.ncbi.nlm.nih.gov/10634264/) | 2000 | Case report | Movement Disorders | Donepezil trialled for Huntington's disease |
| [18321753](https://pubmed.ncbi.nlm.nih.gov/18321753/) | 2008 | Case report (adverse effect) | Parkinsonism Relat Disord | Donepezil-induced jaw tremor — opposite-direction safety signal |
| [24127392](https://pubmed.ncbi.nlm.nih.gov/24127392/) | 2014 | Pharmacovigilance study | Pharmacotherapy | FAERS analysis linking cholinesterase inhibitors (incl. donepezil) to Pisa syndrome (a dystonia) |
| [40791064](https://pubmed.ncbi.nlm.nih.gov/40791064/) | 2025 | Systematic Review | J Huntington's Disease | Efficacy/safety of cholinesterase inhibitors and memantine for cognitive symptoms in Huntington's disease |

## UK Market Information

No MHRA marketing authorisation licences are recorded for donepezil in this evidence pack (0 licences). This is very likely a data-collection gap rather than a true absence from the UK market, and should be verified directly against the MHRA products database and BNF before being used in any regulatory or clinical decision.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Data gap flagged as blocking:** UK/MHRA label warnings and contraindications for donepezil were not available in this pack (DG001), which prevents any formal Stage 1 safety screening for these candidates. Notably, several of the literature findings above are themselves safety signals (donepezil-induced jaw tremor, Pisa syndrome/dystonia, movement disorders associated with AChEIs) rather than efficacy evidence, underscoring the need for the full label data before proceeding.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The lead candidate (psychogenic movement disorders) has no supporting evidence whatsoever — a pure model prediction (L5/S0).
- Across the other 7 candidates in this multi-indication record, evidence is either absent (4 candidates), directionally conflicted (extrapyramidal/movement disease — efficacy and adverse-effect literature coexist), or not yet formally scored despite moderate literature (chronic tic disorder; tardive dyskinesia spectrum).
- No clinical trials exist for any candidate, and the blocking safety data gap (DG001) prevents formal safety screening regardless of indication.

**To proceed, the following is needed:**
- Resolve DG001 (blocking): obtain MHRA SmPC warnings/contraindications for donepezil before any Stage 1 safety screening.
- Resolve DG002: obtain a formal DrugBank mechanism-of-action record.
- Complete the pending evidence-tier scoring for chronic tic disorder and lingual-facial-buccal dyskinesia, given the existing Cochrane-level literature already identified.
- Verify donepezil's actual UK marketing-authorisation status against the MHRA products database — the 0-licence record here appears to be a data gap, not a true finding.
- If the tardive-dyskinesia-spectrum indication is prioritised for further work, commission an updated systematic review building on the two Cochrane reviews already identified in this pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

