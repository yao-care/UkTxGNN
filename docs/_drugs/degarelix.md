---
layout: default
title: Degarelix
parent: Model Prediction Only (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# Degarelix
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Degarelix: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

> Degarelix is a GnRH (gonadotropin-releasing hormone) receptor antagonist established in oncology for advanced hormone-dependent prostate cancer, though it holds **no current UK marketing authorisation** and its formal mechanism-of-action record in this evidence pack remains a data gap.
> The TxGNN model's top-ranked prediction for this drug is **Hypertrichosis (disease)**, with a very high similarity score (**99.99%**) but **zero supporting clinical trials and zero literature**.
> This is a model-only prediction (Evidence Level L5) with a weak, non-specific mechanistic rationale, and the recommended decision is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced hormone-dependent prostate cancer (from published prescribing information; not confirmed within this evidence pack — see Data Gaps below) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Degarelix is flagged as a data gap in this evidence pack (DG002, High severity). Based on information embedded elsewhere in the pack's own repurposing rationale, Degarelix acts as a GnRH receptor antagonist: it directly blocks pituitary GnRH receptors, suppressing LH/FSH release and, downstream, testosterone production. This androgen-deprivation mechanism underlies its established oncology use.

The proposed link to hypertrichosis (excessive hair growth) rests on the idea that if a case of hypertrichosis is androgen-driven (i.e. related to hyperandrogenism), suppressing testosterone could plausibly reduce it. However, the evidence pack's own rationale is explicit that this connection is weak: the general hypertrichosis category is most commonly caused by drug exposure, congenital factors, or other non-hormonal mechanisms unrelated to androgen signalling. The mechanistic link is therefore described as "unclear and overly generic" rather than disease-specific.

In short, while the TxGNN similarity score is very high, no biological specificity or independent evidence currently substantiates this particular pairing — the score alone should not be read as clinical plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Degarelix does not currently hold a UK marketing authorisation (0 licences recorded in this evidence pack), so no MHRA product entry is available to summarise.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal/endocrine antineoplastic (GnRH receptor antagonist; androgen-deprivation therapy) — not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Not established in this evidence pack; GnRH antagonists are not typically associated with significant myelosuppression |
| Emetogenicity Classification | Not established in this evidence pack |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: this evidence pack flags TFDA/SmPC warnings and contraindications as a **Blocking** data gap (DG001) — a formal safety review cannot proceed to S1 until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction is supported only by a TxGNN similarity score, with no clinical trials, literature, mechanistic specificity, or UK regulatory footing (drug not marketed) to corroborate it.

**To proceed, the following is needed:**
- Resolution of the Blocking safety data gap (DG001: SmPC warnings/contraindications)
- Confirmation of mechanism of action and original licensed indication (DG002)
- Any preclinical or case-level evidence specifically linking GnRH antagonism to androgen-driven hypertrichosis
- Re-evaluation should Degarelix obtain UK marketing authorisation

*Note: within this same evidence pack, rank 9 ("central precocious puberty 1") shows a substantially stronger and more disease-specific mechanistic rationale — Degarelix's GnRH-antagonist action directly parallels the established use of GnRH agonists in this condition — and is scored "Research Question" rather than "Hold". It may warrant separate evaluation despite its lower TxGNN rank.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

