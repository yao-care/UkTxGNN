---
layout: default
title: Ciprofibrate
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 10
---

# Ciprofibrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Using this as a direct content-generation task against the given template — no codebase skill matches "write a repurposing report from a supplied evidence pack," so I'll produce the report following the v5 prompt's structure exactly, drawing only on data present in the JSON (no fabricated licences/history).

A few data-handling notes before the report:
- `taiwan_regulatory.licenses` is empty and `original_moa` is a data gap, so there is no "original indication" text to extract — I've stated this plainly rather than inventing one.
- Ciprofibrate's own predicted indications evidence pack flags that rank‑1 ("hyperlipoproteinemia") is the *classic* fibrate indication, not a novel hypothesis — I've kept that caveat visible rather than glossing over it.
- Safety fields are all data gaps → used the mandated fallback sentence.
- Not an antineoplastic drug → Cytotoxicity section omitted entirely.
- `DG001` (Blocking: missing label warnings/contraindications) is carried into Conclusion & Next Steps since it materially limits how far this candidate can proceed.

---

# Ciprofibrate: From Unlicensed Fibrate to Hyperlipoproteinemia

## One-Sentence Summary

Ciprofibrate is a fibrate-class lipid-lowering agent with no current UK marketing authorisation on file in this evidence pack. The TxGNN model's top-ranked prediction is **Hyperlipoproteinemia** — which, on review of the supporting literature, corresponds to the drug's long-established classical use rather than a genuinely novel repurposing hypothesis — supported by **0 registered clinical trials** and **20 publications**, including several historical randomised controlled trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no UK marketing authorisation on file); pharmacologically a fibrate historically used for hyperlipidaemia/hyperlipoproteinaemia |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available for Ciprofibrate in this evidence pack. However, the collected literature and the model's own rationale consistently describe it as a **PPAR-α (peroxisome proliferator-activated receptor alpha) agonist**. Activation of PPAR-α upregulates lipoprotein lipase (LPL) and apolipoprotein A-I/A-II expression, which together lower VLDL and triglyceride levels and produce a modest rise in HDL cholesterol.

Importantly, this mechanism maps directly onto the pathophysiology of hyperlipoproteinaemia (Fredrickson types IIa, IIb and IV) — elevated LDL, VLDL and/or triglycerides with reduced HDL. This is precisely the disorder that fibrates as a drug class, including ciprofibrate, were originally developed and extensively studied to treat.

