---
layout: default
title: Cefadroxil
parent: Model Prediction Only (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cefadroxil: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Urinary tract infection, tonsillitis, streptococcal infection…"
monitor_inn: "Cefadroxil"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "Ureaplasma urethritis", "gonococcal urethritis", "septicemic plague"]
---

# Cefadroxil
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

# Cefadroxil: From Urinary Tract Infection to Hyperamylasemia

## One-Sentence Summary

Cefadroxil is a first-generation oral cephalosporin antibiotic, originally used for urinary tract infection, tonsillitis and staphylococcal and streptococcal infections.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but there are **0 clinical trials** and **0 publications** supporting this prediction, and no plausible mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, tonsillitis, streptococcal infection, staphylococcal infection (from the knowledge graph; no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cefadroxil is a first-generation cephalosporin that inhibits bacterial cell wall synthesis. Its efficacy in bacterial infections of the urinary tract, throat and skin is established.

Hyperamylasemia, however, is a laboratory finding of raised serum amylase. It has pancreatic, salivary or renal causes, and is not a bacterial process. No plausible mechanistic link to an antibacterial has been identified. The high TxGNN score is a graph-based prediction only, and it should be treated as a hypothesis-generating signal rather than a reason to pursue the indication.

Other top-ranked predictions (for example polyclonal hyperviscosity syndrome, congenital analbuminemia and monoclonal gammopathy) show the same pattern, with no mechanistic rationale. Among the infection-related predictions, gonococcal urethritis is the only one with partial plausibility, because cephalosporins act on *Neisseria gonorrhoeae*. Even there, current guidelines rely on parenteral ceftriaxone, and oral first-generation agents have limited gonococcal activity. Ureaplasma urethritis is biologically implausible, because Ureaplasma lacks a cell wall.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature has been found for hyperamylasemia. The only literature item among the top ten predictions concerns gonococcal urethritis and is shown below for context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2673664](https://pubmed.ncbi.nlm.nih.gov/2673664/) | 1989 | Cohort | Current Medical Research and Opinion | Reports on 1,000 patients treated with cefetamet pivoxil, with cefadroxil and cefaclor among the comparators in 505 patients. Single doses of cefetamet pivoxil were effective in gonorrhoea. This concerns a different drug and gives only indirect, class-level support. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501021B0AAAAAA | Cefadroxil capsules 500 mg | Capsule (inferred from product name) | Not available in the data compiled for this report |

The BNF classification code embedded in the identifier (05.1.2, cephalosporins) is consistent with the product's drug class. The identifier is not in the usual UK PL number format, so the authorisation details should be verified against the MHRA register.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: Clostridium difficile colitis, perinatal necrotizing enterocolitis, and impaired renal function.
- **Drug Interactions**: 51 potential interactions were identified. Two are classed as Moderate: balsalazide and picosulfuric acid. The others, including aspirin, pantoprazole, doxycycline, morphine, metformin, omeprazole, prednisolone and metronidazole, have no severity grading.

Please refer to the SmPC and BNF for authoritative warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score, with no clinical trials, no literature and no plausible mechanism for hyperamylasemia. Evidence level is L5.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking an antibacterial to the predicted condition, or a shift of focus to infection-related predictions such as gonococcal urethritis, assessed against current resistance data and guidelines
- Mechanism of action data for cefadroxil
- Approved indication text and dosage form for the UK authorisation, verified against the MHRA register
- SmPC and BNF warnings and contraindications to support a formal safety screen
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

