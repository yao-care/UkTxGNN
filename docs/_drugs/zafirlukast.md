---
layout: default
title: Zafirlukast
parent: Model Prediction Only (L5)
nav_order: 658
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Zafirlukast: predicted new indication Bronchitis (evidence level L5). Approved use: Asthma (including intrinsic and allergic asthma). The UK authorisatio…"
monitor_inn: "Zafirlukast"
predicted_indications: ["bronchitis", "obstructive lung disease"]
---

# Zafirlukast
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

## Zafirlukast: From Asthma to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Zafirlukast is a cysteinyl leukotriene receptor antagonist, originally used to treat asthma.
The TxGNN model predicts it may be effective for **bronchitis** (score 99.93%), but **no clinical trials or publications** were found for this indication, so the prediction rests on the model alone.
A second prediction, obstructive lung disease, is supported by **18 publications** (mostly reviews) but no clinical trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (including intrinsic and allergic asthma). The UK authorisation record contains no indication text. |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, zafirlukast is a selective, competitive antagonist of the CysLT1 receptor. It blocks the effects of the cysteinyl leukotrienes LTC4, LTD4 and LTE4, which drive bronchoconstriction, airway oedema, mucus secretion and eosinophil recruitment.

Asthma and bronchitis are both inflammatory airway conditions in which mucus hypersecretion and airway narrowing play a part. A mechanistic link is therefore plausible. However, this is a computational prediction only. The very high score may partly reflect the overlap between asthma and other airway diseases rather than genuine new-indication evidence. No primary data were available to verify the link.

For context, the second-ranked prediction, **obstructive lung disease** (score 99.17%, evidence level L4), is supported by reviews such as the Busse et al. 1999 review of leukotriene pathway inhibitors in asthma and COPD. This evidence is indirect, and the prediction is largely explained by the existing asthma indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bronchitis.

---

## Literature Evidence

Currently no related literature available for bronchitis.

For reference, the literature retrieved for the second prediction (obstructive lung disease) includes the following. All are reviews or pharmacology overviews, and none are primary trials.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10421833](https://pubmed.ncbi.nlm.nih.gov/10421833/) | 1999 | Review | Clin Exp Allergy | Leukotriene pathway inhibitors (zafirlukast, montelukast, zileuton) in asthma and COPD |
| [10023966](https://pubmed.ncbi.nlm.nih.gov/10023966/) | 1999 | Review | Lancet | Leukotriene-receptor antagonists act as both anti-inflammatory and bronchodilator drugs, with activity across asthma severities |
| [9463793](https://pubmed.ncbi.nlm.nih.gov/9463793/) | 1998 | Review | Drugs | Pharmacology and therapeutic potential of zafirlukast in chronic asthma |
| [11270943](https://pubmed.ncbi.nlm.nih.gov/11270943/) | 2001 | Review | Drugs | Update on zafirlukast efficacy in asthma; 20 mg twice daily effective in placebo-controlled studies of up to 13 weeks |
| [31544544](https://pubmed.ncbi.nlm.nih.gov/31544544/) | 2019 | Review | Expert Rev Respir Med | Update on leukotriene treatments and leukotriene-related airway inflammation in asthma |
| [26385352](https://pubmed.ncbi.nlm.nih.gov/26385352/) | 2015 | Review | Curr Allergy Asthma Rep | Antileukotrienes in upper airway inflammatory diseases |
| [11888331](https://pubmed.ncbi.nlm.nih.gov/11888331/) | 2002 | Review | Clin Pharmacokinet | Pharmacokinetic profile of zafirlukast |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0303020Z0AAAAAA | Zafirlukast tablets 20 mg | Tablet (not specified in the data) | Not stated in the data compiled for this report |

The identifier above follows a BNF-style code format rather than a standard PL number, and the BNF section 3.3.2 (leukotriene receptor antagonists) is the relevant classification. Please confirm the authorisation details with the MHRA.

---

## Safety Considerations

- **Contraindications (from knowledge graph associations, not label text):** liver disease, cirrhosis of liver, gallbladder disease, insomnia, anxiety, anxiety disorder, neurotic disorder and dysthymic disorder. These should be checked against the SmPC.
- **Drug Interactions:** 100 interactions were identified. Those listed as moderate include aprepitant, acetylsalicylic acid, metronidazole, budesonide (including nasal), saxagliptin, eliglustat, naltrexone, nateglinide, nitisinone, repaglinide, rosuvastatin, simvastatin and tinidazole. Sibutramine is listed as minor. Pantoprazole, mesalazine, morphine, metformin and omeprazole have an unknown severity level.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction has a very high model score but no supporting trials or literature (evidence level L5). The UK record also lacks indication and safety label data, so the benefit-risk balance cannot be assessed.

**To proceed, the following is needed:**
- Clinical trial or observational evidence for zafirlukast in bronchitis, with the type of bronchitis (acute, chronic or eosinophilic) specified
- Confirmed mechanism of action data and a clearer link between asthma and bronchitis
- UK SmPC warnings, contraindications and approved indication text, particularly for hepatic safety
- A review of the interactions with statins, repaglinide, nateglinide and corticosteroids
- Further evaluation of obstructive lung disease (such as COPD) as a separate research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

