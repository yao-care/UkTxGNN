---
layout: default
title: Memantine
parent: Model Prediction Only (L5)
nav_order: 391
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Memantine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the data compiled for this report"
---

# Memantine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Memantine: From Dementia Treatment to Migraine Disorder

## One-Sentence Summary

Memantine is an NMDA receptor antagonist marketed in the UK in oral solution and tablet forms. The data compiled for this report do not record an approved indication for it.
The TxGNN model's most clinically supported prediction is **migraine disorder** (second-ranked overall; the top-ranked prediction, pulmonary hypertension, has no supporting studies), with **1 completed Phase 3 trial** and **19 publications**, including a meta-analysis of RCTs. The evidence base is small and of limited quality, so this should be treated as provisional.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report |
| Predicted New Indication | Migraine disorder (rank 2; selected because rank 1, pulmonary hypertension, has no supporting evidence) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L1 (provisional; based on one small Phase 3 trial) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Memantine is, however, a known non-competitive NMDA receptor antagonist, and the retrieved literature is consistent with that.

Glutamate and NMDA receptor signalling are implicated in migraine. This includes cortical spreading depression, central sensitisation and trigeminovascular activation. Blocking the NMDA receptor is therefore a plausible route to migraine prophylaxis. Reviews of glutamate receptors as migraine targets and of NMDA antagonists (memantine and ketamine) as anti-migraine agents support this reasoning.

The other predictions are weaker. Pulmonary hypertension and kyphoscoliotic heart disease have high scores but no supporting trials or relevant studies. Migraine with brainstem aura rests only on indirect extrapolation from general migraine data. Of the predictions retrieved, migraine disorder has by far the strongest support.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Phase 3 | Completed | 33 | Memantine compared with sodium valproate for prophylaxis of episodic migraine. Directly relevant, but the small sample and active-comparator design limit conclusions about efficacy over placebo. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Meta-analysis of RCTs | Clin Neuropharmacol | Examines memantine versus placebo in migraine patients; the efficacy of memantine for migraine is described as controversial. |
| [26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/) | 2016 | RCT | Headache | Double-blind, placebo-controlled study of memantine for prophylaxis of migraine without aura. |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Network meta-analysis | Front Pharmacol | Compares the efficacy and safety of oral preventive medications for migraine in adults aged 18-65. |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Systematic review | Headache | Assesses the efficacy and safety of memantine for prophylaxis of episodic migraine. |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Review | Naunyn Schmiedebergs Arch Pharmacol | Presents memantine and ketamine as potential anti-migraine agents; some evidence of benefit. |
| [25159002](https://pubmed.ncbi.nlm.nih.gov/25159002/) | 2014 | Review | Ann Pharmacother | Reviews data on the efficacy and safety of memantine for preventing primary headache disorders. |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Commentary | Headache | "Big promise but little evidence": highlights the limited evidence base for memantine in migraine. |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Retrospective study | J Headache Pain | Retrospective study of 60 patients given memantine as migraine preventive therapy. |
| [29508147](https://pubmed.ncbi.nlm.nih.gov/29508147/) | 2018 | Review | Neurotherapeutics | Glutamate and its receptors as therapeutic targets in migraine. |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Clinical practice guideline | Ann Intern Med | 2023 US VA/DoD guideline on the management of headache, covering migraine treatment and prevention. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0411000G0AAABAB | Memantine HCl oral solution 5 mg/pump | Oral solution | Not stated |
| 0411000G0AAAAAA | Memantine HCl tablets 10 mg | Tablet | Not stated |

Both authorisations are valid single-ingredient products. The data compiled for this report do not include approved indication text, so please check the BNF and SmPC for the licensed indication and any NICE-appraised use. Migraine prophylaxis would be off-label use.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug-disease links, not label text): liver disease, gallbladder disease and impaired renal function.
- **Drug Interactions**: 100 interactions were recorded. Those listed in the data include:
  - **Moderate**: anticholinergic or antimuscarinic agents (hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, methscopolamine, propantheline, scopolamine, trospium, mepenzolate).
  - **Minor**: ranitidine, metformin, cimetidine, potassium citrate.
  - **Unknown severity**: glimepiride, doxycycline, lansoprazole, loperamide, famotidine, acetylsalicylic acid.
- **Monitoring in a migraine setting**: the data suggest watching for dizziness, headache and somnolence, and checking renal function and concomitant medicines.

Label warnings and contraindications are not available in the data compiled for this report. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Migraine disorder is the only prediction with a completed Phase 3 trial and meta-analytic evidence. However, the trial is small (n=33) and compared memantine with an active drug rather than placebo. The literature itself describes the evidence as limited, so the L1 grade is provisional. The other predictions (pulmonary hypertension, kyphoscoliotic heart disease, migraine with brainstem aura) are not supported by direct evidence and should be held or treated as research questions.

**To proceed, the following is needed:**
- Larger, adequately powered, placebo-controlled RCTs in migraine prophylaxis
- Critical appraisal of the existing meta-analysis (PMID 33961371) and the Phase 3 trial results
- Confirmation of the licensed indications and labelled warnings from the SmPC and BNF
- Mechanism of action data to be added to the record
- A medicines-review and renal function check plan, given the large number of recorded interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

