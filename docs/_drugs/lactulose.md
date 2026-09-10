---
layout: default
title: Lactulose
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 8
---

# Lactulose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Lactulose: From an Unrecorded Original Indication to Acute Urate Nephropathy

## One-Sentence Summary

Lactulose's original licensed indication could not be determined from this evidence pack — the drug is currently **Not Marketed** in the UK and no marketing authorisation or mechanism-of-action data is on file. The TxGNN model's top-ranked prediction is **Acute Urate Nephropathy**, but this candidate is supported by **zero clinical trials** and **zero publications**, so the prediction should be treated as a model-only signal rather than a clinical lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no marketing authorisation or indication data on record for Lactulose in this pack |
| Predicted New Indication | Acute Urate Nephropathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Lactulose is not currently available in this evidence pack, and it has been flagged as a High-severity data gap. Based on what is known generally about the compound class, lactulose acts as an osmotic laxative and is metabolised by colonic bacteria, with downstream effects on ammonia absorption and colonic pH — but no original indication was captured in the regulatory data provided, so a direct comparison to the predicted indication cannot be made from this pack alone.

Critically, the model's own rationale for this candidate states there is **no known mechanistic link**: lactulose acts on colonic flora metabolism and ammonia absorption, which does not intersect with urate generation or excretion pathways (xanthine oxidase, renal tubular urate transporters). The high TxGNN score most likely reflects an indirect "kidney–drug" node association within the knowledge graph rather than genuine biological plausibility.

Given the complete absence of clinical trials or literature, and an explicit statement of mechanistic implausibility from the model's own rationale, this prediction should not be interpreted as a promising repurposing lead at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

No UK marketing authorisations are currently on record for Lactulose in this evidence pack. Market status is recorded as **Not Marketed**, with 0 total licences.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Acute Urate Nephropathy) has no supporting clinical trials or literature, and the model's own mechanistic rationale explicitly states there is no known biological link between lactulose's pharmacology and urate handling. A high TxGNN score alone, without corroborating evidence, is insufficient to justify progression.

**To proceed, the following is needed:**
- Lactulose mechanism-of-action data (DrugBank API query, currently a High-severity gap)
- UK/EU marketing authorisation and SmPC data, including warnings and contraindications (currently a Blocking-severity gap)
- Any preclinical or mechanistic studies specifically linking lactulose to urate metabolism, should this candidate be revisited
- Given the absence of supporting evidence for this specific candidate, consideration should be given to reviewing other candidates in the same evidence pack with materially stronger evidence (see appendix below)

---

## Appendix: Other Candidate Indications in This Evidence Pack

This evidence pack ("TW-DB00581-multi") contains eight TxGNN-predicted indications for Lactulose. Evidence quality varies substantially and does **not** track TxGNN score — the highest-scoring candidates have no supporting evidence, while a mid-ranked candidate has meaningful clinical and mechanistic support.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|
| 1 | Acute Urate Nephropathy | 99.89% | L5 | Hold |
| 2 | Nephrolithiasis | 99.78% | L5 | Hold |
| 3 | **Obstructive Jaundice** | 99.53% | **L2** | **Research Question** |
| 4 | Bile Duct Disease | 99.47% | L3 | Research Question |
| 5 | Biliary Tract Disease | 99.38% | L4 | Hold |
| 6 | Hyperphosphatemia | 99.37% | L5 | Hold |
| 7 | Exercise-Induced Malignant Hyperthermia | 99.14% | L5 | Hold |
| 8 | Bile Duct Neoplasm | 99.12% | L4 | Hold |

**Notable candidate: Obstructive Jaundice (Rank 3)**

Unlike the top-ranked prediction, this candidate is supported by a completed Phase 4 study (NCT01090193, n=20), a multicentre randomised study of preoperative lactulose in obstructive jaundice (PMID [2032107](https://pubmed.ncbi.nlm.nih.gov/2032107/), 1991, tier 1), and 21 supporting publications spanning human and animal studies. The proposed mechanism — reduction of gut-derived endotoxaemia and bacterial translocation via lactulose's acidification of the colonic environment — is biologically coherent and repeatedly described in the literature, in contrast to the implausible link underlying the top-ranked prediction.

**Recommendation:** If this evidence pack is being used to select a lead candidate for further evaluation, Obstructive Jaundice (Rank 3) warrants priority review over the top TxGNN-scored candidate, which lacks any corroborating evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

