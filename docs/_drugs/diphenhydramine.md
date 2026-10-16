---
layout: default
title: Diphenhydramine
parent: Model Prediction Only (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Diphenhydramine: predicted new indication Rhinitis (evidence level L5). Approved use: Insomnia"
monitor_inn: "Diphenhydramine"
predicted_indications: ["rosacea conjunctivitis", "rhinitis", "allergic urticaria", "cold urticaria", "cauda equina syndrome", "nasopharyngitis", "viral conjunctivitis", "neuralgia", "trigeminal autonomic cephalalgia", "glossodynia"]
---

# Diphenhydramine
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

# Diphenhydramine: From Allergic and Vasomotor Rhinitis to Rhinitis (Label-Consistent Extension)

## One-Sentence Summary

Diphenhydramine is a first-generation H1 antihistamine, originally used for insomnia, allergic and vasomotor rhinitis, and several forms of conjunctivitis.
The TxGNN model's top-ranked prediction is **rosacea conjunctivitis** (no supporting evidence), but the best-supported prediction is **rhinitis**, which has **5 clinical trials** and **19 publications** (including 2 RCTs), although it largely overlaps with the existing use of the drug.
This report evaluates the best-supported prediction, rhinitis, and summarises the other predictions briefly at the end.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia; vasomotor rhinitis; allergic rhinitis; atopic, papillary and vernal conjunctivitis (the product record held no approved indication text) |
| Predicted New Indication | Rhinitis (rank 2; the rank 1 prediction, rosacea conjunctivitis, has no evidence) |
| TxGNN Prediction Score | 98.35% (rhinitis); 99.20% (rosacea conjunctivitis) |
| Evidence Level | L1 (for rhinitis, per the data compiled for this report) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, diphenhydramine is a first-generation H1 receptor antagonist. It blocks histamine-mediated nasal symptoms such as sneezing, rhinorrhoea and itching.

The drug is already used for allergic and vasomotor rhinitis, so the predicted indication is largely a label-consistent extension and not a true repurposing. The model is effectively recognising an established use, which supports its plausibility.

The main caveat is tolerability. Sedation, anticholinergic effects and cognitive impairment (including in children and older adults) mean that second-generation antihistamines are generally preferred as first-line therapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00648973](https://clinicaltrials.gov/study/NCT00648973) | Phase 4 | Completed | 1021 | Randomised, double-blind, placebo- and pseudoephedrine-controlled study of diphenhydramine 25 mg and 50 mg for nasal congestion in seasonal allergic rhinitis. Directly relevant and the strongest trial. |
| [NCT00762749](https://clinicaltrials.gov/study/NCT00762749) | Phase 1 | Completed | 36 | Single-dose pharmacokinetics in children (2 to <12 years) and adolescents (12 to <18 years). Informs dosing, not efficacy. |
| [NCT05586477](https://clinicaltrials.gov/study/NCT05586477) | Phase 4 | Completed | 20 | Effect of diphenhydramine on thermoregulation during exercise. A physiological safety study, not efficacy. |
| [NCT06217367](https://clinicaltrials.gov/study/NCT06217367) | Phase 4 | Unknown | 16 | Thermoregulatory effects of over-the-counter antihistamines during passive heat stress. Peripheral safety information only. |
| [NCT01177852](https://clinicaltrials.gov/study/NCT01177852) | Phase 3 | Withdrawn | 0 | Planned comparison of a diphenhydramine, dropropizine and pseudoephedrine combination in children aged 2 to 12 with cough and acute rhinitis. Withdrawn, so no evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16680933](https://pubmed.ncbi.nlm.nih.gov/16680933/) | 2006 | RCT | Ann Allergy Asthma Immunol | Diphenhydramine compared with desloratadine and placebo in moderate-to-severe seasonal allergic rhinitis. |
| [14582817](https://pubmed.ncbi.nlm.nih.gov/14582817/) | 2003 | RCT | Ann Allergy Asthma Immunol | Diphenhydramine versus desloratadine on vigilance and cognitive function in ragweed-induced allergic rhinitis. |
| [8634878](https://pubmed.ncbi.nlm.nih.gov/8634878/) | 1996 | RCT | Ann Allergy Asthma Immunol | Effects of acrivastine/pseudoephedrine and diphenhydramine on learning in seasonal allergic rhinitis. |
| [40152721](https://pubmed.ncbi.nlm.nih.gov/40152721/) | 2025 | Review | Med Lett Drugs Ther | Treatment of allergic rhinitis and allergic conjunctivitis. |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clin Allergy Immunol | H1-antihistamines in children are useful in allergic rhinoconjunctivitis; use in upper respiratory infections is not well supported. |
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Position statement | Allergy Asthma Clin Immunol | CSACI statement: newer-generation H1-antihistamines are safer and should be first-line over first-generation agents such as diphenhydramine. |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Efficacy and safety of first- and newer-generation oral antihistamines in allergic rhinitis and urticaria. |
| [36420548](https://pubmed.ncbi.nlm.nih.gov/36420548/) | 2022 | Pilot study | Tokai J Exp Clin Med | Transdermal diphenhydramine applied to the nasal ala in allergic rhinitis and asthma. |
| [12743547](https://pubmed.ncbi.nlm.nih.gov/12743547/) | 2003 | Consensus statement | J Allergy Clin Immunol | Expert consensus on managing antihistamine-related impairment in allergic rhinitis. |
| [36759413](https://pubmed.ncbi.nlm.nih.gov/36759413/) | 2023 | Preclinical | AAPS PharmSciTech | Diphenhydramine nasal nano-gel and nano-emulgel in a rabbit model of allergic rhinitis. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0304010N0AAAGAG (BNF-style product code; not a PL number) | Diphenhydramine HCl tablets 25 mg | Tablet (not specified in the data) | Not specified in the data |

The compiled data holds one valid single-ingredient product record. Please check the current SmPC and the BNF (antihistamines chapter) for the licensed indications and doses, as well as any relevant NICE guidance.

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interactions; 20 are shown in the data compiled for this report. Two are classed as **Major**: **potassium citrate** and **eliglustat**. The rest listed are Moderate, and many are additive anticholinergic or sedative combinations, including hyoscyamine, atropine, glycopyrronium, dicyclomine, clidinium, mepenzolate, methscopolamine, loperamide, morphine, nabilone, dronabinol, bupropion, metoclopramide, eluxadoline, lorcaserin and glycerol phenylbutyrate.
- **Class concerns from the literature**: Sedation, cognitive impairment, dry mouth, dizziness and orthostatic hypotension, with particular caution in children and older adults.

Label warnings and contraindications are not available in the compiled data. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Other Predicted Indications (Brief Summary)

| Rank | Predicted Indication | Score | Evidence Level | Recommendation | Comment |
|------|------|------|------|------|------|
| 1 | Rosacea conjunctivitis | 99.20% | L5 | Hold | No trials or literature; the disease is driven mainly by meibomian gland dysfunction and inflammation, so the link is weak. |
| 3 | Allergic urticaria | 98.24% | L3 | Proceed with Guardrails | H1 blockade is standard; one small Phase 3 pilot (NCT02023164, n=36) used IV diphenhydramine as a comparator. Newer antihistamines are preferred. |
| 4 | Cold urticaria | 95.92% | L4 | Research Question | Only old treatment reports and case reports. |
| 5 | Cauda equina syndrome | 95.57% | L5 | Hold | No plausible mechanism; probably a network artefact. |
| 6 | Nasopharyngitis | 94.96% | L4 | Research Question | One indirect RCT of a combination product; symptomatic benefit only. |
| 7 | Viral conjunctivitis | 93.97% | L5 | Hold | Not primarily histamine-driven; no evidence. |
| 8 | Neuralgia | 92.30% | L4 | Hold | Trials involved other drugs; diphenhydramine appears mostly as an active placebo. |
| 9 | Trigeminal autonomic cephalalgia | 92.25% | L4 | Research Question | One small terminated emergency department trial of primary headache; a 1952 anecdotal report. |
| 10 | Glossodynia | 92.08% | L5 | Hold | No data. |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for rhinitis)

**Rationale:**
Rhinitis is supported by a large completed trial (n=1021) and several RCTs, but it is essentially an existing use of diphenhydramine, so it is not a novel repurposing finding. The drug's sedative and anticholinergic burden favours second-generation antihistamines as first-line therapy. The top-scoring prediction, rosacea conjunctivitis, has no supporting evidence and should be held.

**To proceed, the following is needed:**
- Mechanism of action data and UK label information (approved indications, warnings and contraindications from the SmPC)
- Confirmation of the product's dosage form, marketing authorisation number and licensed indications
- Comparative effectiveness and safety data against second-generation antihistamines, with specific guardrails for children and older adults
- Review of the major interactions (potassium citrate, eliglustat) and additive anticholinergic or sedative combinations
- For the lower-ranked predictions, targeted studies only where a plausible mechanism exists (for example, urticaria in acute settings)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

