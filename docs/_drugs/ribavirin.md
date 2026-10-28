---
layout: default
title: Ribavirin
parent: High Evidence (L1-L2)
nav_order: 539
evidence_level: L1
indication_count: 9
monitor_inn: "Ribavirin"
predicted_indications: ["chronic hepatitis B virus infection", "primitive portal vein thrombosis", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "hepatic porphyria", "IgG4-related pachymeningitis", "eosinophilic angiocentric fibrosis", "IgG4-related mesenteritis"]
last_modified_at: 2026-10-23
description: "Ribavirin: predicted new indication Chronic hepatitis B virus infection (evidence level L5). Approved use: Chronic hepatitis C virus infection"
---

# Ribavirin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **9** 
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

## Ribavirin: From Chronic Hepatitis C Virus Infection to Chronic Hepatitis B Virus Infection
{: .text-alpha }

## One-Sentence Summary

Ribavirin is an antiviral medicine whose known indications are chronic hepatitis C virus infection and respiratory syncytial virus infection.
The TxGNN model predicts it may be effective for **chronic hepatitis B virus infection**, but the supporting evidence is largely indirect: of the **15 clinical trials** and **20 publications** retrieved, only a few examine hepatitis B, and none isolates ribavirin's own contribution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection (relation recorded in the knowledge graph; the UK licence record contains no indication text) |
| Predicted New Indication | Chronic hepatitis B virus infection |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L1 (see note below) |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

*Note on evidence level:* NCT00114361 is a completed Phase 3 trial directly in HBeAg-negative chronic hepatitis B, and NCT03759782 is a Phase 3 trial of ribavirin in HBV, but its status is unknown. Only one directly relevant Phase 3 trial has a completed status, which on a strict reading falls short of the L1 criterion (two or more completed Phase 3 RCTs). That trial tests peginterferon plus ribavirin, so ribavirin's separate effect is not isolated. The level is therefore best treated as provisional and weaker than "L1" suggests.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Ribavirin is a guanosine nucleoside analogue with broad activity against RNA viruses such as hepatitis C. Its proposed actions include inhibiting IMPDH, depleting the GTP pool and modulating the immune response.

Hepatitis B is a DNA virus, so direct antiviral activity is mechanistically weak. Any benefit is more plausibly immunomodulatory, for example as an add-on to interferon-based therapy by shifting the immune response towards Th1 and enhancing interferon signalling. Much of the retrieved clinical context also involves HBV/HCV co-infection, where ribavirin acts on the hepatitis C component.

The very high TxGNN score is a network-based prediction. It does not confirm efficacy against HBV specifically.

---

## Clinical Trial Evidence

