---
layout: default
title: Darunavir
parent: Moderate Evidence (L3-L4)
nav_order: 196
evidence_level: L4
indication_count: 4
---

# Darunavir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Darunavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Darunavir is an HIV-1 protease inhibitor (data confirmed via the drug's repurposing rationale; formal MOA record is a data gap), most widely known for treating human HIV/AIDS in combination antiretroviral regimens.
The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)**, with a **99.97% prediction score**, but the single supporting clinical trial is judged to be a poor match and this candidate is likely a knowledge-graph ontology artefact (FIV vs. HIV node confusion) rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (known pharmacological class information; not documented in this evidence pack — see Data Gaps) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a formal mechanism-of-action record is not available for this evidence pack. Based on the information present, Darunavir is an HIV-1 protease inhibitor, typically used as part of ritonavir- or cobicistat-boosted combination antiretroviral therapy (cART) for HIV-1 infection.

The top-ranked predicted indication, Feline Acquired Immunodeficiency Syndrome (FIV), is a **veterinary** disease caused by feline immunodeficiency virus, a lentivirus related to but distinct from HIV. The only supporting clinical trial identified (NCT02770508) is in fact a human Phase 4 study comparing darunavir-based cART regimens in HIV-1-infected adults — it has no connection to feline disease. This mismatch has been flagged (relevance grade C) as most likely reflecting an ontology/node-mapping error in the knowledge graph (FIV vs. HIV), rather than genuine pharmacological evidence. On that basis, this specific prediction should **not** be interpreted as a credible repurposing opportunity.

A biologically more plausible — though still non-human — related prediction is Simian Immunodeficiency Virus (SIV) infection (rank 2, also 99.97%, L3/Research Question). SIV is the standard macaque model virus for HIV/AIDS research, and darunavir-containing cART regimens are used in this model to study viral reservoirs. This reflects translational/animal-model research use rather than a new human clinical indication.

---

## Clinical Trial Evidence

*(from the top-ranked prediction, Feline Acquired Immunodeficiency Syndrome)*

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Compared boosted darunavir + lamivudine vs. boosted darunavir + emtricitabine/tenofovir or lamivudine/tenofovir in **treatment-naïve human HIV-1-infected adults**. **Note:** this trial is in humans with HIV-1, not cats with FIV — it does not support the stated feline indication and is very likely a knowledge-graph mismatch. |

---

## Literature Evidence

Currently no related literature is registered for the top-ranked (Feline AIDS) prediction.

*For completeness, the closely related rank-2 prediction (Simian Immunodeficiency Virus infection) is supported by 4 PubMed records (PMIDs 26150024, 25033210, 22737073, 21505294), all animal-model cohort studies (Tier 3) evaluating darunavir-containing cART in SIV-infected macaques — these describe translational research use, not an approved or emerging human indication.*

---

## Other Predicted Indications (Not Recommended)

This evidence pack contains four TxGNN candidates for Darunavir, none of which currently support progression:

| Rank | Predicted Indication | Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|---|
| 1 | Feline Acquired Immunodeficiency Syndrome | 99.97% | L4 | Hold | Likely FIV/HIV ontology mismatch; sole trial is a human HIV study |
| 2 | Simian Immunodeficiency Virus infection | 99.97% | L3 | Research Question | Animal-model translational research only, not a human indication |
| 3 | Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.97% | L5 | Hold | Rare monogenic syndrome; no mechanistic link, no supporting trials/literature |
| 4 | Obsolete familial combined hyperlipidemia | 99.19% | L5 | Hold | Mechanistically contradictory — boosted PIs are known to *cause* dyslipidaemia as an adverse effect, not treat it; disease node is itself marked obsolete |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the four TxGNN-predicted indications for Darunavir currently constitute a credible human repurposing candidate. The top-ranked prediction (feline AIDS) appears to be a knowledge-graph artefact rather than genuine evidence, the second-ranked prediction (SIV) reflects animal-model research rather than a new clinical indication, and the remaining two candidates (L5) have no supporting mechanism, trials, or literature — one of them is mechanistically implausible. Darunavir also has no current UK marketing authorisation recorded in this evidence pack.

**To proceed, the following is needed:**
- Resolve the FIV/HIV node-mapping issue in the knowledge graph before this candidate can be re-scored
- Confirm formal mechanism-of-action (MOA) documentation (currently a data gap)
- Obtain manufacturer/SmPC safety data (warnings, contraindications, DDI) — currently a blocking data gap for any safety pre-assessment
- Clarify UK market status/licensing pathway, since no marketing authorisations are currently on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