For that reason, this should **not be read as a novel repurposing signal**: the predicted indication is essentially the drug's classical, well-characterised use rather than a new therapeutic hypothesis. The clinical value of this evidence pack lies less in "discovering" a new indication and more in confirming that TxGNN correctly recovers a well-known drug–disease relationship — useful as a sanity check on the model, but not something that would independently justify a repurposing programme. Several lower-ranked candidates in this pack (e.g. CETP deficiency, HTGL deficiency, CYP7A1 deficiency, familial hypercholesterolaemia) extend the same PPAR-α/lipid-lowering mechanism into related but less-established territory, and are correspondingly rated L5/Hold pending further evidence; two candidates (prostate fibroma, prostate/brain cancer susceptibility) are flagged in the source data itself as probable knowledge-graph noise with no biological or literature support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9015467](https://pubmed.ncbi.nlm.nih.gov/9015467/) | 1996 | RCT | Postgraduate Medical Journal | Multicentre, open, parallel-group trial (n=174) comparing ciprofibrate 100 mg/day with sustained-release bezafibrate 400 mg/day in type II hyperlipidaemia; both agents were effective and well tolerated. |
| [8831920](https://pubmed.ncbi.nlm.nih.gov/8831920/) | 1996 | Cohort/open-label | Atherosclerosis | Pooled efficacy/safety data from roughly 3,000 patients on ciprofibrate 100 mg/day across type IIa, IIb and IV hyperlipoproteinaemia; consistent reductions in total cholesterol, triglycerides, apoB and LDL-C. |
| [3994783](https://pubmed.ncbi.nlm.nih.gov/3994783/) | 1985 | RCT (double-blind, comparative) | Atherosclerosis | 3-month double-blind comparison of ciprofibrate 100 mg/day vs fenofibrate 300 mg/day; both reduced TC, LDL-C and VLDL-C and increased HDL-C and apoA. |
| [12915663](https://pubmed.ncbi.nlm.nih.gov/12915663/) | 2003 | Clinical mechanistic study | Journal of Clinical Endocrinology and Metabolism | Ciprofibrate 100 mg/day in patients with type IIb hyperlipidaemia reduced atherogenic VLDL subclasses and enhanced HDL-mediated cholesterol efflux. |
| [17414592](https://pubmed.ncbi.nlm.nih.gov/17414592/) | 2007 | Clinical study | American Journal of Therapeutics | Ciprofibrate reduced non-HDL cholesterol and triglycerides while raising HDL-C in patients with Fredrickson type IV dyslipidaemia. |
| [6753860](https://pubmed.ncbi.nlm.nih.gov/6753860/) | 1982 | RCT (double-blind, placebo-controlled) | Atherosclerosis | Randomised, placebo-controlled 12-week trial of ciprofibrate 50/100 mg/day in type II hypercholesterolaemia; dose-dependent lipid lowering, well tolerated. |
| [2289217](https://pubmed.ncbi.nlm.nih.gov/2289217/) | 1990 | Multicentre trial | Clinical Therapeutics | Italian multicentre study of 127 diet-resistant patients with type IIa/IIb hyperlipidaemia on ciprofibrate 100 mg/day for 12 weeks; significant reductions in TC, LDL-C, VLDL-C, TG and apoB, with increases in HDL-C and apoA-I. |
| [11048518](https://pubmed.ncbi.nlm.nih.gov/11048518/) | 2000 | Multicentre cohort | Vnitřní Lékařství | 633 patients across 23 Czech centres treated with ciprofibrate (Lipanor) 100 mg/day for 3 months; cholesterol fell 13%, triglycerides fell over 41%, HDL-C rose 15%. |
| [6951582](https://pubmed.ncbi.nlm.nih.gov/6951582/) | 1982 | Dose-response study | Atherosclerosis | Dose-response study (50/100/200 mg/day) in 50 patients with type IIA/IIB/IV hyperlipoproteinaemia; 200 mg/day gave the greatest lipid-lowering effect, normalising LDL-C in types IIA/IIB. |
| [9364979](https://pubmed.ncbi.nlm.nih.gov/9364979/) | 1997 | Comparative study | Thrombosis and Haemostasis | Compared effects of gemfibrozil and ciprofibrate on t-PA, PAI-1 and fibrinogen in hyperlipidaemic patients, exploring haemostatic effects beyond lipid lowering. |

---

## UK Market Information

Ciprofibrate is not currently marketed in the UK — this evidence pack records no active MHRA marketing authorisations (0 licences on file). Any repurposing pathway would therefore need to proceed via a new marketing authorisation application or an equivalent regulatory route, not a variation to an existing licence.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: This evidence pack flags the absence of label warnings/contraindications and drug-drug interaction data as a blocking gap for formal safety evaluation — see Conclusion and Next Steps below.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between ciprofibrate's PPAR-α-mediated lipid-lowering activity and hyperlipoproteinaemia is strong and well supported by decades of published RCTs and cohort studies — but this reflects the drug's classical, long-established use rather than a novel repurposing opportunity, and no registered clinical trials currently exist for this specific indication in this dataset.

**To proceed, the following is needed:**
- Structured mechanism-of-action data (currently a data gap; sourced provisionally from literature/rationale text only)
- SmPC/label warnings and contraindications (flagged as a **blocking** gap in this evidence pack — required before any formal safety (S1) evaluation can proceed)
- Formal drug-drug interaction (DDI) data (current query returned no results)
- Clarification of regulatory strategy given zero existing UK marketing authorisations
- A reassessment of whether this candidate merits further repurposing investment, given that the top-ranked prediction largely reproduces ciprofibrate's known pharmacological class use rather than identifying a new therapeutic avenue
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

