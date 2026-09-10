---
layout: default
title: Ethambutol
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 5
---

# Ethambutol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ethambutol: From Tuberculosis to Epiglottitis

## One-Sentence Summary

Ethambutol is a first-line antituberculosis agent, established for treating *Mycobacterium tuberculosis* infection. The TxGNN model predicts it may be effective for **Epiglottitis**, but this is currently supported only by **2 publications** (no clinical trials), both of which actually discuss laryngeal tuberculosis rather than epiglottitis itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (established antituberculosis agent; no formal UK licence text is present in this evidence pack — see Safety Considerations) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The drug record's formal mechanism-of-action field is not populated. However, the evidence pack's own analysis identifies ethambutol as an arabinosyl transferase inhibitor that blocks arabinogalactan synthesis in the mycobacterial cell wall — the pharmacological basis for its established role as a first-line antituberculosis agent, active against *Mycobacterium tuberculosis* and some non-tuberculous mycobacteria.

Acute epiglottitis, as conventionally defined, is caused by encapsulated pyogenic bacteria such as *Haemophilus influenzae* and *Streptococcus* species. Ethambutol has no known antimicrobial activity against these organisms, so there is no direct mechanistic basis for efficacy in typical bacterial epiglottitis.

The two supporting publications do not actually describe epiglottitis as commonly understood — they describe **laryngeal tuberculosis**, a rarer manifestation in which mycobacterial disease spreads to laryngeal structures (including, in some case series, the epiglottis as one of several affected sites) and is treated with standard antituberculous combination therapy. This indicates a label-level mismatch between TxGNN's broad "epiglottitis" disease node and the narrower TB-specific entity the literature actually supports, which is why the mechanistic link is assessed as weak despite the very high TxGNN score.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14720571](https://pubmed.ncbi.nlm.nih.gov/14720571/) | 2004 | Review | The Lancet Infectious Diseases | Reviews laryngeal tuberculosis; does not specifically address epiglottitis |
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Cohort | European Respiratory Journal | Case series of 41 laryngeal TB patients (treated with isoniazid, rifampicin, ethambutol); epiglottis noted as one of several affected laryngeal sites, not a primary epiglottitis cohort |

## UK Market Information

No UK marketing authorisations are recorded in this evidence pack for ethambutol (market status: Not marketed; 0 licences on file). Prescribers should verify current MHRA/BNF listing status directly, as ethambutol-containing products (e.g. as part of antituberculosis regimens) may be available via specific licensing routes not captured here.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: key warnings, contraindications and formal drug-interaction data for ethambutol were not available in this evidence pack (flagged as a Blocking data gap), so a full safety assessment cannot be completed from this report alone.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted disease label ("epiglottitis") does not match the pathogen profile ethambutol is active against, and the only two supporting publications actually concern laryngeal tuberculosis rather than typical bacterial epiglottitis — evidence is indirect and mechanistically weak (L4).

**To proceed, the following is needed:**
- Formal UK/MHRA safety information (warnings, contraindications, interactions) — currently a blocking data gap
- Confirmation of the intended disease scope (general epiglottitis vs. TB-related laryngeal/epiglottic involvement)
- Any dedicated case data or studies on ethambutol specifically for epiglottitis rather than laryngeal tuberculosis broadly

**Note for reviewers:** within the same evidence pack, the rank-2 candidate (laryngitis, specifically tuberculous laryngitis) has notably stronger support — L3 evidence, 20 literature hits, and an existing precedent as part of standard antituberculous therapy — and may warrant separate evaluation as a more tractable candidate than epiglottitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

