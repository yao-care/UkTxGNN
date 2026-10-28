---
layout: default
title: Misoprostol
parent: Model Prediction Only (L5)
nav_order: 420
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Misoprostol: predicted new indication amenorrhea (disease) (evidence level L4). Approved use: Not available in the data compiled for this report"
monitor_inn: "Misoprostol"
predicted_indications: ["amenorrhea (disease)", "atypical coarctation of aorta"]
---

# Misoprostol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Misoprostol: From an Unspecified Original Indication to amenorrhea (disease)
{: .text-alpha }

## One-Sentence Summary

Misoprostol is a prostaglandin E1 analogue marketed in the UK as a 200 microgram tablet, but the data compiled for this report do not include its approved indication text.
The TxGNN model predicts it may be effective for **amenorrhoea**, but there are **no registered clinical trials** and only **7 publications**, none of which show that misoprostol treats amenorrhoea itself.
This prediction rests essentially on model output and is not supported by direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 0.9964 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, misoprostol is a prostaglandin E1 analogue that induces uterine contraction and cervical ripening. It is used with mifepristone for early medical abortion and in the management of missed abortion.

The identified literature concerns pregnancy-related amenorrhoea, mainly early pregnancy termination, and not amenorrhoea as a disease. In those studies, "amenorrhoea" describes the duration of early pregnancy (for example, 35 days or less) and is not the condition being treated. No mechanism has been established by which misoprostol would restore menses in primary or secondary amenorrhoea.

The high TxGNN score is probably driven by network proximity to reproductive and endometrial conditions. It should be read as a computational association, not as evidence of benefit. Misoprostol could induce uterine evacuation in a pregnancy-related setting such as missed abortion or anembryonic pregnancy, but that is a different clinical problem.

A second prediction, atypical coarctation of the aorta (score 0.9930), has no supporting trials or literature. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; it may be linked to the use of PGE1 (alprostadil) to keep the ductus arteriosus open in neonates. Misoprostol is not an appropriate substitute and carries teratogenic and uterotonic risks.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reprod Sci | 744 women with ultra-early pregnancy (amenorrhoea ≤35 days) received low-dose mifepristone with hospital-administered or self-administered misoprostol for medical abortion; efficacy, safety and acceptability assessed |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT | Reprod Sci | Dose-ranging trial in 2,500 women with ultra-early pregnancy; oral mifepristone 50–150 mg followed by misoprostol 200 µg, with complete abortion without surgery as primary endpoint |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Clinical study | Hum Reprod | Low-dose mifepristone plus misoprostol before expected menstruation for preventing unintended pregnancy |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Clinical study | J Obstet Gynaecol Res | Safety and efficacy of low-dose mifepristone with self-administered misoprostol for early pregnancy termination |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Review | BMJ | Medical management of missed abortion and anembryonic pregnancy |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Endometrial ablation for abnormal uterine bleeding; not directly related to misoprostol for amenorrhoea |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case report | Cureus | Acute fatty liver of pregnancy presenting with amenorrhoea; not a misoprostol efficacy study |

None of these publications evaluates misoprostol as a treatment for amenorrhoea.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0103040M0AAAAAA | Misoprostol Tab 200mcg | Tablet (not stated in the data) | Not available in the data compiled for this report |

The identifier shown is as recorded in the compiled data and is not in the usual MHRA PL number format. Manufacturer and approved indication text were not available. Please verify against the current SmPC and BNF.

---

## Safety Considerations

**Contraindications suggested by the knowledge graph** (derived from TxGNN/PrimeKG drug-disease edges, not from label text, so they should be checked against the SmPC):
- Cardiovascular: hypertension, congestive heart failure, myocardial infarction, coronary thrombosis, stroke and cerebrovascular disorders, cerebral infarction, other heart and cardiovascular disease
- Hepatic: liver failure, liver disease, drug-induced liver injury, gallbladder disease
- Gastrointestinal: inflammatory bowel disease, active peptic ulcer disease
- Respiratory: asthma (including intrinsic and allergic forms)
- Haematological: blood coagulation disease, haemoglobinopathy, anaemia (including macrocytic anaemia)
- Other: substance abuse/dependence, non-infectious meningitis

**Drug Interactions** (100 interactions recorded; main ones shown):
- **Major:** dinoprostone (topical)
- **Moderate:** magnesium-containing antacids (magnesium oxide, carbonate, hydroxide; magaldrate) and quinapril
- **Minor:** sodium citrate, aluminium hydroxide, calcium carbonate, sodium bicarbonate and naproxen
- **Severity not classified:** goserelin, ciclosporin, cyanocobalamin, calcitriol, folic acid, pravastatin, valsartan, ramipril and lorazepam

Label warnings and contraindications were not available. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no registered trials, the literature addresses pregnancy termination rather than treatment of amenorrhoea, and no plausible mechanism has been established. The high TxGNN score reflects network proximity, not demonstrated benefit. The evidence level is L4 at best (L5 for the aortic coarctation prediction).

**To proceed, the following is needed:**
- Confirmation of the approved UK indication, dosage form and manufacturer from the MHRA record and SmPC
- Label warnings and contraindications from the SmPC and BNF
- Detailed mechanism of action data, and a rationale for how misoprostol could treat primary or secondary amenorrhoea
- Clinical evidence in non-pregnancy amenorrhoea, as the current literature concerns pregnancy termination
- A clear assessment of teratogenic and uterotonic risks in women of reproductive age
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

