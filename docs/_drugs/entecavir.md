---
layout: default
title: Entecavir
parent: Moderate Evidence (L3-L4)
nav_order: 236
evidence_level: L4
indication_count: 10
---

# Entecavir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Entecavir: From Chronic Hepatitis B Virus Infection to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a nucleoside analogue whose established, approved use is chronic hepatitis B virus (HBV) infection. The TxGNN model's top-ranked prediction proposes potential efficacy in **chronic hepatitis C virus (HCV) infection**, but of the 40 clinical trials and 20 publications reviewed, none provide direct evidence of anti-HCV activity — the trials largely reflect entecavir being used to manage the HBV component in HBV/HCV co-infected patients, not HCV treatment itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection (established approved use; not captured in this dataset's licence records — see Data Gaps) |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| UK Market Status | Not marketed (per this dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data is not recorded in this dataset (flagged as a High-severity data gap), but the evidence pack's own mechanistic review supplies the relevant pharmacology: entecavir is a guanosine nucleoside analogue that, after intracellular phosphorylation, directly inhibits the HBV DNA polymerase (reverse transcriptase), blocking priming, reverse transcription and DNA strand elongation. This is its original, approved mechanism for chronic hepatitis B — not a newly discovered pathway.

HCV, by contrast, is a *Flaviviridae* RNA virus that replicates via an RNA-dependent RNA polymerase and does not involve a reverse-transcription step at any stage of its life cycle. Entecavir's molecular target therefore has no established pharmacological basis for inhibiting HCV replication.

Reviewing the underlying evidence supports this conclusion: the great majority of trials returned for this "HCV" prediction are actually chronic hepatitis B studies, or studies of HBV/HCV co-infected patients in which entecavir is used solely to control the HBV component (e.g., preventing HBV reactivation during HCV-directed DAA therapy), while HCV itself is treated by other agents. The assessment team's own relevance grading (mostly C, with a few B) reflects this — no trial or publication in this pack tests entecavir as an HCV antiviral. The most plausible explanation is that the TxGNN score reflects a knowledge-graph co-occurrence artefact (both diseases share "hepatitis," similar patient populations, and frequent co-infection literature) rather than a genuine pharmacological repurposing signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04157257](https://clinicaltrials.gov/study/NCT04157257) | Phase 2 | Unknown | 60 | QL-007 (NS5A inhibitor) plus entecavir/tenofovir in HBV/HCV-relevant nucleoside-experienced CHB patients; entecavir arm addresses the HBV component only |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Unknown | 60 | Nucleoside analogue (incl. entecavir) prophylaxis against HBV reactivation in HCV/HBV co-infected patients receiving DAA therapy for chronic hepatitis C — not an HCV efficacy endpoint |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Direct-acting antivirals for chronic HCV/HBV co-infection; entecavir is not the primary HCV-directed agent |
| [NCT03272009](https://clinicaltrials.gov/study/NCT03272009) | Phase 1 | Completed | 73 | Safety/PK/PD study of an unrelated FXR agonist (EYP001a) in chronic HBV infection; not HCV efficacy evidence |
| [NCT01037166](https://clinicaltrials.gov/study/NCT01037166) | Phase 2 | Completed | 84 | Japanese Phase 2 study of entecavir antiviral activity in chronic hepatitis B with incomplete lamivudine response — an HBV, not HCV, study |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | Unknown | 540 | Pegasys plus entecavir vs entecavir vs Pegasys for HBeAg-negative chronic hepatitis B; unrelated to HCV |
| [NCT01022801](https://clinicaltrials.gov/study/NCT01022801) | Phase 2 | Completed | 120 | Entecavir vs lamivudine dose-response in Japanese chronic hepatitis B patients; HBV only |
| [NCT06566248](https://clinicaltrials.gov/study/NCT06566248) | Phase 2 | Recruiting | 90 | Nucleoside analogues (TQA3810) in chronic hepatitis B; presumed HBV-related, no HCV data |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | Completed | 130 | Arabinoxylan rice bran for hepatocellular carcinoma and hepatitis B/C infection; unrelated to entecavir mechanism |
| [NCT03662568](https://clinicaltrials.gov/study/NCT03662568) | Phase 1 | Completed | 56 | Drug–drug interaction/PK study of an unrelated agent combined with entecavir or tenofovir in healthy subjects; not an efficacy trial |

No trial in this dataset tests entecavir as a direct anti-HCV therapy.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wiener medizinische Wochenschrift | Overview of chronic hepatitis B and C treatment options; positions entecavir within HBV therapy, separate from HCV regimens |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Advances in treatment of HBV/HCV co-infection; highlights the need for effective therapy in dual infection but does not attribute anti-HCV activity to entecavir |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterologica e Dietologica | Reviews antiviral medications for HBV and HCV and their renal effects; lists entecavir under HBV-approved agents only |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Review | World Journal of Hepatology | Management of hepatitis B and C before/after liver and kidney transplantation; entecavir discussed for HBV prevention/recurrence only |
| [21497740](https://pubmed.ncbi.nlm.nih.gov/21497740/) | 2011 | Review | Best Practice & Research Clinical Gastroenterology | Fibrosis in chronic viral hepatitis; entecavir referenced for HBV-related fibrosis regression, not HCV |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | HCV reactivation in anti-HCV antibody-positive CHB patients following anti-HBV (nucleos(t)ide analogue) therapy; entecavir's role is HBV suppression, with HCV reactivation as an observed phenomenon, not a treatment outcome |

None of these publications report entecavir as an effective treatment for HCV.

## UK Market Information

No marketing authorisation records are present in this dataset (0 licences; status recorded as "Not marketed"). This should be treated as a data completeness issue rather than a definitive statement of UK availability — see Conclusion for the associated blocking data gap on regulatory/label information.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted HCV indication is supported only by knowledge-graph score (evidence level L4) with no trial or publication demonstrating direct anti-HCV activity. Entecavir's mechanism (HBV reverse transcriptase inhibition) has no pharmacological basis against HCV, an RNA virus that does not use reverse transcription. The signal is most consistent with a knowledge-graph co-occurrence artefact from HBV/HCV co-infection literature rather than a genuine repurposing opportunity.

**To proceed, the following is needed:**
- Confirmed UK marketing authorisation and SmPC data for entecavir (currently a Blocking data gap — no licence or label data available for safety screening)
- Formal mechanism-of-action documentation (currently a High-severity data gap)
- Direct in vitro or preclinical evidence of anti-HCV activity, if this candidate is to be pursued further, before any clinical investigation is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

