---
layout: default
title: Tazobactam
parent: High Evidence (L1-L2)
nav_order: 596
evidence_level: L1
indication_count: 2
last_modified_at: 2026-10-15
description: "Tazobactam: predicted new indication Pneumonia (evidence level L1). Approved use: Bacterial pneumonia, peritonitis, appendicitis…"
monitor_inn: "tazobactam"
predicted_indications: ["urinary tract infection (disease)"]
---

# Tazobactam
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **2** 
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

# Tazobactam: From Bacterial Pneumonia to Pneumonia (Hospital-Acquired and Ventilator-Associated)

## One-Sentence Summary

> Tazobactam is a beta-lactamase inhibitor that is always given with a partner antibiotic (for example piperacillin), and is originally used for bacterial pneumonia, peritonitis, appendicitis and staphylococcal infections.
> The TxGNN model predicts it may be effective for **pneumonia** (and, as a second prediction, **urinary tract infection**),
> with **20 clinical trials** and **20 publications** compiled for the pneumonia prediction. This is better seen as an extension of an existing use than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, peritonitis, appendicitis, staphylococcal infection (the UK licence records contain no approved indication text) |
| Predicted New Indication | Pneumonia |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L1 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known information, tazobactam is a beta-lactamase inhibitor. It has no meaningful antibacterial activity of its own and works by protecting its partner beta-lactam (piperacillin or ceftolozane) from enzymatic breakdown. This extends activity to beta-lactamase-producing Gram-negative and other pathogens.

Its efficacy in bacterial pneumonia is already established, and "pneumonia" is very close to that existing indication. The prediction therefore mostly covers settings such as hospital-acquired and ventilator-associated pneumonia and infections caused by multidrug-resistant Gram-negative organisms. Efficacy depends on the partner antibiotic.

The second prediction, **urinary tract infection** (score 99.12%), rests on the same mechanism. Tazobactam protects the partner drug against ESBL-producing Enterobacterales, which are common causes of complicated UTI and pyelonephritis. Caveat: the evidence for ESBL-producing organisms is mixed, and carbapenems are often preferred.

---

## Clinical Trial Evidence

