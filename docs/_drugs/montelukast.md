---
layout: default
title: Montelukast
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 5
---

# Montelukast
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

# Montelukast: From Asthma to Bronchitis

## One-Sentence Summary

Montelukast is a cysteinyl leukotriene receptor antagonist (LTRA) originally established for the treatment of **asthma** (and, in wider clinical use, allergic rhinitis). The TxGNN model's top-ranked prediction identifies **Bronchitis** as a candidate new indication, with **23 clinical trials** and **20 publications** currently retrieved as supporting evidence — though, as discussed below, this evidence spans several distinct clinical entities that sit under the single "bronchitis" label.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (established LTRA indication; formal UK licence text is not available in this evidence pack — see Data Gaps) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| UK Market Status | Not marketed (0 authorisations on record in this evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available for this evaluation (flagged as Data Gap DG002). Based on known information, Montelukast belongs to the leukotriene receptor antagonist (LTRA) class, selectively blocking the cysteinyl leukotriene 1 (CysLT1) receptor. Its efficacy in asthma — where it reduces leukotriene-mediated bronchoconstriction, mucus secretion and eosinophilic airway inflammation — is well established, and this same pathway is mechanistically plausible in other airway inflammatory conditions.

The evidence retrieved for "bronchitis" is genuinely relevant to this mechanism, but it is important to note that the TxGNN ontology term "bronchitis" bundles together at least three pharmacologically distinct clinical entities: (1) viral bronchiolitis in infants (where RSV infection raises cysteinyl leukotriene levels), (2) non-asthmatic eosinophilic bronchitis (NAEB, a corticosteroid-responsive eosinophilic airway disease), and (3) bronchiolitis obliterans syndrome (BOS) — a fibrotic, obstructive complication of lung or haematopoietic stem cell transplantation and chronic graft-versus-host disease. These three conditions do not share a single pathophysiology, so the aggregated evidence base is heterogeneous and should be read as three separate, smaller bodies of evidence rather than one coherent case.

