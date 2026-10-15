---
layout: default
title: Procyclidine
parent: Model Prediction Only (L5)
nav_order: 522
evidence_level: L5
indication_count: 10
---

# Procyclidine
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

# Procyclidine: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Procyclidine is an anticholinergic (muscarinic antagonist) medicine, originally used to treat Parkinson's disease and related movement disorders such as dystonia.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, but **no clinical trials and no publications** were found in the data compiled for this report, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease and related parkinsonian and dystonic disorders (from the knowledge graph; no indication text is recorded on the UK authorisation data) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on its drug class, procyclidine is a muscarinic antagonist. It is used in parkinsonism and dystonia to restore the balance between cholinergic and dopaminergic signalling in the basal ganglia.

Rasmussen encephalitis is a different kind of condition. It is a chronic, immune-mediated, T-cell-driven inflammation of one brain hemisphere, causing focal seizures and progressive atrophy. Blocking muscarinic receptors does not address this inflammation. The very high TxGNN score is most likely driven by shared neurological neighbours in the knowledge graph, not by a demonstrated pharmacological link.

At most, an anticholinergic might relieve secondary movement symptoms. The mechanistic case is therefore weak.

### Other Predicted Indications

The model produced nine further predictions. None has trial or literature support in the compiled data, and all are currently recommended as Hold.

| Rank | Predicted Indication | Score | Comment |
|---|---|---|---|
| 2 | Myelitis | 99.65% | Anticholinergics could at most ease secondary spasticity or dystonia; inflammation is not addressed |
| 3 | PLA2G6-associated neurodegeneration | 99.63% | Symptomatic overlap with dystonia-parkinsonism only; not disease-modifying |
| 4 | Attention deficit-hyperactivity disorder | 99.63% | Mechanistic direction questionable, as anticholinergics may impair cognition and attention |
| 5 | Faciodigitogenital syndrome | 99.45% | No plausible mechanistic link; likely a graph artefact |
| 6 | Transaldolase deficiency | 99.42% | No recognised link to anticholinergic activity |
| 7 | Progressive supranuclear palsy-corticobasal syndrome | 99.42% | Related to parkinsonism, but limited benefit and added cognitive risk in older patients |
| 8 | Juvenile paralysis agitans (of Hunt) | 99.37% | Historical term for juvenile parkinsonism; largely redundant with existing indications (L4) |
| 9 | Perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis | 99.34% | Structural developmental disorder; no plausible role |
| 10 | Fructose-1,6-bisphosphatase deficiency | 99.34% | No mechanistic relationship evident |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0409020S0AAAEAE | Procyclidine HCl tablets 5 mg | Tablet | Not recorded in the compiled data |

The identifier above is a classification-style code, not a standard PL number, and no manufacturer or indication text is recorded. Please check the current MHRA-authorised products, the SmPC and the BNF (Chapter 4, Central nervous system: drugs used in parkinsonism and related disorders) for the licensed indications. No NICE appraisal information was available in the compiled data.

## Safety Considerations

Label-based warnings and contraindications were not available in the compiled data. The knowledge graph does, however, link procyclidine to contraindications in the following conditions. These are consistent with the known effects of anticholinergics, but they are not taken from label text.

- **Contraindication-linked conditions (knowledge graph):**
  - Eye: angle-closure glaucoma
  - Gastrointestinal: paralytic ileus, intestinal obstruction, pyloric stenosis, achalasia and megaoesophagus, hiatus hernia, ulcerative colitis and inflammatory bowel disease, toxic megacolon, gastric ulcer
  - Genitourinary: benign prostatic hyperplasia, bladder neck obstruction
  - Neuromuscular: myasthenia gravis
  - Cardiovascular and endocrine: hypertension, coronary artery disease, hyperthyroidism
  - Organ disease: kidney, liver and gallbladder disease
- **Drug interactions:** 70 interactions were identified. The main ones from the first 20 reviewed are below.
  - **Major:** potassium chloride and potassium citrate.
  - **Moderate:** other antimuscarinic agents (hyoscyamine, atropine, glycopyrronium, dicyclomine, trospium, mepenzolate, methscopolamine, clidinium), opioids and related agents (morphine, opium, loperamide, eluxadoline), cannabinoids (dronabinol, nabilone), metoclopramide and pramlintide.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, Rasmussen encephalitis, has no trial or literature support (L5). The proposed mechanism does not address the underlying immune-mediated inflammation. The anticholinergic safety profile (cognitive effects, and the many conditions in which it should be avoided) adds caution.

**To proceed, the following is needed:**
- Mechanism of action data to allow a proper mechanistic analysis
- Any preclinical or clinical evidence linking muscarinic antagonism to Rasmussen encephalitis
- Label-based warnings and contraindications from the current SmPC and BNF
- Confirmation of the licensed indication and product details for the UK authorisation
- If the project is redirected, consider the symptomatic movement-disorder predictions (e.g. PLA2G6-associated neurodegeneration, atypical parkinsonism) for focused literature review, bearing in mind their limited disease-modifying potential
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

