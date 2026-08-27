---
layout: default
title: Minoxidil
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
---

# Minoxidil
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

Using the drug-repurposing evaluation report format to write this up for the Minoxidil → hypotrichosis simplex candidate.

I focused the report on the top-ranked prediction (`predicted_indications[0]`, hypotrichosis simplex of the scalp), consistent with how the template's extraction rules are written (all reference index `[0]`), and reconciled two structural gaps in this evidence pack:

1. `taiwan_regulatory.licenses` is empty (0 UK-equivalent authorisations) and `drug.original_indications`/`original_moa` are marked `[Data Gap]` — so the "Original Indication" and MOA sections had nothing to extract from the pack directly. I used Minoxidil's well-established original indication (hypertension, oral) and drew the mechanism explanation from the *literature evidence already present in the pack* (PMID 34159872), rather than fabricating unsupported MOA claims.
2. The pack's own `scoring.recommendation` value is "Research Question" (not one of Go/Hold/Proceed with Guardrails). Given L4 evidence (3 uncontrolled case reports, zero trials) plus a **Blocking**-severity safety data gap (DG001 — no product label warnings/contraindications available, which per the pack blocks entry to S1 safety pre-assessment), I mapped this to **Hold** and explained why in the Conclusion.

---

# Minoxidil: From Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

> Minoxidil was originally developed as an oral vasodilator for severe, treatment-resistant hypertension, with topical formulations later established for androgenetic alopecia.
> The TxGNN model now predicts it may also be effective for **Hypotrichosis Simplex of the Scalp**, a rare inherited hair-loss disorder,
> though this is currently supported only by **3 published case reports** and **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (oral, historical); androgenetic alopecia (topical, established repurposed use) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.9999% |
| Evidence Level | L4 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data for Minoxidil is not recorded in this evidence pack (flagged as a data gap). However, literature evidence gathered for related indications (see Literature Evidence below, e.g. PMID 34159872) indicates that Minoxidil acts through multiple pathways: it is a potassium-channel opener with direct vascular smooth-muscle relaxant activity, and separately, it promotes hair follicles into the anagen (growth) phase via induction of Wnt/β-catenin signalling, alongside mild anti-androgen effects. This anagen-promoting activity is the pharmacological basis for its long-established use in androgenetic alopecia.

Hypotrichosis simplex of the scalp is a distinct, rare monogenic disorder (associated with variants in the *CDSN* gene encoding corneodesmosin) rather than an androgen-driven condition. Nonetheless, both conditions converge on abnormal hair follicle growth-cycle regulation, giving some biological plausibility to extending Minoxidil's anagen-promoting effect to this genetic disorder. This off-label use already appears in dermatology practice, reflected in the case reports below.

Because Minoxidil's general safety profile is already well characterised from decades of use in hypertension and androgenetic alopecia, the principal uncertainty here is one of **efficacy evidence for this specific rare genetic disorder**, not of drug safety per se. That said, the formal safety documentation needed to confirm this for UK regulatory purposes is itself a data gap (see Safety Considerations and Conclusion).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Case Report | Dermatologic Therapy | Hereditary hypotrichosis simplex of the scalp treated with oral minoxidil combined with growth factors |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Case Report | Frontiers in Genetics | 8-year-old boy with *CDSN*-mutation-confirmed hypotrichosis simplex treated with combined botanical extracts and minoxidil; notes a continued lack of definitive effective treatments for this disorder |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Case Report | Journal of Dermatological Treatment | 14-year-old patient with hereditary hypotrichosis simplex successfully treated with platelet-rich plasma injection combined with topical minoxidil 2% |

---

## UK Market Information

Minoxidil currently holds no UK marketing authorisations in this evidence pack (0 licences recorded; market status "Not Marketed"). No product-specific UK licence or approved-indication text is available to summarise.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence specific to hypotrichosis simplex of the scalp consists only of three uncontrolled case reports (Evidence Level L4), with no registered clinical trials. Compounding this, the evidence pack flags a **Blocking**-severity data gap (product label warnings/contraindications, DG001) that currently prevents completion of even an initial safety assessment, and Minoxidil holds no UK marketing authorisation. The mechanistic rationale is plausible but not yet substantiated by controlled studies in this specific genetic disorder.

**To proceed, the following is needed:**
- Product safety labelling (warnings and contraindications) to complete initial safety assessment — currently a Blocking data gap
- Documented original mechanism-of-action data for Minoxidil (currently a data gap)
- Prospective case-series or controlled trial data specifically in genetically-confirmed hypotrichosis simplex (existing evidence is limited to 3 individual case reports)
- Paediatric dosing and safety assessment, since reported cases include patients as young as 8 years old
- Confirmation of intended route of administration (oral vs. topical) and formulation strategy for this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

