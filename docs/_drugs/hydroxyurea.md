---
layout: default
title: Hydroxyurea
parent: Model Prediction Only (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Hydroxyurea: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Melanoma, sickle cell anaemia, ovarian cancer"
monitor_inn: "Hydroxyurea"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin c disease syndrome", "sickle cell-hemoglobin E disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "cervical adenosarcoma", "colon mucinous adenocarcinoma", "rectum mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma"]
---

# Hydroxyurea
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

## Hydroxyurea: From Melanoma and Sickle Cell Anaemia to Female Breast Carcinoma
{: .text-alpha }

## One-Sentence Summary

Hydroxyurea is an antineoplastic and fetal haemoglobin-inducing drug, originally used for conditions such as melanoma, ovarian cancer and sickle cell anaemia.
The TxGNN model predicts it may be effective for **female breast carcinoma**, but there are **no registered clinical trials** and the **20 publications** retrieved are almost entirely preclinical or not breast-specific.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Melanoma, sickle cell anaemia, ovarian cancer (from the knowledge graph; no approved indication text is available for the UK licence) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the compiled data. From published knowledge, hydroxyurea inhibits ribonucleotide reductase, which depletes the deoxyribonucleotide (dNTP) pool and causes replication stress in dividing cells. This is the basis of its use in cancers and myeloproliferative conditions.

Several preclinical papers use hydroxyurea as a replication-stress tool compound in breast and ovarian cancer cells. These include work on RPA2 hyperphosphorylation and DNA repair, valproic acid sensitisation, and ATR inhibition. They suggest breast cancer cells may be vulnerable to replication stress, which makes the prediction biologically plausible.

However, these studies do not show that hydroxyurea is an effective breast cancer therapy. The older clinical studies (1991–1992) were phase 1 combination regimens in mixed solid tumours, not breast-specific. The very high TxGNN score is a computational prediction and is not clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No randomised trials or breast-specific clinical studies were found. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In-silico/Preclinical | Drug Research | Designed hydroxyurea–lipid conjugates to improve cellular uptake in breast cancer, targeting the PI3K/AKT/mTOR pathway |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid sensitised breast cancer cells to hydroxyurea by inhibiting RPA2 hyperphosphorylation-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | A valproic acid analogue influenced RPA2-mediated DNA repair in breast carcinoma cells; hydroxyurea used as the sensitising agent |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | Preclinical | Br J Cancer | Identified the ATR inhibitor NU6027 in breast and ovarian cancer cell lines |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | Preclinical | Mol Pharmacol | A novel ribonucleotide reductase inhibitor (COH29) inhibited DNA repair in BRCA1-defective breast cancer cells, with hydroxyurea as a reference RNR inhibitor |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase 1 | Am J Clin Oncol | Sequential 5-FU/leucovorin then hydroxyurea in 20 patients with advanced gastrointestinal and breast cancers (not breast-specific) |
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | Phase 1/2 | Cancer Chemother Pharmacol | 5-FU, leucovorin, hydroxyurea and cisplatin with radiotherapy in mixed advanced solid tumours |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | Case report | Case Rep Hematol | Management of coexisting breast cancer and essential thrombocythaemia |
| [34661718](https://pubmed.ncbi.nlm.nih.gov/34661718/) | 2022 | Preclinical | Naunyn-Schmiedeberg's Arch Pharmacol | Hydroxyurea-loaded nanoparticles showed pH-dependent release and cell cycle arrest in vitro |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 190400000AACBCB | Ichthammol_(S) | Not specified | Not specified |

The single authorisation recorded in the compiled data is listed under a product name (Ichthammol) that does not correspond to hydroxyurea. It also has no dosage form or indication text. This record should be verified against the MHRA register before any reliance is placed on it. The data compiled for this report does not include NICE appraisals or BNF classification for this drug.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite; ribonucleotide reductase inhibitor) |
| Myelosuppression Risk | High. The knowledge graph links hydroxyurea with leukopenia, thrombocytopenia and anaemia |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | FBC with differential, platelet count, renal and liver function |
| Handling Protection | Follow local cytotoxic drug handling procedures |

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: kidney disease, pyoureter, thrombocytopenia, anaemia, macrocytic anaemia, leukopenia, cutaneous vasculitis.
- **Drug Interactions**: 100 potential interactions were identified. Only levofloxacin is graded (Minor); the rest, including doxycycline, amphotericin B, hydrocortisone, aspirin, morphine, metformin and simvastatin, have no severity grade, so their clinical significance is unknown.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Support for breast carcinoma rests on a model prediction and preclinical replication-stress studies, with no registered trials and no breast-specific clinical efficacy data. Hydroxyurea's marrow toxicity also needs weighing against uncertain benefit.

**To proceed, the following is needed:**
- Breast-cancer-specific clinical evidence, starting with phase 2 studies or well-designed preclinical models of efficacy
- Verified MHRA licensing details, SmPC warnings and contraindications for hydroxyurea
- Detailed mechanism-of-action data
- Review of interaction severity for key co-medications, particularly other myelosuppressive agents

---

### Other Predicted Indications (for context)

The same data lists stronger candidates than breast carcinoma elsewhere in the ranking:

- **Sickle cell–haemoglobin C disease** (TxGNN 99.67%, evidence level L2): one terminated phase 2 trial ([NCT00532883](https://clinicaltrials.gov/study/NCT00532883), n=44) plus a 2025 trial publication in NEJM Evidence ([39647172](https://pubmed.ncbi.nlm.nih.gov/39647172/)) and cohort data. This is the best-supported prediction, and adequately powered RCT confirmation is still needed.
- **Sickle cell–beta-thalassaemia** (L3): supportive but not disease-specific evidence.
- **Other sickle cell variants and rare mucinous or cervical tumours**: indirect evidence or model prediction only (L4–L5); Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

