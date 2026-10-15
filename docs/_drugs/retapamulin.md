---
layout: default
title: Retapamulin
parent: Model Prediction Only (L5)
nav_order: 538
evidence_level: L5
indication_count: 10
---

# Retapamulin
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

# Retapamulin: From Impetigo to Hordeolum

## One-Sentence Summary

Retapamulin is a topical pleuromutilin antibacterial, originally used for impetigo and bullous impetigo.
The TxGNN model predicts it may be effective for **hordeolum**, but **no clinical trials and no publications** were found in the data compiled for this report, so this is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Impetigo, bullous impetigo (from the knowledge graph; no approved indication text is available for the UK licence) |
| Predicted New Indication | Hordeolum |
| TxGNN Prediction Score | 98.82% |
| Evidence Level | L5 (model prediction only; no actual studies. The underlying data lists L4, but with no trials, literature or mechanism studies the L5 definition applies.) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism of action data are not available in the data compiled for this report. Based on general pharmacological knowledge, retapamulin is a pleuromutilin antibacterial that inhibits bacterial protein synthesis by binding the 50S ribosomal subunit (peptidyl transferase centre).

Impetigo and hordeolum are both commonly caused by *Staphylococcus aureus*. A hordeolum is an infection of the eyelid glands. The drug's anti-staphylococcal activity therefore gives a plausible, but indirect, rationale.

There are important limits. No ophthalmic formulation exists, and the available product is a skin ointment. There is no trial or literature support, so the high score should be treated as a hypothesis to test, not as evidence of efficacy.

**Other predictions in the top 10.** The remaining predictions are much less plausible:
- **Staphylococcal scalded skin syndrome (rank 2):** The pathogen link is plausible, but the condition is systemic and toxin-mediated and is usually treated with systemic antibiotics. A topical agent is unlikely to be sufficient.
- **Cysticercosis, coenurosis, intestinal helminthiasis and fascioliasis:** These are parasitic infections. Retapamulin has no known antiparasitic activity.
- **Oesophageal, invasive, congenital and neonatal candidiasis:** These are fungal infections. Retapamulin has no known antifungal activity, and a topical skin product is unsuited to oesophageal or systemic disease. The identical scores for congenital and neonatal candidiasis suggest a shared graph artefact rather than independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1310011AAAAAAAA | Retapamulin Oint 1% | Ointment (as implied by the product name) | Not stated in the available data |

The authorisation number above is as recorded in the compiled data and is not in the standard MHRA "PL" format, so it should be checked against the MHRA register. NICE appraisal and BNF classification details were not available.

---

## Safety Considerations

- **Knowledge-graph contraindication signal:** The knowledge graph links retapamulin to a contraindication with **dermatitis**. This comes from graph relationships, not label text, so it should be verified against the SmPC.
- **Drug interactions:** No interaction data were found.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hordeolum prediction scores highly, but it is supported only by an indirect anti-staphylococcal rationale. There are no trials or publications, no ophthalmic formulation, and no mechanism or label safety data in the compiled data. Other predictions have no biological plausibility.

**To proceed, the following is needed:**
- A literature and trial search for topical or ophthalmic pleuromutilin or retapamulin use in hordeolum and blepharitis
- Mechanism of action data confirmed from DrugBank
- SmPC warnings and contraindications (the BNF/label safety data are currently missing, which blocks safety screening)
- Assessment of safety and formulation suitability for periocular or ophthalmic use, including the dermatitis contraindication signal
- A route-compatibility assessment, since the current ointment is for skin use
- Comparison against established treatments for hordeolum (warm compresses, topical antibiotics) to define any unmet need
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

