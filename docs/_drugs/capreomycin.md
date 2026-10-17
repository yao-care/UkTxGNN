---
layout: default
title: Capreomycin
parent: Model Prediction Only (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Capreomycin: predicted new indication Gout (evidence level L5). Approved use: Pulmonary tuberculosis"
monitor_inn: "Capreomycin"
predicted_indications: ["gout", "rheumatoid arthritis", "osteoarthritis", "osteoarthritis susceptibility", "sclerosing cholangitis", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "meningococcal infection", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type"]
---

# Capreomycin
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

# Capreomycin: From Pulmonary Tuberculosis to Gout

## One-Sentence Summary

Capreomycin is an injectable antibiotic originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **gout**, but this rests on the model score alone, with **0 clinical trials** and **0 publications** supporting the prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis (the licence record has no approved indication text, so this is taken from the TxGNN knowledge graph) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, capreomycin is a cyclic peptide antibiotic used against mycobacteria, and its efficacy in pulmonary tuberculosis is established. It is generally understood to act on bacterial protein synthesis.

No convincing mechanistic link to gout has been identified. Gout is driven by urate crystal-induced inflammation, which has no obvious connection to an antimycobacterial agent. The high TxGNN score (99.91%) reflects a model-based association only and is not supported by any trial or publication.

Other predicted indications show the same pattern. Rheumatoid arthritis (99.85%), osteoarthritis (99.74%), sclerosing cholangitis (99.65%) and meningococcal infection (99.57%) all have no trials or literature behind them. Meningococcal infection is the only one with an antibacterial rationale. However, capreomycin has no data showing activity against *Neisseria meningitidis*, its CNS penetration is poor, and effective established alternatives exist. Several other top predictions are rare congenital skeletal or developmental conditions, for which no pharmacological rationale is apparent.

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
| 0501090C0AAAAAA | Capreomycin Inj 1g Vl | Injection (vial) | Not stated in the compiled data |

The identifier above is a drug-code style reference, not a standard MHRA "PL" number. The authorisation details should be verified against the MHRA records and the BNF.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (not label text): kidney disease, pyoureter, liver disease, gallbladder disease, potassium deficiency, hearing loss disorder, and X-linked mixed deafness with perilymphatic gusher. These are consistent with the known risks of nephrotoxicity, ototoxicity and electrolyte disturbance, which is particularly relevant to a gout population where renal urate handling matters.
- **Drug Interactions**: 58 interactions were identified. Two are rated **Major**:
  - **Kanamycin**
  - **Neomycin**

  Most others are rated Moderate, including amphotericin B (including lipid, cholesteryl sulfate and liposomal formulations), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone), proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, rabeprazole, dexlansoprazole), aminosalicylates (mesalazine, balsalazide, olsalazine) and exenatide.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based on the model score alone (Evidence Level L5), with no trials, no literature and no plausible mechanistic link between an antimycobacterial injectable and gout. Its nephrotoxicity, ototoxicity, electrolyte effects and parenteral-only administration are also unfavourable for a chronic condition.

**To proceed, the following is needed:**
- Mechanism of action data and any evidence linking capreomycin to urate or inflammatory pathways
- Preclinical or mechanistic studies supporting activity in gout
- Verified MHRA authorisation details, including the approved indication and dosage form
- SmPC warnings and contraindications to complete the safety assessment
- A risk-benefit assessment against established gout treatments, given the renal and auditory toxicity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

