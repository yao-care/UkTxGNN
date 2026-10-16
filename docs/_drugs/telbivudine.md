---
layout: default
title: Telbivudine
parent: Model Prediction Only (L5)
nav_order: 598
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Telbivudine: predicted new indication Chronic hepatitis C virus infection (evidence level L5). Approved use: Chronic hepatitis B virus infection"
monitor_inn: "Telbivudine"
predicted_indications: ["chronic hepatitis C virus infection", "hepatitis B virus infection", "HIV infectious disease", "hepatitis C virus infection", "disorder of phenylalanine metabolism", "disorder of tyrosine metabolism", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria"]
---

# Telbivudine
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

# Telbivudine: From Chronic Hepatitis B Virus Infection to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Telbivudine is a nucleoside analogue antiviral originally used to treat chronic hepatitis B virus (HBV) infection.
The TxGNN model predicts it may be effective for **chronic hepatitis C virus (HCV) infection**, but there are **no registered clinical trials** and **6 publications**, all general hepatitis reviews or HBV-focused studies. None of them shows anti-HCV activity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection (the UK authorisation record does not include indication text) |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. The published literature describes telbivudine as an L-nucleoside analogue of thymidine. It is phosphorylated to its active triphosphate form and inhibits HBV DNA polymerase, terminating viral DNA chain elongation. Its efficacy in chronic hepatitis B is established.

The link to hepatitis C is weak. HCV is an RNA virus that replicates through the NS5B RNA-dependent RNA polymerase, which is a different target class from HBV DNA polymerase. No direct mechanistic link has been established. The high TxGNN score most likely reflects the shared hepatitis and antiviral context in the literature, because HBV and HCV are often discussed together. It probably does not reflect real anti-HCV activity.

Telbivudine's approved HBV use also appears separately in the model output as a lower-ranked prediction. That is the drug's established indication, not a repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25233195](https://pubmed.ncbi.nlm.nih.gov/25233195/) | 2014 | Review | J Perinatol | Reviews HBV and HCV in pregnancy and efforts to reduce mother-to-child transmission. It does not test telbivudine in HCV. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Overview of current and future treatment of chronic hepatitis B and C. The HBV section covers peginterferon and lamivudine. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Describes the effects of hepatitis B and C antiviral drugs, including telbivudine, on kidney function. Telbivudine is discussed as an HBV agent. |
| [18340426](https://pubmed.ncbi.nlm.nih.gov/18340426/) | 2008 | Review | Internist (Berl) | German guideline update on antiviral therapy for hepatitis B and C. Telbivudine is listed among HBV monotherapy options. |
| [21999649](https://pubmed.ncbi.nlm.nih.gov/21999649/) | 2011 | Review | Paediatr Drugs | Medical management of chronic liver disease in children, focusing on potentially curable conditions. |
| [23697556](https://pubmed.ncbi.nlm.nih.gov/23697556/) | 2013 | Cohort | J Interferon Cytokine Res | Studied serum IL-37 levels and HBeAg seroconversion in 40 HBeAg-positive chronic hepatitis B patients on telbivudine. The study population had HBV, not HCV. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503030D0AAAAAA (BNF-style code; no PL number in the compiled data) | Telbivudine tablets 600 mg | Tablet (600 mg) | Not stated in the compiled data |

The compiled data list one valid single-ingredient authorisation. No indication text, manufacturer or NICE-appraised indication is available. The NICE single technology appraisal of telbivudine for chronic hepatitis B (PMID 19846025) concerned HBV, not HCV.

---

## Safety Considerations

- **Disease associations from the knowledge graph (not label text):** Contraindication-type links were found for kidney disease, myopathy and other muscle diseases (including myositis and dermatomyositis), peripheral neuropathy and other peripheral nervous system disease, familial periodic paralysis, lactic acidosis, fatty liver disease and non-alcoholic steatohepatitis, and pyoureter. Reviews of nucleoside analogues describe myopathy, neuropathy and lactic acidosis as class adverse effects. These links should be confirmed against the SmPC.
- **Drug interactions:** 96 interactions were identified. All 20 listed in the compiled data are rated Moderate. The main groups are:
  - corticosteroids (hydrocortisone, dexamethasone, prednisone, betamethasone, budesonide, triamcinolone)
  - amphotericin B formulations
  - aminoglycosides and glycopeptides (kanamycin, neomycin, vancomycin)
  - statins (simvastatin, rosuvastatin)
  - aminosalicylates (mesalazine, sulfasalazine, balsalazide, olsalazine)
  - metronidazole and orlistat

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials for HCV, and the retrieved literature does not show anti-HCV activity. Telbivudine targets HBV DNA polymerase, whereas HCV depends on NS5B RNA polymerase, so there is no credible mechanistic link. Current HCV treatment relies on direct-acting antivirals, so the prediction appears to be a knowledge-graph artefact.

**To proceed, the following is needed:**
- In vitro evidence of anti-HCV activity (for example, replicon assays)
- A plausible mechanism for telbivudine acting on HCV
- Detailed mechanism of action data for telbivudine
- SmPC-based warnings and contraindications to replace the knowledge-graph associations
- Comparison against current direct-acting antiviral regimens to establish any unmet need
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

