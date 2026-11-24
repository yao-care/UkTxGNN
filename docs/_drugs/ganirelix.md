---
layout: default
title: Ganirelix
parent: Model Prediction Only (L5)
nav_order: 312
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Ganirelix"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial male-limited precocious puberty", "persistent fetal circulation syndrome", "aromatase excess syndrome", "centra precocious puberty 1", "familial isolated trichomegaly"]
description: "Ganirelix: predicted new indication Hypertrichosis (disease) (evidence level L5). In the UK: 1 NHSBSA BNF presentation code"
---

# Ganirelix
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Ganirelix: Hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Ganirelix is a GnRH receptor antagonist used to prevent premature ovulation in women undergoing ovarian stimulation during fertility treatment.
The TxGNN model predicts it may be effective for **hypertrichosis**,
but there are currently **no clinical trials** and **no publications** supporting this direction, so the prediction is based on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (1 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ganirelix blocks the GnRH receptor (GNRHR) in the pituitary. This suppresses LH and FSH release and, indirectly, gonadal sex hormone production. According to the Clinical Pharmacology section of the US FDA-approved prescribing information for ganirelix: "The pulsatile release of GnRH stimulates the synthesis and secretion of luteinizing hormone (LH) and follicle-stimulating hormone (FSH). The frequency of LH pulses in the mid and late follicular phase is approximately 1 pulse per hour. […] Ganirelix acetate acts by competitively blocking the GnRH receptors on the pituitary gonadotroph and subsequent transduction pathway." ([DailyMed: Fyremadel (ganirelix acetate) prescribing information, Ferring Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f0908b5-3551-47fd-95f7-3669b0dff7f1), label version 2026-10-16; accessed 2026-11-20.)

The only conceivable link to hypertrichosis is an indirect reduction of androgen drive. However, most forms of hypertrichosis are not androgen-dependent (they are congenital or drug-induced), so this mechanism is unlikely to apply to them.

The other nine predictions are weaker still. Most concern congenital or structural conditions (Ambras syndrome, Dandy-Walker malformation, hair shaft abnormalities, familial trichomegaly, odontal/periodontal malformation syndromes) with no plausible link to gonadotropin signalling. Two are hormonal and deserve a brief mention as research questions only:

- **Central precocious puberty** (score 0.9975): GnRH receptor blockade is mechanistically coherent, but the standard of care is GnRH agonists. Ganirelix is short-acting with no depot form, which limits practicality.
- **Familial male-limited precocious puberty** (score 0.9985): This is driven by activating LHCGR mutations that act independently of the pituitary, so a GnRH antagonist is expected to be ineffective.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0607020W0BBAAAA | Orgalutran 250microgram/0.5ml inj pre-filled syringe | Ganirelix |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

**Drug Interactions** (7 records; six rated Moderate, one pharmacological target record):

- Gonadorelin (Moderate)
- Chorionic gonadotropin (human) (Moderate)
- Menotropins (Moderate)
- Triptorelin (Moderate)
- Follitropin (Moderate)
- Urofollitropin (Moderate)

The interactions are mainly with other gonadotropins and GnRH-related agents, which is expected given overlapping pharmacology.

Warnings and contraindications were not available. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5.

**To proceed, the following is needed:**
- Label warnings and contraindications from the SmPC/BNF (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the UK product, and the PL number
- Any preclinical or clinical evidence linking GnRH antagonism to hypertrichosis
- If a hormonal direction is pursued, a focused literature review on GnRH antagonists in central precocious puberty (research question only)

<!-- review:begin uk-lic-20261124d-ganirelix-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Approved indication text for the UK authorisation, and the PL number" Corrected wording only: the text described this site's UK market data as MHRA licences, marketing authorisations, licence numbers or licence records, or rested on a UK licence status. This site's UK market data is the NHSBSA BNF prescribing code list (snapshot of the Release data-20261116-160902): these are NHS prescribing codes, not MHRA licences, they carry no indication text, and MHRA licence status is not included. The wording was changed to BNF prescribing codes (or the unsupported premise was removed); the rest of the sentence is unchanged. See the Quick Overview and the BNF code table under UK Market Information. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261124d-ganirelix-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Detailed mechanism of action data is not otherwise available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Fyremadel (ganirelix acetate) prescribing information, Ferring Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f0908b5-3551-47fd-95f7-3669b0dff7f1) |
| 2026-11-24 | Corrected: "Approved indication text for the UK authorisation, and the PL number" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

