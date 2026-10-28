---
layout: default
title: Zidovudine
parent: Model Prediction Only (L5)
nav_order: 660
evidence_level: L5
indication_count: 4
monitor_inn: "Zidovudine"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-28
description: "Zidovudine: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: HIV infection and AIDS"
---

# Zidovudine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Zidovudine: From HIV Infection to Simian Immunodeficiency Virus Infection
{: .text-alpha }

## One-Sentence Summary

Zidovudine is a nucleoside reverse transcriptase inhibitor, originally used for HIV infection and AIDS (as recorded in the knowledge graph).
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, an animal disease model rather than a human indication.
There are **no registered clinical trials** and **20 publications** (all preclinical or animal studies), none of them human studies of this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection and AIDS (relation recorded in the knowledge graph; no approved indication text is available in the UK licence data) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

The predicted indication is a non-human disease. The cited macaque studies directly examine SIV infection, but they are animal studies, not human clinical evidence. The evidence level is therefore conservatively set at L5 in line with the reporting rules, which reserve L1–L4 for studies directly supporting a human clinical use. The source scoring labelled this L4; this report does not adopt that level.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, zidovudine is an NRTI. Its antiviral effect depends on blocking reverse transcriptase, the enzyme that retroviruses use to copy their genetic material.

SIV is a lentivirus closely related to HIV and replicates through the same reverse transcriptase-dependent cycle. This explains why the model links zidovudine to SIV, and why macaques infected with SIV are widely used as a model of HIV infection.

However, this is a model-organism connection. SIV infection is not a human disease, so the prediction mainly reflects the drug's known anti-retroviral activity rather than a new human therapeutic opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The compiled literature is almost entirely animal or in vitro work. The most relevant items are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | Animal study | AIDS | Post-exposure prophylaxis with zidovudine, lamivudine and indinavir after vaginal SIV exposure in macaques |
| [7695293](https://pubmed.ncbi.nlm.nih.gov/7695293/) | 1995 | Animal study | Antimicrob Agents Chemother | Immediate oral zidovudine in SIV-infected newborn macaques prevented infection or reduced virus load and improved antiviral immune responses |
| [7690823](https://pubmed.ncbi.nlm.nih.gov/7690823/) | 1993 | Animal study | J Infect Dis | Zidovudine started 1 to 72 hours after SIV inoculation in rhesus monkeys; effect depended on timing of initiation |
| [7797947](https://pubmed.ncbi.nlm.nih.gov/7797947/) | 1995 | Animal study | J Infect Dis | In perinatally infected rhesus macaques, zidovudine prolonged survival and lowered CNS virus load, but did not prevent infection |
| [2016686](https://pubmed.ncbi.nlm.nih.gov/2016686/) | 1991 | Animal study | J Acquir Immune Defic Syndr | In cynomolgus monkeys, neither zidovudine nor 3'-fluorothymidine prevented infection; the latter was about ten times more potent in delaying antigen appearance |
| [7848683](https://pubmed.ncbi.nlm.nih.gov/7848683/) | 1994 | Animal study | AIDS Res Hum Retroviruses | Animal model of acute SIV infection in zidovudine-treated cynomolgus macaques, examining viral load kinetics |
| [9021180](https://pubmed.ncbi.nlm.nih.gov/9021180/) | 1997 | In vitro / animal | Antimicrob Agents Chemother | Zidovudine-resistant SIV mutant (Q151M) caused AIDS in newborn macaques |
| [11020686](https://pubmed.ncbi.nlm.nih.gov/11020686/) | 2000 | Review | Ann Emerg Med | Review of non-occupational HIV post-exposure prophylaxis; no direct human efficacy studies, with indirect support from animal studies |
| [14610172](https://pubmed.ncbi.nlm.nih.gov/14610172/) | 2003 | Animal study | J Virol | Early post-exposure antiretroviral combinations including zidovudine and effects on lymphocyte proliferation in SIV-infected macaques |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503010Y0AAABAB | Zidovudine capsules 250 mg | Capsule | Not stated in the data compiled for this report |

One single-ingredient record is listed and its status is valid. The listed identifier follows a BNF-style code format rather than a standard PL number, so it should be verified against MHRA records.

---

## Safety Considerations

**Contraindication relations recorded in the knowledge graph** (these are not label text, and they need confirmation against the SmPC):
- Liver: liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis
- Kidney and urinary: kidney disease, pyoureter
- Pancreas and gallbladder: pancreatitis, gallbladder disease
- Muscle: myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, dermatomyositis, myositis
- Blood: neutropenia, agranulocytosis, anaemia, macrocytic anaemia
- Metabolic: lactic acidosis, hypertriglyceridaemia, obesity disorder, monogenic obesity

**Drug interactions** (100 recorded; main examples from the interaction database):
- Moderate: amphotericin B (including cholesteryl sulfate and lipid complex forms), corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone, prednisolone, prednisone, triamcinolone), naltrexone, rosuvastatin, simvastatin, orlistat
- Minor: cimetidine, clarithromycin
- Severity not classified: pantoprazole, morphine, metformin, omeprazole

Label warnings and contraindications were not available. Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link is strong, but SIV infection is an animal model of HIV, not a human indication, and there are no clinical trials. Zidovudine's established role in HIV is already captured by its original indication, so this prediction offers little new for UK clinical practice.

**To proceed, the following is needed:**
- Clarify whether the question is research use (model organism) or a genuine human indication; if the former, no repurposing action is needed
- Mechanism of action data from DrugBank
- Approved indication text and SmPC warnings and contraindications from the MHRA/BNF
- Verification of the licence record (identifier format, dosage form and indication text are missing)

---

### Other predictions in the data (for reference)

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Feline acquired immunodeficiency syndrome | 0.9996 | L5 | Veterinary use only. Animal studies exist, including cat toxicity data (anaemia in FeLV-infected cats). Not a human indication |
| Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 0.9996 | L5 | Model prediction only; no mechanistic link identified. Zidovudine's mitochondrial, muscle and haematological toxicities argue for caution |
| Obsolete familial combined hyperlipidaemia | 0.9962 | L5 | Model prediction only; the term is obsolete. Antiretroviral therapy is associated with lipid disturbances, so benefit is implausible |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

