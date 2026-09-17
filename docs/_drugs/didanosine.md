---
layout: default
title: Didanosine
parent: Model Prediction Only (L5)
nav_order: 209
evidence_level: L5
indication_count: 3
---

# Didanosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Didanosine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Didanosine (ddI) is a nucleoside reverse transcriptase inhibitor (NRTI) whose established clinical role is HIV‑1 antiretroviral therapy. The TxGNN model's top-ranked prediction — **Simian Immunodeficiency Virus (SIV) infection** — is not a human disease but a primate model used in HIV/AIDS research, so despite a **99.33%** prediction score, this is not an actionable human repurposing candidate; the supporting evidence base consists entirely of **12 preclinical/animal publications and 0 clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV‑1 infection (antiretroviral therapy) — general pharmacological knowledge; not captured in the licence data supplied |
| Predicted New Indication | Simian immunodeficiency virus infection (an animal-model disease, not a human clinical indication) |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L4 (preclinical/animal studies only) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for didanosine were not available in this evidence pack (flagged as a High-severity data gap). From general pharmacology, didanosine is a purine nucleoside analogue that, after intracellular phosphorylation to ddATP, inhibits HIV reverse transcriptase and causes chain termination — the basis of its efficacy in HIV‑1 infection.

The mechanistic rationale behind this TxGNN prediction is that SIV and HIV are both lentiviruses with closely homologous reverse transcriptase enzymes, so an NRTI active against HIV would be expected to also inhibit SIV replication in vitro and in animal models. This is pharmacologically plausible and is in fact supported by direct evidence: PMID 9282812 and 9923010 both describe didanosine reducing SIV viral load in macaques.

However, SIV infection is a **veterinary/laboratory research model**, not a disease that occurs — or is treated — in humans. TxGNN's high score reflects "mechanistic similarity between related viral targets," not a genuine unmet human clinical need. The same limitation applies to the model's second-ranked prediction, feline acquired immunodeficiency syndrome (feline AIDS, also L4, Hold), which is likewise a veterinary indication. The third-ranked prediction (a rare neurodevelopmental disorder) has **zero supporting trials or literature** (L5) and is essentially an unvalidated graph-network association; didanosine's known mitochondrial/neurological toxicity would argue against, rather than for, this direction. None of the three top predictions currently represents a credible human repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

*(Evidence for the top-ranked prediction, simian immunodeficiency virus infection — all preclinical/animal or in vitro studies; no human trials or case series exist for this "indication.")*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9282812](https://pubmed.ncbi.nlm.nih.gov/9282812/) | 1997 | Animal study | AIDS Res Hum Retroviruses | Didanosine, but not high-dose hydroxyurea, rescued pigtail macaques from a lethal dose of SIV(smmpbj14) |
| [9923010](https://pubmed.ncbi.nlm.nih.gov/9923010/) | 1998 | Animal study | Research in Virology | Pre-treatment with ddI reduced acute SIVmac251 viral load and altered cytokine profiles in cynomolgus macaques |
| [22013040](https://pubmed.ncbi.nlm.nih.gov/22013040/) | 2012 | Animal study / adverse event report | Journal of Virology | Fatal pancreatitis occurred in SIV-infected macaques treated with ddI plus stavudine after immune-checkpoint blockade — a safety signal |
| [15182307](https://pubmed.ncbi.nlm.nih.gov/15182307/) | 2004 | Animal study | European Journal of Neuroscience | Related dideoxynucleoside analogue lowered brain viral burden and IDO expression in SIV-infected rhesus monkeys |
| [8870848](https://pubmed.ncbi.nlm.nih.gov/8870848/) | 1996 | Animal study | AIDS Res Hum Retroviruses | Cytokine mRNA expression profiled in tissues during acute SIVmac251 infection of macaques |
| [14965468](https://pubmed.ncbi.nlm.nih.gov/14965468/) | 2004 | Animal study | DNA and Cell Biology | T-cell receptor excision circles evaluated as a surrogate marker in SHIV/SIV macaque models |
| [11090360](https://pubmed.ncbi.nlm.nih.gov/11090360/) | 2000 | Animal study (randomised, non-human primate) | Science | Structured treatment interruption with HAART controlled SIV viral rebound in acutely infected macaques |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro study | Antiviral Therapy | Susceptibility of HIV‑2, SIV and SHIV strains to approved anti-HIV‑1 compounds evaluated |
| [8554904](https://pubmed.ncbi.nlm.nih.gov/8554904/) | 1995 | Model description | AIDS Res Hum Retroviruses | Human thymic organ culture developed as an in vitro model for studying HIV/SIV pathogenesis |
| [11435599](https://pubmed.ncbi.nlm.nih.gov/11435599/) | 2001 | In vitro study | Journal of Virology | Efficacy of dideoxynucleosides (including didanosine's class) against human foamy virus assessed |

---

## UK Market Information

No UK marketing authorisation was identified for didanosine in the data reviewed. The product is recorded as **not currently marketed** in the UK (0 authorisations on file).

---

## Safety Considerations

Structured safety data (key warnings, contraindications, drug interactions) were not available for this evidence pack (Blocking data gap — TFDA/MHRA SmPC warnings and contraindications could not be retrieved).

Two preclinical safety signals emerged from the literature search and are worth noting for risk assessment, though they are not formal SmPC data:
- **Fatal pancreatitis**: reported in SIV-infected macaques treated with didanosine plus stavudine following immune-checkpoint blockade (PMID 22013040) — pancreatitis is a recognised class effect of didanosine in humans.
- **Sensory neuropathy**: didanosine induced sensory neuropathy with impaired mitochondrial and neurotrophic gene expression in a feline immunodeficiency virus model (PMID 17616550) — consistent with the known human risk of antiretroviral toxic neuropathy with this drug.

Please refer to the SmPC and BNF for complete safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications fail to clear the bar for further evaluation: the top two (SIV infection, feline AIDS) are animal/veterinary diseases rather than human indications, and the third has no supporting evidence at all (L5). No human clinical trials exist for any of them, and a blocking data gap (missing SmPC warnings/contraindications) prevents even a basic safety review.

**To proceed, the following is needed:**
- TFDA/MHRA-equivalent SmPC warnings and contraindications for didanosine (Blocking gap, DG001)
- A confirmed mechanism-of-action record from DrugBank (High-priority gap, DG002)
- Re-examination of the TxGNN candidate list for genuine human-disease predictions further down the ranking, since the top three are not clinically actionable
- If a credible human indication is identified, a fresh evidence pack with clinical trial and literature searches specific to that indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

