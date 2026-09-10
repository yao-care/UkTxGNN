---
layout: default
title: Norfloxacin
parent: 僅模型預測 (L5)
nav_order: 422
evidence_level: L5
indication_count: 10
---

# Norfloxacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Norfloxacin: From Urinary Tract Infections to Hyperamylasemia

## One-Sentence Summary

Norfloxacin is a fluoroquinolone antibacterial, noted in the evidence pack as being used mainly for urinary tract infections. The TxGNN model's top-ranked prediction is **Hyperamylasemia**, but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review concludes there is no plausible pharmacological link between the two.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed via UK licensing data (product holds no UK marketing authorisation); described in the evidence pack's drug-class notes as mainly used for urinary tract infections |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for norfloxacin in this evidence pack (flagged as a **High-severity data gap**, DG002). What can be established from the pack is that norfloxacin is a fluoroquinolone antibacterial that inhibits bacterial DNA gyrase/topoisomerase IV, and that it is mainly used clinically for urinary tract infections.

For the top-ranked prediction — hyperamylasemia — the evidence pack's own assessment is explicit and should be taken at face value: there is **no known pharmacological relationship** between norfloxacin's antibacterial mechanism and pancreatic amylase metabolism, and no clinical trials or literature exist to support this link. This appears to be a high-scoring TxGNN output without independent validation, i.e. a candidate that should not be advanced on current evidence.

Of the ten indications the model surfaced for this drug (see below), only one — septicemic plague (rank 10) — has any biological plausibility, based on a fluoroquinolone class effect (ciprofloxacin, levofloxacin and moxifloxacin are FDA-approved for plague). Norfloxacin itself, however, lacks drug-specific human clinical evidence for this use, owing to its comparatively low tissue penetration and systemic bioavailability.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for hyperamylasemia.

---

## Other Model-Predicted Indications Considered

For transparency, all ten TxGNN-ranked candidates for norfloxacin from this evidence pack are summarised below, as none reached a "Go" recommendation.

| Rank | Predicted Indication | Score | Evidence Level | Decision | Assessment |
|------|----------------------|-------|-----------------|----------|------------|
| 1 | Hyperamylasemia | 99.70% | L5 | Hold | No mechanism, no evidence; likely model noise |
| 2 | Polyclonal hyperviscosity syndrome | 99.70% | L5 | Hold | No mechanism, no evidence |
| 3 | Congenital analbuminemia | 99.67% | L5 | Hold | Hereditary hepatic disorder, unrelated to MOA |
| 4 | Blood group incompatibility | 99.55% | L5 | Hold | Immunohaematological, unrelated to MOA |
| 5 | Punctate epithelial keratoconjunctivitis | 99.54% | L4 | Hold | Literature concerns microsporidial (parasitic), not bacterial, infection — likely name-matching artefact |
| 6 | Premalignant hematological system disease | 99.48% | L5 | Hold | Diagnosis too vague to assess; no evidence |
| 7 | Diffuse scleroderma | 99.44% | L5 | Hold | Autoimmune fibrotic disease, no mechanistic overlap |
| 8 | Monoclonal gammopathy | 99.42% | L5 | Hold | Only related literature concerns antibiotic-resistance side effects, not treatment efficacy |
| 9 | Haematological disease with acquired peripheral neuropathy | 99.38% | L5 | Hold | Fluoroquinolone peripheral neuropathy is a **safety signal** (FDA boxed warning), not a therapeutic indication |
| 10 | Septicemic plague | 99.37% | L4 | Research Question | Class-effect plausibility (DNA gyrase inhibition vs. *Yersinia pestis*); no norfloxacin-specific human evidence |

**Recommendation:** none of these candidates meet the threshold to proceed as a repurposing programme. Rank 10 (septicemic plague) may warrant a research question / literature deep-dive on comparative fluoroquinolone pharmacokinetics, but this is a mechanistic hypothesis, not a treatment recommendation.

---

## UK Market Information

Norfloxacin is not currently marketed in the UK — the evidence pack records **0 marketing authorisations** and no licence entries. There is therefore no UK-approved indication text available to reference.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: this evidence pack flags TFDA/MHRA product warnings and contraindications as a **Blocking** data gap — DG001 — meaning a formal safety pre-assessment (S1) cannot proceed until official product labelling is retrieved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (hyperamylasemia) has no supporting clinical trials, no supporting literature, and no plausible mechanistic link per the evidence pack's own review — it is best treated as an unvalidated model output. None of the other nine candidates fare better, and the drug itself is unlicensed in the UK with no available mechanism-of-action or safety data.

**To proceed, the following is needed:**
- Product labelling / warnings and contraindications (Blocking gap — source: official regulator PDF)
- Mechanism of action data (High-severity gap — source: DrugBank API)
- Independent literature or preclinical validation specifically linking norfloxacin to any of the ten predicted indications
- If pursuing the plague hypothesis (rank 10), comparative pharmacokinetic data versus approved fluoroquinolones (ciprofloxacin, levofloxacin)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

