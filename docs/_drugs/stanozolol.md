---
layout: default
title: Stanozolol
parent: Moderate Evidence (L3-L4)
nav_order: 538
evidence_level: L3
indication_count: 10
---

# Stanozolol
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

Using no additional tools — this is a direct content-generation task with a fully specified format; proceeding straight to the report.

# Stanozolol: From Anabolic Androgenic Steroid Use to C1 Inhibitor Deficiency (Hereditary Angioedema)

## One-Sentence Summary

Stanozolol is an anabolic androgenic steroid (attenuated androgen) with no current UK marketing authorisation and no original indication recorded in this evidence pack. The TxGNN model predicts it may be effective for **C1 Inhibitor Deficiency (Hereditary Angioedema)**, a signal reinforced by decades of published clinical experience — **20 publications**, including a systematic review, already document this use — although **no registered clinical trials** currently support the indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No UK-approved indication on record (anabolic androgenic steroid; historically used off-label, including HAE prophylaxis) |
| Predicted New Indication | C1 Inhibitor Deficiency (Hereditary Angioedema) |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L3 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Stanozolol is not available in this evidence pack (DrugBank field returned a data gap). However, the literature identified here provides strong mechanistic context: stanozolol belongs to the class of attenuated (17α-alkylated) androgens, alongside danazol, which have long been used off-label to increase hepatic synthesis of C1 esterase inhibitor (C1-INH) and thereby dampen bradykinin-mediated vascular permeability.

Hereditary angioedema (HAE) due to C1 inhibitor deficiency arises from *SERPING1* mutations causing low or dysfunctional C1-INH and uncontrolled bradykinin release, resulting in recurrent episodes of swelling. Attenuated androgens are proposed to upregulate C1-INH gene transcription, partially correcting the deficiency and reducing attack frequency and severity.

Critically, this is not a purely computational inference: the evidence pack's own literature (case series, case reports, and a systematic review) documents prophylactic stanozolol use in HAE patients going back to the 1980s–1990s and as recently as 2021. This makes the TxGNN prediction for C1 inhibitor deficiency an unusually well-corroborated one relative to typical repurposing candidates, though the underlying safety and UK regulatory data remain incomplete.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25707325](https://pubmed.ncbi.nlm.nih.gov/25707325/) | 2015 | Systematic Review | Ann Allergy Asthma Immunol | Systematic review of risk–benefit of long-term androgen (incl. stanozolol) use in HAE |
| [18220148](https://pubmed.ncbi.nlm.nih.gov/18220148/) | 2008 | Review | Ann Allergy Asthma Immunol | State-of-the-art review of attenuated androgens for HAE treatment |
| [31826031](https://pubmed.ncbi.nlm.nih.gov/31826031/) | 2018 | Review | Allergologie select | Updated overview of acute and prophylactic HAE treatment options |
| [22729959](https://pubmed.ncbi.nlm.nih.gov/22729959/) | 2012 | Review | Curr Allergy Asthma Rep | Current management options for HAE, including androgen prophylaxis |
| [1518394](https://pubmed.ncbi.nlm.nih.gov/1518394/) | 1992 | Case Series | Medicine | Biological/clinical characteristics of 235 patients with hereditary and acquired C1-INH deficiency |
| [8356982](https://pubmed.ncbi.nlm.nih.gov/8356982/) | 1993 | Case Series | Am J Med | 8 patients with autoimmune (acquired) C1 inhibitor deficiency and treatment response |
| [3146615](https://pubmed.ncbi.nlm.nih.gov/3146615/) | 1988 | Mechanistic Study | J Clin Chem Clin Biochem | Coagulation/fibrinolysis parameters evaluated during low-dose anabolic steroid prophylaxis |
| [23248378](https://pubmed.ncbi.nlm.nih.gov/23248378/) | 2012 | Case Report | Indian J Dermatol | Type 1 HAE patient started on stanozolol 2 mg three times daily |
| [18447143](https://pubmed.ncbi.nlm.nih.gov/18447143/) | 2008 | Case Report | J Investig Allergol Clin Immunol | HAE patient remained stable on long-term stanozolol therapy |
| [1869690](https://pubmed.ncbi.nlm.nih.gov/1869690/) | 1991 | Review | J Am Acad Dermatol | Angioedema management overview; prophylaxis with danazol or stanozolol described |

## UK Market Information

Stanozolol currently holds **no UK marketing authorisation** (market status: Not Marketed, 0 licenses on record). No product-level licensing, formulation, or approved-indication data is available for the UK market at this time.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: A Blocking data gap exists for UK-specific warnings/contraindications, and a High-severity gap exists for mechanism-of-action data — both must be resolved before formal safety screening can proceed (see Conclusion).*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Literature evidence for stanozolol's use in HAE/C1 inhibitor deficiency is unusually strong for a TxGNN-derived candidate (systematic review plus multiple case series spanning decades), but a Blocking data gap in safety information (warnings/contraindications) prevents entry into the S1 safety pre-assessment, and the drug currently has no UK marketing authorisation.

**To proceed, the following is needed:**
- UK SmPC/product safety data (warnings, contraindications, DDI) — source: MHRA/manufacturer SmPC
- Mechanism of action confirmation via DrugBank API query
- Confirmation of UK regulatory pathway for an unlicensed anabolic androgenic steroid (including controlled-drug status considerations)
- Clinical dosing/monitoring protocol appropriate to UK HAE prophylaxis practice, given absence of registered clinical trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

