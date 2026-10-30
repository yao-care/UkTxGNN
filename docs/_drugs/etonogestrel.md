---
layout: default
title: Etonogestrel
parent: Model Prediction Only (L5)
nav_order: 266
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
description: "Etonogestrel: predicted new indication amenorrhea (disease) (evidence level L5). Approved use: Not stated in the data compiled for this report (implant product…"
monitor_inn: "Etonogestrel"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "blunt duct adenosis of breast", "apocrine adenosis of breast", "benign mammary dysplasia"]
---

# Etonogestrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Etonogestrel: From Contraception to Amenorrhea (disease)
{: .text-alpha }

## One-Sentence Summary

Etonogestrel is a progestin, marketed in the UK as a 68 mg subdermal implant. The TxGNN model predicts it may be effective for **amenorrhoea**, but there are **no registered clinical trials** and **no relevant publications** supporting this prediction. The only linked paper concerns a different drug in COVID-19, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (implant product, 68 mg) |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Etonogestrel is a progestin. Progestins generally suppress the hypothalamic-pituitary-ovarian axis and cause endometrial atrophy.

This prediction is probably not a genuine therapeutic signal. Amenorrhoea is a well-known effect of the etonogestrel implant, which alters bleeding patterns. The model has likely picked up an existing pharmacological action, not a treatment use. Using a drug that induces amenorrhoea to treat amenorrhoea is mechanistically contradictory.

Other predicted indications are benign breast conditions: fibrocystic breast disease (score 0.9961), blunt duct adenosis of the breast and apocrine adenosis of the breast (both 0.9929, identical scores that come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence), and benign mammary dysplasia (0.9921). The rationale is hypothetical progestogenic counter-regulation of oestrogen-driven breast tissue proliferation. None has supporting trials or publications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT protocol (unrelated) | Trials | Study protocol for BIO101 in preventing respiratory deterioration in COVID-19 pneumonia. Not relevant to etonogestrel or amenorrhoea. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0703022P0AAAAAA (BNF code) | Etonogestrel implant 68 mg | Implant | Not available |

The BNF classification code (section 7.3.2, progestogen-only contraceptives) is shown in place of a PL number.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (drug-disease links in the TxGNN knowledge graph, not label text): hypertension, epilepsy, anxiety and neurotic disorders, porphyria, kidney disease, liver disease, gallbladder disease, systemic lupus erythematosus, asthma, diabetes mellitus and diabetic ketoacidosis, hypertriglyceridaemia and hyperlipidaemia, female breast carcinoma, thrombophlebitis, migraine, coronary artery disease and obesity. These must be checked against the SmPC.
- **Drug Interactions** (100 recorded; mostly moderate severity). Examples include:
  - Antidiabetic agents: acarbose, metformin, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, glimepiride, chlorpropamide, semaglutide, dulaglutide, albiglutide and various insulins.
  - Others: aprepitant, clarithromycin and linaclotide.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). Amenorrhoea is an expected effect of etonogestrel, not a plausible treatment target. The same applies to the benign breast conditions, which have no supporting trials or literature.

**To proceed, the following is needed:**
- Approved indication and SmPC details for the UK implant product
- Mechanism of action data
- Published or registered clinical evidence for any predicted indication, particularly benign breast conditions
- Clarification of whether the amenorrhoea prediction reflects therapeutic use or an adverse effect
- Review of the knowledge-graph contraindications against the SmPC, and of the antidiabetic interactions, before any new use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

