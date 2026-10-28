---
layout: default
title: Loteprednol Etabonate
parent: Model Prediction Only (L5)
nav_order: 382
evidence_level: L5
indication_count: 9
monitor_inn: "Loteprednol etabonate"
predicted_indications: ["serous conjunctivitis except viral", "chronic follicular conjunctivitis", "parasitic conjunctivitis", "conjunctival folliculosis", "pseudomembranous conjunctivitis", "Angelucci syndrome", "acute hemorrhagic conjunctivitis", "acute contagious conjunctivitis", "otitis externa"]
last_modified_at: 2026-10-28
description: "Loteprednol Etabonate: predicted new indication Serous conjunctivitis except viral (evidence level L5). Approved use: Not recorded in the local data"
---

# Loteprednol Etabonate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Loteprednol Etabonate: Serous conjunctivitis except viral
{: .text-alpha }

## One-Sentence Summary

Loteprednol etabonate is a topical corticosteroid eye drop, with uveitis and allergic or inflammatory conditions of the conjunctiva recorded as its original uses in the knowledge graph.
The TxGNN model predicts it may be effective for **pseudomembranous conjunctivitis** (the top-ranked prediction with any supporting publication), but there are **no clinical trials** and only **1 indirect publication** supporting this direction.
The evidence is therefore very limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Serous conjunctivitis except viral |
| TxGNN Prediction Score | 0.9969 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

**Note on evidence level:** the only publication for pseudomembranous conjunctivitis concerns adenoviral conjunctivitis, a related condition, and does not directly study the predicted disease. Under the evidence rules this is L5, although the underlying data compilation labelled it L4.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, loteprednol etabonate is a topical corticosteroid. Corticosteroids as a class suppress inflammation, and the TxGNN model (deep learning) scores it for several inflammatory and allergic eye conditions. These scores may reflect similarities the model learned between related diseases, not biological evidence.

The predicted conditions are mostly forms of conjunctivitis, which share an inflammatory component with the conditions already recorded for this drug. For pseudomembranous conjunctivitis, topical corticosteroids are used clinically in severe adenoviral cases with pseudomembranes or subepithelial infiltrates to reduce inflammation. This is the main rationale for the prediction.

There are important caveats. Many predicted conditions are infectious (viral, parasitic, chlamydial or bacterial), where a steroid does not treat the cause and may worsen infection or prolong viral shedding. The benefit-risk balance is therefore an open question. The high model scores (up to 0.9969) reflect model output, not clinical proof.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40638366](https://pubmed.ncbi.nlm.nih.gov/40638366/) | 2025 | Comparative study (design not verified) | Ocular Immunology and Inflammation | Evaluated topical ganciclovir, povidone-iodine and their combination with loteprednol etabonate for reducing viral load and improving clinical outcomes in adenoviral conjunctivitis, using PCR. Indirect evidence: it addresses adenoviral conjunctivitis, not pseudomembranous conjunctivitis specifically. Results are not available in the data compiled |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1104010W0AAAAAA | Loteprednol Etabonate Eye Drops 0.5% | Not stated | Not stated in the licence record |

The licence list is complete (1 single-ingredient product, valid). The data compiled for this report did not include BNF or NICE indication details for this product.

---

## Safety Considerations

- **Conditions recorded as contraindications in the knowledge graph** (relations from the knowledge graph, not label text): ocular hypertension, glaucoma, herpes simplex virus keratitis, fungal eye infection, viral eye infection, ocular tuberculosis and ophthalmic herpes zoster. These are particularly relevant to the predicted infectious conjunctivitis indications, where steroid use could be harmful without pathogen control.
- **Drug Interactions:** 30 potential interactions were recorded, all with an unclassified severity level. Examples include other corticosteroids (triamcinolone, prednisone), warfarin, clopidogrel, acetylsalicylic acid, ibuprofen, hydroxychloroquine, simvastatin, rosuvastatin and several proton pump inhibitors. The clinical significance is not established in the data compiled. These interaction records are primarily systemic and their relevance to an eye drop is uncertain.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All nine predictions are supported by model scores only, apart from one indirect publication on adenoviral conjunctivitis. No clinical trials exist for any predicted indication. Several predicted conditions are infectious, and the knowledge graph records viral, fungal and herpetic eye infections as contraindications, so there is a real safety concern.

**To proceed, the following is needed:**
- Direct clinical studies in the predicted condition (for pseudomembranous conjunctivitis, ideally randomised and including safety outcomes on viral shedding)
- Full text of PMID 40638366 to confirm the design, the role of loteprednol and the results
- Mechanism of action data
- Licence indication text and SmPC warnings and contraindications for the UK product
- A clear approach to excluding infectious causes before any steroid use
- For otitis externa, an assessment of formulation, route and tympanic membrane integrity, since this product is an eye drop
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

