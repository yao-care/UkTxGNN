---
layout: default
title: Dihydrocodeine
parent: Model Prediction Only (L5)
nav_order: 227
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Dihydrocodeine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Common cold, rhinitis, pharyngitis and nasopharyngitis"
---

# Dihydrocodeine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Dihydrocodeine: From Common Cold and Rhinitis Symptoms to Nasal Cavity Disease

## One-Sentence Summary

Dihydrocodeine is an opioid originally used in combination products for symptom relief in conditions such as the common cold, rhinitis and pharyngitis.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are currently **no clinical trials** and **no publications** supporting this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Common cold, rhinitis, pharyngitis and nasopharyngitis (from the knowledge graph; no approved indication text is available in the UK licence records) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Dihydrocodeine is an opioid with antitussive and analgesic effects. Its efficacy in the symptoms of cold-type illnesses is the basis of its original use, and mechanistically it may be applicable to nasal conditions in the same way.

The predicted indication overlaps substantially with the original ones (rhinitis, nasopharyngitis, common cold). The prediction therefore probably reflects the known upper-airway symptom-relief use rather than a genuinely new indication. In practice, this means the model score is high mainly because of proximity to existing uses.

Other predictions in the list are weaker. Several allergic or cold-related conditions (allergic urticaria, cold urticaria, papillary conjunctivitis) have no clear mechanistic rationale, and opioids can cause histamine release, which may worsen urticaria. Pain-related predictions (cervical disc degenerative disorder, headache disorders) are plausible through analgesia, but no efficacy evidence was supplied. Opioid use in headache is also associated with medication-overuse headache.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature is available for nasal cavity disease.

For context, two publications were retrieved for a lower-ranked prediction (headache disorder). Neither supports efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11915306](https://pubmed.ncbi.nlm.nih.gov/11915306/) | 2002 | Clinical study | Nihon Arukoru Yakubutsu Igakkai Zasshi | Three cases of abuse of a cough-suppressant syrup; the earlier formulation contained dihydrocodeine, which is linked to dependence |
| [28521551](https://pubmed.ncbi.nlm.nih.gov/28521551/) | 2017 | Review | J Pain Palliat Care Pharmacother | General digest of Cochrane reviews; no direct evidence for this drug |

---

## UK Market Information

The 20 marketing authorisation records are all single-ingredient entries with a valid status. Licence numbers shown are the identifiers held in the compiled data (BNF-style codes, not PL numbers). Dosage form and approved indication text are not available. The drug appears within BNF chapter 4 (central nervous system) codes. Main products:

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0407010X0CFAABD | Lemsip Max Cold & Flu powder sachets | Powder sachet | Not available |
| 0407010X0BKACA0 | Propain Plus | Caplet | Not available |
| 0407010X0BIABAI | Remedeine Forte | Tablet | Not available |
| 0407010X0BXACBL | Paramol Soluble 500mg/7.46mg | Soluble tablet | Not available |
| 0407010X0BVAAAT | Panadol Night Pain | Tablet | Not available |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): hypertension, liver failure and liver disease, epilepsy, chronic obstructive pulmonary disease, kidney disease, pancreatitis, gallbladder disease, peptic ulcer disease, inflammatory bowel disease, diabetes and diabetic ketoacidosis, hypothyroidism, benign prostatic hyperplasia, thrombocytopenia, substance abuse or dependence, and coronary artery disease or myocardial infarction. These need verification against the SmPC.
- **Drug Interactions**: 119 interactions were identified. Major interactions include **alvimopan** and **bupropion**. Moderate interactions include aprepitant, atropine, cimetidine, dexamethasone, loperamide, glycopyrronium and several other anticholinergic or antiemetic agents.
- **Other considerations**: Dependence and abuse have been reported with dihydrocodeine-containing cough products.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by model score only (L5), with no trials or literature. It largely overlaps with existing symptom-relief uses, so it is unlikely to represent true repurposing. Opioid-related risks, including dependence, and the many contraindications and interactions add caution.

**To proceed, the following is needed:**
- Label warnings and contraindications from the SmPC and BNF (currently missing, which blocks safety screening)
- Mechanism of action data (for example from DrugBank)
- Approved indication text and dosage forms for the UK authorisations
- Clinical or literature evidence specific to nasal cavity disease, or a clear case that the prediction is distinct from existing licensed uses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