For context, the evidence pack also flags "asthma" itself as one of the model's top five predictions (rank 3, score 99.54%). This is explicitly annotated in the underlying data as a **positive control** — asthma is Montelukast's already-approved indication, and its appearance here confirms the model can correctly recall known drug–disease relationships rather than representing a genuine repurposing opportunity. Two further candidates (atopic eczema, L2; obstructive lung disease/COPD, L3) and one non-actionable genetic susceptibility signal (L5, Hold) were also identified but fall outside the scope of this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Phase 3 | Completed | 1,125 | Large placebo-controlled RCT of montelukast (MK0476) for respiratory symptoms of RSV-induced bronchiolitis in children aged 3–24 months |
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | N/A | Completed | 141 | Randomised, double-blind, placebo-controlled trial of daily montelukast for first-time viral bronchiolitis in infants |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | N/A | Completed | 146 | Montelukast for acute bronchiolitis and post-bronchiolitis viral-induced wheezing in infants 3–12 months |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Phase 4 | Unknown | 63 | Randomised, double-blind, placebo-controlled add-on montelukast to inhaled budesonide for non-asthmatic eosinophilic bronchitis (NAEB) |
| [NCT04613180](https://clinicaltrials.gov/study/NCT04613180) | Phase 4 | Unknown | 100 | Evaluated montelukast for treatment and prevention of recurrent obstructive bronchitis in children aged 1–7 years |
| [NCT03369119](https://clinicaltrials.gov/study/NCT03369119) | Phase 4 | Completed | 100 | Assessed additive benefit of oral montelukast added to standard treatment in preschool children hospitalised for acute asthma/bronchitic exacerbation |
| [NCT02479074](https://clinicaltrials.gov/study/NCT02479074) | Phase 4 | Completed | 49 | Compared feNO-guided response to montelukast versus prednisolone in the differential diagnosis of chronic cough |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Phase 2 | Completed | 25 | Multi-institutional Phase II study of montelukast for bronchiolitis obliterans following stem cell/bone marrow transplantation |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Phase 2 | Completed | 36 | Phase II trial of fluticasone + azithromycin + montelukast (FAM) for bronchiolitis obliterans after stem cell transplant |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Phase 4 | Completed | 30 | RCT of montelukast to slow progression of bronchiolitis obliterans syndrome (chronic rejection) after lung transplantation |

*Note: a further 13 trials were retrieved for "bronchitis" but were judged lower relevance (mostly studies of other agents — e.g. ibrutinib, ruxolitinib, belumosudil — in overlapping transplant-lung populations, or montelukast bioequivalence/PK-only studies) and are omitted here for clarity.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | RCT | Chinese Medical Journal | Add-on montelukast to budesonide improved quality of life, reduced airway eosinophilia and cough versus budesonide alone in NAEB |
| [20976161](https://pubmed.ncbi.nlm.nih.gov/20976161/) | 2010 | RCT | PLoS ONE | Compared fish oil and montelukast, alone and combined, on airway inflammation and exercise-induced bronchoconstriction |
| [38485149](https://pubmed.ncbi.nlm.nih.gov/38485149/) | 2024 | Clinical Practice Guideline | European Respiratory Journal | Joint ERS/EBMT guideline on management of pulmonary chronic GVHD in adults, including BOS treatment approaches |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Review | Therapeutic Advances in Respiratory Disease | Reviewed therapeutic potential and possible mechanisms of montelukast in BOS after lung/HSC transplantation |
| [26475726](https://pubmed.ncbi.nlm.nih.gov/26475726/) | 2016 | Cohort/Case Series | Biology of Blood and Marrow Transplantation | Phase II single-arm study of fluticasone/azithromycin/montelukast (FAM) for new-onset BOS after HCT |
| [27229850](https://pubmed.ncbi.nlm.nih.gov/27229850/) | 2016 | Comparative/Cohort | Respiratory Research | Investigated budesonide/formoterol, montelukast and N-acetylcysteine for BOS after HSCT |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clinical Evidence | Overview of bronchiolitis epidemiology and management in infants |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Review | BMJ Clinical Evidence | Earlier review of bronchiolitis presentation and management in infants |
| [24345788](https://pubmed.ncbi.nlm.nih.gov/24345788/) | 2014 | Review | Current Opinion in Allergy and Clinical Immunology | Reviewed mechanisms of chronic cough, relevant to eosinophilic bronchitis pathophysiology |
| [28545478](https://pubmed.ncbi.nlm.nih.gov/28545478/) | 2017 | Preclinical | Journal of Cardiothoracic Surgery | Rat model examining LTB4 and montelukast in transplantation-related bronchiolitis obliterans |

*A further 10 literature entries were retrieved but remain unclassified (study type/tier pending) at the time of this report.*

---

## UK Market Information

No marketing authorisation records are present in this evidence pack (`total_licenses = 0`). This is flagged as a data gap requiring direct verification against the MHRA products database, since it conflicts with the drug's well-documented licensed status for asthma and allergic rhinitis. Until this is resolved, no BNF classification or authorised product details can be cited from this pack.

---

## Safety Considerations

The structured safety fields in this evidence pack (key warnings, contraindications, drug–drug interactions) are all currently empty (Data Gap DG001, severity: Blocking). This gap prevents even an initial (S1) safety screen for this candidate.

Separately, the literature retrieved under related indications in this evidence pack repeatedly references an important, well-documented safety signal for montelukast as a class: multiple recent studies (systematic reviews and nationwide cohort studies) describe an FDA boxed warning (issued 2020) concerning **neuropsychiatric adverse events** associated with montelukast use, particularly in children. This is drawn from literature evidence rather than the structured SmPC data field, so it should be treated as a prompt to check the current SmPC rather than a substitute for it.

Please refer to the SmPC and BNF for full safety information before any prescribing decision. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Efficacy evidence for the "bronchitis" candidate is L2 (multiple completed Phase 2–4 studies, but only one completed Phase 3 RCT, and evidence is split across three pharmacologically distinct sub-conditions — viral bronchiolitis, NAEB, and post-transplant BOS).
- A **Blocking** data gap (DG001) means MHRA-sourced warnings, contraindications and interaction data are entirely absent, so a basic safety screen cannot yet be completed.
- UK marketing authorisation data currently shows zero authorisations on record, which itself needs to be reconciled with reality before any further evaluation proceeds.

**To proceed, the following is needed:**
- Download and parse the current MHRA SmPC for montelukast to resolve DG001 (warnings, contraindications, interactions)
- Obtain formal mechanism-of-action documentation to resolve DG002
- Disambiguate the target indication — decide whether the repurposing case is being made for viral bronchiolitis, NAEB, or post-transplant BOS, as these require separate evidence appraisal and separate trial designs
- Verify and record actual UK marketing authorisation details (PL numbers, product names, licensed indications)
- Once safety data is available, re-run the S1–S3 evaluation stages for the specific chosen sub-indication before considering a "Proceed with Guardrails" recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

