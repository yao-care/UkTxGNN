---
layout: default
title: Maraviroc
parent: 僅模型預測 (L5)
nav_order: 355
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: From HIV-1 Infection to Multiple Endocrine Neoplasia

## One-Sentence Summary

> Maraviroc is a CCR5 antagonist originally used to treat HIV-1 infection (CCR5-tropic strains) by blocking viral entry into host cells.
> The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia**, with a very high prediction score,
> but this candidate currently has **no supporting clinical trials and no supporting literature** — the underlying evidence pack itself flags this as a likely false-positive knowledge-graph artefact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (CCR5-tropic strains) — based on established pharmacology; not captured in this evidence pack's licensing data because Maraviroc has no UK marketing authorisation on record |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Maraviroc is flagged as a data gap in this evidence pack (DG002). Based on established pharmacological knowledge, Maraviroc is a small-molecule CCR5 antagonist: it binds CCR5, a chemokine co-receptor on host CD4+ T-cells, blocking the entry of CCR5-tropic HIV-1 into the cell. This mechanism is unrelated to cell proliferation, tumour suppressor genes, or endocrine signalling pathways.

Multiple Endocrine Neoplasia (MEN) is a hereditary endocrine tumour syndrome driven by germline mutations in *MEN1* or *RET*, causing tumours across the pituitary, parathyroid, pancreas and/or thyroid. There is no established biological link between CCR5 chemokine signalling and *MEN1*/*RET*-driven tumourigenesis.

The repurposing rationale supplied with this candidate explicitly states that the high TxGNN score likely reflects an indirect node connection within the knowledge graph rather than a true mechanistic relationship — a recognised pattern of false positives in graph-based prediction models. With zero clinical trials and zero literature records supporting this pairing, the evidence level is L5 (model prediction only), and the appropriate decision at this stage is to **hold**, not to pursue this candidate further without independent mechanistic justification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Maraviroc currently holds **no marketing authorisation in the UK** (0 licences on record in this evidence pack). No dosage form, product name, or approved indication data is available for this jurisdiction.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Note: TFDA/MHRA-equivalent warnings and contraindications data are recorded as a Blocking data gap (DG001) in this evidence pack and have not yet been reviewed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high raw TxGNN score, the mechanistic rationale supplied alongside this prediction indicates no known biological connection between CCR5 antagonism and MEN pathogenesis, and there is no supporting clinical trial or literature evidence (L5, decision stage S0). This profile is consistent with a knowledge-graph false positive rather than a genuine repurposing signal, so this candidate should not proceed past the current hold stage.

**To proceed, the following is needed:**
- Confirmed mechanism of action data for Maraviroc (currently a High-severity data gap, DG002)
- UK/MHRA regulatory and SmPC data, including warnings and contraindications (currently a Blocking data gap, DG001)
- A dedicated preclinical or mechanistic study directly testing CCR5 involvement in *MEN1*/*RET*-driven endocrine tumourigenesis, if this hypothesis is to be pursued at all
- Ongoing monitoring of the knowledge graph/model outputs, as this pattern suggests the underlying node connectivity for this drug–disease pair warrants review

**Note on other candidates in this evidence pack:**
Although ranked lower by TxGNN score, two other predictions in this dataset show comparatively stronger mechanistic coherence and have already progressed to decision stage S1 ("Research Question"): HER2-positive breast carcinoma (rank 10), where a cited preclinical study (PMID 32404410) shows autocrine CCL5 signalling through its receptor CCR5 drives trastuzumab resistance via ERK activation — a plausible target for Maraviroc; and cutaneous T-cell lymphoma (ranks 3 and 5), where CCR5/CCL5 signalling has a theoretical role in malignant T-cell skin homing. Both remain at the preclinical/mechanistic evidence level (L4) and require further validation, but they represent a more defensible starting point for further evaluation than the top-ranked MEN prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

