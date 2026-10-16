---
layout: default
title: Adefovir Dipivoxil
parent: Model Prediction Only (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Adefovir Dipivoxil: predicted new indication Chronic hepatitis C virus infection (evidence level L5). Approved use: Chronic hepatitis B virus infection"
---

# Adefovir Dipivoxil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Adefovir Dipivoxil: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Adefovir dipivoxil is an oral nucleotide analogue antiviral, originally used to treat chronic hepatitis B virus (HBV) infection.
The TxGNN model predicts it may be effective for **chronic hepatitis C virus (HCV) infection** (score 99.97%), but **no clinical trials** are registered for this prediction and the 10 publications retrieved are mostly general viral hepatitis reviews focused on HBV, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection (the UK licence record contains no indication text, so this comes from the TxGNN knowledge graph) |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From established pharmacology, adefovir dipivoxil is an oral prodrug of adefovir, an acyclic nucleotide analogue of adenosine monophosphate. Its active diphosphate form inhibits HBV DNA polymerase/reverse transcriptase and terminates viral DNA chain elongation.

The link to HCV is weak. HCV is an RNA virus that replicates through the NS5B RNA-dependent RNA polymerase, a different target from the one adefovir inhibits. The retrieved literature consists of general viral hepatitis reviews and HBV-focused papers, and none of it shows adefovir activity against HCV. The high TxGNN score most likely reflects network proximity between viral hepatitis disease nodes in the knowledge graph rather than a shared pharmacological mechanism.

Among the other predictions, **HIV infection** has a more credible basis. Several completed Phase 2 trials and a placebo-controlled randomised trial (PMID 11546945) exist, because adefovir inhibits retroviral reverse transcriptase. However, the doses needed for HIV were limited by nephrotoxicity, and tenofovir later replaced adefovir for HIV. This is not a favourable case for revival.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for chronic hepatitis C virus infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15588803](https://pubmed.ncbi.nlm.nih.gov/15588803/) | 2004 | Review | Best Pract Res Clin Gastroenterol | Treatment of chronic viral hepatitis; mainly covers interferon, lamivudine and adefovir for HBV |
| [16107195](https://pubmed.ncbi.nlm.nih.gov/16107195/) | 2005 | Not classified | Expert Rev Anti Infect Ther | Peginterferon alfa-2a for hepatitis B; notes monotherapy with interferon, lamivudine or adefovir remains unsatisfactory |
| [15918324](https://pubmed.ncbi.nlm.nih.gov/15918324/) | 2004 | Not classified | Lijec Vjesn | Treatment and prevention of viral hepatitis; discusses interferon and lamivudine, including YMDD mutations |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral drugs for hepatitis B and C and their effects on kidney function |
| [19149648](https://pubmed.ncbi.nlm.nih.gov/19149648/) | 2009 | Not classified | Med Chem | Bicyclol, a novel agent for hepatitis B and C; not about adefovir |
| [16699274](https://pubmed.ncbi.nlm.nih.gov/16699274/) | 2006 | Not classified | Dig Dis | Established and emerging viral hepatitis therapies; adefovir is licensed for HBV, while HCV is treated with interferon plus ribavirin |
| [18221137](https://pubmed.ncbi.nlm.nih.gov/18221137/) | 2006 | Not classified | Recent Pat Anti Infect Drug Discov | Pegylated interferons for chronic hepatitis B; adefovir listed among approved HBV drugs |
| [24797262](https://pubmed.ncbi.nlm.nih.gov/24797262/) | 2014 | Not classified | Viral Immunol | Serum cytokine profiles associated with HBeAg seroconversion after stopping nucleos(t)ide therapy |
| [22370225](https://pubmed.ncbi.nlm.nih.gov/22370225/) | 2012 | Guideline/Consensus | Orv Hetil | Hungarian consensus guideline for hepatitis B, C and D |
| [31572002](https://pubmed.ncbi.nlm.nih.gov/31572002/) | 2019 | Not classified | Cancer Manag Res | Antiviral therapy and survival in HBV-related small hepatocellular carcinoma |

None of these publications reports adefovir activity against HCV.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503030B0AAAAAA | Adefovir Dipivoxil 10 mg tablets | Tablet | Indication text not available in the licence record |

The identifier in the licence record resembles a BNF classification code rather than a standard PL number, so the authorisation details should be verified against the MHRA register. One single-ingredient authorisation is recorded as valid.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not taken from label text, so they need confirmation in the SmPC): kidney disease, pyoureter, obesity disorder, monogenic obesity, fatty liver disease, non-alcoholic steatohepatitis, lactic acidosis.
- **Renal function**: one retrieved review (PMID 25027705) addresses the effects of antivirals on kidney function. Nephrotoxicity is a recognised concern with adefovir and was dose-limiting in HIV studies.
- **Drug interactions**: 25 potential interactions were identified, none with a severity grading in the source. Examples include proton pump inhibitors (pantoprazole, omeprazole, lansoprazole, rabeprazole), H2 antagonists (ranitidine, famotidine), warfarin, heparin, ibuprofen, morphine, lidocaine, kanamycin, prednisolone and potassium chloride. These are unverified, so check against the SmPC and BNF.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HCV prediction has no registered trials, no supporting HCV-specific publications and no plausible mechanistic link. Modern direct-acting antivirals already treat HCV effectively, so there is also no clear unmet need.

**To proceed, the following is needed:**
- In vitro evidence of adefovir activity against HCV, to establish any mechanistic basis
- Detailed mechanism of action data and verified UK licence details (authorisation number and indication text)
- A renal safety monitoring plan, given the known nephrotoxicity risk
- If a repurposing direction is still wanted, assess HIV (which has Phase 2 data) or HBV co-infection settings instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

