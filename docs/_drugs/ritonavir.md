---
layout: default
title: Ritonavir
parent: Moderate Evidence (L3-L4)
nav_order: 546
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "Ritonavir"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Ritonavir: predicted new indication Simian immunodeficiency virus infection (evidence level L4). Approved use: Not recorded in the local data"
---

# Ritonavir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

## Ritonavir: Simian immunodeficiency virus infection
{: .text-alpha }

## One-Sentence Summary

Ritonavir is an HIV protease inhibitor, originally used to treat HIV infection/AIDS and hepatitis C virus infection (as a pharmacokinetic booster).
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**,
but there are **no registered clinical trials** and the **10 publications** identified are almost entirely animal or in vitro studies. SIV is a non-human primate disease, so this is not a genuine human repurposing opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L4 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ritonavir is an HIV-1 protease inhibitor and a strong CYP3A4 inhibitor, widely used at low doses to boost the exposure of other antiretrovirals.

SIV is a close lentiviral relative of HIV, and its protease is structurally and functionally similar to HIV-1 protease. In vitro work supports this: ritonavir inhibited SIVmac239 with a 50% effective concentration of about 13 nM, compared with about 25 nM for HIV-1 (PMID 12709355).

However, the high TxGNN score most likely reflects the similarity of SIV to the already established HIV indication. SIV infection is a research model in non-human primates, not a human clinical condition. This should be regarded as supporting preclinical modelling rather than a true repurposing opportunity.

The other two predictions are weaker. Feline acquired immunodeficiency syndrome (score 0.9992, L5) is a veterinary disease with no supporting literature or trials. A rare neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter (score 0.9992, L5) has no identifiable mechanistic link to ritonavir and is likely a TxGNN model (deep learning) artefact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro | Antimicrob Agents Chemother | SIVmac239 inhibited by ritonavir (EC50 about 13 nM), comparable to HIV-1 (about 25 nM) |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antivir Ther | Susceptibility of HIV-2, SIV and SHIV to 16 approved anti-HIV-1 drugs, relevant to treatment and post-exposure prophylaxis |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal (macaque) | J Virol Methods | Oral HAART including lopinavir/ritonavir given to SHIV-infected rhesus macaques; effect on the CD8 subset assessed |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal (macaque) | PLoS Pathog | Highly intensified multidrug ART produced long-term viral suppression and limited the viral reservoir in a simian AIDS model |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal (macaque) | PLoS One | Suppressive combination ART plus the HDAC inhibitor SAHA in SIV-infected Chinese rhesus macaques, studying viral reservoirs |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal (macaque) | J Virol | Rapid viral decay in SIV-infected macaques given quadruple antiretroviral therapy |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal (macaque) | mBio | Lentiviral infection persisted in the brain despite effective ART |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal model development | Microbes Infect | Novel SHIV carrying an HIV-1 protease gene, developed as a tool for testing protease inhibitors in vivo |

Several of these studies concern antiretroviral regimens generally rather than ritonavir specifically. No human clinical studies in SIV were identified, as expected for a non-human disease.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503010U0AAACAC (BNF-style product code, not a PL number) | Ritonavir tablets 100 mg | Tablet | Not stated in the data compiled |

One single-ingredient authorisation is recorded as valid. Within the BNF, ritonavir sits in the HIV protease inhibitor group (chapter 5, infections).

## Safety Considerations

The knowledge graph links ritonavir to contraindication or caution signals in the following conditions (these are graph-derived and are not label text):

- **Cardiac:** long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, cardiomyopathy (including hypertrophic), myocardial ischaemia, coronary artery disease
- **Hepatic and biliary:** liver disease, cirrhosis, gallbladder disease, hyperbilirubinaemia, Gilbert syndrome, chronic hepatitis B virus infection
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hypertriglyceridaemia, familial combined hyperlipidaemia, potassium deficiency, gout/hyperuricaemia
- **Other:** pancreatitis, haemophilia

**Drug interactions:** 100 interactions were found. Examples of those graded **Major** include loperamide, triamcinolone and budesonide. Moderate interactions include acarbose, metformin, hydrocortisone, dexamethasone, bupropion, aprepitant, clarithromycin and metronidazole. Ritonavir's strong CYP3A4 inhibition underlies many of these, particularly with corticosteroids.

Label warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
SIV infection is a non-human primate research model, not a human indication, and the supporting evidence is limited to in vitro and animal studies (L4) with no clinical trials. The high TxGNN score reflects similarity to the existing HIV indication rather than a new therapeutic opportunity.

**To proceed, the following is needed:**
- Confirmation of whether any human or veterinary clinical use is intended; otherwise, deprioritise this prediction
- Mechanism of action data (DrugBank) and the approved indication text from the SmPC
- SmPC and BNF warnings and contraindications (a blocking gap for safety screening)
- A review of the two other predictions (feline AIDS and the neurodevelopmental disorder), which currently have no supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

