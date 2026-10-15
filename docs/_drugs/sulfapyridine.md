---
layout: default
title: Sulfapyridine
parent: Model Prediction Only (L5)
nav_order: 582
evidence_level: L5
indication_count: 10
---

# Sulfapyridine
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

# Sulfapyridine: From Dermatitis Herpetiformis to Heparin-Induced Thrombocytopenia

## One-Sentence Summary

Sulfapyridine is a sulfonamide originally used to treat dermatitis herpetiformis.
The TxGNN model predicts it may be effective for **heparin-induced thrombocytopenia (HIT)**, but there are currently **no clinical trials and no publications** supporting this prediction. It is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis herpetiformis |
| Predicted New Indication | Heparin-induced thrombocytopenia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sulfapyridine is a sulfonamide whose efficacy in dermatitis herpetiformis is established, which is generally attributed to anti-inflammatory and neutrophil-modulating effects.

No mechanistic link to HIT has been identified. HIT is an antibody-mediated (anti-PF4/heparin) prothrombotic disorder, which is very different from the neutrophil-driven skin disease for which sulfapyridine is used. Sulfonamides are also occasionally associated with drug-induced thrombocytopenia, which argues against benefit. The high score most likely reflects proximity in the knowledge graph rather than a biological rationale.

**Other predictions reviewed (all L5 unless stated, all Hold):**

| Predicted Indication | Score | Comment |
|------|------|------|
| Hereditary angioedema | 99.82% | Unproven hypothesis only; established therapies exist |
| Hereditary angioedema with C1Inh deficiency | 99.82% | Same as above |
| Acquired aplastic anaemia | 99.82% | Sulfonamides can cause bone marrow suppression; safety concern |
| C1 inhibitor deficiency | 99.81% | Prediction only |
| Autoimmune haemolytic anaemia | 99.81% | Sulfonamides can cause haemolysis; may worsen the condition |
| Serpinopathy with toxic serpin polymerisation | 99.75% | No identified mechanism |
| Disorder of GPI anchor biosynthesis | 99.72% | No identified mechanism |
| Haemoglobinuria | 99.70% | Evidence level L4; only a 1945 case report of an adverse reaction |
| Venous insufficiency | 99.54% | No identified mechanism |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction (HIT).

For the ninth-ranked prediction (haemoglobinuria), the only publication is:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20986275](https://pubmed.ncbi.nlm.nih.gov/20986275/) | 1945 | Case report | Proceedings. Transvaal Mine Medical Officers' Association | Haemoglobinuria following sulfapyridine administration, an adverse reaction rather than a therapeutic effect |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501080V0AAADAD | Sulfapyridine Cap 250mg | Capsule (per product name) | Not stated in the data compiled |

The data compiled for this report list one valid single-ingredient authorisation. The identifier shown is not in the usual MHRA PL format, so it should be verified against the MHRA register and the BNF.

## Cytotoxicity

Not applicable (sulfapyridine is not an antineoplastic drug), so this section is omitted.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note from the prediction review: sulfonamides are recognised causes of blood dyscrasias, including bone marrow suppression, immune-mediated or G6PD-related haemolysis, and thrombocytopenia. This is particularly relevant to the haematological predictions above.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no trials or publications, no plausible mechanism, and a known haematological toxicity profile that runs contrary to the proposed haematological indications. Established HIT management does not involve sulfonamides.

**To proceed, the following is needed:**
- Mechanism of action data for sulfapyridine
- SmPC/BNF warnings and contraindications, and the approved indication text for the UK product
- Verification of the UK authorisation record
- Preclinical or mechanistic evidence for any biological link to HIT (or the other predicted conditions) before further consideration
- A formal haematological safety assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

