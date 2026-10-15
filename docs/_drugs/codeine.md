---
layout: default
title: Codeine
parent: Model Prediction Only (L5)
nav_order: 189
evidence_level: L5
indication_count: 4
---

# Codeine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Codeine: From Headache Disorder and Upper Respiratory Symptoms to Nasal Cavity Disease

## One-Sentence Summary

Codeine is an opioid originally used for symptomatic relief in conditions such as headache disorder, rhinitis, pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are **no clinical trials** and only **1 publication** (a case report describing a complication of opioid misuse, not a benefit).
The prediction is therefore not supported by actual evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder (knowledge graph indications; no approved indication text is available for the UK product) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, codeine is an opioid analgesic and cough suppressant, here represented by an ibuprofen/codeine combination product (Solpadeine Mig). Its use in rhinitis, the common cold and headache is symptomatic.

The high score most likely reflects proximity in the knowledge graph between nasal-related nodes (rhinitis, nasopharyngitis) and "nasal cavity disease". It does not reflect a treatment mechanism. There is no plausible pharmacological route by which codeine would treat structural or other disease of the nasal cavity.

The only publication retrieved reports a rhinolith (nasal stone) formed around a hardened codeine and opium mixture lodged in the nose. This is a complication of misuse, not a therapeutic signal.

Other high-scoring predictions in the data show similar problems:
- **Acute laryngopharyngitis** (score 99.92%): no trials or literature. It is an extension of existing symptomatic use, and opioid antitussives have a poor benefit-risk profile in acute upper respiratory infections.
- **Trigeminal autonomic cephalalgia** (score 99.43%): the literature does not evaluate codeine. Opioids are generally not recommended for cluster headache because of limited efficacy, medication-overuse headache and dependence.
- **Allergic urticaria** (score 99.37%): codeine directly degranulates mast cells and is used as a positive control in skin tests. It is a known cause of urticaria, so this link points to harm rather than treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose & Throat Journal | A 21-year-old man had a unilateral rhinolith formed around a hardened codeine and opium mixture ("opioma"), causing nasal obstruction and recurrent purulent rhinorrhoea. This describes harm, not benefit. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010J0DGAAAY | Solpadeine Mig Ibuprofen/Codeine Tab | Not stated | Not stated |

The licence number shown is the identifier held in the compiled data and is not in standard MHRA "PL" format. Please verify it against the MHRA register.

---

## Safety Considerations

**Contraindications and cautions from the knowledge graph** (these come from drug-disease graph links, not product label text, and should be verified against the SmPC):
- Cardiovascular and respiratory: hypertension, chronic obstructive pulmonary disease
- Hepatic, renal and pancreatic: liver failure, liver disease, kidney disease, pancreatitis, gallbladder disease
- Neurological and psychiatric: epilepsy, insomnia, anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder
- Metabolic and endocrine: porphyria (including inherited porphyria), hypothyroidism (including myxoedema and congenital hypothyroidism)
- Gastrointestinal: peptic ulcer disease, inflammatory bowel disease, gastritis
- Haematological and skin: thrombocytopenia, dermatitis herpetiformis
- Other: pyoureter

**Drug interactions:** 449 interactions were identified. Examples shown include:
- **Major:** alvimopan, bupropion
- **Moderate:** atropine, cimetidine, dexamethasone, dicyclomine, glycopyrronium, granisetron, hyoscyamine, loperamide, eluxadoline, fenfluramine

**Additional considerations from the literature:** codeine can cause urticaria and allergic reactions through direct mast cell activation, and opioid misuse carries risks of dependence and medication-overuse headache.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The very high TxGNN score is not backed by any trial or therapeutic publication. The one paper describes a complication of opioid misuse. The related predictions (laryngopharyngitis, cluster headache, urticaria) are either extensions of existing symptomatic use or point toward harm. Opioid antitussives and analgesics also have an unfavourable benefit-risk profile for these conditions.

**To proceed, the following is needed:**
- Mechanism of action data and a credible rationale for a benefit in nasal cavity disease
- Product-level data for the UK authorisation (dosage form, approved indication, SmPC warnings and contraindications)
- Clinical evidence of efficacy, which does not currently exist
- A benefit-risk assessment covering dependence, misuse and medication-overuse headache
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

