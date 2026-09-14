---
layout: default
title: Phenoxymethylpenicillin
parent: 僅模型預測 (L5)
nav_order: 457
evidence_level: L5
indication_count: 2
---

# Phenoxymethylpenicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Phenoxymethylpenicillin: From Unspecified Indication to Epiglottitis

## One-Sentence Summary

Phenoxymethylpenicillin (Penicillin V) is a narrow-spectrum oral β-lactam antibiotic; its originally licensed indication is not recorded in this evidence pack. The TxGNN model predicts potential efficacy in **Epiglottitis**, but this direction is currently supported by **no clinical trials and no published literature** — it is a pure computational prediction with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A structured mechanism-of-action (MOA) record is not available for phenoxymethylpenicillin in this evidence pack (flagged as data gap DG002, High severity). Drawing on the repurposing rationale accompanying the prediction, Penicillin V is described as a narrow-spectrum oral β-lactam antibiotic that inhibits cell-wall synthesis in susceptible bacteria, such as streptococci.

Epiglottitis was historically caused predominantly by *Haemophilus influenzae* type b; since the introduction of Hib vaccination, streptococcal species now account for a larger proportion of cases. On this basis, an antibacterial such as Penicillin V has a theoretical rationale for activity against some causative organisms.

However, epiglottitis is an airway emergency for which standard care is intravenous broad-spectrum antibiotics combined with urgent airway management. Oral Penicillin V's bioavailability and narrow antibacterial spectrum are unlikely to be adequate for this clinical scenario. Critically, this prediction is derived purely from the TxGNN knowledge-graph model — there are currently no clinical trials, case reports, or published literature specific to epiglottitis to support it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Supplementary Evidence: Rank 2 Predicted Indication — Laryngitis

The evidence pack also contains a second, closely related prediction (rank 2, score 99.85%) for **laryngitis**, an anatomically adjacent upper-airway condition. Unlike epiglottitis, this prediction is backed by substantial literature (Evidence Level L1) — but the evidence **argues against**, rather than for, antibacterial efficacy, and is presented here as important context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3918495](https://pubmed.ncbi.nlm.nih.gov/3918495/) | 1985 | RCT (double-blind) | Ann Otol Rhinol Laryngol | 100 adults with acute laryngitis: Penicillin V produced no greater resolution of vocal symptoms than placebo — direct evidence of inefficacy |
| [1632252](https://pubmed.ncbi.nlm.nih.gov/1632252/) | 1992 | RCT | Acta Otolaryngol Suppl | Notes that "phenoxymethylpenicillin had no effect on the clinical course" in prior studies; erythromycin trial vs placebo in 106 patients |
| [26002823](https://pubmed.ncbi.nlm.nih.gov/26002823/) | 2015 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Updated review (earlier versions 2005, 2007, 2013 reached the same conclusion): insufficient evidence to support routine antibiotic use in acute laryngitis in adults |

**Interpretation:** Rather than supporting repurposing, this evidence shows that antibiotics — specifically including Penicillin V — have been directly tested in acute laryngitis and found ineffective, across a controlled RCT and four successive Cochrane systematic review updates. This weakens, rather than strengthens, the plausibility of extending Penicillin V into related upper-respiratory-tract indications such as epiglottitis.

---

## UK Market Information

No marketing authorisation records for phenoxymethylpenicillin were found in this evidence pack. UK market status is recorded as **Not marketed** (0 licences).

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: this evidence pack flags TFDA/MHRA label warnings and contraindications as a **Blocking** data gap (DG001) — this must be resolved before any safety pre-assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The epiglottitis prediction is a pure TxGNN model association (Evidence Level L5) with zero supporting clinical trials or literature, and MOA data is missing (DG002).
- Critically, label-level safety data (warnings, contraindications) required for initial safety screening is entirely absent (DG001, Blocking) — this alone prevents progression regardless of efficacy evidence.
- The closely related indication laryngitis (rank 2) has robust L1 evidence (RCTs + repeated Cochrane reviews) directly demonstrating that antibiotics, including Penicillin V, provide no clinical benefit — which undermines rather than supports the plausibility of repurposing into adjacent airway indications.

**To proceed, the following is needed:**
- MHRA/SmPC label data: warnings, contraindications, and drug interactions (resolves DG001, blocking)
- Structured MOA data via DrugBank API (resolves DG002)
- Epiglottitis-specific preclinical or clinical evidence (currently none exists)
- A reassessment of biological plausibility in light of the negative RCT evidence for the pharmacologically related laryngitis indication
- Given "Not marketed" UK status, clarification of the regulatory pathway required before any further development could be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

