---
layout: default
title: Moxonidine
parent: Model Prediction Only (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
---

# Moxonidine
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

# Moxonidine: From Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Moxonidine is a centrally acting antihypertensive, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**,
but **no clinical trials and no relevant publications** currently support this direction. It is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (the UK authorisation record has no approved indication text; hypertension is taken from the knowledge-graph indication data) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, moxonidine is an imidazoline I1 / alpha-2 adrenergic agonist that lowers sympathetic outflow, and it is used to lower blood pressure. Pharmacology records also list it as binding the alpha-2A, alpha-2B and alpha-2C adrenoceptors.

The link between this mechanism and scalp hair loss is **speculative**. One could imagine a role for vascular or neurogenic modulation of the hair follicle, but nothing in the supplied data supports it. The high TxGNN score reflects proximity in a knowledge graph and should not be read as evidence of benefit.

The other top-ranked predictions are also unsupported by clinical data:

- **Other hair disorders** (congenital hypotrichosis milia, diffuse alopecia areata, alopecia): no trials. Alopecia areata is an immune-mediated condition with no established link to sympatholytic action.
- **Hypertension-related conditions** (malignant hypertensive renal disease, malignant renovascular hypertension): these are mechanistically closer to the original indication, but they are hypertensive emergencies usually managed with rapid-acting parenteral agents. They are classed as research questions only.
- **Pulmonary hypertension and other rare conditions** (pulmonary hypertension variants, Braddock syndrome, primary hereditary glaucoma): no supporting evidence. The scores for the pulmonary hypertension entries likely reflect the shared "hypertension" term. Glaucoma has a class-level rationale only, since other alpha-2 agonists lower intraocular pressure.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no relevant literature is available for hypotrichosis simplex of the scalp.

For the related prediction "alopecia", one publication was retrieved: [40007390](https://pubmed.ncbi.nlm.nih.gov/40007390/) (2024, case report, Georgian Medical News), describing Graham-Little-Piccardi-Lasseur syndrome, a variant of lichen planopilaris. It does not appear to involve moxonidine and is likely a spurious retrieval, so it is not evidence of efficacy.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0205020M0AAAAAA | Moxonidine tablets 200 microgram | Not recorded | Not recorded |

The authorisation number above is the identifier in the compiled record and is not in the standard MHRA "PL" format. It should be verified against the MHRA register. The record contains no dosage form, manufacturer or approved indication text.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

The only interaction data compiled are pharmacological target records (alpha-2A, alpha-2B and alpha-2C adrenoceptors). They are not drug-drug interactions, and no clinical interaction information is available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or relevant publications, and the proposed mechanistic link to scalp hair biology is speculative. Evidence is at the lowest level (L5).

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a credible hypothesis linking alpha-2 / I1-imidazoline signalling to hair follicle biology
- Preclinical studies (for example follicle culture or animal models) to test the hypothesis
- A systematic literature search to identify any moxonidine-specific hair or scalp data
- The SmPC and BNF warnings and contraindications, which are currently missing, before any safety screening
- Review of whether a systemic antihypertensive is appropriate for a non-life-threatening cosmetic or dermatological condition, including the route of administration (for example topical delivery)
- If a hypertension-related prediction is of interest, a separate assessment of its clinical positioning against standard emergency treatments
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

