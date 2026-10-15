---
layout: default
title: Tapentadol
parent: Model Prediction Only (L5)
nav_order: 593
evidence_level: L5
indication_count: 3
---

# Tapentadol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tapentadol: From Pain Management to Migraine Disorder

## One-Sentence Summary

Tapentadol is an opioid analgesic that is currently marketed in the UK, although the data compiled for this report do not include an approved indication text.
The TxGNN model predicts it may be effective for **migraine disorder**, but this is a model prediction only, with **no clinical trials** and **no directly relevant publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Based on general pharmacological knowledge, tapentadol combines mu-opioid receptor agonism with noradrenaline reuptake inhibition. In theory, this dual action could modulate central pain pathways that are also relevant to migraine.

The TxGNN score is very high (0.997), but it reflects a knowledge-graph prediction only. The mechanistic link is speculative. Opioids are generally discouraged for migraine because of the risk of medication-overuse headache, chronification and dependence.

Two related predictions were also returned: migraine with brainstem aura (score 99.57%) and migraine with or without aura, susceptibility to (score 99.08%). The first probably reflects propagation from the parent migraine node. The second describes genetic susceptibility rather than a treatable clinical condition, so it is of limited practical use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications directly test tapentadol in migraine. Two indirect publications were retrieved for the related prediction "migraine with or without aura, susceptibility to":

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29760569](https://pubmed.ncbi.nlm.nih.gov/29760569/) | 2018 | Cohort | Drug, Healthcare and Patient Safety | Opioids are not recommended for routine migraine treatment because the risks of medication-overuse headache and dependence outweigh the benefits. Examines concomitant opioid use with triptans or serotonergic antidepressants, following a safety warning about serotonin syndrome. |
| [33689517](https://pubmed.ncbi.nlm.nih.gov/33689517/) | 2021 | Review | Expert Opinion on Pharmacotherapy | Reviews NSAIDs and paracetamol as non-opioid alternatives to opioids for acute pain, amid concerns about opioid overdose. |

Neither paper provides efficacy evidence for tapentadol in migraine. The 2018 study raises a safety signal rather than support for efficacy.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0407020AGAAAAAA | Tapentadol HCl tablets 50 mg | Not specified | Not specified |

The number shown is a BNF-style product code rather than a standard PL number. Please check the MHRA record and the BNF (opioid analgesics section) for the authorised indications and formulations.

## Safety Considerations

**Drug Interactions**

The interaction check returned 100 interacting drugs in total. Examples of those flagged as **Major**:
- Bupropion
- Morphine
- Lorcaserin
- Diethylpropion
- Phentermine
- Dolasetron
- Palonosetron

Examples flagged as **Moderate** include epinephrine, atropine, hyoscyamine, glycopyrronium, dicyclomine, trospium, naloxone, nabilone, dronabinol and eluxadoline.

**Migraine-specific consideration:** The literature highlights a risk of serotonin syndrome when opioids are used with triptans or serotonergic antidepressants (SSRIs/SNRIs). Tapentadol's noradrenaline reuptake inhibition makes this relevant to any migraine use.

Please also refer to the SmPC and BNF for warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any clinical trials or directly relevant literature (Evidence Level L5). Opioids are generally discouraged in migraine because of medication-overuse headache and dependence, and there is a potential serotonin-syndrome interaction with commonly used migraine treatments.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to assess the link to migraine pathophysiology
- The approved indications and formulations from the SmPC or MHRA record
- Warnings and contraindications from the SmPC and BNF, so that safety screening can proceed
- Preclinical or clinical studies of tapentadol in migraine, including assessment of medication-overuse headache risk
- Comparison against existing guideline-recommended migraine treatments, such as NICE-recommended options, to establish whether a role exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

