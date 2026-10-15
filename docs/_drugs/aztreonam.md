---
layout: default
title: Aztreonam
parent: Model Prediction Only (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Aztreonam
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

# Aztreonam: From Bacterial Infections (Urinary Tract Infection, Pseudomonas Infection) to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Aztreonam is a monobactam antibiotic, originally used for gram-negative bacterial infections such as urinary tract infection, Pseudomonas aeruginosa infection and peritonitis.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** support this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, Pseudomonas aeruginosa infection, peritonitis and other gram-negative infections (the UK authorisation record has no indication text, so this comes from the drug's known indications) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Aztreonam is known as a monobactam that inhibits bacterial cell wall synthesis by binding penicillin-binding protein 3 (PBP3), which makes it active against gram-negative bacteria.

That mechanism does not plausibly connect to polyclonal hyperviscosity syndrome. This condition involves raised serum viscosity from excess immunoglobulins, and aztreonam has no known effect on serum viscosity or immunoglobulin dynamics. The high TxGNN score most likely reflects relationships in the underlying knowledge graph rather than real biology. In this assessment, the prediction is not supported mechanistically.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501023A0AAAFAF | Aztreonam powder and solvent for nebuliser solution, 75 mg vial with device | Powder and solvent for nebuliser solution (inhaled) | Not specified in the compiled record |

The identifier shown is not in standard PL number format and appears to be a BNF-style product code. The authorisation should be checked against the MHRA register. The only listed product is an inhaled nebuliser formulation, so route compatibility with any systemic indication has not been assessed.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are graph-derived associations, not label text): kidney disease, pyoureter, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotising enterocolitis and bronchial disease.
- **Drug Interactions**: 27 potential interactions were identified. Those graded **Moderate** are picosulfuric acid, dicoumarol and warfarin, so anticoagulant co-prescription needs particular care. Other listed interacting drugs have no severity grade. They include vancomycin, amikacin, amphotericin B, tacrolimus, heparin, metronidazole, fluconazole, aciclovir, morphine, hydrocortisone, dexamethasone, ondansetron, salbutamol, acetylsalicylic acid and the proton pump inhibitors omeprazole, pantoprazole and lansoprazole.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials or publications and no plausible mechanism linking an antibacterial to a disorder of serum viscosity. It should not be pursued further on current information.

Other predictions in the same output look more promising, though they are outside this report's focus. Gonococcal urethritis has L3 evidence, including a 2020 single-arm open-label trial of 2 g intramuscular aztreonam and several older single-dose studies. It is better treated as a separate research question, taking into account reported gonococcal resistance to aztreonam and current ceftriaxone-based standard care.

**To proceed, the following is needed:**
- Any mechanistic or clinical rationale linking aztreonam to hyperviscosity syndrome, which seems unlikely to exist
- Detailed mechanism of action data (MOA) from DrugBank
- SmPC warnings and contraindications for the authorised product, to complete safety screening
- Confirmation of the MHRA authorisation number, dosage form and approved indication
- Assessment of whether a separate evaluation of gonococcal urethritis is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

