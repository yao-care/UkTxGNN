---
layout: default
title: Entecavir
parent: Model Prediction Only (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a nucleoside analogue originally used to treat chronic hepatitis B virus (HBV) infection.
The TxGNN model predicts it may be effective for **chronic hepatitis C virus (HCV) infection**, but the supporting evidence concerns HBV control in patients co-infected with HCV and HBV rather than treatment of HCV itself.
Currently **2 related clinical trials** and **20 publications** are linked to this prediction, and none shows anti-HCV activity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 (observational and review evidence only; no study shows entecavir treating HCV) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, entecavir is a guanosine nucleoside analogue that inhibits HBV polymerase. Its efficacy in chronic hepatitis B is well established.

The mechanistic link to HCV is weak. HCV is an RNA virus that replicates through a different polymerase (NS5B), and entecavir has no known direct activity against it. The high TxGNN score probably reflects the close association between the two diseases in the knowledge graph. Both are chronic viral hepatitides, they often co-occur, and they share treatment settings.

The only plausible clinical link is indirect. In patients with HCV/HBV co-infection, clearing HCV with direct-acting antivirals (DAAs) can trigger HBV reactivation. Entecavir suppresses HBV replication in that setting. This is management of the co-infecting HBV, not treatment of HCV.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of HBV reactivation during DAA treatment of HCV/HBV co-infection. It tests DAAs, not entecavir against HCV. |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | Not applicable | Unknown | 60 | Randomised, open-label study of prophylactic nucleos(t)ide analogue (12 versus 24 weeks) to prevent HBV reactivation during DAA therapy. It supports the HBV-prophylaxis role, not anti-HCV activity. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | RCT | Clin Gastroenterol Hepatol | Randomised trial of entecavir to prevent HBV reactivation during DAA treatment of HCV/HBV dual infection. |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | 66 anti-HCV-positive patients with chronic hepatitis B on nucleos(t)ide analogues, assessed for HCV reactivation and viral load changes. |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Observational | J Gastroenterol Hepatol | Risk of HBV reactivation when treating chronic hepatitis C with DAAs in patients also infected with HBV. |
| [35108715](https://pubmed.ncbi.nlm.nih.gov/35108715/) | 2022 | Observational | Dig Dis | Incidence and clinical course of HBV reactivation in HBsAg- and/or anti-HBc-positive patients treated with DAAs for HCV. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Treatment advances in HBV/HCV co-infection; these patients are at high risk of cirrhosis and hepatocellular carcinoma. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antivirals for hepatitis B (including entecavir) and C, and their effects on kidney function. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Overview of treatment and future prospects for chronic hepatitis B and C. |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Review | World J Hepatol | Management of hepatitis B and C around liver and kidney transplantation; entecavir needs renal dose adjustment. |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clin Res Hepatol Gastroenterol | Present and future management of hepatitis B and C in children. |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Review | Biomedicines | Therapy of chronic viral hepatitis; long-term nucleos(t)ide analogue therapy has transformed chronic hepatitis B outcomes. |

---

## UK Market Information

| Reference Code | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503030C0AAAAAA | Entecavir tablets 500 micrograms | Tablet | Not specified in the data compiled for this report |

One authorisation is recorded, with status valid and a single-ingredient product. The data compiled for this report did not include the authorisation number (PL), approved indication text or manufacturer, so please check the MHRA register, the SmPC and the BNF.

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** impaired renal function, fatty liver disease, non-alcoholic steatohepatitis and lactic acidosis. Confirm against the SmPC.
- **Monitoring points from the literature:**
  - lactic acidosis;
  - severe hepatitis flares after discontinuation;
  - renal dose adjustment;
  - thrombocytopenia (one case report, [PMID 34823407](https://pubmed.ncbi.nlm.nih.gov/34823407/)).
- **Drug Interactions:** 44 interactions were recorded, all of those listed being moderate severity. The main groups are:
  - potentially nephrotoxic agents: amphotericin B (including lipid, liposomal and cholesteryl sulfate formulations), vancomycin, kanamycin, neomycin and polymyxin B;
  - acid suppressants: famotidine, ranitidine and cimetidine;
  - metformin;
  - aminosalicylates: mesalazine, balsalazide, olsalazine and sulfasalazine;
  - amoxicillin, levofloxacin and orlistat.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No evidence shows that entecavir treats HCV, and it has no known activity against HCV polymerase. The trials and papers concern HBV reactivation risk in HCV/HBV co-infection, where entecavir acts on HBV. Modern DAAs already cure HCV in the great majority of patients.

**To proceed, the following is needed:**
- Preclinical or clinical evidence of direct anti-HCV activity, which is currently absent.
- If the aim is HBV prophylaxis during DAA therapy, reframe it as a co-infection management question rather than a new HCV indication.
- Mechanism of action data and SmPC warnings and contraindications for entecavir.
- The MHRA authorisation number, approved indication text and dosage form for the UK product.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

