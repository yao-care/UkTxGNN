---
layout: default
title: Methysergide
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 7
---

# Methysergide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Methysergide: From Unrecorded Original Indication to Migraine Disorder

## One-Sentence Summary

> Methysergide's originally licensed indication is not recorded in this evidence pack, though the literature confirms it is a semisynthetic ergot alkaloid used since the 1960s for **migraine prophylaxis**. The TxGNN model predicts efficacy for **Migraine Disorder** with a **99.95%** score, supported by **1 clinical trial** and **20 publications** — however, this most likely represents re-identification of a well-established historical use rather than a genuine new repurposing signal, since the drug's `original_indications` field was empty when the model ran.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the evidence pack (source data gap); literature indicates historical use as a migraine prophylactic agent since the 1960s |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 (as scored in evidence pack — see caveat under "Why is this prediction reasonable?") |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The structured mechanism-of-action field for methysergide is not populated in this evidence pack. Based on the pharmacological information available, methysergide is a semisynthetic ergot alkaloid (a methylated derivative of methylergometrine, itself derived from lysergic acid) that acts as an antagonist at 5‑HT2A/5‑HT2B/5‑HT2C serotonin receptors, with partial agonist activity at 5‑HT1 receptors. This blocks serotonin-mediated cranial vasodilation and neurogenic inflammation — the classical mechanism underpinning migraine prophylaxis.

Importantly, "migraine disorder" is very likely **not a novel repurposing candidate** for this drug. Methysergide (marketed historically as Sansert/Deseril) was one of the original migraine-prophylactic agents used clinically from the 1960s onward. It appears here as a high-scoring TxGNN prediction because the `original_indications` field in the source data was empty — the model is essentially rediscovering the drug's own established use rather than identifying a genuinely new therapeutic direction. This should be treated as a data-quality artefact requiring confirmation before it is presented as a "repurposing" opportunity.

The same 5‑HT2B agonist activity that gives methysergide its therapeutic effect on cranial vessels is also responsible for its well-documented fibrotic toxicity (retroperitoneal fibrosis, pleuropulmonary fibrosis, and restrictive cardiac valvulopathy caused by fibroblast stimulation), which led to its withdrawal from many markets and the requirement for mandatory "drug holidays" during long-term use. The same serotonergic pathway is also implicated — in the opposite, harmful direction — in the pathogenesis of pulmonary arterial hypertension, underscoring a narrow therapeutic window for this pharmacological class.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00460616](https://clinicaltrials.gov/study/NCT00460616) | N/A | Completed | 50 | Observational study of cardiac valvular abnormalities/regurgitation in patients on chronic dopamine agonist therapy (cabergoline). Not a methysergide efficacy trial — included here as an analogous class safety signal, since ergot-derived 5‑HT2B agonists (methysergide, pergolide, cabergoline) share a mechanism-based risk of fibrotic valvulopathy. |

No trials directly evaluating methysergide's efficacy in migraine were captured in this evidence pack; historical efficacy trials (e.g. 1960s open-label studies) predate structured clinical trial registries.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27449673](https://pubmed.ncbi.nlm.nih.gov/27449673/) | 2017 | Survey/Review | Cephalalgia | International Headache Society survey: 71.3% of respondents had prescribed methysergide for migraine/cluster headache; 79.8% would prescribe it again if reintroduced, despite EMA safety review. |
| [9793694](https://pubmed.ncbi.nlm.nih.gov/9793694/) | 1998 | Review | Cephalalgia | Comprehensive review confirming methysergide's efficacy as a 5‑HT2 antagonist/5‑HT1 agonist in migraine prophylaxis, particularly in high-frequency resistant cases; outlines contraindications. |
| [22444161](https://pubmed.ncbi.nlm.nih.gov/22444161/) | 2012 | Review | Headache | Basic science review comparing methysergide, ergotamine, dihydroergotamine and sumatriptan as 5‑HT1B/1D/1F agonists relevant to migraine treatment. |
| [6398056](https://pubmed.ncbi.nlm.nih.gov/6398056/) | 1984 | Review | Aust NZ J Med | Review of serotonin antagonists including methysergide across migraine and other serotonin-mediated conditions. |
| [18644039](https://pubmed.ncbi.nlm.nih.gov/18644039/) | 2008 | Historical Review | Cephalalgia | History of methysergide's development from lysergic acid and its introduction as an anti-serotonin migraine therapy. |
| [4885283](https://pubmed.ncbi.nlm.nih.gov/4885283/) | 1968 | Review | Proc Aust Assoc Neurol | Early clinical appraisal of methysergide in migraine. |
| [2045831](https://pubmed.ncbi.nlm.nih.gov/2045831/) | 1991 | Review | J Neurol | Reviews 5‑HT2 receptor antagonists (methysergide, pizotifen, cyproheptadine) in migraine prophylaxis. |
| [25217187](https://pubmed.ncbi.nlm.nih.gov/25217187/) | 2014 | Review | Eur J Clin Pharmacol | Reviews lactation risk of common anti-migraine drugs, including methysergide. |
| [9829155](https://pubmed.ncbi.nlm.nih.gov/9829155/) | 1998 | Review | Drugs | Practical guide to migraine management and prevention, situating methysergide among prophylactic options. |
| [31889312](https://pubmed.ncbi.nlm.nih.gov/31889312/) | 2020 | Review | Headache | Modern perspective on the migraine treatment pipeline (CGRP antibodies, neurostimulation), contextualising older agents such as methysergide. |

---

## UK Market Information

No MHRA marketing authorisations are currently on record for methysergide (0 licenses). The product (formerly marketed as Deseril®/Sansert®) is understood to have been withdrawn from the UK market historically, consistent with the fibrotic and cardiac valvulopathy safety concerns described above. This should be verified against the current MHRA products register before any regulatory conclusions are drawn.

---

## Safety Considerations

**Known Safety Signals (from literature and mechanistic evidence in this pack):**
- Long-term use is associated with **retroperitoneal, pleuropulmonary and cardiac valvular fibrosis**, mediated by 5‑HT2B receptor agonism on fibroblasts — historically the principal reason for market withdrawal and for mandatory periodic "drug holidays" during treatment.
- The same serotonergic mechanism has been separately linked in the literature to the pathogenesis of **pulmonary arterial hypertension**, suggesting this should be treated as a caution/contraindication direction rather than a therapeutic opportunity for that condition.
- Ergotism (peripheral vasospasm/ischaemia) has been reported with methysergide and related ergot alkaloids.

No structured MHRA/SmPC-derived warnings, contraindications, or drug interaction data were available in this evidence pack. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Migraine efficacy is well supported qualitatively across decades of literature, but the "new indication" signal most likely reflects rediscovery of methysergide's own historical licensed use rather than genuine repurposing, and the drug carries serious, mechanism-linked fibrotic and cardiac toxicity that historically led to market withdrawal.

**To proceed, the following is needed:**
- Confirmation of the drug's actual original licensed indication(s) (currently unrecorded) to determine whether this is a true repurposing case or a data-artefact re-identification
- TFDA/MHRA product label (SmPC) for formal warnings, contraindications and monitoring requirements (currently blocking — DG001)
- Confirmed DrugBank mechanism-of-action data (currently high-severity gap — DG002)
- A structured cardiac/fibrosis monitoring and "drug holiday" protocol before any clinical use is considered, given the class-level valvulopathy risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

