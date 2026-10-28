---
layout: default
title: Azithromycin
parent: Model Prediction Only (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Azithromycin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Streptococcal infection, bacterial pneumonia…"
monitor_inn: "Azithromycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Azithromycin
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

## Azithromycin: From Bacterial Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Azithromycin is a macrolide antibiotic, originally used to treat bacterial infections such as streptococcal and staphylococcal infections, bacterial pneumonia and conjunctivitis.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but **no clinical trials and no publications** support this prediction, so it should be treated as a model signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal infection, bacterial pneumonia, staphylococcal infection and others (the UK licence record contains no indication text) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, azithromycin is a macrolide antibiotic, its efficacy in bacterial infections is established, but there is no identifiable mechanistic link to hyperamylasemia.

Hyperamylasemia is a laboratory finding with many causes (pancreatic, salivary and renal), not a disease that an antibacterial would be expected to treat. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions in the list have more plausible, though still indirect, rationales. These are not the primary prediction but are worth noting:

- **Punctate epithelial keratoconjunctivitis (score 0.9978):** conjunctivitis is already an original indication, and azithromycin has anti-inflammatory effects on the ocular surface. The only supplied paper is a case report on microsporidial keratoconjunctivitis that does not test azithromycin.
- **Monoclonal gammopathy (score 0.9961):** one in vitro study shows macrolides block autophagy flux and sensitise myeloma cells to bortezomib. This is preclinical only.
- **Sickle cell disease and other congenital haematological disorders (score 0.9940):** azithromycin's anti-inflammatory effects could plausibly reduce acute chest syndrome. Two trials testing this were withdrawn with no participants enrolled.
- **Septicaemic plague (score 0.9952):** an in vitro study found azithromycin had poor activity against *Yersinia pestis* strains, and effective standard treatments already exist.

## Clinical Trial Evidence

Currently no related clinical trials registered for hyperamylasemia.

## Literature Evidence

Currently no related literature available for hyperamylasemia.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501050A0AAAAAA (BNF-style code, not a PL number) | Azithromycin capsules 250 mg | Capsule | Not stated in the data compiled for this report |

The BNF classification for this product is not stated in the compiled data. Please verify the licence details and approved indications against the MHRA record and the current SmPC.

## Safety Considerations

The compiled data contain no label-based warnings or contraindications. The following come from the knowledge graph and drug interaction databases.

- **Knowledge-graph contraindication signals (not label text):** long QT syndrome (including familial), torsades de pointes, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotising enterocolitis, myasthenia gravis (including adult-onset), neuromuscular junction disease, and hearing or auditory system disorders.
- **Drug interactions:** 100 interactions were identified, of which 20 were listed in the compiled data. The most clinically important are the two **Major** interactions:
  - Cisapride
  - Dolasetron

  Both are most likely related to QT prolongation. Moderate interactions include clarithromycin, levofloxacin, granisetron, famotidine, loperamide, balsalazide, aluminium hydroxide and magnesium-containing antacids, and several laxatives (bisacodyl, castor oil, glycerin, lactitol and lactulose). Minor interactions include amoxicillin and metronidazole.

Please refer to the SmPC and BNF for complete safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, hyperamylasemia, has no supporting trials or literature and no plausible mechanism, so it is best regarded as a TxGNN model (deep learning) artefact (Evidence Level L5). Of the other predictions, sickle cell disease complications (acute chest syndrome prophylaxis) and ocular surface inflammation are the most biologically plausible research questions, but neither has usable clinical data.

**To proceed, the following is needed:**
- Mechanism of action data for azithromycin
- Label-based warnings and contraindications from the SmPC (the current data are incomplete)
- Licence details, including dosage form and approved indication text, from the MHRA record
- For hyperamylasemia: any clinical rationale and supporting data; otherwise deprioritise it
- For sickle cell disease and acute chest syndrome: a new, adequately powered trial, since both registered trials were withdrawn without enrolment
- For ocular surface disease: direct clinical studies of azithromycin in punctate epithelial keratoconjunctivitis
- A QT-risk assessment and a review of interacting drugs for any future study population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

