---
layout: default
title: Atomoxetine Hcl
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 0
---

# Atomoxetine Hcl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Atomoxetine Hydrochloride: Repurposing Evaluation — Insufficient Evidence Pack Data

---

## One-Sentence Summary

Atomoxetine hydrochloride is a selective norepinephrine reuptake inhibitor (NRI) licensed in multiple countries for the treatment of attention-deficit/hyperactivity disorder (ADHD). The current Evidence Pack contains **no TxGNN-predicted new indications** and several unresolved data gaps of blocking or high severity. A full repurposing evaluation **cannot be completed** until these gaps are remediated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) *(from general pharmacological knowledge; not recorded in Evidence Pack)* |
| Predicted New Indication | None available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — prediction stage not reached |
| UK Market Status | Not recorded in Evidence Pack *(see note below)* |
| Number of Marketing Authorisations | 0 (per Evidence Pack) |
| Recommended Decision | **Hold** |

> **⚠ Market Status Discrepancy:** The Evidence Pack records zero MHRA licences and a "not marketed" status. This is inconsistent with known regulatory information: atomoxetine (Strattera®, Eli Lilly) holds MHRA marketing authorisation for ADHD in children, adolescents, and adults, and is listed in the BNF (Chapter 4 — CNS stimulants and other drugs for ADHD). The MHRA regulatory data collection step should be re-run before this report is finalised.

---

## Why is This Prediction Reasonable?

No TxGNN prediction has been generated for this candidate, so no formal mechanism-to-new-indication bridge can be constructed at this stage.

From general pharmacological knowledge: atomoxetine is a potent and selective inhibitor of the presynaptic norepinephrine transporter (NET), increasing norepinephrine availability primarily in the prefrontal cortex. Unlike methylphenidate and amphetamine-based treatments, it has no clinically significant dopamine transporter (DAT) activity at therapeutic doses, which underpins its status as a non-controlled medicine in the UK — a practically important distinction for prescribers.

Until the TxGNN prediction pipeline has been re-run with a confirmed DrugBank ID and mechanism of action, a mechanistically reasoned repurposing hypothesis cannot be presented. Please refer to the data gap remediation steps in the **Conclusion** section below.

---

## Clinical Trial Evidence

Currently no clinical trial evidence is linked to a predicted repurposing indication. Once a TxGNN prediction is available, this section will be populated with relevant registered trials from ClinicalTrials.gov, ISRCTN, and the EU Clinical Trials Register.

---

## Literature Evidence

Currently no literature evidence is linked to a predicted repurposing indication. Once a TxGNN prediction is available, this section will be populated with relevant PubMed publications.

---

## UK Market Information

The Evidence Pack records no MHRA marketing authorisations for this drug. As noted above, this appears to be a data collection gap rather than a true absence of authorisation. The table below cannot be populated until the MHRA data collection step is successfully re-run.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|--------------|-------------|---------------------|
| *Not recorded — data collection required* | — | — | — |

---

## Safety Considerations

No safety data is available in the current Evidence Pack. Please refer to the **Strattera Summary of Product Characteristics (SmPC)** available via the MHRA or electronic Medicines Compendium (emc), and consult **BNF Chapter 4** for prescribing guidance. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN-predicted indications, no MHRA licence data, and no safety information; a meaningful repurposing evaluation is not possible without first resolving the outstanding data gaps.

**To proceed, the following is needed:**

1. **Resolve Blocking Data Gap (DG001) — MHRA SmPC warnings and contraindications:** Download the Strattera SmPC PDF from the MHRA website or emc (https://www.medicines.org.uk/emc) and parse key warnings and contraindications.
2. **Resolve High-Priority Data Gap (DG002) — Mechanism of action:** The DrugBank ID is currently null. Search the DrugBank API using the INN "atomoxetine" to retrieve the confirmed DrugBank ID, full MOA, pharmacodynamic data, and toxicity profiles.
3. **Re-run MHRA regulatory data collection:** Repopulate licence records to correctly reflect Strattera's current MHRA authorisation status, dosage forms, and approved indications.
4. **Re-run TxGNN prediction pipeline:** Once the DrugBank ID, MOA, and regulatory data are confirmed, resubmit the drug to the TxGNN model to generate ranked repurposing candidates with confidence scores.
5. **Collect drug interaction data:** No DDI records were returned. Once the DrugBank ID is confirmed, re-query the DrugBank interaction database and cross-reference with the MHRA/BNF interaction checker.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

