---
layout: default
title: Ribavirin
parent: Model Prediction Only (L5)
nav_order: 539
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ribavirin: predicted new indication Chronic hepatitis B virus infection (evidence level L5). Approved use: Chronic hepatitis C virus infection"
monitor_inn: "Ribavirin"
predicted_indications: ["chronic hepatitis B virus infection", "hepatopulmonary syndrome", "hepatoportal sclerosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "hepatic porphyria", "IgG4-related pachymeningitis", "IgG4-related mediastinitis", "eosinophilic angiocentric fibrosis"]
---

# Ribavirin
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

## Ribavirin: From Chronic Hepatitis C to Chronic Hepatitis B Virus Infection
{: .text-alpha }

## One-Sentence Summary

Ribavirin is an oral nucleoside analogue antiviral, originally used to treat chronic hepatitis C virus infection and respiratory syncytial virus (RSV) disease.
The TxGNN model predicts it may be effective for **chronic hepatitis B virus infection**, with **15 registered clinical trials** and **20 publications** linked to this prediction. However, most of this evidence concerns hepatitis C or HCV/HBV co-infection, so direct evidence for ribavirin in hepatitis B is limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection; RSV infection (the UK licence record compiled for this report has no indication text) |
| Predicted New Indication | Chronic hepatitis B virus infection |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 (as assigned in the compiled data; see the note below) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

> **Note on evidence level:** The L1 label rests on the count of completed Phase 3 trials. Only one completed Phase 3 trial (NCT00114361) tests ribavirin directly in hepatitis B, and its contribution of ribavirin over peginterferon alone is unconfirmed. A stricter reading would place the evidence closer to L2. The recommendation is therefore Hold rather than Go.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ribavirin is generally understood to be a nucleoside analogue with broad antiviral activity. Its proposed actions include inhibiting inosine monophosphate dehydrogenase (IMPDH), depleting intracellular guanosine triphosphate (GTP) pools, and modulating immune responses.

Hepatitis C and hepatitis B both cause chronic viral liver disease, and ribavirin has an established role in the former, usually alongside interferon-based or direct-acting antiviral therapy. This is the likely basis for the model's prediction.

The mechanistic case is weak, however. Ribavirin has no established direct activity against HBV, a DNA virus that replicates via reverse transcription. Any benefit is more plausibly indirect, by enhancing interferon-driven immune responses when given with peginterferon. Many of the listed trials involve HCV treatment or HCV/HBV co-infection, so the evidence is confounded. Modern first-line hepatitis B therapies (entecavir, tenofovir) have also made ribavirin-based approaches largely obsolete.

---

## Clinical Trial Evidence

The table lists the most relevant trials from the 15 compiled. Most are HCV studies in which ribavirin is a background drug.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | Completed | 138 | Peginterferon alfa-2a plus ribavirin versus peginterferon alone in HBeAg-negative chronic hepatitis B. This is the most direct test, but ribavirin's added value needs checking against the comparator arms. |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | Completed | 120 | Pilot of interferon alpha-2b plus ribavirin in chronic hepatitis B. Limited power. |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Phase 3 | Unknown | 24 | Pilot of ribavirin's immune-modulating properties to enhance nucleoside analogue therapy in hepatitis B. |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | Unknown | 320 | Peginterferon alfa-2a plus ribavirin in HCV/HBV co-infection versus HCV alone. Ribavirin's role in HBV is unclear. |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Phase 4 | Unknown | 20 | Pilot of pegylated interferon alfa-2b plus ribavirin in dual hepatitis B and delta (HDV) infection. |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | Completed | 36 | Direct-acting antivirals plus ribavirin in HCV with decompensated cirrhosis. HBV outcomes are not attributable to ribavirin. |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Phase 4 | Completed | 129 | Peginterferon alfa-2a plus ribavirin in genotype 1 HCV, looking at IL-28B expression. HCV-focused. |
| [NCT01195181](https://clinicaltrials.gov/study/NCT01195181) | Phase 4 | Completed | 506 | Surveillance and control programme for chronic hepatitis C. Not a ribavirin efficacy trial for HBV. |
| [NCT01425970](https://clinicaltrials.gov/study/NCT01425970) | Phase 2 | Terminated | 210 | INX-08189 with peginterferon and ribavirin in HCV genotype 2/3. Terminated early. |
| [NCT01795911](https://clinicaltrials.gov/study/NCT01795911) | Phase 2 | Completed | 165 | Peginterferon lambda with ribavirin and direct-acting antivirals in HCV. Ribavirin is background therapy. |

Five further trials, all in HCV, were also listed in the compiled data (NCT01309932, NCT00911963, NCT03186313, NCT02483156, NCT01001754, NCT01830127). They give no direct evidence for ribavirin in hepatitis B.

---

## Literature Evidence

No randomised controlled trials were identified in the compiled literature. The 20 publications are mostly narrative reviews of HBV/HCV co-infection or general viral hepatitis management.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV co-infection. Earlier recommendations favoured peginterferon plus ribavirin for patients with detectable HCV RNA. |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | Treatment and outcomes of dual HCV/HBV infection. Co-infected patients have a higher risk of disease progression. |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Review | Hepatology | Immunological aspects of antiviral therapy in chronic HBV and HCV. |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Review | World J Gastroenterol | IL28B polymorphism and HBV infection outcomes. Its link to peginterferon plus ribavirin response is established in HCV. |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Review | Curr Opin Virol | Effect of IL28B genotype on HBV and HCV infection. |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | Treatment options for chronic hepatitis B and C in children. |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Review | Annu Rev Med | Treatment strategies for chronic hepatitis B and C. Interferon and lamivudine were the main HBV options at the time. |
| [11929032](https://pubmed.ncbi.nlm.nih.gov/11929032/) | 2002 | Review | Indian J Pediatr | Management of chronic HBV and HCV infections. |
| [24379612](https://pubmed.ncbi.nlm.nih.gov/24379612/) | 2013 | Review | World J Gastroenterol | Prevention of hepatocellular carcinoma in chronic HBV and HCV infection. |
| [8314494](https://pubmed.ncbi.nlm.nih.gov/8314494/) | 1993 | Review | Gut | Historical treatment of chronic hepatitis B and C before interferon. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0503050B0AAAEAE | Ribavirin tablets 200 mg | Tablet | Not stated in the compiled data |

The identifier above is a drug product code from the compiled data rather than a standard MHRA PL number. The dosage form and approved indication text were not available. Please verify the current authorisation, indications and NICE appraisal status in the BNF and the MHRA records.

---

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report. The following signals come from other sources.

- **Knowledge-graph contraindication signals** (not label text): the TxGNN knowledge graph links ribavirin to contraindications in the following groups.
  - **Haematological:** anaemia, haemolytic anaemia, sickle cell anaemia, haemoglobinopathy, pancytopenia, inherited aplastic anaemia.
  - **Cardiovascular:** myocardial infarction, coronary artery disease, atherosclerosis, myocardial ischaemia.
  - **Respiratory:** COPD, asthma, interstitial lung disease, sarcoidosis.
  - **Hepatic, renal and other:** cirrhosis of the liver, autoimmune hepatitis, impaired renal function, pancreatitis, periodontitis.
- **Drug interactions:** 100 potential interactions were identified, but none has a severity grade in the compiled data. Examples include calcitriol, pantoprazole, glimepiride, mesalazine, doxycycline, metformin, omeprazole, morphine, prednisone and amphotericin B. These need verification against the BNF interaction checker and the SmPC.
- **Setting-specific concern:** ribavirin-associated haemolytic anaemia is a recognised concern in cirrhosis and related conditions.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only one completed Phase 3 trial tests ribavirin directly in chronic hepatitis B, and it was a combination with peginterferon. The mechanistic rationale for direct HBV activity is weak, most of the remaining evidence is HCV-related or confounded by co-infection, and established nucleos(t)ide analogue therapy has largely superseded such approaches. The safety profile, particularly haemolytic anaemia, adds further caution.

**To proceed, the following is needed:**
- Review of the NCT00114361 results to determine whether ribavirin adds benefit beyond peginterferon alone.
- Confirmation of the population in NCT00275938 (hepatitis B versus C) and the results of NCT03759782.
- Mechanism of action data and comparison against current first-line HBV therapies (entecavir, tenofovir).
- UK SmPC and BNF safety information, including label warnings and contraindications, and confirmation of the licensed indications and dosage form.
- A safety plan for haematological and cardiovascular risk, including monitoring.

**Other predicted indications:** The remaining nine predictions (for example hepatopulmonary syndrome, hepatoportal sclerosis and hepatic porphyria) have either no supporting studies or only reports of adverse events during HCV therapy. All are at Hold with no credible mechanistic rationale.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

