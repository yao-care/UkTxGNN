---
layout: default
title: Cefuroxime
parent: Model Prediction Only (L5)
nav_order: 144
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cefuroxime: predicted new indication Hyperamylasaemia (evidence level L5). Approved use: Infectious otitis media, bacterial pneumonia, bacterial meningitis…"
---

# Cefuroxime
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

# Cefuroxime: From Bacterial Infections to Urinary Tract Infection

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic, originally used for infections such as otitis media, pneumonia, meningitis, gonorrhoea and Lyme disease.
The TxGNN model's top-ranked prediction is **hyperamylasaemia**, but this has no supporting evidence; the best-supported candidate in the list is **urinary tract infection (UTI)**, with **5 clinical trials** and **20 publications** retrieved. These are mostly indirect, and UTI is a close extension of cefuroxime's existing anti-infective use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Infectious otitis media, bacterial pneumonia, bacterial meningitis, gonorrhoea, Lyme disease and other bacterial infections (the UK licence entries contain no indication text) |
| Predicted New Indication | Hyperamylasaemia (rank 1); UTI is the best-supported candidate and is assessed below |
| TxGNN Prediction Score | 99.76% (hyperamylasaemia); 99.62% (UTI) |
| Evidence Level | L5 for hyperamylasaemia; L3 for UTI |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 2 |
| Recommended Decision | Hold (hyperamylasaemia); UTI is a research question only |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Cefuroxime is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis. Its efficacy in several bacterial infections is established, and it has activity against common respiratory pathogens and many Enterobacterales.

**Hyperamylasaemia (rank 1):** There is no plausible mechanistic link. Cefuroxime has no known effect on serum amylase, and no trials or literature support the prediction. The high score appears to be an artefact of the knowledge-graph model. Other top-ten predictions (polyclonal hyperviscosity syndrome, congenital analbuminaemia, blood group incompatibility, premalignant haematological disease, monoclonal gammopathy, and haematological disease associated with acquired peripheral neuropathy) are likewise mechanistically unsupported.

**Urinary tract infection:** Mechanistic plausibility is strong. Cefuroxime is active against common uropathogens such as *E. coli* and is excreted in urine. The available trials concern prophylaxis, stewardship or the consequences of inappropriate therapy, so they do not give direct randomised efficacy evidence. Local resistance patterns also limit empirical use.

**Other predictions with plausible biology:** Peptostreptococcus infection (indirect 1981 in-vitro data only; anaerobic coverage is variable) and suppurative otitis media (largely overlaps with the existing otitis media indication; evidence is mostly reviews and susceptibility surveys).

---

## Clinical Trial Evidence

