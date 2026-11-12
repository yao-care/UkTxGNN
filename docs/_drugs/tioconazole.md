---
layout: default
title: Tioconazole
parent: Model Prediction Only (L5)
nav_order: 619
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
monitor_inn: "Tioconazole"
predicted_indications: ["vulvitis", "postmenopausal atrophic vaginitis"]
description: "Tioconazole: predicted new indication Vulvitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Tioconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Tioconazole: Vulvitis
{: .text-alpha }

## One-Sentence Summary

Tioconazole is a topical imidazole antifungal. The TxGNN model predicts it may be useful for **vulvitis**, but there are **no registered clinical trials** and the literature compiled for this report concerns candidal vaginal infection rather than vulvitis itself, so the evidence for this specific prediction is limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vulvitis |
| TxGNN Prediction Score | 0.9920 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (2 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Tioconazole is an imidazole antifungal. In fungi and yeasts it inhibits the cytochrome P450 enzyme lanosterol 14-α demethylase (CYP51/ERG11), which converts lanosterol to ergosterol, an essential cell membrane component. Without ergosterol the organism cannot survive. It also inhibits the human enzyme CYP8B1, which takes part in bile acid biosynthesis. Its pharmacology entry describes topical use for common fungal and yeast infections, including *Candida*.

The rationale for vulvitis rests on overlap with candidal infection of the vulvar and vaginal area, where antifungal activity against *Candida* is plausible. This link is weak: the available literature does not address non-infectious vulvitis, so the prediction is not a distinct repurposing signal. A candidal cause would be a plausible fit; other causes of vulvitis would not be expected to respond to an antifungal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No publication in the compiled set directly studies vulvitis. The papers below concern tioconazole or azole antifungals in candidal vaginal infection and are indirect context only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | RCT | Antimicrob Agents Chemother | Single-dose 6.5% tioconazole ointment vs 3-day clotrimazole in 80 patients: 84% vs 85% remained asymptomatic at 4 weeks |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | Double-blind placebo-controlled trial | Gynakol Rundsch | Tioconazole vs placebo in vaginal candidiasis, including assessment of systemic absorption |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Review | Drugs | Broad in vitro antimicrobial activity; trials showed efficacy and safety of topical tioconazole in superficial dermatophyte and yeast infections |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Review | Expert Rev Anti Infect Ther | Overview of non-invasive azole options for vulvovaginal candidiasis, including recurrent disease |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | Randomised open-label study | J Int Med Res | Single-dose topical tioconazole 6% vs 5 days of oral ketoconazole; both eradicated infection, with faster symptom response on topical therapy |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Clinical study | Acta Obstet Gynecol Scand | 2% vaginal cream for 3 days, repeated once: mycological cure rate 88.5% |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | Open-label comparative trial | Gynakol Rundsch | 3-day tioconazole vs econazole in vaginal candidiasis |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Open non-comparative study | J Int Med Res | 2% cream for 3 days in *Trichomonas vaginalis* or mixed infections: 95% (19/20) cured at first follow-up |
| [30553009](https://pubmed.ncbi.nlm.nih.gov/30553009/) | 2019 | Formulation study | Int J Pharm | Chitosan-HPMC tioconazole vaginal films developed as an alternative dosage form |

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1310020T0AAAAAA | Tioconazole 283mg/ml medicated nail lacquer | Tioconazole |
| 1310020T0BBAAAA | Trosyl 283mg/ml nail solution | Tioconazole |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: Two interaction records were found. Omeprazole is listed with an unclassified severity level. The pharmacology entry also notes that tioconazole inhibits the human enzyme CYP8B1.

Please refer to the SmPC and BNF for further safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No cited study directly addresses vulvitis, and there are no registered trials, so the prediction rests on model output and indirect candidal data only.
- The plausible mechanism applies only to a fungal cause, and the UK product recorded in the data is a nail lacquer, not a vulvar or vaginal formulation.

<!-- review:begin uk-lic-20261106-tioconazole-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The plausible mechanism applies only to a fungal cause, and the licensed UK product recorded in the data is a nail lacquer, not a vulvar or vaginal formulation." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 2 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-tioconazole-1 -->

**To proceed, the following is needed:**
- Studies or trials that directly test tioconazole in vulvitis, with the cause (candidal or non-infectious) clearly defined
- Confirmation of an appropriate vulvar or vaginal formulation and route in the UK
- Warnings and contraindications from the SmPC and BNF, which are not available in the data compiled for this report

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "licensed" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