Most trials below involve tazobactam either in a combination under test (ceftolozane/tazobactam) or as the piperacillin/tazobactam comparator. They are therefore indirect evidence. Selected trials for pneumonia (up to 10):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | Completed | 537 | Imipenem/relebactam vs piperacillin/tazobactam in HABP/VABP (primary outcome all-cause mortality); piperacillin/tazobactam is the comparator |
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | Completed | 726 | Ceftolozane/tazobactam vs meropenem in ventilated nosocomial pneumonia (non-inferiority on Day 28 mortality) |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | Completed | 460 | Levofloxacin vs piperacillin/tazobactam in mild to moderate hospital-acquired pneumonia (non-inferiority) |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Phase 1 | Completed | 41 | Safety, tolerability and PK of ceftolozane/tazobactam in children with nosocomial pneumonia |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | N/A | Recruiting | 42 | Model-guided vs empirical dosing of piperacillin-tazobactam in elderly pneumonia patients |
| [NCT06977347](https://clinicaltrials.gov/study/NCT06977347) | N/A | Not yet recruiting | 100 | Piperacillin/tazobactam alone vs plus a fluoroquinolone in severe community-acquired pneumonia (South Korea) |
| [NCT04986254](https://clinicaltrials.gov/study/NCT04986254) | N/A | Completed | 179 | Individualised antibiotic dosing in ICU pneumonia, including piperacillin/tazobactam |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Phase 3 | Terminated | 4 | Ceftolozane/tazobactam vs piperacillin/tazobactam in VAP; too few participants for usable results |
| [NCT03006679](https://clinicaltrials.gov/study/NCT03006679) | Phase 3 | Withdrawn | 0 | Meropenem-vaborbactam vs piperacillin/tazobactam in HABP/VABP; never enrolled |
| [NCT04673175](https://clinicaltrials.gov/study/NCT04673175) | Phase 4 | Terminated | 17 | Ceftolozane-tazobactam pilot for Pseudomonas infections in haematological malignancy; limited evidence |

For the UTI prediction, the key trials are [NCT03687255](https://clinicaltrials.gov/study/NCT03687255) (Phase 3, completed, n=1043, cefepime-enmetazobactam vs piperacillin/tazobactam in complicated UTI) and [NCT03230838](https://clinicaltrials.gov/study/NCT03230838) (Phase 2, completed, n=134, ceftolozane/tazobactam vs meropenem in paediatric complicated UTI). [NCT03891433](https://clinicaltrials.gov/study/NCT03891433) (piperacillin/tazobactam vs carbapenems in ESBL UTI) is suspended.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP: ceftolozane-tazobactam vs meropenem in Gram-negative nosocomial pneumonia (phase 3, non-inferiority) |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Phase III non-inferiority trial of imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Systematic review / network meta-analysis | Clin Microbiol Infect | Empiric antibiotic regimens for non-ventilator-associated HAP |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Systematic review | Int J Antimicrob Agents | PK/PD of novel beta-lactam/beta-lactamase inhibitor combinations in carbapenem-resistant Gram-negative pneumonia |
| [36543346](https://pubmed.ncbi.nlm.nih.gov/36543346/) | 2022 | Review | Eur Respir Rev | Overview of newly approved antibiotics for Gram-negative pneumonia |
| [35088403](https://pubmed.ncbi.nlm.nih.gov/35088403/) | 2022 | Review | Semin Respir Crit Care Med | New antibiotics for HAP and VAP |
| [32600375](https://pubmed.ncbi.nlm.nih.gov/32600375/) | 2020 | Review | Crit Care | Update on treatment of nosocomial pneumonia in the ICU |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Review/Guideline | Int J Antimicrob Agents | Italian and French practical approach to multidrug-resistant Gram-negative infections |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Cohort | Clin Infect Dis | Resistance emergence was lower with ceftolozane-tazobactam than ceftazidime-avibactam in MDR *P. aeruginosa* bacteraemia or pneumonia (10% vs 40%) |

For UTI, the main RCTs are [36194218](https://pubmed.ncbi.nlm.nih.gov/36194218/) (JAMA 2022, cefepime/enmetazobactam vs piperacillin/tazobactam), [29486041](https://pubmed.ncbi.nlm.nih.gov/29486041/) (JAMA 2018, TANGO I) and [30861061](https://pubmed.ncbi.nlm.nih.gov/30861061/) (Clin Infect Dis 2019, ZEUS, fosfomycin vs piperacillin-tazobactam).

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501014S0BBABAB | Tazocin Inj 4.5g Vl | Not recorded | Not recorded in the data compiled |
| 0501014S0AAABAB | Piperacillin/Tazobactam Inj 4g/0.5g Vl | Not recorded | Not recorded in the data compiled |

Both authorisations are single-ingredient-listed, valid products. Please check the current SmPC and BNF for the licensed indications.

---

## Safety Considerations

The data compiled for this report holds no label-based warnings, contraindications or interaction data. The knowledge graph links tazobactam to the following conditions as potential contraindications. These come from the model's knowledge graph, not from label text, and should be checked against the SmPC:

- Kidney disease
- Pyoureter
- Neutropenia and agranulocytosis
- Blood coagulation disease
- *Clostridium difficile* colitis
- Perinatal necrotizing enterocolitis
- Infectious mononucleosis and chronic Epstein-Barr virus infection syndrome

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 3 RCTs (for example ASPECT-NP and RESTORE-IMI 2) test tazobactam-containing regimens in hospital-acquired and ventilator-associated pneumonia, and the same mechanism supports UTI. However, tazobactam is never used alone, most trials use it as a comparator or test combinations, and the indication is close to the existing one, so this is an extension of current use rather than a new discovery.

**To proceed, the following is needed:**
- Licensed indication text, dosage forms and manufacturer details from the UK SmPC for both authorisations
- Label-based warnings, contraindications and interaction data (the knowledge-graph contraindications need verifying)
- Detailed mechanism of action data
- Clarification of the evidence for ESBL-producing organisms (outcome of NCT03891433, currently suspended)
- Local antimicrobial stewardship and resistance guidance, with renal dosing adjustments
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

