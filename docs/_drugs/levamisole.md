---
layout: default
title: Levamisole
parent: High Evidence (L1-L2)
nav_order: 342
evidence_level: L2
indication_count: 10
---

# Levamisole
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Levamisole: From Immunomodulatory Anthelmintic to Adjuvant Immunotherapy in Head and Neck Cancer (Hypopharynx)

## One-Sentence Summary

> Levamisole is a long-established anthelmintic and immunomodulator, historically used alongside 5-fluorouracil as adjuvant therapy in Dukes' C colon cancer before being withdrawn from many markets over agranulocytosis and vasculitis risk.
> TxGNN's highest-scoring prediction ("drug-induced osteoporosis") has **no supporting clinical trials or literature** and is flagged in the evidence itself as likely model noise; the only candidate with genuine clinical evidence is **adjuvant immunotherapy in head and neck cancer of the hypopharynx region**, supported by **2 historical clinical studies (1 RCT, 1 randomised pilot)** and no registered clinical trials.
> Evidence is dated, small-scale, and targets malignant rather than "benign" disease — treat this as a research hypothesis, not an actionable indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No licensed indication on record. Historically used as an anthelmintic and (per literature within this evidence pack) as an immunomodulatory adjuvant to 5-FU in Dukes' C colon cancer, later withdrawn in many markets due to agranulocytosis/vasculitis risk |
| Predicted New Indication | Benign neoplasm of hypopharynx (evidence base actually concerns adjuvant immunotherapy in malignant head & neck squamous cell carcinoma — see ontology caveat below) |
| TxGNN Prediction Score | 99.996% (rank 140 of model output) |
| Evidence Level | L2 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

**Note on TxGNN ranking:** The model's single top-ranked prediction for this drug ("drug-induced osteoporosis", score 99.999%) and several other top-10 candidates (benign tongue neoplasm, cervical neuroblastoma, epiglottis neoplasm, schwannoma of jugular foramen, etc.) have **zero clinical trials and zero or clearly irrelevant literature**. The evidence pack's own rationale explicitly flags these as likely model noise — Levamisole's node scores >0.9999 against many unrelated diseases, indicating poor discriminative power at this score range. This report therefore focuses on the one candidate (hypopharynx neoplasm, rank 9) that is actually supported by real clinical studies.

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is currently unavailable (data gap). Based on information contained in the evidence pack's own literature rationale, Levamisole is an immunostimulant that enhances T-cell mediated immunity and promotes neutrophil/macrophage chemotaxis and function, in addition to its established anthelmintic activity. It was historically combined with 5-fluorouracil as postoperative adjuvant immunotherapy in Dukes' C colon cancer — a use later discontinued in many jurisdictions because of agranulocytosis and vasculitis risk.

This same immune-stimulating mechanism was explored, in the 1980s and again in 2001, as postoperative adjuvant therapy in head and neck squamous cell carcinoma, including laryngeal and hypopharyngeal sites — the biological rationale being enhanced immune surveillance against residual tumour cells after surgery or radiotherapy. This is mechanistically coherent with the drug's known immunomodulatory profile.

**Important caveat:** the TxGNN-predicted disease label is "**benign** neoplasm of hypopharynx", but the only supporting literature concerns adjuvant treatment of **malignant** squamous cell carcinoma of the larynx/hypopharynx. This is very likely a disease-ontology mapping artefact rather than a genuine signal for benign disease, and should be clarified before any further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11735172](https://pubmed.ncbi.nlm.nih.gov/11735172/) | 2001 | RCT | Eur J Surg Oncol | Prospective randomised study of postoperative adjuvant chemotherapy with levamisole + UFT (tegafur/uracil) in head and neck squamous cell carcinoma |
| [7003457](https://pubmed.ncbi.nlm.nih.gov/7003457/) | 1980 | Randomised pilot (placebo-controlled) | Oncology | Levamisole as adjuvant to surgery/radiotherapy in 24 patients with laryngeal/hypopharyngeal squamous cell carcinoma; lower recurrence rate reported in the treated arm |

---

## UK Market Information

Levamisole currently holds **no UK marketing authorisation** (0 licences on record; market status: Not marketed). No product name, dosage form, or approved indication text is available for review.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: manufacturer/regulatory label warnings and contraindications for Levamisole could not be retrieved for this evidence pack (classified as a **Blocking** data gap) — this alone is sufficient to prevent any safety pre-assessment. Historically, levamisole has been associated with agranulocytosis and cutaneous vasculitis (including reports of levamisole-adulterated cocaine causing vasculitis/agranulocytosis), which was a principal reason for its withdrawal from oncology use in several markets. This history should be treated as a material safety signal pending full label review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only candidate indication with genuine clinical evidence (adjuvant immunotherapy in head & neck cancer of the hypopharynx) is supported by two small, dated studies (1980, 2001) targeting malignant disease, whereas the TxGNN-predicted label specifies "benign" neoplasm — an unresolved ontology mismatch. Combined with a complete absence of regulatory safety-label data (Blocking gap), no current UK marketing authorisation, and a known historical safety signal (agranulocytosis/vasculitis), the evidence does not support proceeding beyond a research question at this time. The remaining nine TxGNN-flagged predictions for this drug (osteoporosis, tongue/buccal/floor-of-mouth/salivary gland neoplasms, schwannoma, neuroblastoma, cystic neoplasm, etc.) have no or irrelevant supporting evidence and should be disregarded as likely model noise.

**To proceed, the following is needed:**
- TFDA/MHRA product label — warnings, contraindications (DG001, Blocking)
- Verified mechanism-of-action documentation from DrugBank (DG002)
- Clarification of the disease-ontology mismatch (benign vs malignant hypopharynx neoplasm)
- A contemporary safety review of agranulocytosis and vasculitis risk before any further clinical exploration
- Assessment of the regulatory pathway, given the drug currently holds no UK marketing authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

