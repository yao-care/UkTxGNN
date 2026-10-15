---
layout: default
title: Guaifenesin
parent: Model Prediction Only (L5)
nav_order: 321
evidence_level: L5
indication_count: 10
---

# Guaifenesin
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

# Guaifenesin: From Upper Respiratory Tract Symptoms to Nasal Cavity Disease

## One-Sentence Summary

Guaifenesin is an expectorant that thins and loosens airway mucus, originally used for conditions such as the common cold, rhinitis and pharyngitis.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are **no registered clinical trials** and only **1 publication** (a 2002 review on respiratory allergies in voice users) that touches on this direction. The evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder (knowledge-graph indications; no approved indication text is available for the UK licence) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction with no actual studies of guaifenesin for this indication; the single review only mentions guaifenesin within a decongestant combination) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on general pharmacology, guaifenesin is an expectorant that thins and loosens airway mucus. Its efficacy as a symptomatic treatment in common cold and upper respiratory conditions is established, and mechanistically it may be applicable to disease of the nasal cavity.

The predicted indication overlaps with the drug's existing indications of rhinitis, nasopharyngitis and the common cold, all of which affect the upper airway. This anatomical and symptomatic closeness is the most likely reason for the high TxGNN score.

There are important limits. The only supporting article, a 2002 review on hidden respiratory allergies in voice users, discusses treatment strategies and mentions decongestants with guaifenesin as possibly useful. It does not test guaifenesin as a treatment for nasal cavity disease. "Nasal cavity disease" is also a broad category, so a specific condition would need to be defined before any evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Review | Logopedics, Phoniatrics, Vocology | Treatment strategies for allergic voice patients. Antihistamines are generally avoided, decongestants with guaifenesin may be useful, and steroids are helpful in perennial allergic symptoms. Guaifenesin was not tested on its own. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0309020G0AAABAB (BNF-style product code; no PL number available) | Guaifenesin oral solution 100 mg/5 ml | Oral solution | Not available |

---

## Safety Considerations

The data compiled for this report contain no label-based warnings, contraindications or interaction data for guaifenesin. The knowledge graph does list a large number of disease associations flagged as contraindications. These come from graph edges rather than product label text, so they should not be treated as confirmed label contraindications. They include:

- **Cardiovascular and metabolic:** hypertension, hypothyroidism, adrenocortical insufficiency (Addison disease)
- **Hepatic and renal:** liver failure, liver disease, cirrhosis, kidney disease
- **Respiratory:** chronic obstructive pulmonary disease
- **Gastrointestinal:** gastric ulcer, peptic ulcer disease, inflammatory bowel disease, pancreatitis, gallbladder disease
- **Neuropsychiatric:** epilepsy, insomnia, anxiety disorder, psychotic disorder
- **Other:** porphyria, thrombocytopenia

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no clinical trials exist, and the one supporting article is a 2002 review that does not test guaifenesin for nasal cavity disease. Mechanism-of-action data and label safety data are also missing, so the prediction cannot yet be advanced.

**Other predictions of note:**
- **Tracheal disease** (score 98.83%, evidence level L3) has the strongest supporting data: a 2012 in vitro study comparing guaifenesin, N-acetylcysteine and ambroxol on MUC5AC and mucociliary transport in human airway cells, plus a 2018 case report. It is better supported than nasal cavity disease and is worth considering as a research question.
- **Acute laryngopharyngitis** (99.98%) is plausible because it is close to the existing pharyngitis indication, but it has no supporting evidence.
- **Faucial diphtheria** (99.54%) lacks a plausible mechanism, because it needs antitoxin and antibiotics, and the score likely reflects network proximity only.
- Predictions for cervical disc degenerative disorder, papillary conjunctivitis, trigeminal autonomic cephalalgia, anorectal stricture, anal polyp and punctate epithelial keratoconjunctivitis have no evidence and no plausible mechanism, and are likely graph artefacts.

**To proceed, the following is needed:**
- Mechanism of action data for guaifenesin
- Label warnings, contraindications and interaction data from the SmPC and BNF
- A defined target condition within "nasal cavity disease", followed by a systematic literature search
- Controlled clinical studies of guaifenesin alone, as opposed to in combination products
- Approved indication text and dosage form details for the UK licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

