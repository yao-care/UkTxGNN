---
layout: default
title: Daptomycin
parent: Moderate Evidence (L3-L4)
nav_order: 207
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Daptomycin: predicted new indication Osteoarthritis (evidence level L4). Approved use: Not recorded in the data compiled for this report"
monitor_inn: "Daptomycin"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "osteoarthritis susceptibility", "gout", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome"]
---

# Daptomycin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Daptomycin: From Gram-Positive Infections to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Daptomycin is an intravenous cyclic lipopeptide antibiotic. The data compiled for this report do not record an approved indication text for the UK authorisation.
The TxGNN model predicts it may be effective for **osteoarthritis** (score 99.86%), but there are **no registered clinical trials**, and the **10 publications** retrieved mostly concern bone and joint *infections* rather than osteoarthritis itself. This is a model prediction with weak supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data compiled for this report |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Daptomycin is generally known as a cyclic lipopeptide antibiotic active against Gram-positive bacteria, but its original indication text was not captured for this report.

For osteoarthritis, the mechanistic case is weak. The retrieved literature describes daptomycin treating Gram-positive osteoarticular and prosthetic joint infections (for example *Staphylococcus*), which is antibacterial use and not treatment of degenerative osteoarthritis. The high TxGNN score probably reflects proximity to joint and bone terms in the knowledge graph rather than a genuine disease-modifying effect.

**Other predictions of note:**
- **Rheumatoid arthritis** (score 99.84%, evidence level L4): a 2025 preclinical study (PMID 39571268) reports that daptomycin reduced collagen-induced arthritis in mice by suppressing inflammatory cytokines and NF-κB signalling. A follow-up study of daptomycin-derived lipopeptides (PMID 40923559) supports this idea. No human data exist, so this is the more scientifically interesting research question, though still preclinical.
- **Osteoarthritis susceptibility, gout and rare skeletal dysplasias** (pseudoachondroplasia, Hunter-Thompson acromesomelic dysplasia, brachyolmia and others) have no credible therapeutic link. The gout report describes daptomycin-induced rhabdomyolysis followed by gouty arthritis, which is an adverse event signal and not evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Publications retrieved for osteoarthritis (up to 10 shown). Most address joint infection and not osteoarthritis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohort | International Orthopaedics | Safety and efficacy of high-dose daptomycin plus rifampicin in Gram-positive osteoarticular infections |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohort | J Antimicrob Chemother | Daptomycin versus standard therapy for osteoarticular infections with *S. aureus* bacteraemia |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Cohort | J Antimicrob Chemother | Clinical experience in knee and hip periprosthetic joint infections |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) for complicated bone, joint and implant-associated Gram-positive infections |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Cohort | Medicina Clínica | EU-CORE registry data on routine daptomycin use in Spain |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Survey/Review | Int J Antimicrob Agents | Survey of current prosthetic joint infection management practices |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Cohort | Surgical Infections | Ten-year microbiological profile of staphylococci in osteoarticular infections |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro | J Antibiotics | Antibiotic susceptibility of staphylococci from prosthetic joint infections |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case report | Case Reports in Orthopedics | Chronic *Corynebacterium striatum* septic arthritis in a patient referred for knee arthroplasty |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Case report | ASM Case Reports | Septic arthritis due to *Corynebacterium propinquum* in a native joint |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501070Y0AAABAB (BNF-style product code; not a PL number) | Daptomycin I/V Infusion 500 mg vial (dry powder) | Powder for intravenous infusion | Not recorded in the compiled data |

One single-ingredient authorisation is recorded as valid; none are cancelled.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (these come from the TxGNN knowledge graph, not from product label text): myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, diarrhoeal disease, *Clostridium difficile* colitis, perinatal necrotising enterocolitis, eosinophilic pneumonia, pulmonary eosinophilia, peripheral neuropathy and peripheral nervous system disease. The muscle-related signal is consistent with the rhabdomyolysis case report retrieved for gout.
- **Drug Interactions** (12 recorded):
  - *Moderate:* picosulfuric acid, rosuvastatin, simvastatin, iobenguane (I-131), ibuprofen, diclofenac, celecoxib, ethinylestradiol, ciclosporin, mycophenolic acid
  - *Minor:* dicoumarol, warfarin
  - Concurrent statin use deserves particular attention given the muscle toxicity signal.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis prediction rests on model output alone, with no trials and no literature showing benefit in degenerative osteoarthritis; the retrieved papers concern infection. A knowledge-graph muscle toxicity signal adds a safety concern for a chronic, non-infectious condition.

**To proceed, the following is needed:**
- Mechanistic and preclinical evidence of benefit in osteoarthritis specifically (none currently exists)
- Confirmation of the approved indication, dosage form and SmPC safety data for the UK product
- Mechanism of action data
- If pursuing a research question, rheumatoid arthritis is the more plausible direction: first replicate the 2025 collagen-induced arthritis findings and assess whether intravenous antibiotic dosing and muscle toxicity are acceptable for a chronic inflammatory condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

