---
layout: default
title: Nystatin
parent: 僅模型預測 (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
---

# Nystatin
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

Using no additional skill — this is a direct content-generation task against a fully specified template already in context.

# Nystatin: From Candidiasis to Vulvovaginitis

## One-Sentence Summary

> Nystatin is a polyene antifungal historically used to treat candidiasis (oral, cutaneous and vaginal). The TxGNN model predicts it may be effective for **vulvovaginitis**, with **0 registered clinical trials** but **20 supporting publications**, including two cohort studies directly evaluating nystatin in vulvovaginal candidiasis. Note: the evidence itself suggests this is less a "new" repurposing than a re‑confirmation of nystatin's existing antifungal role, since vulvovaginitis is most commonly caused by *Candida albicans*.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this dataset (`original_indications` and `original_moa` are data gaps — DG002). Based on drug-class knowledge, nystatin is a polyene antifungal traditionally used for candidiasis. |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a data gap in the underlying evidence pack (DG002). However, the model's own repurposing rationale provides sufficient mechanistic detail to assess plausibility: nystatin is a polyene antifungal that binds ergosterol in the fungal cell membrane, forming pores that cause leakage of intracellular contents and fungal cell death.

Vulvovaginitis is most commonly caused by *Candida albicans* infection, and this pathogen-driven mechanism maps directly onto nystatin's established antifungal action. The evidence pack itself notes that this prediction falls within nystatin's **existing core indication range** rather than representing atypical drug repurposing — in other words, this is closer to confirming a known clinical use than discovering a genuinely novel one.

Two cohort studies in the literature evidence directly support this: one evaluating combined vaginal nystatin/nifuratel therapy for mixed vulvovaginitis, and another correlating in-vitro nystatin susceptibility with clinical outcomes in complicated vulvovaginal candidiasis. This gives the prediction a stronger empirical basis than a pure model-only inference.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Cohort | Mycoses | In-vitro fluconazole/nystatin susceptibility testing in 287 *Candida* isolates from complicated VVC, correlated with clinical treatment outcome |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Cohort | Ceska gynekologie | Evaluation of combined vaginal nifuratel + nystatin therapy for mixed/miscellaneous vulvovaginitis |
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Update on management of fluconazole-resistant VVC; nystatin discussed alongside boric acid and newer agents (oteseconazole, ibrexafungerp) |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Womens Health | Review of boric acid for recurrent VVC, discussing nystatin as an alternative in azole-resistant non-albicans species |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | General overview of vulvovaginal candidiasis; *C. albicans* accounts for 85–90% of cases |
| [21718579](https://pubmed.ncbi.nlm.nih.gov/21718579/) | 2010 | Review | BMJ Clinical Evidence | General overview of vulvovaginal candidiasis epidemiology and treatment |
| [19454049](https://pubmed.ncbi.nlm.nih.gov/19454049/) | 2007 | Review | BMJ Clinical Evidence | General overview of vulvovaginal candidiasis epidemiology and treatment |
| [12228137](https://pubmed.ncbi.nlm.nih.gov/12228137/) | 2002 | Review | BMJ | Overview of vulvovaginal candidiasis diagnosis and management |
| [4919155](https://pubmed.ncbi.nlm.nih.gov/4919155/) | 1970 | Review | Med Clin North Am | Historical review of nystatin pharmacology and clinical use |
| [11363911](https://pubmed.ncbi.nlm.nih.gov/11363911/) | 1996 | Review | J Int Assoc Physicians AIDS Care | Review of candidiasis management |

## UK Market Information

Nystatin currently has no marketing authorisations recorded in this dataset (`total_licenses: 0`, `licenses: []`); UK market status is **Not marketed**.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: key warnings, contraindications and DDI fields in this evidence pack are unpopulated/data-gap (DG001, Blocking severity) — MHRA label data would need to be sourced separately before any safety initial assessment can proceed.)*

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two cohort studies plus a consistent body of review literature support nystatin's mechanistic and clinical plausibility for vulvovaginitis, and the underlying rationale indicates this prediction largely reconfirms nystatin's existing antifungal indication rather than a novel use — but there are no clinical trials, no UK marketing authorisation, and safety/label data are currently missing (Blocking gap DG001).

**To proceed, the following is needed:**
- MHRA-equivalent SmPC data (warnings, contraindications, DDI) — currently a Blocking data gap
- Confirmation of nystatin's formally documented original indication(s) and MOA (currently a High-severity gap)
- Clarification of whether this represents genuine repurposing or simply an unlicensed-in-UK formulation of an already-established antifungal use
- A route-of-administration assessment (vaginal formulation availability), since `route_compatibility` data is currently unpopulated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

