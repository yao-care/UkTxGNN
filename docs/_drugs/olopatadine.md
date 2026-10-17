---
layout: default
title: Olopatadine
parent: Model Prediction Only (L5)
nav_order: 461
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Olopatadine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis…"
monitor_inn: "Olopatadine"
predicted_indications: ["conjunctival folliculosis"]
---

# Olopatadine
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

# Olopatadine: From Allergic Conjunctivitis to Rosacea Conjunctivitis

## One-Sentence Summary

Olopatadine is an antihistamine and mast cell stabiliser, originally used for allergic eye and nasal conditions such as allergic rhinitis and atopic, vernal and papillary conjunctivitis.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**,
but there are currently **no clinical trials** and **no publications** supporting this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, olopatadine is an H1 antagonist and mast cell stabiliser, and its efficacy in allergic and atopic conjunctivitis is established. Mechanistically, it may be applicable to inflammatory conjunctival conditions with an allergic component.

The link to rosacea conjunctivitis is indirect and speculative. Ocular rosacea is driven mainly by meibomian gland dysfunction, inflammation and *Demodex*, rather than mast cell-mediated allergy. The high TxGNN score therefore reflects network similarity in the knowledge graph, not demonstrated clinical benefit.

Other predicted indications are also mostly conjunctival conditions. The highest-ranked alternatives, none of which have clinical trial data, are:

- **Punctate epithelial keratoconjunctivitis** (score 98.81%): one case report on atopic keratoconjunctivitis, which did not test olopatadine for this indication.
- **Parasitic conjunctivitis** (score 97.89%): one preclinical-type article on allergic conjunctivitis induced by *Acanthamoeba* protein. It is unclear whether olopatadine was tested.
- **Angelucci syndrome** (score 97.84%): some plausibility because of overlap with vernal conjunctivitis, but no direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for rosacea conjunctivitis.

For context, the two articles retrieved for other predicted indications are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22606467](https://pubmed.ncbi.nlm.nih.gov/22606467/) | 2011 | Case report | Case Rep Ophthalmol Med | Limbitis secondary to autologous serum eye drops in a patient with atopic keratoconjunctivitis; olopatadine 0.2% was part of her background treatment (predicted indication: punctate epithelial keratoconjunctivitis) |
| [34029500](https://pubmed.ncbi.nlm.nih.gov/34029500/) | 2021 | Preclinical | Curr Eye Res | Allergic conjunctivitis induced by *Acanthamoeba* excretory-secretory protein; assessed resolvin D1 and antiallergic agents (predicted indication: parasitic conjunctivitis) |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1104020Z0AAAAAA | Olopatadine eye drops 1 mg/ml | Eye drops | Not available in the data compiled for this report |

This entry appears to be a BNF-style product code (BNF chapter 11, eye) rather than a standard MHRA PL number, so the authorisation details should be verified against the MHRA register.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not product label text): lower respiratory tract disease, paranasal sinus disease, nasal cavity disease and upper respiratory tract disease. These should be verified against the SmPC.
- **Drug Interactions**: the interaction database returned 100 entries, but none has a severity grading. Examples include pantoprazole, doxycycline, clotrimazole, metformin, omeprazole, simvastatin and prednisolone. These are likely to be of limited relevance for topical ocular use and need review against the SmPC.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials or directly relevant literature. The mechanistic link to ocular rosacea is weak, because its main drivers are meibomian gland dysfunction and *Demodex* rather than allergy.

**To proceed, the following is needed:**
- Detailed mechanism of action data for olopatadine
- A targeted literature search for olopatadine in ocular rosacea and meibomian gland dysfunction
- Clinical evidence, such as a pilot study in patients with ocular rosacea who have a clear allergic component
- Full SmPC-based warnings, contraindications and approved indication text for the UK product
- Verification of the UK marketing authorisation number and dosage form
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

