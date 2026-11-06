---
layout: default
title: Acyclovir
parent: Model Prediction Only (L5)
nav_order: 24
evidence_level: L5
indication_count: 10
monitor_inn: "acyclovir"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "common wart", "post-infectious neuralgia", "hepatitis C induced liver cirrhosis", "eosinophilic pustular folliculitis", "sequela of COVID-19", "vulvovaginal candidiasis", "papular urticaria", "disease of orbital region", "epidemic keratoconjunctivitis"]
last_modified_at: 2026-11-06
description: "Acyclovir: predicted new indication punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Acyclovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Aciclovir: nucleoside analogue antiviral → Punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Aciclovir is an antiviral nucleoside analogue that is marketed in the UK in oral suspension and topical cream products.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, with a score of 0.9967.
No clinical trials are registered for this disease, and the two retrieved publications are case series on unrelated conditions, so the evidence is **model prediction only**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (45 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 45 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Aciclovir is a guanosine analogue antiviral that is generally understood to act against herpesviruses by being activated by viral thymidine kinase and inhibiting viral DNA synthesis.

A mechanistic link is plausible only if the keratoconjunctivitis in question is herpesvirus-related. The two retrieved papers concern microsporidial keratoconjunctivitis and drug-induced corneal lipidosis in AIDS. Neither condition is expected to respond to aciclovir. The high TxGNN score is therefore not supported by clinical data, and the prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case series | Indian J Pathol Microbiol | Characteristics of microsporidial keratoconjunctivitis in an eastern Indian cohort; a different cause from herpesvirus disease and not a study of aciclovir |
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Case series | Am J Ophthalmol | Drug-induced corneal lipidosis in two patients with AIDS treated for opportunistic infections; not a study of aciclovir efficacy |

## UK Market Information

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0503021C0AAAKAK | Aciclovir 1g/40ml solution for infusion vials | Aciclovir |
| 0503021C0AAAGAG | Aciclovir 200mg dispersible tablets | Aciclovir |
| 0503021C0AAABAB | Aciclovir 200mg tablets | Aciclovir |
| 0503021C0AAAAAA | Aciclovir 200mg/5ml oral suspension sugar free | Aciclovir |
| 0503021B0AAAAAA | Aciclovir 250mg powder for solution for infusion vials | Aciclovir sodium |
| 0503021C0AAAIAI | Aciclovir 250mg/10ml solution for infusion vials | Aciclovir |
| 1103030C0AAAAAA | Aciclovir 30mg/g eye ointment | Aciclovir |
| 0503021C0AAAHAH | Aciclovir 400mg dispersible tablets | Aciclovir |
| 0503021C0AAACAC | Aciclovir 400mg tablets | Aciclovir |
| 0503021C0AAAFAF | Aciclovir 400mg/5ml oral suspension sugar free | Aciclovir |
| 1310030C0AAAAAA | Aciclovir 5% cream | Aciclovir |
| 0503021B0AAABAB | Aciclovir 500mg powder for solution for infusion vials | Aciclovir sodium |
| 0503021C0AAAJAJ | Aciclovir 500mg/20ml solution for infusion vials | Aciclovir |
| 0503021C0AAAEAE | Aciclovir 800mg dispersible tablets | Aciclovir |
| 0503021C0AAADAD | Aciclovir 800mg tablets | Aciclovir |
| 1310030C0BIAAAA | Aviral 5% cream | Aciclovir |
| 1310030C0BHAAAA | Clearsore 5% cream | Aciclovir |
| 1310030C0BNAAAA | Cymex Ultra 5% cream | Aciclovir |
| 0503021C0BDAAAE | Duvimex 800mg dispersible tablets | Aciclovir |
| 1310030C0BJAAAA | Galpharm Cold Sore 5% cream | Aciclovir |

Showing 20 of 45 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

## Safety Considerations

- **Drug Interactions**: 454 potential interactions are recorded. Those graded Moderate are balsalazide, mesalazine, olsalazine, sulfasalazine and trospium. Several others (for example amphotericin B, metformin, morphine and omeprazole) are recorded with an unknown severity grade.

For warnings and contraindications, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trials or relevant publications for this disease. The retrieved papers concern conditions that are not expected to respond to aciclovir, so the evidence level is L5.

**To proceed, the following is needed:**
- Clarification of whether the target condition is herpesvirus-related, and any clinical or laboratory evidence that supports aciclovir use in it
- Detailed mechanism of action data
- Review of ophthalmic route and formulation options, as the UK products identified are an oral suspension and topical creams
- Warnings and contraindications from the SmPC and BNF
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

