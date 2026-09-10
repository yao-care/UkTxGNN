---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 267
evidence_level: L5
indication_count: 2
---

# Fentanyl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Using no additional skill — this is a direct report-generation task with a fully specified template, not something requiring brainstorming, debugging, or a domain skill.

I'm using **predicted_indications[0]** (rank 1, "nephrogenic syndrome of inappropriate antidiuresis", the highest-scoring TxGNN prediction) as the primary subject per the template's field-extraction rules. Its `scoring` block was left as `"pending"` in the pack, so I derived Evidence Level myself from the actual evidence counts (0 trials, 0 literature → L5) and set the recommendation to Hold consistent with that level and with rank 2's own Hold outcome under identical evidence conditions.

---

# Fentanyl: From Severe Pain Management to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a well-established potent opioid analgesic, most familiar in the UK for severe and breakthrough pain management and anaesthesia. The TxGNN model predicts a possible link to **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests on the model score alone. (A second candidate indication, Tourette syndrome, was also flagged with a similarly high score and was independently assessed as Hold due to lack of mechanistic plausibility.)

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (data gap); Fentanyl is internationally established for severe/breakthrough pain management and anaesthesia |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is currently a data gap. Based on what is known, Fentanyl is a high-potency synthetic μ-opioid receptor agonist; its efficacy in severe pain control and anaesthesia is well established, but this pharmacology has no documented mechanistic connection to NSIAD.

NSIAD is a rare, typically hereditary condition caused by gain-of-function mutations in the vasopressin V2 receptor, which produces receptor activation and water retention independent of circulating antidiuretic hormone (ADH) levels. Opioids such as fentanyl are generally known to *suppress* ADH release rather than act on the V2 receptor itself, so there is no obvious pharmacological pathway linking fentanyl to a receptor-level, ADH-independent disorder like NSIAD.

The `repurposing_rationale` for this candidate was left as `"pending"` in the evidence pack, meaning no mechanistic linkage or similarity-to-original-indication analysis has actually been produced yet. This prediction should therefore be read as a raw knowledge-graph association rather than a mechanistically supported hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

No UK marketing authorisation records are currently available for Fentanyl in this evidence pack (market status: Not marketed; 0 licences on record).

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: the label warnings/contraindications field for this drug is flagged as a **Blocking** data gap in the evidence pack (unable to complete initial safety screening), and the drug interaction check returned no result (`not_found`). Given Fentanyl's known high-risk profile (opioid dependence, respiratory depression, extensive CYP3A4-mediated interactions), this gap should be closed before any further evaluation.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5 evidence, no trials or literature), the mechanistic rationale is explicitly unfilled/pending, and a **Blocking**-severity data gap in label warnings and contraindications means this candidate cannot even complete initial safety screening (S1). Combined with Fentanyl's inherently high-risk safety profile as a potent opioid, there is no basis to proceed at this time.

**To proceed, the following is needed:**
- MHRA/manufacturer SmPC warnings and contraindications (currently Blocking gap)
- Mechanism-of-action data confirming or refuting a plausible pathway to NSIAD
- A completed mechanistic rationale and similarity-to-original-indication analysis (currently marked "pending")
- Any preclinical, case-report, or observational evidence, however limited, to move beyond pure model prediction
- Drug interaction data (current query returned no result)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

