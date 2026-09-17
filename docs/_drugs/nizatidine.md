---
layout: default
title: Nizatidine
parent: High Evidence (L1-L2)
nav_order: 421
evidence_level: L1
indication_count: 7
---

# Nizatidine
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **7** 
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

# Nizatidine: From Peptic Ulcer Disease (Established Use) to Active Peptic Ulcer Disease (TxGNN Top Prediction)

## One-Sentence Summary

Nizatidine is a histamine H2-receptor antagonist historically used to treat duodenal and gastric ulcer disease. The TxGNN model's top-ranked prediction for this drug is **Active Peptic Ulcer Disease** — but this is, in fact, nizatidine's own long-established indication rather than a genuinely novel use. The signal is strongly supported by **6 randomised controlled trials** and **4 further reviews/cohort studies** from the 1980s–1990s, confirming the model has correctly recovered known pharmacology rather than uncovering a new repurposing opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic/duodenal ulcer disease (H2-receptor antagonist class; established use — no formal licence text available in this evidence pack) |
| Predicted New Indication | Active Peptic Ulcer Disease *(caveat: this is the drug's own known indication, not a novel signal — see below)* |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The evidence pack flags `original_moa` as a data gap (DG002), but this reflects a gap in the source dataset, not genuine pharmacological uncertainty. The extensive literature attached to this candidate confirms nizatidine's mechanism clearly: it is a histamine H2-receptor antagonist that inhibits basal, nocturnal and stimulated gastric acid secretion by blocking H2 receptors on gastric parietal cells — a mechanism directly relevant to healing acid-related mucosal lesions.

The relationship between "original" and "predicted" indication here is, unusually, one of near-identity. Nizatidine's approved and studied use has always been peptic/duodenal ulcer disease; the top TxGNN prediction of "active peptic ulcer disease" is therefore a **confirmatory recovery of known pharmacology**, not a repurposing discovery. The model's rationale in this evidence pack explicitly acknowledges this ("非真正老藥新用" — not true drug repurposing), which is an important caveat for decision-makers: the very high score and L1 evidence level here demonstrate the model is working correctly, but they do not represent new therapeutic value.

Mechanistically, the fit is nonetheless excellent — acid suppression is the direct, guideline-recognised treatment for peptic ulcer disease, which is why decades of RCT data exist. For genuine repurposing interest, the more informative signals in this evidence pack sit at lower TxGNN ranks, e.g. gastroduodenitis/NSAID-induced mucosal injury prevention (rank 6, evidence level L3, with two direct nizatidine RCTs: PMID 7863248 and PMID 1969684), where the mechanistic extension beyond the original label is more genuine.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2570656](https://pubmed.ncbi.nlm.nih.gov/2570656/) | 1989 | RCT | Clin Pharmacol Ther | Two-phase, placebo-controlled trial: nizatidine 150 mg BID significantly promoted duodenal ulcer healing versus placebo |
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clin Pharmacol Ther | 8-week multicentre RCT: nizatidine (150 mg BID or 300 mg nocte) superior to placebo for benign gastric ulcer healing and symptom relief |
| [2892259](https://pubmed.ncbi.nlm.nih.gov/2892259/) | 1987 | RCT | Scand J Gastroenterol Suppl | 1-year maintenance RCT (n=513): nizatidine 150 mg nocte cut duodenal ulcer recurrence to 34% vs 64% with placebo at 12 months |
| [7960687](https://pubmed.ncbi.nlm.nih.gov/7960687/) | 1994 | RCT | Isr J Med Sci | Double-blind RCT: nizatidine promoted duodenal ulcer healing and reduced mucosal inflammatory mediators versus placebo |
| [9198292](https://pubmed.ncbi.nlm.nih.gov/9198292/) | 1997 | RCT | Chin Med J | RCT evaluating clarithromycin-based *H. pylori* eradication combination therapy in peptic ulcer disease |
| [1982108](https://pubmed.ncbi.nlm.nih.gov/1982108/) | 1990 | RCT | Hepatogastroenterology | 8-week randomised comparison: nizatidine (both dosing regimens) achieved comparable healing rates to ranitidine in gastric ulcer |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Early pharmacodynamic/pharmacokinetic review confirming nizatidine as a potent acid-secretion inhibitor with established efficacy in peptic ulcer disease |
| [2184124](https://pubmed.ncbi.nlm.nih.gov/2184124/) | 1990 | Review | Gastroenterol Clin North Am | Overview of medical therapy for peptic ulcer disease; nizatidine noted as safe and effective, comparable to other H2 blockers |
| [8097411](https://pubmed.ncbi.nlm.nih.gov/8097411/) | 1993 | Review | Bailliere's Clin Gastroenterol | Reviews the neural/hormonal/paracrine regulation of gastric acid secretion underlying H2-antagonist mechanism |
| [1974318](https://pubmed.ncbi.nlm.nih.gov/1974318/) | 1990 | Cohort | Medicina (Firenze) | Nizatidine reduced gastric pepsin concentration and raised gastric pH in duodenal ulcer patients, versus misoprostol |

## UK Market Information

No MHRA marketing authorisations are recorded for nizatidine in this evidence pack (0 licences on file; market status: Not Marketed). As a member of the H2-receptor antagonist class, such products would normally fall under BNF Chapter 1.3.1 (H2-receptor antagonists) if and when marketed, but no current UK product-specific licence data is available to confirm this for nizatidine.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: label-derived warnings, contraindications and drug-interaction data for nizatidine are recorded as a Blocking data gap in this evidence pack — see Conclusion below.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking-severity data gap (DG001 — missing MHRA/TFDA label warnings and contraindications) prevents completion of the mandatory initial safety screening (S1), which overrides the otherwise favourable evidence-based staging (S3, "Proceed with Guardrails") assigned to the top-ranked indication.
- The top prediction, active peptic ulcer disease, is nizatidine's own long-established indication rather than a genuine repurposing candidate, so it offers limited incremental value even once the safety data gap is resolved.

**To proceed, the following is needed:**
- Retrieve and parse the MHRA/TFDA SmPC (warnings, contraindications, drug interactions) to resolve DG001 before any safety screening can proceed
- Confirm `original_moa` via the DrugBank API to close DG002 (the H2-antagonist mechanism is well documented in the attached literature but not yet captured in the structured drug record)
- If genuine repurposing value is the goal, prioritise lower-ranked but mechanistically distinct candidates with direct trial support instead — notably NSAID-induced gastroduodenitis prevention (rank 6, evidence level L3, supported by PMID 7863248 and PMID 1969684)
- Confirm current UK marketing status, since this evidence pack records nizatidine as not marketed with zero authorisations on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

