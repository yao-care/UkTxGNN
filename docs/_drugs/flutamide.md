---
layout: default
title: Flutamide
parent: Model Prediction Only (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Flutamide: predicted new indication Prostate cancer/brain cancer susceptibility (evidence level L5). Approved use: Prostate cancer"
monitor_inn: "Flutamide"
predicted_indications: ["fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "prostate leiomyoma", "benign prostate phyllodes tumor", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
---

# Flutamide
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

## Flutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility
{: .text-alpha }

## One-Sentence Summary

Flutamide is a non-steroidal antiandrogen, originally used to treat prostate cancer.
The TxGNN model predicts it may be relevant to **prostate cancer/brain cancer susceptibility**, but **no clinical trials and no publications** were found for this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Flutamide is known as a non-steroidal androgen receptor antagonist, and its efficacy in prostate cancer is established. Mechanistically, it could be applicable to androgen-dependent disease.

The high score most likely reflects the prostate cancer component of this susceptibility entity, which is the drug's existing indication. No data were found linking flutamide to the brain cancer component or to the susceptibility concept. The prediction therefore shows no added value beyond the current use.

Other predicted conditions show a similar pattern:
- **Male reproductive organ cancer**: this category is dominated by prostate cancer. It includes a Phase 2 trial of flutamide as chemoprevention in prostatic intraepithelial neoplasia (NCT00006214), but the evidence mainly supports the existing indication.
- **Benign reproductive system neoplasm**: a small, older study of flutamide in benign prostatic hyperplasia exists (PMID 1722793, 1991), but it is not RCT-level evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

---

## Literature Evidence

Currently no related literature available for this predicted indication.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0803042H0AAAAAA | Flutamide Tablets 250 mg | Tablet | Indication text not recorded in the compiled data |

The compiled data list one valid single-ingredient authorisation. The dosage form is inferred from the product name, and the identifier is not in the usual PL format. Please verify the authorisation details against the MHRA register, the SmPC and the BNF.

---

## Cytotoxicity

Flutamide is used in prostate cancer, but it is a hormonal antiandrogen, not a conventional cytotoxic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (non-steroidal antiandrogen), not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Liver function (hepatotoxicity is a recognised concern); please refer to the SmPC for the full monitoring schedule |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Hepatotoxicity**: the compiled data flag hepatotoxicity as a concern with flutamide. This is important when weighing any extension of use.
- **Disease-level contraindications from a knowledge graph** (these are not label text and must be checked against the SmPC): liver failure, liver disease, gallbladder disease, methaemoglobinaemia, sulfhaemoglobinaemia, hyperbilirubinaemia (including hereditary forms and Gilbert syndrome), G6PD deficiency, glycogen storage disease, cystinuria, galactosaemia, and pyruvate dehydrogenase E3 deficiency.
- **Drug Interactions**: 100 interactions are recorded. Those classed as **Major** include dolasetron and cisapride. Many are **Moderate**, including clarithromycin, levofloxacin, ondansetron, palonosetron, famotidine, naltrexone, obeticholic acid, loperamide, and several laxatives and bowel-preparation agents (bisacodyl, picosulfuric acid, lactulose, lactitol, polyethylene glycol, sodium sulfate, castor oil, glycerin). Metronidazole is classed as **Minor**.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (Evidence Level L5). It largely overlaps with flutamide's existing prostate cancer indication and has no trials or publications of its own. Hepatotoxicity and the large number of recorded drug interactions add caution.

**To proceed, the following is needed:**
- A clear definition of what "prostate cancer/brain cancer susceptibility" means as a treatment target, and evidence for the brain cancer component
- Detailed mechanism of action data
- Verification of the SmPC warnings and contraindications, including the authorisation details
- If a genuinely new use is sought, a review of the more promising signals, such as chemoprevention in prostatic intraepithelial neoplasia (NCT00006214) and benign prostatic disease, against the available alternatives
- A hepatic safety monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

