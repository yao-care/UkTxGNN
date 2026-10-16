---
layout: default
title: Trifluridine
parent: Model Prediction Only (L5)
nav_order: 641
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Trifluridine: predicted new indication Cecum villous adenoma (evidence level L5). Approved use: Herpes simplex virus keratitis"
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

# Trifluridine: From Herpes Simplex Virus Keratitis and Colorectal Cancer to Cecum Villous Adenoma

## One-Sentence Summary

Trifluridine is a thymidine analogue, originally used for herpes simplex virus keratitis (as an eye drop) and, with tipiracil, for colorectal cancer.
The TxGNN model predicts it may be effective for **cecum villous adenoma**, but there are currently **no clinical trials** and **no publications** supporting this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes simplex virus keratitis; colorectal cancer (colonic neoplasm) |
| Predicted New Indication | Cecum villous adenoma |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known pharmacology, trifluridine is a thymidine analogue that is incorporated into DNA and inhibits thymidylate synthase. Combined with tipiracil, it is approved for metastatic colorectal cancer.

A villous adenoma of the cecum is a benign precursor lesion of the colon, so a shared colonic epithelial origin makes a link plausible. The high score probably reflects closeness to colorectal neoplasms in the knowledge graph.

However, the clinical rationale is weak. Benign adenomas are managed by endoscopic resection, and systemic cytotoxic therapy is not clinically justified for them. This is a model prediction only.

Other top-ranked predictions show the same pattern: colonic lipoma, lymphangioma, leiomyoma and cavernous hemangioma (all benign, with no mechanistic rationale), cecal neuroendocrine tumour G1 (low proliferative index, so unlikely to respond to an S-phase-dependent antimetabolite), and photosensitivity disease (no plausible link, probably a graph artefact). "Rectosigmoid junction neoplasm" is largely a re-labelling of the existing colorectal cancer indication rather than a new repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cecum villous adenoma.

---

## Literature Evidence

Currently no related literature available for cecum villous adenoma.

For information only, publications were retrieved for two lower-ranked predictions, but none supports a new indication:
- "Cecal disease" (rank 7): three case reports in metastatic colorectal cancer, covering readministration of cancer drugs ([32655959](https://pubmed.ncbi.nlm.nih.gov/32655959/), 2020), trifluridine/tipiracil-associated vasculitis ([30677817](https://pubmed.ncbi.nlm.nih.gov/30677817/), 2018) and pain management ([30692384](https://pubmed.ncbi.nlm.nih.gov/30692384/), 2018). They relate to the already-approved colorectal indication or its toxicity.
- "Benign neoplasm of cecum" (rank 8): one cohort study of irinotecan-loaded bead chemoembolisation for colorectal liver metastases ([37500124](https://pubmed.ncbi.nlm.nih.gov/37500124/), 2023). This is a malignant, off-target setting and appears to be a retrieval mismatch.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1103030T0AAADAD | Trifluridine eye drops 1% (preservative-free) | Not specified | Not specified in the data compiled |

Note: the identifier above is not in standard MHRA "PL" format, and the indication text and dosage form were not available. Please verify the authorisation against the MHRA database and the BNF.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (thymidine-based antimetabolite, when used with tipiracil for colorectal cancer) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions (FBC is generally monitored with oral trifluridine/tipiracil) |
| Handling Protection | Please refer to the SmPC warnings and precautions |

The authorisation in the compiled data is for an ophthalmic preparation, so these points apply mainly to the oral trifluridine/tipiracil product used in colorectal cancer.

---

## Safety Considerations

- **Drug Interactions**: 81 interactions were recorded in total. The main ones flagged as Major are:
  - Deferiprone
  - Samarium (153Sm) lexidronam
  - Adalimumab
  - Baricitinib
  - Certolizumab pegol
  - BCG live vaccine (Tice substrain)

  Moderate interactions include strontium chloride Sr-89, roflumilast, chloramphenicol (systemic and ophthalmic), azathioprine, alemtuzumab, anakinra, canakinumab, and several live vaccines or antigens. Many of these reflect additive immunosuppression or myelosuppression.

Please refer to the SmPC and BNF for warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by model score only (L5), with no trials or literature. Benign adenomas are treated by endoscopic resection, so systemic cytotoxic therapy is not clinically justified.

**To proceed, the following is needed:**
- A clear clinical rationale for systemic therapy in a benign lesion, or a decision to redirect effort to a malignant colonic indication already covered by existing evidence
- Mechanism of action data (for example from DrugBank)
- Warnings and contraindications from the SmPC and BNF
- Confirmation of the UK authorisation details (PL number, dosage form, approved indication)
- Any preclinical or observational evidence specific to villous adenoma
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

