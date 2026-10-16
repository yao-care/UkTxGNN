---
layout: default
title: Fosfomycin
parent: Moderate Evidence (L3-L4)
nav_order: 306
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-15
description: "Fosfomycin: predicted new indication Gonococcal urethritis (evidence level L3). Approved use: Urinary tract infection"
monitor_inn: "fosfomycin"
predicted_indications: ["gonococcal urethritis", "Ureaplasma urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "pyelitis"]
---

# Fosfomycin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Fosfomycin: From Urinary Tract Infection to Gonococcal Urethritis

## One-Sentence Summary

> Fosfomycin (as fosfomycin trometamol) was originally used to treat urinary tract infection.
> The TxGNN model predicts it may be effective for **gonococcal urethritis**,
> with **no registered clinical trials** and **6 publications**, including **one open randomised controlled trial (2016)**, currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection |
| Predicted New Indication | Gonococcal urethritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fosfomycin inhibits MurA (UDP-N-acetylglucosamine enolpyruvyl transferase). This blocks the first committed step of bacterial peptidoglycan (cell wall) synthesis and gives a bactericidal effect. Its efficacy in urinary tract infection is established, and it reaches high concentrations in urine.

*Neisseria gonorrhoeae* is a cell-walled bacterium that infects the urogenital tract, so the mechanism is biologically plausible. The older and newer clinical reports suggest activity:
- A 1977 uncontrolled series reported bacteriological and clinical cure in most men treated with intramuscular fosfomycin.
- A 2016 open randomised trial studied oral fosfomycin trometamol 3 g for uncomplicated gonococcal urethritis in men.

There are important limits:
- Resistance is a concern.
- Guideline-preferred agents such as ceftriaxone remain the standard of care.
- The 1977 data used an intramuscular formulation, not the oral trometamol sachet marketed in the UK.
- The design, comparator and efficacy results of the 2016 trial could not be verified from the data compiled for this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27064136](https://pubmed.ncbi.nlm.nih.gov/27064136/) | 2016 | RCT (open-label) | Clin Microbiol Infect | 152 men with suspected uncomplicated gonococcal urethritis enrolled, 126 completed. The fosfomycin trometamol arm (n=60) received 3 g orally on days 1, 3 and 5. Efficacy results were not available in the data compiled. |
| [832528](https://pubmed.ncbi.nlm.nih.gov/832528/) | 1977 | Clinical study (uncontrolled) | Chemotherapy | 70 patients with acute or subacute gonococcal urethritis treated with intramuscular fosfomycin. 11/12 (92%) were cured with 4 g in divided doses, and 37/43 (86%) with a single 4 g dose. |
| [832523](https://pubmed.ncbi.nlm.nih.gov/832523/) | 1977 | Bacteriological clinical study | Chemotherapy | Spanish hospital study of 959 patients with various infections, including gonococcal urethritis, assessing fosfomycin's broad-spectrum behaviour. |
| [19593988](https://pubmed.ncbi.nlm.nih.gov/19593988/) | 2009 | Review | Zhonghua Nan Ke Xue | Diagnosis and treatment of male genitourinary infection with non-gonococcal *Neisseria*. Indirect relevance. |
| [35820778](https://pubmed.ncbi.nlm.nih.gov/35820778/) | 2023 | Secondary analysis of RCT | Sex Transm Infect | Spontaneous clearance of asymptomatic gonorrhoea in the NABOGO trial. Not fosfomycin-specific. |
| [17878816](https://pubmed.ncbi.nlm.nih.gov/17878816/) | 2007 | Case report | J Fr Ophtalmol | Gonococcal conjunctivitis with corneal perforation in an adult. The isolate was resistant to penicillins, tetracyclines and fluoroquinolones, and the patient was treated with high-dose parenteral therapy. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501130D0AAAAAA | Fosfomycin trometamol 3 g sachet | Sachet | Not recorded in the data compiled; refer to the SmPC |

This is the only authorisation (single-ingredient, valid). The identifier appears in the format of a BNF code rather than a PL number, so please check the product's PL number against the MHRA register. Dosage form and approved indication text were not recorded.

---

## Safety Considerations

- **Contraindication-related conditions (from drug–disease relationships in the TxGNN knowledge graph, not label text):** kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotising enterocolitis. These need confirmation against the SmPC.
- **Drug Interactions (3 identified):**
  - Balsalazide: Moderate
  - Picosulfuric acid: Moderate
  - Metoclopramide: Minor

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and there is one open RCT plus older uncontrolled data. However, there are no registered trials, the RCT results could not be verified, and resistance concerns and guideline-preferred agents such as ceftriaxone limit the case for repurposing. Evidence is L3, and the model's own assessment was a research question rather than a development candidate.

**To proceed, the following is needed:**
- Full text of the 2016 RCT (comparator, cure rates, and per-site microbiological outcomes)
- Current UK susceptibility and resistance data for *N. gonorrhoeae* against fosfomycin
- Comparison with current UK guideline-recommended regimens
- Confirmation of the approved indication, dosage form and PL number from the SmPC and MHRA register
- Detailed mechanism-of-action data from a primary source

**Note:** Within the same prediction list, **pyelitis** (upper urinary tract infection) has much stronger support. It has a Phase 2/3 RCT (ZEUS, IV fosfomycin versus piperacillin-tazobactam) and an evidence level of L1, and it was assessed as Proceed with Guardrails. It is largely an extension of the existing UTI indication, and intravenous fosfomycin is not approved in all jurisdictions. It may merit a separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

