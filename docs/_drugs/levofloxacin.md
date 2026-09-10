---
layout: default
title: Levofloxacin
parent: 僅模型預測 (L5)
nav_order: 348
evidence_level: L5
indication_count: 10
---

# Levofloxacin
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

# Levofloxacin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Levofloxacin is a fluoroquinolone antibacterial; this evidence pack contains no verified UK-licensed indication text, so its established use cannot be quoted directly from source data. The TxGNN model's top-ranked prediction is **Punctate Epithelial Keratoconjunctivitis**, but this is supported by only **1 case-series publication** (an outbreak report, not a treatment study) and **no clinical trials**, with the underlying pathogen (Microsporidia) mechanistically mismatched to levofloxacin's antibacterial mode of action.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not currently marketed in the UK and no licence text was provided in this evidence pack |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for levofloxacin in this evidence pack (flagged as a High-severity data gap). Based on known pharmacological class information, levofloxacin is a fluoroquinolone antibacterial that inhibits bacterial DNA gyrase and topoisomerase IV; ophthalmic levofloxacin formulations are established for bacterial conjunctivitis and keratitis.

However, the single literature source supporting this prediction describes an outbreak of **microsporidial** keratoconjunctivitis linked to swimming-pool water contamination in Taiwan. Microsporidia are eukaryotic parasites, not bacteria, and levofloxacin has no established direct mechanism against them. The rationale text explicitly flags this mismatch: the publication is an epidemiological outbreak report, not a treatment efficacy study, and the pathogen class does not align with levofloxacin's known mode of action.

On mechanistic grounds alone, this prediction should be treated as a knowledge-graph association rather than a biologically well-supported repurposing hypothesis. It illustrates a case where a high TxGNN score does not equate to a plausible mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Case Series (Outbreak Report) | American Journal of Ophthalmology | Reports an outbreak of microsporidial keratoconjunctivitis traced to swimming-pool water contamination in Taiwan; describes the outbreak event, not levofloxacin treatment outcomes |

---

## UK Market Information

Levofloxacin has no current UK marketing authorisation recorded in this evidence pack (market status: Not marketed; 0 licences). No product name, dosage form, or approved-indication text is available for citation.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is supported only by a single outbreak/epidemiology case series rather than a treatment study, and the causative pathogen (Microsporidia) is mechanistically unrelated to levofloxacin's antibacterial activity. Combined with a Blocking-severity gap in TFDA/MHRA label warnings and contraindications (preventing any initial safety screen) and a High-severity gap in mechanism-of-action data, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- MHRA/SmPC warnings, contraindications and drug-interaction data (currently blocking — required before any S1 safety screen)
- Detailed mechanism of action (MOA) data for levofloxacin
- A treatment-outcome study (not merely an outbreak description) evaluating levofloxacin, or an alternative agent with documented anti-microsporidial activity, before this indication can be re-scored
- Confirmation of UK marketing/licensing status if repurposing evaluation is to proceed locally

**Note for future evaluation:** among the other 9 candidates screened, rank 7 (monoclonal gammopathy / multiple myeloma — antibacterial prophylaxis) is supported by materially stronger evidence, including the TEAMM trial (a completed, multicentre, double-blind, placebo-controlled Phase 3 RCT, *Lancet Oncology* 2019) plus multiple retrospective cohort studies on levofloxacin prophylaxis in myeloma/HSCT patients. This candidate's scoring/decision fields are still marked "pending" in the evidence pack and were not evaluated as the primary prediction in this report, but it warrants independent assessment as it is mechanistically coherent (antibacterial prophylaxis in immunocompromised patients) and has considerably higher-quality supporting literature than the current top-ranked candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

