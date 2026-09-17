---
layout: default
title: Tiotropium
parent: High Evidence (L1-L2)
nav_order: 579
evidence_level: L1
indication_count: 10
---

# Tiotropium
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Tiotropium: From Chronic Obstructive Pulmonary Disease to Obstructive Lung Disease

## One-Sentence Summary

Tiotropium is a long-acting muscarinic antagonist (LAMA) bronchodilator, with published literature in this Evidence Pack establishing its long-standing use as a maintenance treatment for chronic obstructive pulmonary disease (COPD). The TxGNN model predicts it may be effective for **Obstructive Lung Disease**, with **34 clinical trials** and **20 publications** currently supporting this direction — though reviewers should note this predicted indication overlaps substantially with tiotropium's already-established clinical role (see "Why is This Prediction Reasonable?" below).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in structured licensing data (data gap); literature in this Evidence Pack consistently identifies COPD maintenance bronchodilation as the drug's established use |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| UK Market Status | Not marketed (per current dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on the accompanying clinical trial and literature evidence, tiotropium is a long-acting muscarinic (M1/M3) receptor antagonist — it dissociates slowly from M3 receptors on airway smooth muscle, producing sustained bronchodilation with once-daily dosing. This anticholinergic mechanism is the pharmacological basis for its use across the spectrum of obstructive airway conditions.

"Obstructive lung disease" is a broad diagnostic category that encompasses COPD, and the mechanistic rationale is therefore strong: LAMA-mediated bronchodilation is a first-line, guideline-endorsed approach for airflow obstruction of this type. The very large and mature trial base (including landmark studies such as the SAFE trial, NCT00277264, and the UPLIFT-type long-term lung function trial, NCT00144339) reflects decades of accumulated evidence for tiotropium's bronchodilator effect in obstructive airway disease.

**Important caveat for reviewers:** the `original_indications` field in this Evidence Pack is empty, and a related lower-ranked candidate in the same prediction set (rank 5, "chronic obstructive pulmonary disease") is essentially synonymous with tiotropium's well-known existing licensed use. This suggests the TxGNN model may be flagging an already-established indication rather than a genuinely novel repurposing opportunity, most likely because the source knowledge graph lacked a populated original-indication record for this drug. This should be clarified with the regulatory data source (see Conclusion) before this candidate is treated as a discovery signal rather than a confirmatory one.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00144339](https://clinicaltrials.gov/study/NCT00144339) | Phase 3 | Completed | 5,993 | Large long-term trial assessing whether daily tiotropium reduces the rate of lung function decline in COPD |
| [NCT01911364](https://clinicaltrials.gov/study/NCT01911364) | Phase 3 | Completed | 3,686 | 52-week trial comparing triple therapy (ICS/LABA/LAMA) with tiotropium alone in severe COPD |
| [NCT02173769](https://clinicaltrials.gov/study/NCT02173769) | N/A | Completed | 1,845 | AKTIV study — real-world change in physical functioning with tiotropium/olodaterol combination therapy |
| [NCT00277264](https://clinicaltrials.gov/study/NCT00277264) | Phase 3 | Completed | 914 | SAFE trial: one-year effect of tiotropium 18 mcg once daily on trough FEV1 versus placebo |
| [NCT01316913](https://clinicaltrials.gov/study/NCT01316913) | Phase 3 | Completed | 872 | 24-week head-to-head comparison of umeclidinium/vilanterol with tiotropium in COPD |
| [NCT00274014](https://clinicaltrials.gov/study/NCT00274014) | Phase 3 | Completed | 1,000 | One-year trial evaluating effect of tiotropium on severity and incidence of COPD exacerbations |
| [NCT03474081](https://clinicaltrials.gov/study/NCT03474081) | Phase 4 | Completed | 800 | 12-week comparison of triple therapy (FF/UMEC/VI) versus tiotropium monotherapy on lung function and symptoms |
| [NCT00776984](https://clinicaltrials.gov/study/NCT00776984) | Phase 3 | Completed | 453 | 48-week add-on trial of tiotropium in severe persistent asthma (graded A: standard efficacy design) |
| [NCT00523991](https://clinicaltrials.gov/study/NCT00523991) | Phase 4 | Completed | 457 | 24-week efficacy/safety trial in maintenance-naïve COPD patients (graded A) |
| [NCT01112241](https://clinicaltrials.gov/study/NCT01112241) | Phase 4 | Completed | 17 | Bronchodilator responsiveness in obliterative bronchiolitis post-haematopoietic stem cell transplant (graded B: obstructive lung disease subtype) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | N Engl J Med | Long-term tiotropium improves lung function and slows decline in mild-to-moderate COPD |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Comprehensive review of tiotropium versus placebo across COPD trials |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Comparison of tiotropium versus ipratropium bromide in stable COPD |
| [22562275](https://pubmed.ncbi.nlm.nih.gov/22562275/) | 2012 | Cohort | Pneumonol Alergol Pol | Effects of formoterol, formoterol+tiotropium and tiotropium alone on lung function and exercise tolerance in COPD |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | Review | Life Sciences | Mechanistic and clinical profile of tiotropium (Spiriva) as an antimuscarinic bronchodilator |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Review | Respiratory Research | Review of tiotropium's clinical development programme in COPD |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Review | Curr Med Res Opin | Evidence review for tiotropium+olodaterol fixed-dose combination in reducing COPD exacerbations |
| [29206658](https://pubmed.ncbi.nlm.nih.gov/29206658/) | 2018 | Review | Curr Opin Pulm Med | Review of lung function trajectories in COPD and pharmacologic intervention points |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Review | Drugs | Pharmacological and clinical review of tiotropium bromide as an anticholinergic bronchodilator |
| [35510163](https://pubmed.ncbi.nlm.nih.gov/35510163/) | 2022 | Cohort | Int J Chron Obstruct Pulmon Dis | Multicentre real-world cohort comparing tiotropium/olodaterol with other LABA/LAMA combinations in COPD |

## UK Market Information

No marketing authorisation records are currently held for this drug in the Evidence Pack (`total_licenses = 0`, market status recorded as "Not marketed"). Given that tiotropium is a long-established respiratory bronchodilator, this is most likely a gap in the underlying regulatory data feed rather than a true absence from the UK market, and should be verified directly against the MHRA product database and current BNF listing before being used in any decision-making.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and clinical trial evidence base for tiotropium in obstructive lung disease is extensive and mature (L1, multiple completed Phase 3 RCTs including large long-term outcome trials), giving high confidence in the pharmacological premise. However, two data gaps prevent unqualified progression: safety/warning data from the marketed product labelling is missing (flagged as Blocking in the source dataset), and the mechanism-of-action record itself is unpopulated, both of which are needed for a formal safety pre-screen.

**To proceed, the following is needed:**
- MHRA-sourced Summary of Product Characteristics (SmPC), including warnings, precautions and contraindications, to complete the safety pre-screen
- Confirmation of current UK marketing authorisation status (the "Not marketed" flag appears inconsistent with tiotropium's known long-standing licensed use and should be reconciled with MHRA records)
- Clarification of whether "obstructive lung disease" represents a genuinely distinct target population from tiotropium's existing licensed COPD indication, since the two largely overlap in this dataset
- Structured original-indication and MOA data to enable a complete mechanistic-similarity assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

