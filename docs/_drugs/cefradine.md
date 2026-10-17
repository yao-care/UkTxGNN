---
layout: default
title: Cefradine
parent: Model Prediction Only (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cefradine: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Urinary tract infection, tonsillitis, otitis media…"
monitor_inn: "Cefradine"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "premalignant hematological system disease", "bronchitis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis"]
---

# Cefradine
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

# Cefradine: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Cefradine is a first-generation cephalosporin antibiotic, originally used for urinary tract, respiratory tract and other bacterial infections.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but there are **no clinical trials and no publications** supporting this prediction, and the data compiled for this report show no credible mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, tonsillitis, otitis media, respiratory tract infections, pneumonia, pharyngitis and other bacterial infections (the UK authorisation record has no indication text) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 96.51% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cefradine is a first-generation cephalosporin, a class that inhibits bacterial cell wall (peptidoglycan) synthesis. Its efficacy in bacterial infections of the urinary and respiratory tracts is established.

Hyperamylasemia is a biochemical finding (raised serum amylase), not an infectious process. There is no credible pharmacological reason why a cell wall-targeting antibiotic would correct it. The high TxGNN score most likely reflects proximity within the knowledge graph rather than a true therapeutic rationale. Without supporting trials or literature, this prediction should be treated as a model artefact.

Other top-ranked predictions show a similar pattern:

- **No credible mechanism**: polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility and premalignant haematological disease.
- **Biologically implausible**: *Ureaplasma* urethritis, because *Ureaplasma* lacks a cell wall and beta-lactams are intrinsically ineffective.
- **Plausible but not supported by current standards of care**: gonococcal urethritis (ceftriaxone is now recommended), uterine inflammatory disease (polymicrobial and anaerobic flora are not adequately covered) and xanthogranulomatous pyelonephritis (management is usually surgical, with culture-directed antibiotics as an adjunct).
- **Extension of existing indications**: bronchitis (rated L4, "Research Question"). Most acute bronchitis is viral, and first-generation cephalosporins are less reliable against *H. influenzae* in bacterial exacerbations of chronic bronchitis.

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
| 0501021M0AAAAAA | Cefradine Capsules 250 mg | Capsule | Not stated in the data compiled |

The record carries a BNF-style code (section 5.1.2, cephalosporins) rather than a standard PL number. The dosage form, manufacturer and approved indication text are not available.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): *Clostridium difficile* colitis and perinatal necrotizing enterocolitis.
- **Drug Interactions** (13 moderate-level interactions identified):
  - Aminoglycosides: amikacin (including liposomal), gentamicin, kanamycin, neomycin, streptomycin
  - Anticoagulant: warfarin
  - Other antibacterial: chloramphenicol
  - Gastrointestinal agents: balsalazide, picosulfuric acid
  - Hormonal: ethinylestradiol
  - Immunosuppressant: mycophenolic acid
  - Antineoplastic: pemetrexed

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hyperamylasemia rests on model score alone (L5). There are no trials or publications, and no plausible mechanism linking a cell wall-targeting antibiotic to a biochemical abnormality. Of the top-ten predictions, only bronchitis reaches L4, and it largely extends existing indications rather than representing true repurposing.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic rationale for hyperamylasemia
- Any preclinical, observational or clinical evidence supporting the prediction
- Full UK authorisation details (PL number, dosage form, approved indications) and SmPC warnings and contraindications
- If a repurposing direction is pursued, consider bronchitis or xanthogranulomatous pyelonephritis, which are more biologically plausible, supported by culture-directed antibiotic use and current guidelines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

