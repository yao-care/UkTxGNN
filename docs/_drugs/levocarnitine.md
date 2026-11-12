---
layout: default
title: Levocarnitine
parent: Model Prediction Only (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
monitor_inn: "Levocarnitine"
predicted_indications: ["autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "rheumatoid arthritis", "sclerosing cholangitis", "gout", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "congestive heart failure", "hypoalphalipoproteinemia"]
description: "Levocarnitine: predicted new indication Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Levocarnitine
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

## Levocarnitine: Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome
{: .text-alpha }

## One-Sentence Summary

Levocarnitine is a form of carnitine that carries long-chain fatty acids into mitochondria for energy production, and it is marketed in the UK as a single-ingredient capsule.
The TxGNN model's ranked predictions include **Congestive Heart Failure**, which has the strongest supporting evidence of the ten candidates reviewed, with **2 clinical trials** and **10 publications** currently supporting this direction.
This report focuses on that top-evidence candidate. Other predictions are summarised briefly at the end of the "Why is This Prediction Reasonable?" section.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 (see note below) |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (17 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 17 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* Under the strict rule (at least two completed Phase 3 RCTs), the evidence is closer to L2. There is one completed Phase 2/3 RCT (n=268), plus a small recruiting Early Phase 1 trial. The L1 label comes from the upstream scoring and should be read with caution.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug in the data compiled for this report. From established physiology, levocarnitine is required for transporting long-chain fatty acids into mitochondria for beta-oxidation.

In failing heart muscle, energy metabolism is impaired and carnitine pools may be depleted. Supplementation could therefore improve myocardial energy supply, reduce the build-up of toxic acyl-CoA species, and improve cardiac function. This is especially relevant in haemodialysis and cardiorenal patients, who are prone to carnitine deficiency. The link between a metabolic carnitine role and heart failure is biologically plausible, but the evidence is not yet definitive.

**Other predictions in the top 10:**
- **Diabetic nephropathy (score 0.9991, L3):** One 2026 clinical study of a levocarnitine-alprostadil combination, so levocarnitine's own contribution cannot be separated out.
- **Rheumatoid arthritis (score 0.9987):** The only trial listed (NCT03953703, Phase 2, n=15) studied dry eye in Sjögren's syndrome rather than rheumatoid arthritis, so it does not directly support this prediction. The "L2" grading appears to be overstated.
- **Seven other predictions (including two rare vascular syndromes, sclerosing cholangitis, gout and hypoalphalipoproteinemia):** Model prediction only, with no trials or literature and no plausible mechanism. These are on Hold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01580553](https://clinicaltrials.gov/study/NCT01580553) | Phase 2/3 | Completed | 268 | Multicentre, randomised, double-blind, placebo-controlled study of L-carnitine injection in Chinese patients with heart failure (7-day treatment, 1-month follow-up). No results are reported in the data compiled. |
| [NCT07201714](https://clinicaltrials.gov/study/NCT07201714) | Early Phase 1 | Recruiting | 20 | Oral L-carnitine in cardiorenal heart failure, assessing symptoms, heart function and quality of life. No results yet. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29468383](https://pubmed.ncbi.nlm.nih.gov/29468383/) | 2018 | Randomised trial | Paediatric Drugs | Levocarnitine added to conventional therapy in 29 children with dilated cardiomyopathy. |
| [30646314](https://pubmed.ncbi.nlm.nih.gov/30646314/) | 2018 | RCT (indirect) | JAMA Network Open | RACE trial of levocarnitine in septic shock. Not heart failure, so only indirect relevance. |
| [40172612](https://pubmed.ncbi.nlm.nih.gov/40172612/) | 2025 | Systematic review and meta-analysis | Int Urol Nephrol | L-carnitine and cardiac function in haemodialysis patients. |
| [30195728](https://pubmed.ncbi.nlm.nih.gov/30195728/) | 2020 | Clinical study | Hellenic J Cardiol | Effects of levocarnitine on cardiac function, urinary albumin, hs-CRP, BNP and troponin in coronary heart disease with heart failure. |
| [30041211](https://pubmed.ncbi.nlm.nih.gov/30041211/) | 2018 | Clinical study | Contrib Nephrol | Levocarnitine in haemodialysis patients: reported effects include improved cardiac function and renal anaemia. |
| [24125620](https://pubmed.ncbi.nlm.nih.gov/24125620/) | 2013 | Clinical study | Zhonghua Liu Xing Bing Xue Za Zhi | Levocarnitine in elderly patients with chronic heart failure, examining cardiac function and endocrine effects. |
| [15591005](https://pubmed.ncbi.nlm.nih.gov/15591005/) | 2004 | Review | Ann N Y Acad Sci | Levocarnitine and propionyl-L-carnitine in cardiovascular disease, with experimental data on reduced ischaemia-reperfusion injury. |
| [37979716](https://pubmed.ncbi.nlm.nih.gov/37979716/) | 2023 | Case series/review (indirect) | Eur J Med Genet | Cardiovascular involvement in later-onset malonyl-CoA decarboxylase deficiency. |
| [35712814](https://pubmed.ncbi.nlm.nih.gov/35712814/) | 2022 | Case report (indirect) | Mol Genet Genomic Med | Early cardiomyopathy in cblB-type methylmalonic acidaemia. |
| [40713745](https://pubmed.ncbi.nlm.nih.gov/40713745/) | 2025 | Preclinical (indirect) | Stem Cell Res Ther | NEXN deficiency and dilated cardiomyopathy in stem-cell-derived cardiomyocytes. |

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0908010C0AAAGAG | Levocarnitine 1.5g/5ml oral solution paediatric | Levocarnitine |
| 0908010C0AAAJAJ | Levocarnitine 1.5g/5ml oral solution paediatric sugar free | Levocarnitine |
| 0908010C0AAABAB | Levocarnitine 1g chewable tablets | Levocarnitine |
| 0908010C0AAALAL | Levocarnitine 1g tablets | Levocarnitine |
| 0908010C0AAAAAA | Levocarnitine 1g/10ml soln unit dose vials sugar free | Levocarnitine |
| 0908010C0AAAHAH | Levocarnitine 1g/5ml solution for injection ampoules | Levocarnitine |
| 0908010C0AAAIAI | Levocarnitine 330mg tablets | Levocarnitine |
| 0908010Z0BDAAAC | Bio-Carnitine 250mg capsules | Levocarnitine |
| 0908010C0BBABAB | Carnitor 1g chewable tablets | Levocarnitine |
| 0908010C0BBADAH | Carnitor 1g/5ml solution for injection ampoules | Levocarnitine |
| 0908010C0BBAEAI | Carnitor 330mg tablets | Levocarnitine |
| 0908010C0BBACAG | Carnitor Paediatric 30% oral solution | Levocarnitine |
| 0908010C0BBAAAA | Carnitor oral single dose 1g solution | Levocarnitine |
| 0908010Z0BCAAAB | Lamberts L-Carnitine 500mg capsules | Levocarnitine |
| 0908010Z0AAACAC | Levocarnitine/L-Carnitine 250mg capsules | Levocarnitine |
| 0908010Z0AAABAB | Levocarnitine/L-Carnitine 500mg capsules | Levocarnitine |
| 0908010C0BCAAAL | ValuBurn L-Carnitine 1000mg tablets | Levocarnitine |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

Please check the current SmPC and BNF for licensed indications.

<!-- review:begin uk-lic-20261106-levocarnitine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "One valid single-ingredient authorisation is recorded. Please check the current SmPC and BNF for licensed indications." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 17 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-levocarnitine-1 -->

---

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):** The TxGNN knowledge graph links levocarnitine to the following conditions: epilepsy, kidney disease, pyoureter, liver disease, gallbladder disease, hypotensive disorder, blood coagulation disease, cholestasis, benign recurrent intrahepatic cholestasis and familial intrahepatic cholestasis. These are model-derived associations and need verification against the SmPC. Kidney disease is particularly relevant because the target population (cardiorenal and haemodialysis patients) overlaps with it.

**Drug Interactions:** 68 interactions are recorded. The main ones with a stated severity are:
- **Warfarin** (Moderate)
- **Dicoumarol** (Moderate)

Anticoagulant response should be monitored (for example INR) if levocarnitine is combined with coumarins. Many other interactions are listed without a severity grade, including topiramate, valproic acid, digoxin, amlodipine, metoprolol, diltiazem, ramipril, omeprazole and pantoprazole. Several are commonly used in heart failure, so they warrant review.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Heart failure has a plausible metabolic rationale, one completed Phase 2/3 randomised trial (n=268), a small ongoing oral trial and several supportive clinical studies. However, no trial results are available in the data, the evidence is mostly from non-UK settings, and the rigorous L1 standard (two completed Phase 3 RCTs) is not met. The other nine predictions should stay on Hold or be treated as research questions.

**To proceed, the following is needed:**
- Published results of NCT01580553 and the outcome of NCT07201714
- A confirmatory Phase 3 RCT in a UK-relevant heart failure population, ideally including cardiorenal or haemodialysis patients with carnitine deficiency
- The licensed indication, dosage form and SmPC safety information (warnings and contraindications) for the UK product, which are not available in the data compiled
- Mechanism of action data
- Review of the knowledge-graph contraindication signals (renal and hepatic disease, hypotension, coagulation disorders), and of the warfarin and heart-failure drug interactions
- Evaluation of a possible oral versus injectable route, since the completed trial used an injection and the UK product is an oral capsule

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "One valid single-ingredient authorisation is recorded" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

