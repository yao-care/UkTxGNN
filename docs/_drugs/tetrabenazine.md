---
layout: default
title: Tetrabenazine
parent: Model Prediction Only (L5)
nav_order: 609
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tetrabenazine: predicted new indication Polycystic kidney disease 3 with or without polycystic liver disease (evidence level L5). Approved use: Huntington disease"
monitor_inn: "Tetrabenazine"
predicted_indications: ["polycystic kidney disease 3 with or without polycystic liver disease", "renal-hepatic-pancreatic dysplasia", "Joubert syndrome with renal defect", "karyomegalic interstitial nephritis", "thoracic malformation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "acute intermittent porphyria", "adult familial nephronophthisis-spastic quadriparesia syndrome", "atypical glycine encephalopathy", "congenital disorder of glycosylation with defective fucosylation"]
---

# Tetrabenazine
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

# Tetrabenazine: From Huntington Disease to Polycystic Kidney Disease 3 (With or Without Polycystic Liver Disease)

## One-Sentence Summary

Tetrabenazine is a VMAT2 inhibitor originally used for hyperkinetic movement disorders such as Huntington disease.
The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease**,
but there are currently **no clinical trials and no publications** supporting this direction. The prediction is based on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Huntington disease (the UK authorisation record holds no indication text; this is taken from the knowledge-graph indication list, which also includes Huntington disease-like syndromes and McLeod neuroacanthocytosis syndrome) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, tetrabenazine is a reversible VMAT2 inhibitor that depletes presynaptic monoamines, which is how it reduces involuntary movements in Huntington disease.

Polycystic kidney/liver disease type 3 is driven by defects in the cystic-protein and ER-processing pathway (for example GANAB/PRKCSH). This has no evident connection to monoamine transport. **No mechanistic link is supported by the available data.** The high TxGNN score (0.999) should be treated as a computational signal that has not been validated.

Other top-ranked predictions show the same pattern. Renal-hepatic-pancreatic dysplasia, karyomegalic interstitial nephritis, acute intermittent porphyria and several congenital developmental or metabolic disorders all lack a plausible link to VMAT2 inhibition. The only even loosely related prediction is Joubert syndrome with renal defect, because of its neurological movement features, but its renal and ciliary pathology is not targeted by tetrabenazine.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction.

For context, the only publication retrieved across the top ten predictions (PMID [11293103](https://pubmed.ncbi.nlm.nih.gov/11293103/), 2001, case report, *Revista de Neurologia*) concerns spasmodic torticollis associated with a vertebral haemangioma. It was retrieved for the lower-ranked prediction "thoracic malformation" and does not show that tetrabenazine treats any predicted condition.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0409030C0AAAAAA (as recorded; not a standard MHRA PL number) | Tetrabenazine Tablets 25 mg | Tablet (not stated in the record) | Not stated in the record |

One valid single-ingredient authorisation is recorded. The record contains no manufacturer, dosage form or indication text, so the licence details should be verified against the MHRA register, the SmPC and the BNF.

## Safety Considerations

The following comes from knowledge-graph contraindication links (not label text) and drug interaction screening.

- **Contraindication-related conditions (knowledge graph):**
  - Movement and neurological: Parkinson disease, parkinsonian disorder, multiple system atrophy, tardive dyskinesia, drug-induced akathisia.
  - Cardiovascular: long QT syndrome (including familial), torsades de pointes, orthostatic hypotension, postural orthostatic tachycardia syndrome, hypotensive disorder.
  - Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder.
  - Hepatobiliary: liver disease, gallbladder disease.
  - Endocrine: hyperprolactinaemia (including familial, acquired and prolactin-producing pituitary tumour).
- **Drug interactions:** 100 interactions were identified. Those listed as **Major** include:
  - Bupropion
  - Dolasetron
  - Metoclopramide

  Many **Moderate** interactions were also listed, including clarithromycin, levofloxacin, morphine, famotidine, loperamide, palonosetron, dronabinol, nabilone and eliglustat. Several of these are QT-prolonging or CNS-active agents.
- Acute intermittent porphyria, a predicted indication, would require a dedicated porphyria safety review before any consideration.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no supporting literature and no plausible mechanistic link between VMAT2 inhibition and polycystic kidney/liver disease. The safety profile also includes QT-related and hepatic cautions that would need careful handling in a renal or hepatic population.

**To proceed, the following is needed:**
- Mechanism of action data and a documented biological rationale linking monoamine depletion to cyst formation.
- Preclinical evidence (for example cell or animal models of the GANAB/PRKCSH pathway).
- Complete UK licence details (dosage form, indication, manufacturer) and SmPC warnings and contraindications.
- A safety assessment covering hepatic impairment, QT prolongation and the major drug interactions.
- Review of whether any of the other top-ranked predictions has a stronger rationale, since none currently has supporting clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

