---
layout: default
title: Tolcapone
parent: Model Prediction Only (L5)
nav_order: 625
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Tolcapone: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Parkinson disease"
monitor_inn: "Tolcapone"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "transaldolase deficiency", "fructose-1,6-bisphosphatase deficiency", "Lewy body dementia", "X-linked intellectual disability-ataxia-apraxia syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "X-linked intellectual disability-cerebellar hypoplasia syndrome", "paralysis agitans, juvenile, of Hunt"]
---

# Tolcapone
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

## Tolcapone: From Parkinson Disease to Rasmussen Subacute Encephalitis
{: .text-alpha }

## One-Sentence Summary

Tolcapone is a catechol-O-methyltransferase (COMT) inhibitor, originally used to treat Parkinson disease.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but there are currently **no clinical trials and no publications** supporting this direction, so it rests on a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (the licence record held no approved indication text, so this is taken from the drug's known indications) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (2 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, tolcapone is a COMT inhibitor that prolongs the availability of levodopa and dopamine in the brain. Its efficacy in Parkinson disease is established, and this is a symptomatic dopaminergic effect.

Rasmussen encephalitis is a rare, immune-mediated, unilateral inflammatory disease of the brain, typically causing refractory seizures and progressive neurological decline. No plausible mechanistic link between COMT inhibition and this condition can be established from the data supplied. The high TxGNN score (0.9993) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The predictions ranked 2 to 10 follow a similar pattern. Most have no supporting studies (for example myelitis, transaldolase deficiency, fructose-1,6-bisphosphatase deficiency and several rare neurodevelopmental syndromes). Two are worth noting:
- **Lewy body dementia** (score 0.9964, evidence level L4) shares dopaminergic dysfunction and alpha-synuclein pathology with Parkinson disease. The only supporting item is one 2024 preclinical iPSC organoid study, so this remains a research question.
- **Paralysis agitans, juvenile, of Hunt** (score 0.9952) is a historical term for juvenile parkinsonism. It is likely a relabelling of an existing indication rather than a true repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for Rasmussen subacute encephalitis.

For the related prediction of Lewy body dementia, one preclinical publication was identified: [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) (2024, *Science Advances*), which modelled Lewy body disease using SNCA-triplication iPSC-derived cortical organoids and screened for therapeutic compounds. It is indirect, preclinical evidence only.

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0409010S0AAAAAA | Tolcapone 100mg tablets | Tolcapone |
| 0409010S0BBAAAA | Tasmar 100mg tablets | Tolcapone |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

The identifier shown does not follow the usual MHRA "PL" format, so check it against the MHRA database. Please confirm the current licensed indication and BNF classification in the SmPC and BNF.

<!-- review:begin uk-lic-20261106-tolcapone-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The data compiled for this report show one valid single-ingredient authorisation. The identifier shown does not follow the usual MHRA "PL" format, so check it against the MHRA database." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 2 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-tolcapone-1 -->

## Safety Considerations

- **Contraindications from the knowledge graph** (these are graph associations, not label text): liver disease, gallbladder disease, melanoma, hypotensive disorder, rhabdomyolysis, nodular fasciitis, tardive dyskinesia and lingual-facial-buccal dyskinesia.
- **Drug Interactions**: 65 interactions were identified in total. Examples of those listed:
  - **Major**: methylene blue.
  - **Moderate**: epinephrine (including ophthalmic and topical forms), morphine (including liposomal), opium, codeine, dronabinol, nabilone, naltrexone, metoclopramide, promethazine, chlorpheniramine, cetirizine, dextromethorphan and ethanol.
  - **Minor**: warfarin and dicoumarol.
  - **Unknown severity**: omeprazole.
- **Known concerns**: tolcapone carries a recognised risk of hepatotoxicity, which would require liver monitoring and is particularly relevant to the metabolic-liver diseases among the predictions. This is general knowledge, as label warning text was not available in the data compiled.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for Rasmussen subacute encephalitis rests on a model score alone, with no clinical trials, no publications and no plausible mechanistic link to COMT inhibition. Combined with tolcapone's hepatotoxicity risk, the balance does not currently support progressing this indication.

**To proceed, the following is needed:**
- Detailed mechanism of action data, and evidence of a biological link between COMT inhibition and the immune-mediated pathology of Rasmussen encephalitis
- Preclinical or clinical studies in the predicted indication
- Verified UK licensing details, including the approved indication text, dosage form and PL number
- Label warnings and contraindications from the SmPC and BNF
- A liver safety monitoring plan
- If a repurposing direction is pursued, consider Lewy body dementia as a better-founded research question, supported by preclinical work and a shared dopaminergic rationale

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The data compiled for this report show one valid single-ingredient authorisation" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

