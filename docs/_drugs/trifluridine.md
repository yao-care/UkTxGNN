---
layout: default
title: Trifluridine
parent: Model Prediction Only (L5)
nav_order: 599
evidence_level: L5
indication_count: 10
---

# Trifluridine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Trifluridine: From Metastatic Colorectal Cancer to Cecum Villous Adenoma

## One-Sentence Summary

Trifluridine is a thymidine analogue best known as a component of the trifluridine/tipiracil combination (TAS-102), an approved cytotoxic treatment for metastatic colorectal cancer. The TxGNN model predicts a possible new application in **Cecum Villous Adenoma**, but this prediction is currently supported by **no clinical trials** and **no published literature**, and the underlying evidence pack flags the mechanistic rationale itself as questionable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the source dataset for this drug record; known pharmacological background indicates trifluridine (as the trifluridine/tipiracil combination) is used in metastatic colorectal cancer |
| Predicted New Indication | Cecum Villous Adenoma |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for trifluridine in this evidence pack. Based on known pharmacological background, trifluridine is a thymidine analogue that, in combination with tipiracil (TAS-102), is approved for metastatic colorectal cancer. Its antitumour effect relies on incorporation into DNA and inhibition of thymidylate synthase — a cytotoxic, antiproliferative mechanism intended for malignant, rapidly dividing tissue.

Cecum villous adenoma, however, is a **benign** colonic lesion. Its standard clinical management is endoscopic or surgical resection, not systemic cytotoxic therapy. The evidence pack's own mechanistic assessment for this candidate concludes that the high TxGNN score most likely reflects the model's learned association between trifluridine and "colon/intestinal" anatomical nodes in the knowledge graph — arising from its approved colorectal cancer indication — rather than any genuine pharmacological rationale for treating a benign adenoma. Exposing a benign lesion to a cytotoxic antimetabolite would introduce unnecessary toxicity without an established therapeutic benefit.

Across all ten of the model's top-ranked predictions for this drug (largely benign or non-malignant colonic conditions — lipoma, lymphangioma, leiomyoma, cavernous haemangioma, and even a probable adverse-effect signal for photosensitivity), the same pattern recurs: the high scores appear to be driven by anatomical proximity rather than mechanistic plausibility, and essentially none are backed by direct clinical or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## UK Market Information

Trifluridine has no marketing authorisation currently recorded in this dataset (total licences: 0), and the drug is listed as not marketed. No product/licence-level detail is available to summarise.

---

## Cytotoxicity

Trifluridine is a cytotoxic antimetabolite agent (thymidine analogue), used clinically as part of the trifluridine/tipiracil (TAS-102) combination for colorectal cancer, and is therefore assessed here as an antineoplastic drug.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (thymidine-based antimetabolite) |
| Myelosuppression Risk | High — associated literature on trifluridine/tipiracil reports leukopenia and neutropenia as recognised adverse effects (PMID 30677817) |
| Emetogenicity Classification | Low to moderate — diarrhoea and vomiting reported in associated case literature |
| Monitoring Items | FBC with differential, renal and hepatic function |
| Handling Protection | As a cytotoxic agent, standard cytotoxic drug handling and disposal protocols apply |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: this evidence pack flags a **Blocking** data gap regarding UK/MHRA label warnings and contraindications for trifluridine, meaning a formal safety pre-assessment cannot currently be completed for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only), with no clinical trials or literature directly supporting the use of trifluridine in cecum villous adenoma. The predicted indication is a benign lesion for which cytotoxic chemotherapy has no established clinical rationale, and the mechanistic assessment itself flags the prediction as likely driven by anatomical proximity in the knowledge graph rather than genuine pharmacology.

**To proceed, the following is needed:**
- Resolve the Blocking data gap on UK/MHRA label warnings and contraindications before any safety pre-assessment can begin
- Obtain confirmed mechanism of action (MOA) data for trifluridine to properly assess mechanistic plausibility
- Independent pharmacological or preclinical evidence specifically linking trifluridine to villous adenoma biology (rather than general colorectal anatomy)
- Re-evaluation of whether a cytotoxic agent is clinically appropriate for a benign neoplasm, given that standard-of-care is endoscopic/surgical resection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

