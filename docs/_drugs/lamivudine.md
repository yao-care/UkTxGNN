---
layout: default
title: Lamivudine
parent: Model Prediction Only (L5)
nav_order: 333
evidence_level: L5
indication_count: 5
---

# Lamivudine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

Using no additional skill — this is a direct report-writing task with an explicit template already specified in the system prompt.

# Lamivudine: From HIV-1/Hepatitis B Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Lamivudine (3TC) is a nucleoside reverse transcriptase inhibitor (NRTI) publicly known for treating HIV-1 infection and chronic hepatitis B, though this evidence pack itself contains no confirmed original indication or UK licence data. The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)** — a veterinary, not human, condition — supported by **0 clinical trials** and **5 preclinical/veterinary publications**, with no data suggesting clinical relevance to human medicine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this evidence pack (no UK licences recorded); lamivudine is widely known as an antiretroviral for HIV-1 infection and chronic hepatitis B |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) — a veterinary condition, not a human disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 (preclinical/mechanistic studies only; no clinical trials) |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack for lamivudine (flagged as a High-severity data gap, DG002). Based on the accompanying literature evidence, lamivudine is known to be a nucleoside reverse transcriptase inhibitor (NRTI), and it is this mechanism — inhibition of retroviral reverse transcriptase — that underpins the TxGNN association with FIV: feline immunodeficiency virus is a lentivirus closely related to HIV, and the literature confirms lamivudine (often combined with zidovudine) has been studied *in vitro* and in cats as an anti-FIV agent, mirroring its established use against HIV in humans.

However, this mechanistic plausibility does not translate into clinical relevance for a UK healthcare setting: FIV is a disease of domestic cats, not humans, so this candidate has no direct human therapeutic application. The evidence pack's own scoring also flags the model's next-ranked predictions as similarly problematic — simian immunodeficiency virus infection (rank 2, also non-human), a rare neurodevelopmental disorder (rank 3, "no identifiable mechanistic link... likely a false positive"), and familial combined hyperlipidaemia (rank 4, "contradicts known pharmacology," since NRTIs are more commonly associated with causing dyslipidaemia than treating it). Chronic hepatitis C infection (rank 5) is mechanistically weak as well, since HCV is a positive-strand RNA virus that does not use reverse transcription, and most of the associated "clinical trials" are mislabelled hepatitis B studies.

Taken together, none of TxGNN's top five predictions for lamivudine currently represent a clinically actionable human repurposing candidate on the evidence available.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Case series (feline, long-term follow-up) | J Feline Med Surg | Long-term antiretroviral therapy (zidovudine-based, with lamivudine literature context) evaluated in FIV-infected domestic cats over 5–6 years |
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Animal study | Viruses | Compared antiretroviral protocols, including zidovudine + lamivudine, in naturally FIV-infected cats in the late asymptomatic stage |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | In vitro/in vivo study | Vet Immunol Immunopathol | AZT/3TC combination showed additive-to-synergistic anti-FIV activity in primary PBMCs but not chronically infected cells |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | In vitro study | Antiviral Res | Zidovudine + lamivudine + abacavir combination suppressed FIV replication in vitro; FIV proposed as an animal model for HIV |
| [11327469](https://pubmed.ncbi.nlm.nih.gov/11327469/) | 2001 | In vitro characterisation study | Am J Vet Res | Characterised a pathogenic FIV molecular clone and two lamivudine (3TC)-resistant reverse transcriptase mutants |

---

## UK Market Information

No UK marketing authorisation records are held for lamivudine in this evidence pack (market status: Not Marketed; 0 licences on file). This is flagged as a Blocking data gap (DG001) pending retrieval of the relevant SmPC/product licence data.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (feline AIDS) is a veterinary condition with no direct application to human patients, and the supporting evidence is limited to five preclinical/veterinary publications with no clinical trials. No UK marketing authorisation, mechanism-of-action confirmation, or safety data (warnings, contraindications, DDI) are available to support progression, and the remaining ranked predictions (SIV infection, a rare neurodevelopmental disorder, familial hyperlipidaemia, chronic HCV) are each independently assessed as mechanistically weak, contradicted by known pharmacology, or non-human in scope.

**To proceed, the following is needed:**
- Confirmation of a clinically meaningful human indication among lamivudine's already-established uses (e.g. HIV-1, chronic hepatitis B) before further repurposing evaluation
- Resolution of Blocking data gap DG001: MHRA/SmPC warnings and contraindications
- Resolution of High-severity data gap DG002: verified mechanism of action from DrugBank
- Re-screening of the TxGNN candidate list for a genuinely human, mechanistically plausible indication, since none of the current top five meet that bar
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

