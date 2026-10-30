---
layout: default
title: Posaconazole
parent: Model Prediction Only (L5)
nav_order: 507
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Posaconazole: predicted new indication Pneumocystosis (evidence level L4). Approved use: Fungal infections (e.g. aspergillosis, candidiasis, oral candidiasis…"
monitor_inn: "Posaconazole"
predicted_indications: ["pneumocystosis"]
---

# Posaconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Posaconazole: From Invasive Fungal Infections to Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Posaconazole is an azole antifungal originally used to treat and prevent a range of fungal infections, including aspergillosis and candidiasis.
The TxGNN model predicts it may be effective for **pneumocystosis**, but only **1 clinical trial** (which tests a different drug) and **5 publications** (none of which test posaconazole for this condition) are linked to this prediction.
The mechanistic reasoning argues against the prediction, so it should be treated as a likely model artefact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (e.g. aspergillosis, candidiasis, oral candidiasis, histoplasmosis, fusariosis, mycetoma). The UK authorisation record compiled for this report has no indication text. |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Posaconazole is a triazole antifungal. This class inhibits fungal CYP51 (lanosterol 14-alpha-demethylase), which blocks ergosterol synthesis in the fungal cell membrane.

Its efficacy in invasive fungal infections is established, which is probably why the model links it to pneumocystosis. However, *Pneumocystis jirovecii* has little or no ergosterol and uses cholesterol-type sterols in its membrane, so an azole is not expected to work. The high score most likely reflects a general antifungal class association rather than a true mechanistic fit. Standard therapy is trimethoprim-sulfamethoxazole.

Other predictions in the list are weaker still. Vulvovaginal candidiasis is mechanistically plausible but is an extension within the already approved antifungal indication family.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Completed | 602 | ReSPECT study: intravenous rezafungin versus the standard antimicrobial regimen to prevent invasive fungal disease after allogeneic blood and marrow transplantation. It tests rezafungin, not posaconazole, so it is not direct evidence for this prediction. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Med Wkly | Overview of invasive candidiasis, aspergillosis, cryptococcosis and *Pneumocystis* pneumonia. Notes that mould-active posaconazole prophylaxis reduced invasive fungal disease in high-risk haemato-oncology patients. |
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Guideline | Lancet Infect Dis | British Society for Medical Mycology 2025 update on diagnosing serious fungal diseases. Diagnostic guidance, not treatment evidence for posaconazole. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Zhonghua Jie He He Hu Xi Za Zhi | Chinese guidelines for diagnosing and managing invasive pulmonary fungal disease. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clin Pharmacokinet | Penetration of antifungal and other anti-infective agents into pulmonary epithelial lining fluid. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transpl Infect Dis | Infectious complications of acute graft-versus-host disease after liver transplantation. |

None of these publications reports posaconazole as a treatment for pneumocystosis.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0502010A0AAAAAA (BNF classification code, not a PL number) | Posaconazole oral suspension 200 mg/5 ml | Oral suspension | Not available in the data compiled for this report |

The code listed appears to be a BNF section/product code (BNF section 5.2.1, triazole antifungals) rather than an MHRA PL number. No NICE-appraised indication data were available.

---

## Safety Considerations

- **Drug Interactions:** 100 interacting drugs were identified. Those listed with a **Major** level include:
  - Loperamide
  - Triamcinolone
  - Budesonide

  **Moderate** interactions include:
  - Acid suppressants (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole)
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone)
  - Aprepitant
  - Clarithromycin
  - Saxagliptin
  - Several bowel preparations (bisacodyl, picosulfuric acid, polyethylene glycol)
- **Pregnancy:** Animal studies raise teratogenicity concerns, so caution is warranted in any developmental or congenital indication.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pneumocystosis prediction is not supported by trial or literature evidence for posaconazole, and the mechanism argues against it because *Pneumocystis* lacks the ergosterol target. The only linked trial tests a different drug. The model score is most likely a class-association artefact.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic case for activity against *Pneumocystis*
- Preclinical or in vitro evidence of posaconazole activity in pneumocystosis, compared with trimethoprim-sulfamethoxazole
- Full MHRA authorisation details (PL number, approved indications, SmPC warnings and contraindications)
- A fuller review of drug-interaction management, particularly with corticosteroids and QT-prolonging drugs
- If a lower-risk repurposing direction is wanted, vulvovaginal candidiasis in fluconazole-resistant or non-albicans infection could be studied as a research question, although current evidence is limited to in vitro and animal data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

