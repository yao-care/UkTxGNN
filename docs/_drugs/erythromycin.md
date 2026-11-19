---
layout: default
title: Erythromycin
parent: Model Prediction Only (L5)
nav_order: 256
evidence_level: L5
indication_count: 4
monitor_inn: "Erythromycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "lymphogranuloma venereum", "necrotizing ulcerative gingivitis"]
last_modified_at: 2026-11-12
description: "Erythromycin: predicted new indication punctate epithelial keratoconjunctivitis (evidence level L5). In the UK: 31 NHSBSA BNF presentation codes"
---

# Erythromycin
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

## Erythromycin: Macrolide antibiotic (50S ribosomal subunit inhibitor) → 點狀上皮角膜結膜炎 (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## One-Sentence Summary

Erythromycin is a macrolide antibiotic with antibacterial and anti-inflammatory activity. The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials** and only **1 publication** (a general paediatric review) support this direction, so the evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (31 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 31 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for erythromycin: "Erythromycin acts by inhibition of protein synthesis by binding 50S ribosomal subunits of susceptible organisms. It does not affect nucleic acid synthesis." ([DailyMed: Ery-Tab (erythromycin) prescribing information, Arbor Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda44eb6-7901-4b80-ba0b-216f6cacf3fd), label version 2018-12-04; accessed 2026-11-19.) Based on general pharmacology, erythromycin is a macrolide that inhibits bacterial protein synthesis at the 50S ribosomal subunit and also has anti-inflammatory properties. Topical ophthalmic erythromycin is widely used in eye infections, so applying it to an ocular surface disease is plausible.

The only retrieved publication is a review of chronic blepharokeratoconjunctivitis in children, a related but different ocular surface condition that is often associated with staphylococcal disease. It does not study punctate epithelial keratoconjunctivitis itself, so the support is indirect. Because no cited study directly addresses the predicted disease, the evidence level is capped at L5 (model prediction only), despite the pipeline's preliminary L4 label.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Review | Journal of Pediatric Ophthalmology and Strabismus | Describes history, symptoms, clinical signs and treatment of chronic blepharokeratoconjunctivitis in children; a related condition, not the predicted disease itself |

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 1103010I0BCAAAA | Erythromycin 0.5% Ophthalmic Ointment | Erythromycin |
| 1103010I0AAAAAA | Erythromycin 0.5% eye ointment | Erythromycin |
| 1306010I0AAADAD | Erythromycin 2% gel | Erythromycin |
| 1306010I0AAAAAA | Erythromycin 2% solution | Erythromycin |
| 0501050C0AAAKAK | Erythromycin 250mg gastro-resistant capsules | Erythromycin |
| 0501050C0AAABAB | Erythromycin 250mg gastro-resistant tablets | Erythromycin |
| 1306010I0AAAEAE | Erythromycin 4% gel | Erythromycin |
| 0501050N0AAAAAA | Erythromycin stearate 250mg tablets | Erythromycin stearate |
| 0501050N0AAABAB | Erythromycin stearate 500mg tablets | Erythromycin stearate |
| 1306010I0BFAAAF | Aknemycin Plus solution | Erythromycin |
| 1306010C0BWAAAY | Benzamycin gel | Benzoyl peroxide |
| 1306010C0AAAYAY | Benzoyl peroxide 5% / Erythromycin 3% gel | Benzoyl peroxide |
| 1306010I0BEAAAD | Eryacne 2 gel | Erythromycin |
| 1306010I0BEABAE | Eryacne 4 gel | Erythromycin |
| 0501050C0BCAAAK | Erymax 250mg gastro-resistant capsules | Erythromycin |
| 0501050N0BBAAAA | Erythrocin 250 tablets | Erythromycin stearate |
| 0501050N0BBABAB | Erythrocin 500 tablets | Erythromycin stearate |
| 0501050K0BBAAAA | Erythrocin IV lactobionate 1g inf vials | Erythromycin lactobionate |
| 0501050N0BCAAAA | Erythrolar 250mg tablets | Erythromycin stearate |
| 0501050N0BCABAB | Erythrolar 500mg tablets | Erythromycin stearate |

Showing 20 of 31 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Drug interaction records compiled for this report include the following notable entries:
- **Major**: loperamide, clarithromycin
- **Moderate**: for example famotidine, hydrocortisone, pioglitazone, alosetron, aprepitant, dexamethasone, budesonide, cimetidine

Only a subset of the 100 recorded interactions is shown here; check the BNF interaction guidance before prescribing.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no trials and the sole publication is an indirect review of a related condition. There is no direct evidence for punctate epithelial keratoconjunctivitis.

**To proceed, the following is needed:**
- Studies that directly examine erythromycin (topical or systemic) in punctate epithelial keratoconjunctivitis
- Mechanism of action data and a clear rationale for the anti-inflammatory versus antibacterial role
- Review of the SmPC and BNF safety information, including QT-prolongation risk and interaction management, for any ocular or systemic use

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Ery-Tab (erythromycin) prescribing information, Arbor Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda44eb6-7901-4b80-ba0b-216f6cacf3fd) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

