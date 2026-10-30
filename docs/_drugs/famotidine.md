---
layout: default
title: Famotidine
parent: Model Prediction Only (L5)
nav_order: 275
evidence_level: L5
indication_count: 4
monitor_inn: "Famotidine"
predicted_indications: ["duodenal obstruction", "abnormality of glucagon secretion", "multiple endocrine neoplasia", "acne (disease)"]
last_modified_at: 2026-10-30
description: "Famotidine: predicted new indication duodenal obstruction (evidence level L5). Approved use: Not recorded in the local data"
---

# Famotidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Famotidine: H2-receptor antagonist → duodenal obstruction
{: .text-alpha }

## One-Sentence Summary

Famotidine is a histamine H2-receptor antagonist that reduces gastric acid secretion.
The TxGNN model predicts it may be relevant to **duodenal obstruction**, with a score of 0.9999.
There are **no registered clinical trials** and only **2 publications** (both case reports that do not test famotidine) in the data compiled for this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | duodenal obstruction |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Famotidine is known as an H2-receptor antagonist acting on gastric parietal cells to reduce acid secretion.

There is no clear mechanistic link between this action and duodenal obstruction. Obstruction is a mechanical or structural problem, for example from Crohn's disease involvement or a complicated marginal ulcer, and is managed surgically or endoscopically. Acid suppression might help adjunctively where ulceration is present, but it is not a treatment for the obstruction itself. The high TxGNN score probably reflects proximity to ulcer-related conditions in the model rather than a tested therapeutic effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9306611](https://pubmed.ncbi.nlm.nih.gov/9306611/) | 1997 | Case report | Surgery today | Surgical treatment of duodenal Crohn's disease with persistent gastric outlet obstruction in one patient; famotidine not tested |
| [8165479](https://pubmed.ncbi.nlm.nih.gov/8165479/) | 1994 | Case report | Surgical endoscopy | Giant marginal ulcer after gastroenterostomy, a complication that can include obstruction; famotidine not tested |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0103010H0AAAAAA | Famotidine_Tab 20mg | Not recorded | Not recorded |

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Drug Interactions:** The interaction screening returned 100 records, mostly of Moderate severity. Examples include:
- Abiraterone (Moderate)
- Acalabrutinib (Moderate)
- Amiodarone (Moderate)
- Amitriptyline (Moderate)
- Tramadol (Moderate)
- Alendronic acid (Minor)
- Aluminium hydroxide (Minor)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study tests famotidine in duodenal obstruction, and the two retrieved publications are case reports on other surgical problems. The mechanism does not support a direct benefit, so the prediction rests on the model score alone (evidence level L5).

**To proceed, the following is needed:**
- Any controlled or observational study of famotidine specifically in duodenal obstruction
- A clear mechanistic rationale beyond adjunctive acid suppression
- Mechanism of action data and SmPC warnings and contraindications for a full safety review
- Review of the interaction records for clinically relevant combinations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