Many of the 15 retrieved trials are hepatitis C studies in which ribavirin is a background agent. The table lists those most relevant to hepatitis B.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | Completed | 138 | Peginterferon alfa-2a plus ribavirin versus peginterferon monotherapy in HBeAg-negative chronic HBV; ribavirin's separate contribution is not clear from the available data |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | Completed | 120 | Pilot study of interferon alpha-2b plus ribavirin in chronic hepatitis B; small and exploratory |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Phase 3 | Unknown | 24 | Pilot study of ribavirin added to nucleoside analogue therapy to boost HBV antiviral activity |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | Unknown | 320 | Peginterferon alfa-2a plus ribavirin in HCV/HBV co-infection and chronic hepatitis C |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Phase 4 | Unknown | 20 | Pilot of pegylated interferon alfa-2b plus ribavirin in dual hepatitis B and D infection |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | Completed | 36 | Direct-acting antivirals plus ribavirin in HCV with decompensated cirrhosis; ribavirin is a backbone agent, so no HBV efficacy is shown |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Phase 4 | Completed | 129 | Peginterferon plus ribavirin and IL-28B expression in HCV genotype 1; little bearing on HBV |
| [NCT01425970](https://clinicaltrials.gov/study/NCT01425970) | Phase 2 | Terminated | 210 | INX-08189 with peginterferon and ribavirin in HCV; terminated early |

The remaining retrieved trials (for example NCT01795911, NCT01309932, NCT00911963, NCT01195181, NCT03186313, NCT02483156, NCT01001754 and NCT01830127) are hepatitis C studies with ribavirin as a background agent and are not HBV evidence.

---

## Literature Evidence

The retrieved publications are almost entirely reviews. None is a randomised trial of ribavirin in hepatitis B.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV co-infection; peginterferon plus ribavirin was previously recommended for co-infected patients with positive HCV RNA |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | Treatment and outcomes of dual HCV/HBV infection, which carries a higher risk of disease progression |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Review | Hepatology | Immunological aspects of antiviral therapy in chronic HBV and HCV |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Review | Curr Opin Virol | Effect of IL28B genotype on treatment response in HBV and HCV |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Review | World J Gastroenterol | IL28B polymorphism and outcomes in HBV infection |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Review | Annu Rev Med | Treatment strategies for chronic hepatitis B and C |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | Treatment options for chronic hepatitis B and C in children |
| [24379612](https://pubmed.ncbi.nlm.nih.gov/24379612/) | 2013 | Review | World J Gastroenterol | Prevention of hepatocellular carcinoma in chronic HBV and HCV |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503050B0AAAEAE | Ribavirin tablets 200 mg | Not recorded | Not recorded in the licence data |

This is one valid single-ingredient record. It carries no indication text, so the UK approved indication cannot be stated from the data compiled for this report. The identifier looks like a BNF-style product code rather than a "PL" number, so check it against the MHRA record.

---

## Safety Considerations

**Relations recorded in the knowledge graph (not label text):** the knowledge graph records contraindication relations between ribavirin and the following conditions. They are not confirmed by SmPC text:
- Respiratory: chronic obstructive pulmonary disease, asthma (including intrinsic and allergic), interstitial lung disease, sarcoidosis
- Liver and pancreas: cirrhosis of liver, autoimmune hepatitis, pancreatitis
- Blood: anaemia (including macrocytic and haemolytic), sickle cell anaemia, haemoglobinopathy, pancytopenia, inherited aplastic anaemia
- Cardiovascular: myocardial infarction, coronary artery disease, atherosclerosis, myocardial ischaemia
- Other: impaired renal function, periodontitis

**Drug interactions:** 100 interactions were found in the DDInter database, but the severity level for each is recorded as "Unknown". Examples include pantoprazole, omeprazole, lansoprazole, metformin, glimepiride, morphine, prednisone and doxycycline. Their clinical significance cannot be judged from these data.

**Other signals in the retrieved literature:** the paper on hepatopulmonary syndrome reports interferon-alpha-induced pulmonary granulomatosis, and several case reports describe porphyria cutanea tarda arising during peginterferon/ribavirin therapy. These are reports of possible adverse events, not evidence of benefit.

Please refer to the SmPC and BNF for authoritative warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Other Predicted Indications (Briefly)

The other eight predictions have no supporting clinical trials, and their evidence level is L5: primitive portal vein thrombosis, hepatoportal sclerosis, early-onset familial noncirrhotic portal hypertension, hepatopulmonary syndrome, hepatic porphyria, IgG4-related pachymeningitis, eosinophilic angiocentric fibrosis and IgG4-related mesenteritis. None has an identifiable mechanistic rationale, and the scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The hepatic porphyria and hepatopulmonary syndrome literature mainly describes adverse events or disease associations, not benefit.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only completed Phase 3 trial in hepatitis B tests ribavirin together with peginterferon and cannot isolate ribavirin's own effect. HBV is a DNA virus, so the mechanistic basis is weak. Ribavirin also has a substantial haematological safety burden, particularly haemolytic anaemia. The strong TxGNN score is not backed by HBV-specific efficacy evidence.

**To proceed, the following is needed:**
- A ribavirin-controlled comparison in HBV (with versus without ribavirin on a common backbone), with the results of NCT00114361 and NCT03759782 reviewed
- Mechanism of action data and a clear immunomodulatory rationale for HBV
- UK licence indication text, dosage form and SmPC warnings and contraindications
- Severity grading of the listed drug interactions
- A safety plan covering anaemia, pulmonary and cardiovascular risks, and pregnancy precautions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

