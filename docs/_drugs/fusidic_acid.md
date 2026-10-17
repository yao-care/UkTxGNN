---
layout: default
title: Fusidic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 309
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Fusidic Acid: predicted new indication Exposure keratitis (evidence level L4). Approved use: Bacterial infections"
monitor_inn: "Fusidic acid"
predicted_indications: ["otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "parasitic eyelid infestation"]
---

# Fusidic Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Fusidic Acid: From Bacterial Infections to Exposure Keratitis

## One-Sentence Summary

Fusidic acid is an antibiotic that inhibits bacterial protein synthesis, originally used for bacterial infections (particularly Gram-positive skin and soft tissue infections).
The TxGNN model predicts it may be useful for **exposure keratitis**,
but there are currently **no registered clinical trials** and only **1 indirect publication** (a case series), so the evidence is very limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (knowledge-graph indications include urinary tract infection, bronchitis, acne, folliculitis and bacterial pneumonia); no indication text is available from the UK authorisation record |
| Predicted New Indication | Exposure keratitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fusidic acid blocks bacterial protein synthesis by inhibiting elongation factor G (EF-G). It is particularly active against Gram-positive bacteria such as *Staphylococcus aureus*. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description draws on the rationale recorded for the prediction.

Exposure keratitis is a disorder of the corneal surface, usually caused by incomplete eyelid closure and drying, and the damaged cornea can become secondarily infected. Any benefit from fusidic acid would be limited to treating or preventing bacterial superinfection. It would not address the underlying disease. The UK product recorded is an ocular formulation (fusidic acid viscous eye drops 1%), which fits the ocular route, although route compatibility has not yet been assessed.

The only linked publication is a case series of ocular *Tsukamurella* infections. It is indirect and does not evaluate fusidic acid for this condition. The high model score therefore reflects graph association rather than direct clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/) | 2019 | Case series | Cornea | Largest case series of *Tsukamurella* ophthalmic infections, covering clinical spectrum, risk factors, treatment and outcome. Indirect evidence; fusidic acid was not evaluated for exposure keratitis |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1103010H0AAAAAA | Fusidic Acid Viscous Eye Drops 1% | Eye drops (viscous) | Not stated in the available record |

The identifier shown is the code held in the compiled record and is not in the standard PL number format. Please verify it against the MHRA register.

---

## Safety Considerations

The following are drawn from knowledge-graph contraindication associations, not from product label text, so they should be treated as signals to verify rather than confirmed contraindications. Conditions flagged include:

- **Eye-related:** herpes simplex virus keratitis, open-angle glaucoma, glaucoma, ocular hypertension, eye infectious disease, conjunctivitis
- **Liver, kidney and gallbladder:** liver failure, liver disease, kidney disease, gallbladder disease
- **Gastrointestinal:** *Clostridium difficile* colitis, colitis, perinatal necrotizing enterocolitis
- **Metabolic and electrolyte:** diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease
- **Cardiac:** atrial fibrillation, atrioventricular block, Adams-Stokes syndrome, Wolff-Parkinson-White syndrome
- **Neuromuscular and respiratory:** myasthenia gravis, neuromuscular junction disease, respiratory failure
- **Other:** pyoureter, central nervous system origin vertigo, oesophageal dyskinesia

Many of these associations look unrelated to a topical ocular product and probably reflect systemic exposure or class-level links in the graph. Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by model score and mechanistic plausibility. There are no clinical trials, the single publication is an indirect case series, and any benefit would be limited to managing secondary bacterial infection. This overlaps with existing antibiotic practice and does not treat the underlying condition.

**To proceed, the following is needed:**
- Product label information (indications, warnings, contraindications) for the UK ocular formulation
- Detailed mechanism of action data
- Evidence of fusidic acid use in infected exposure keratitis, such as microbiological susceptibility data for corneal isolates and comparative clinical studies against current topical antibiotics
- Route and formulation compatibility assessment
- Review of the knowledge-graph contraindication signals for relevance to topical ocular use

**Other predictions reviewed:** The remaining nine predictions (for example otitis externa, postinfectious vasculitis and Chagas cardiomyopathy) also have no clinical trial support. Otitis externa has plausible Gram-positive coverage, but its literature is mostly veterinary or bacteriological surveys. It is best treated as a research question rather than a candidate for progression.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

