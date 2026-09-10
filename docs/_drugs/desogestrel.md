---
layout: default
title: Desogestrel
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
---

# Desogestrel
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

# Desogestrel: From Contraception to Amenorrhoea

## One-Sentence Summary

Desogestrel is a progestogen used as a component of combined and progestogen-only oral contraceptives. The TxGNN model predicts a possible association with **Amenorrhoea**, with a prediction score of **99.96%**, but no clinical trials and only literature-level evidence (16 publications) currently support this direction — and much of that literature suggests the link may reflect a known **adverse effect** of desogestrel rather than a genuine therapeutic use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (progestogen component of combined/progestogen-only oral contraceptives — per literature evidence; formal licensed indication text not available) |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on the literature retrieved in this pack, desogestrel is a gonane-derived progestogen used in combined oral contraceptives (with ethinylestradiol) and as a progestogen-only pill; it acts primarily by inhibiting ovulation and altering endometrial and cervical mucus characteristics.

The relationship between desogestrel and amenorrhoea is mechanistically plausible but directionally ambiguous. Secondary amenorrhoea and irregular bleeding are well-documented **adverse effects** of progestogen-only and combined hormonal contraceptives — several of the retrieved papers (e.g. PMID 35261299, PMID 3161265) discuss amenorrhoea as a bleeding-pattern side effect rather than a treatment target. It is therefore likely that the TxGNN model has picked up a drug–disease co-occurrence signal driven by adverse-event literature, rather than evidence that desogestrel is used therapeutically to treat amenorrhoea. A small subset of literature (PMID 11725730, PMID 23221134) does discuss oral contraceptives, including desogestrel-containing formulations, being used in the management of hypothalamic oligo-/amenorrhoea, which keeps a therapeutic interpretation open — but this requires manual clarification before further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18843653](https://pubmed.ncbi.nlm.nih.gov/18843653/) | 2008 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Reviews estrogen dose reduction in combined oral contraceptives and its effect on bleeding-pattern outcomes, including amenorrhoea |
| [21249657](https://pubmed.ncbi.nlm.nih.gov/21249657/) | 2011 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Updated Cochrane review of low- vs higher-dose estrogen COCs on efficacy and bleeding control |
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | Cohort | Gynecol Endocrinol | Compares bleeding profile of a drospirenone-only pill vs desogestrel 75 mcg; notes desogestrel's known poor cycle control and association with amenorrhoea |
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | Comparative study | Br J Obstet Gynaecol | Compares two desogestrel-containing COC formulations for reliability, cycle control and side effects |
| [8324604](https://pubmed.ncbi.nlm.nih.gov/8324604/) | 1993 | Review | Br Med Bull | General review of combined oral contraceptive acceptability and safety |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Pharmacodynamic study | Acta Obstet Gynecol Scand Suppl | Evaluates androgenicity of progestogens including desogestrel; discusses amenorrhoea in the context of PCOS-like presentations |
| [11725730](https://pubmed.ncbi.nlm.nih.gov/11725730/) | 2001 | Observational study | J Reprod Med | Examines bone mineral density in young women with hypothalamic oligo-amenorrhoea treated with oral contraceptives |
| [23221134](https://pubmed.ncbi.nlm.nih.gov/23221134/) | 2012 | Observational study | Georgian Med News | Investigates management of central (hypothalamic) oligomenorrhoea/amenorrhoea, including hormonal therapy |
| [1436906](https://pubmed.ncbi.nlm.nih.gov/1436906/) | 1992 | Review | Obstet Gynecol Surv | Overview of newer progestogens (desogestrel, norgestimate, gestodene) in oral contraception |
| [8447356](https://pubmed.ncbi.nlm.nih.gov/8447356/) | 1993 | Review | Am J Obstet Gynecol | Tolerability profile of desogestrel/ethinyl estradiol combined oral contraception |

## UK Market Information

Desogestrel is currently **not marketed** in the UK under this evidence pack, with **0 marketing authorisations** on record. No MHRA licence or product data is available to summarise.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The amenorrhoea signal is supported only by literature (L4, no clinical trials), and much of that literature indicates amenorrhoea is a known adverse effect of desogestrel-containing contraceptives rather than a validated treatment target — the causal direction is unresolved. A blocking data gap on UK label warnings/contraindications also prevents a safety pre-screen.

**To proceed, the following is needed:**
- Manual clarification of whether the desogestrel–amenorrhoea association reflects therapeutic use or adverse-effect co-occurrence
- Mechanism of action (MOA) data from DrugBank
- UK product labelling (warnings, contraindications) to complete an initial safety screen
- Purpose-designed studies evaluating desogestrel specifically for treating amenorrhoea, rather than reporting it as a side effect

*Note: within this evidence pack, the rank-4 candidate (Acne, TxGNN score 99.91%) has notably stronger evidence — an L2 rating with a completed Phase 4 RCT and a supporting RCT/comparative literature base — and may warrant separate evaluation as a more advanced repurposing candidate.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

