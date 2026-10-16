---
layout: default
title: Efavirenz
parent: Moderate Evidence (L3-L4)
nav_order: 245
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
description: "Efavirenz: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L4). Approved use: HIV infectious disease"
monitor_inn: "Efavirenz"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Efavirenz
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Efavirenz: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI), originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary indication,
but there are **no registered clinical trials** and only **1 in vitro/structural publication** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the UK authorisation record contains no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, efavirenz is an HIV-1 NNRTI. Its efficacy in HIV infection is established, and it works by binding directly to the viral reverse transcriptase enzyme.

Feline immunodeficiency virus (FIV) is a related lentivirus that causes an AIDS-like syndrome in cats. This relationship is the likely reason for the very high TxGNN score. However, FIV reverse transcriptase differs structurally from HIV-1 reverse transcriptase, and NNRTIs are generally expected to have weak or no activity against it. The single available study (2023) compared NNRTIs, including efavirenz, against feline and human immunodeficiency viruses at the biochemical and structural level. Only its title and introductory text were available, so it is not possible to confirm whether efavirenz was active against FIV.

The score reflects similarity to the known HIV indication and is not independent clinical support. This is also a veterinary indication, so it falls outside the scope of human drug repurposing.

For completeness, the data also include two other predictions:
- **Simian immunodeficiency virus infection** (score 99.80%, L4, Hold). Wild-type SIV is intrinsically resistant to NNRTIs. The animal studies use RT-SHIV, a chimeric virus carrying HIV-1 reverse transcriptase, in macaques. They show efavirenz-containing regimens suppress viral load in this model, which reflects the HIV-1 target rather than a distinct SIV indication.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.77%, L5, Hold). There is no clinical trial or literature support and no established mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Biochemical/structural in vitro study | Journal of Veterinary Science | Compared nevirapine, efavirenz and rilpivirine against feline and human immunodeficiency virus reverse transcriptase to assess the potential of NNRTIs for treating FIV infection. No effective treatment currently exists for infected cats. Efavirenz-specific results could not be confirmed from the available text. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BNF code 0503010D0AAADAD | Efavirenz tablets 600 mg | Tablet (as named in the record) | Not stated in the available record |

The record is a single-ingredient product with valid status. The BNF classification code (section 5.3.1, HIV infection) corresponds to antiviral treatment of HIV. A formal MHRA marketing authorisation (PL) number was not provided.

## Cytotoxicity

Efavirenz is not an antineoplastic drug, so this section does not apply.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** The TxGNN knowledge graph links efavirenz with the following conditions. These should be checked against the SmPC:
  - Liver: liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, chronic hepatitis B and C virus infection
  - Neurological and psychiatric: epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, delusional disorder, paranoid schizophrenia
  - Renal and metabolic: kidney disease, Fanconi renotubular syndrome, lactic acidosis, hypertriglyceridemia, hypophosphatemia, osteomalacia, rickets, obesity disorders
  - Other: gallbladder disease, pyoureter
- **Drug Interactions:** 100 interactions were recorded. Those listed below are examples from the first 20 entries retrieved (sample, not a complete list).
  - **Major:** dolasetron
  - **Moderate:** acarbose, famotidine, rabeprazole, bupropion, aprepitant, clarithromycin, loperamide, pioglitazone, saxagliptin, minocycline, dronabinol, and corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone)

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is limited to a single in vitro/structural study with no clinical trials, and efavirenz is not expected to inhibit FIV reverse transcriptase effectively. The very high TxGNN score reflects similarity to the existing HIV indication rather than independent support. The proposed indication is also veterinary, outside the scope of human drug repurposing.

**To proceed, the following is needed:**
- Full text of the 2023 biochemical study to confirm efavirenz-specific activity against FIV reverse transcriptase
- In vivo data in cats, if a veterinary pathway is being considered (this would be a separate regulatory route from human medicines)
- Mechanism of action data (for example, from DrugBank)
- Authorised indication text and the MHRA marketing authorisation number for the UK product
- Full SmPC warnings and contraindications to complete the safety review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

