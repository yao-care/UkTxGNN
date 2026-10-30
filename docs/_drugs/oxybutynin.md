---
layout: default
title: Oxybutynin
parent: Model Prediction Only (L5)
nav_order: 470
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "Oxybutynin"
predicted_indications: ["restless legs syndrome", "gastroduodenitis", "peptic ulcer disease"]
description: "Oxybutynin: predicted new indication Restless legs syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Oxybutynin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Oxybutynin: Restless legs syndrome
{: .text-alpha }

## One-Sentence Summary

Oxybutynin is an antimuscarinic drug originally used to treat overactive bladder and related neurogenic bladder conditions.
The TxGNN model predicts it may be effective for **restless legs syndrome**, but there are currently **no clinical trials** and **no publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Restless legs syndrome |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (2 of 2) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Oxybutynin is a muscarinic antagonist with a direct musculotropic antispasmodic effect on smooth muscle. This is how it reduces involuntary bladder contractions in overactive bladder.

The link to restless legs syndrome is weak. The condition is mainly associated with dopaminergic dysfunction and brain iron deficiency, and anticholinergic drugs are not normally used for it. They may even worsen symptoms through sedation or other central effects. The very high score (0.9974) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The data compiled for this report do not support a plausible mechanistic link.

Two other predictions were also generated, both with no clinical trials. They are lower priority for this report:
- **Gastroduodenitis** (score 0.9962, L5): anticholinergic activity could in theory reduce GI motility and secretion, but no data support efficacy, and anticholinergic effects may worsen reflux and dyspepsia.
- **Peptic ulcer disease** (score 0.9931, L4): anticholinergics were historically used to reduce gastric secretion and motility, so the mechanism is plausible. However, the evidence is indirect and dated, and modern acid suppression (PPIs, *H. pylori* eradication) has replaced these drugs.

## Clinical Trial Evidence

Currently no related clinical trials registered for restless legs syndrome.

## Literature Evidence

Currently no related literature available for restless legs syndrome.

For context, the following publications relate to the lower-ranked prediction of peptic ulcer disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2360335](https://pubmed.ncbi.nlm.nih.gov/2360335/) | 1990 | Case report (adverse event) | DICP: The Annals of Pharmacotherapy | Reported oxybutynin-induced reflux esophagitis, probably from reduced lower oesophageal sphincter tone; a safety signal for upper GI harm |
| [4380481](https://pubmed.ncbi.nlm.nih.gov/4380481/) | 1965 | Pharmacology / mechanism review | Archives Internationales de Pharmacodynamie et de Thérapie | Describes oxybutynin as a musculotropic antispasmodic with moderate anticholinergic action |
| [14173506](https://pubmed.ncbi.nlm.nih.gov/14173506/) | 1964 | Clinical evaluation (older, likely uncontrolled) | Current Therapeutic Research | Clinical evaluation of oxybutynin chloride in gastrointestinal disease |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0704020J0AAAUAU | Oxybutynin transdermal patch 3.9 mg/24 hrs | Transdermal patch | Not available in the compiled data |
| 0704020J0AAAAAA | Oxybutynin HCl tablet 2.5 mg | Tablet | Not available in the compiled data |

Both authorisations are valid single-ingredient products. The identifiers listed appear to be BNF-style product codes (BNF section 7.4.2, drugs for urinary frequency, enuresis and incontinence) rather than MHRA PL numbers, so they should be checked against the MHRA register.

## Safety Considerations

- **Contraindications (from the TxGNN model (deep learning), not label text):** The model links oxybutynin to the following conditions. This may reflect similarities the model learned between related diseases, not biological evidence. These should be verified against the SmPC.
  - Urinary and genitourinary: bladder neck obstruction, benign prostatic hyperplasia, pyoureter
  - Gastrointestinal: paralytic ileus, intestinal obstruction, toxic megacolon, ulcerative colitis, inflammatory bowel disease, hiatus hernia, gastro-oesophageal reflux disease, oesophagitis, familial visceral myopathy
  - Ocular: angle-closure glaucoma
  - Neuromuscular: myasthenia gravis and other neuromuscular junction disease
  - Cardiovascular: hypertension, coronary artery disease, sudden cardiac arrest, heart conduction disease
  - Endocrine: hyperthyroidism, Graves disease, thyrotoxicosis
  - Hepatic and renal: liver disease, kidney disease, gallbladder disease
- **Drug Interactions:** The interaction screen returned 100 interactions in total; the 20 listed in the compiled data are mostly moderate.
  - **Major:** potassium citrate and potassium chloride
  - **Moderate (additive anticholinergic effects):** hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, trospium, mepenzolate, methscopolamine, propantheline
  - **Moderate (other):** loperamide, morphine, opium, eluxadoline, metoclopramide, aprepitant, pramlintide
- **Safety signal relevant to GI predictions:** A published case report links oxybutynin to reflux oesophagitis.

Label-based warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for restless legs syndrome rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no trials or publications, and the pharmacology argues against benefit, since anticholinergic effects may worsen symptoms. The gastrointestinal predictions are also unsupported by modern evidence and carry a safety signal.

**To proceed, the following is needed:**
- A documented mechanistic rationale linking muscarinic antagonism to restless legs syndrome
- Preclinical or early clinical data in restless legs syndrome
- Detailed mechanism of action data
- Approved indication text and SmPC safety information for the UK authorisations
- A review of the contraindication associations against the SmPC, particularly given the interaction burden with other anticholinergics
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

