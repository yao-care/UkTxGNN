---
layout: default
title: Calcipotriol
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
---

# Calcipotriol
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

# Calcipotriol: From Psoriasis to Seborrheic Keratosis

## One-Sentence Summary

Calcipotriol is a synthetic vitamin D3 analogue primarily indicated for the topical treatment of plaque psoriasis, where it acts through the vitamin D receptor (VDR) to regulate keratinocyte differentiation and suppress epidermal hyperproliferation.
The TxGNN model predicts it may be effective for **Seborrheic Keratosis**, another condition characterised by benign keratinocyte overgrowth, with a prediction score of 99.96%.
Currently, **no clinical trials** and **no publications** directly support this specific repurposing direction; the evidence rests entirely on computational model prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Plaque psoriasis (topical treatment; based on established clinical use — no formal UK licence data returned in this evidence pack) |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| UK Market Status | Not marketed (per regulatory data in this evidence pack — see note below) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

> **Data Note:** The regulatory query returned zero UK licences for Calcipotriol. This likely reflects a data collection gap rather than a genuine absence of authorisation, as topical Calcipotriol products (e.g. Dovonex® cream and ointment, Leo Laboratories) are established in UK clinical practice for psoriasis. Clinicians should verify current MHRA licence status directly via the MHRA Product Licence register and the BNF (Chapter 13: Skin).

---

## Why Is This Prediction Reasonable?

Calcipotriol is a synthetic analogue of calcitriol (1,25-dihydroxyvitamin D₃), specifically engineered to retain the anti-proliferative and pro-differentiating effects of endogenous vitamin D on epithelial cells whilst substantially reducing the risk of systemic hypercalcaemia — an important side-effect associated with natural vitamin D compounds. Its principal mechanism of action is agonism at the vitamin D receptor (VDR), a nuclear receptor that, upon activation, regulates transcription of genes controlling cell cycle arrest (via up-regulation of p21/p27), terminal differentiation, and apoptosis in keratinocytes. In plaque psoriasis, this suppresses the pathological hyperproliferation and abnormal maturation of epidermal cells that underlie visible plaques.

> **MOA Data Status:** Formal mechanism of action data was not retrieved from DrugBank in this evidence pack (data gap DG002). The description above is based on established pharmacological knowledge of Calcipotriol in the published literature and its BNF classification as a vitamin D analogue for skin disorders.

Seborrheic keratosis is a benign condition characterised by clonal expansion of keratinocytes, with commonly identified driver mutations in *FGFR3* and *PIK3CA* converging on proliferative signalling. The theoretical mechanistic overlap with psoriasis — both involving hyperproliferative keratinocytes — provides some rationale for VDR-mediated intervention: Calcipotriol could in principle attenuate the proliferative drive through its established cell cycle and differentiation effects. The TxGNN knowledge graph likely reflects this connection through strong node linkage between Calcipotriol and keratinocyte-related disease entities.

However, it is important to note that seborrheic keratosis lacks the inflammatory component that is central to psoriasis pathophysiology. The high prediction score (99.96%) most plausibly reflects the broad connectivity of Calcipotriol with skin keratinocyte nodes within the knowledge graph, rather than any disease-specific mechanistic or clinical evidence for seborrheic keratosis specifically. There are no preclinical studies, clinical trials, or published case reports currently available to support this hypothesis. The prediction should therefore be interpreted as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No MHRA marketing authorisations were returned for Calcipotriol in this evidence pack. This is likely a data collection gap. Clinicians should consult the following resources directly:

- **MHRA Product Licence Register**: [https://products.mhra.gov.uk/](https://products.mhra.gov.uk/)
- **BNF Chapter 13.5.2** – Vitamin D analogues for psoriasis
- **NICE guidance on psoriasis**: [TA177](https://www.nice.org.uk/guidance/ta177) (Calcipotriol-containing products)

Known UK-licensed formulations (for reference only, not sourced from this evidence pack):

| Product | Dosage Form | Established Indication |
|---------|-------------|----------------------|
| Dovonex® (Leo Laboratories) | Cream / Ointment | Stable plaque psoriasis |
| Dovobet® (Leo Laboratories) | Gel / Ointment | Plaque psoriasis (combination with betamethasone dipropionate) |
| Enstilar® (Leo Laboratories) | Cutaneous foam | Plaque psoriasis (combination with betamethasone dipropionate) |

---

## Safety Considerations

Formal safety data (warnings, contraindications, drug interactions) were not retrieved in this evidence pack. All fields returned as data gaps.

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** at [https://yellowcard.mhra.gov.uk/](https://yellowcard.mhra.gov.uk/).

Key safety considerations known from the established literature (for contextual reference):

- **Hypercalcaemia/hypercalciuria**: Risk increases with excessive application or use over large body surface areas; routine monitoring of serum and urinary calcium is advised in prolonged use
- **Topical irritation**: Local skin irritation, burning, and erythema are common adverse effects
- **Use in sensitive areas**: Caution required near the face, flexures, and genitalia due to enhanced systemic absorption

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (99.96%) driven by Calcipotriol's established VDR-mediated anti-proliferative effects on keratinocytes, no clinical trials, preclinical studies, or published literature currently exist to support its use in seborrheic keratosis. At Evidence Level L5, this candidate does not yet meet the threshold for further resource investment in this specific indication.

**To proceed, the following would be needed:**

- **MOA confirmation**: Retrieve formal DrugBank mechanism of action data to document the VDR pathway (remediation: DrugBank API query for DB02300)
- **Safety data retrieval**: Obtain SmPC warnings and contraindications from the MHRA to complete the safety assessment before any clinical evaluation is considered
- **Preclinical proof of concept**: A targeted in vitro or murine model study examining VDR expression and Calcipotriol activity in seborrheic keratosis keratinocytes would be a low-cost first step to validate or refute this hypothesis
- **UK regulatory verification**: Confirm current MHRA licence status and approved indications via the MHRA register before any off-label use discussions

---

> **Notable Alternative Prediction:** Whilst seborrheic keratosis is the top-ranked prediction, clinicians and researchers may wish to note that **Vulvar Neoplasm** (rank 5, TxGNN score 99.51%, Evidence Level **L4**) has two published case reports/series supporting the use of topical Calcipotriol in combination with fluorouracil for extramammary Paget disease (EMPD) — a rare intraepithelial adenocarcinoma of the vulva. See PMID [30785593](https://pubmed.ncbi.nlm.nih.gov/30785593/) and PMID [27789051](https://pubmed.ncbi.nlm.nih.gov/27789051/) for details. This direction, whilst supported by only case-level evidence, has a more specific and better-characterised mechanistic rationale and may represent a higher-priority candidate for further investigation.

---

*This report is generated for research purposes only. It does not constitute medical advice. All repurposing candidates require prospective clinical validation before any change in clinical practice. This report was generated by the TxGNN UK Drug Repurposing System (v4, data cutoff: 2026-04-05).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