The table covers the UTI prediction, the only candidate with registered trials.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04616352](https://clinicaltrials.gov/study/NCT04616352) | N/A | Completed | 973 | Effect of inappropriate cefuroxime therapy in adults hospitalised with pyelonephritis; observational design, assesses outcomes of inappropriate therapy rather than efficacy |
| [NCT01507974](https://clinicaltrials.gov/study/NCT01507974) | N/A | Completed | 220 | Preventive antibiotics in pregnant women with recurrent UTI; cefuroxime-specific contribution unclear |
| [NCT05577273](https://clinicaltrials.gov/study/NCT05577273) | N/A | Unknown | 1000 | Antibiotic prophylaxis at urinary catheter removal; role of cefuroxime unclear |
| [NCT02789579](https://clinicaltrials.gov/study/NCT02789579) | Early Phase 1 | Unknown | 150 | One-week antimicrobial regimen to prevent UTI before minimally invasive upper tract lithotomy; weak evidence |
| [NCT02009098](https://clinicaltrials.gov/study/NCT02009098) | Phase 4 | Withdrawn | 0 | Antibiotic prophylaxis for postpartum infection after caesarean section; no data, not UTI-specific |

No clinical trials are registered for the other predicted indications.

---

## Literature Evidence

The table covers the UTI and suppurative otitis media predictions (most relevant publications).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41693075](https://pubmed.ncbi.nlm.nih.gov/41693075/) | 2026 | Systematic review | Pharmacotherapy | Oral β-lactams versus trimethoprim/sulfamethoxazole and fluoroquinolones in complicated UTI: effectiveness, safety and pharmacokinetics |
| [38215770](https://pubmed.ncbi.nlm.nih.gov/38215770/) | 2024 | Randomised trial | Lancet Infect Dis | De-escalation from antipseudomonal β-lactams in Enterobacterales bacteraemia (not cefuroxime-specific) |
| [8799689](https://pubmed.ncbi.nlm.nih.gov/8799689/) | 1996 | Review | Drugs | Cefuroxime axetil: antibacterial activity, pharmacokinetics and therapeutic efficacy |
| [18611587](https://pubmed.ncbi.nlm.nih.gov/18611587/) | 1994 | Review | Int J Antimicrob Agents | Cefuroxime axetil: high sensitivity of common respiratory pathogens |
| [6349019](https://pubmed.ncbi.nlm.nih.gov/6349019/) | 1983 | Review | Ther Drug Monit | Cefuroxime antimicrobial activity, pharmacology, toxicity and clinical efficacy |
| [6344037](https://pubmed.ncbi.nlm.nih.gov/6344037/) | 1983 | Review | Pharmacotherapy | Broad Gram-positive and Gram-negative activity; Pseudomonas and *B. fragilis* resistant |
| [35733866](https://pubmed.ncbi.nlm.nih.gov/35733866/) | 2022 | Cohort study | Front Med | Carbapenem prophylaxis and cephalosporin-resistant Enterobacterales UTI after kidney transplant |
| [36496392](https://pubmed.ncbi.nlm.nih.gov/36496392/) | 2022 | Surveillance | Antimicrob Resist Infect Control | 10-year antibiotic resistance trends in uropathogens, Bangladesh |
| [7142073](https://pubmed.ncbi.nlm.nih.gov/7142073/) | 1982 | Pharmacokinetic study | J Antimicrob Chemother | Cefuroxime diffusion into middle ear effusions in chronic purulent otitis media |
| [19802974](https://pubmed.ncbi.nlm.nih.gov/19802974/) | 1981 | In vitro study | J Antimicrob Chemother | Cefuroxime inhibited 79% of anaerobic isolates at 16 mg/l (Peptostreptococcus data indirect) |

The remaining retrieved papers are mostly resistance surveillance studies and general reviews. The single paper retrieved for blood group incompatibility concerns salmonella resistance in Kenya and is unrelated.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501021K0BBABAB | Zinnat Tab 250mg | Tablet | Not specified in the data compiled |
| 0501021K0AAAAAA | Cefuroxime Axetil Tab 125mg | Tablet | Not specified in the data compiled |

Both are valid single-ingredient products. The identifiers shown are the reference numbers in the compiled data, not PL numbers. Please check the MHRA records and the BNF for licensed indications.

---

## Safety Considerations

- **Disease associations of concern (knowledge graph, not label text)**: kidney disease, pyoureter, liver disease, gallbladder disease, blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotising enterocolitis, congenital prothrombin deficiency.
- **Drug Interactions**: 143 interactions were identified; the 20 listed are all moderate. Main groups:
  - Acid-suppressing agents: famotidine, ranitidine, cimetidine, nizatidine, and the proton pump inhibitors omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole and rabeprazole
  - Antacids: aluminium hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide
  - Aminoglycosides: kanamycin, neomycin
  - Balsalazide

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, hyperamylasaemia, and for all non-infectious predictions). UTI may be pursued only as a research question.

**Rationale:**
- The highest-scoring predictions have no mechanistic basis and no supporting studies, so they appear to be model artefacts. UTI and otitis media are biologically plausible but are extensions of existing anti-infective use, supported only by indirect evidence (L3 and L4 respectively).

**To proceed, the following is needed:**
- Review of the licensed indications in the MHRA SmPC and BNF, as the compiled data holds no indication text
- Mechanism of action data
- Warnings and contraindications from the SmPC (a blocking gap for safety screening)
- For UTI: direct randomised comparative evidence for cefuroxime, plus UK local resistance data to judge empirical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

