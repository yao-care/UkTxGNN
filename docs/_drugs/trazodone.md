---
layout: default
title: Trazodone
parent: High Evidence (L1-L2)
nav_order: 636
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-15
description: "Trazodone: predicted new indication Obsessive-compulsive disorder (evidence level L2). Approved use: Not stated in the UK authorisation data"
---

# Trazodone
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Trazodone: From Depression to Obsessive-Compulsive Disorder

## One-Sentence Summary

Trazodone is an antidepressant, originally used for depressive disorders and anxiety disorders.
The TxGNN model predicts it may be effective for **obsessive-compulsive disorder (OCD)**,
but the supporting evidence is **small and dated**: no registered clinical trials and **20 publications**, only one of which is a placebo-controlled RCT.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the UK authorisation data; knowledge-graph indications are unipolar depression, endogenous depression, major depressive disorder and anxiety disorder |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails (research question only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, trazodone acts on serotonergic pathways: it antagonises 5-HT2A/2C receptors and weakly inhibits serotonin reuptake. Its active metabolite, m-CPP, is also serotonergic.

Serotonergic modulation is the established basis of OCD drug treatment. Trazodone is already used in depression and anxiety, so a serotonergic effect on obsessive-compulsive symptoms is plausible. However, trazodone's serotonin reuptake inhibition is weak compared with agents established in OCD, and the clinical evidence is small and mostly from the 1980s and 1990s.

The remaining top predictions (schizotypal, schizoid, paranoid and histrionic personality disorders, benign paroxysmal torticollis of infancy, Ohdo syndrome) have no meaningful supporting evidence and are not pursued here. Agoraphobia, phobic disorder and dysthymic disorder have limited older evidence (see the Conclusion).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1629380](https://pubmed.ncbi.nlm.nih.gov/1629380/) | 1992 | RCT (double-blind, placebo-controlled) | J Clin Psychopharmacol | Controlled study of trazodone in OCD, designed to test its anti-obsessive efficacy; the results excerpt was not available in the data compiled |
| [2119885](https://pubmed.ncbi.nlm.nih.gov/2119885/) | 1990 | Case series / open-label | Clin Neuropharmacol | Nine clomipramine-resistant OCD patients: mild improvement overall; three responded well, with symptoms returning on withdrawal and improving on re-administration |
| [3571943](https://pubmed.ncbi.nlm.nih.gov/3571943/) | 1986 | Open pilot study | Int Clin Psychopharmacol | Trazodone plus tryptophan in 11 patients: benefit marginal and the combination poorly tolerated by several |
| [3501130](https://pubmed.ncbi.nlm.nih.gov/3501130/) | 1987 | Open-label / correlational | Psychopathology | Treatment response correlated with changes in caudate glucose metabolism on PET |
| [26088119](https://pubmed.ncbi.nlm.nih.gov/26088119/) | 2015 | Review | Curr Pharm Des | Off-label trazodone use, including OCD, with evidence, benefits and risks |
| [27744763](https://pubmed.ncbi.nlm.nih.gov/27744763/) | 2017 | Review | Postgrad Med | Trazodone in psychiatric and medical conditions, covering mechanism, dosing and adverse effects |
| [8993077](https://pubmed.ncbi.nlm.nih.gov/8993077/) | 1996 | Review | Psychopharmacol Bull | Mono- and polypharmacotherapy of OCD; serotonin reuptake inhibitors are the principal responsive class |
| [4009160](https://pubmed.ncbi.nlm.nih.gov/4009160/) | 1985 | Case report | J Nerv Ment Dis | Two patients with OCD and depression, resistant to other antidepressants, improved on trazodone |
| [8434675](https://pubmed.ncbi.nlm.nih.gov/8434675/) | 1993 | Case report / small series | Am J Psychiatry | Trazodone in OCD and trichotillomania |
| [6703152](https://pubmed.ncbi.nlm.nih.gov/6703152/) | 1984 | Case report | Am J Psychiatry | Early report of trazodone in OCD |

Most of the other retrieved papers are further case reports, reviews or pharmacology papers. The abstract for the controlled study (PMID 1629380) was truncated in the data compiled, so its outcome should be checked in the full paper.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0403010X0AAAAAA | Trazodone HCl capsule 50 mg | Capsule (as named in the product description) | Not available in the data compiled |

The data compiled for this report list only one authorisation, and the number shown is not in the standard MHRA "PL" format, so it should be checked against the MHRA register. The BNF classifies trazodone among antidepressant drugs. NICE-appraised indication details were not available.

---

## Safety Considerations

- **Contraindications and risk conditions (from the drug–disease knowledge graph, not label text):** multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, long QT syndrome (including familial), torsades de pointes, potassium deficiency, benign prostatic hyperplasia, blood coagulation disease, heart disease and cardiovascular disease, priapism, and inappropriate ADH secretion (including the nephrogenic form).
- **Drug interactions:** 100 interactions were identified; the 20 reviewed include these **Major** interactions: bupropion, lorcaserin, dolasetron, palonosetron, cisapride, dexfenfluramine and fenfluramine. Many involve serotonergic or QT-prolonging combinations. **Moderate** interactions include famotidine, loperamide, aprepitant, morphine, clarithromycin, dronabinol, eliglustat, and several laxatives and bowel-preparation agents.

Label-based warnings were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (as a research question, not a clinical recommendation)**

**Rationale:**
- The TxGNN score is very high and the serotonergic mechanism is plausible, and one double-blind placebo-controlled RCT exists. However, the RCT is more than 30 years old and its result is not confirmed here, the other studies are small open-label reports and case reports, and the data cover only the rank 1 prediction. OCD treatment relies on established serotonin reuptake inhibitors, so trazodone is at most a candidate for treatment-resistant cases or for use as an adjunct. The other predicted indications are weaker: agoraphobia, phobic disorder and dysthymic disorder have only older, small studies, and the personality disorders, benign paroxysmal torticollis of infancy and Ohdo syndrome have none, so they are on Hold.

**To proceed, the following is needed:**
- Review of the full text and results of the 1992 placebo-controlled RCT (PMID 1629380)
- A modern, adequately powered randomised trial in OCD, including treatment-resistant patients and adjunctive use
- Mechanism of action data (MOA) from DrugBank
- UK label information (indications, warnings, contraindications) from the SmPC and BNF, plus verification of the authorisation record
- A cardiac and interaction risk assessment (QT prolongation, serotonergic combinations) before any use in the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

