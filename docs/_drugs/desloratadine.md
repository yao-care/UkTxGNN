---
layout: default
title: Desloratadine
parent: High Evidence (L1-L2)
nav_order: 215
evidence_level: L2
indication_count: 6
last_modified_at: 2026-10-15
description: "Desloratadine: predicted new indication Cold urticaria (evidence level L2). Approved use: Allergic rhinitis"
monitor_inn: "Desloratadine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic"]
---

# Desloratadine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **6** 
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

# Desloratadine: From Allergic Rhinitis to Cold Urticaria

## One-Sentence Summary

Desloratadine is a second-generation antihistamine, originally used for allergic rhinitis and urticaria.
The TxGNN model predicts it may be effective for **cold urticaria**,
with **2 clinical trials** and **6 publications** (3 of them randomised controlled trials) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (indication text is not available in the UK authorisation record; taken from the knowledge graph) |
| Predicted New Indication | Cold urticaria |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, desloratadine is a selective peripheral H1 receptor antagonist (inverse agonist). Its efficacy in allergic rhinitis and in idiopathic and allergic urticaria is established.

Cold urticaria is a mast cell-driven physical urticaria. Histamine released through H1 receptors produces the wheals and itching, so desloratadine acts directly on the principal mediator pathway. This is the same pathway that underlies its existing urticaria use.

Increasing the dose above the standard 5 mg (to 10 mg and 20 mg) is the guideline-endorsed approach for cold urticaria that does not respond to standard dosing. The trial data below show a dose-dependent improvement in cold provocation thresholds. Note that this up-dosing is outside the standard licensed dose.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Completed | 30 | Multi-centre, double-blind, dose-escalating comparison of desloratadine 5 mg, 10 mg and 20 mg in acquired cold urticaria, aiming to find the dose sufficient to inhibit symptoms |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Completed | 33 | Exploratory, randomised, double-blind, placebo-controlled crossover study comparing 5 mg vs 20 mg on experimentally induced lesions (thermography, volumetry, photography) |

Both studies are small and no Phase 3 pivotal trial is available.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | Randomised, placebo-controlled crossover study: high-dose desloratadine reduced wheal volume and improved cold provocation thresholds compared with standard dose |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | Randomised trial of H1-antihistamine dose escalation using critical temperature threshold measurement in cold urticaria |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatolog Treat | Desloratadine 5 mg for 4 days tested with ice-cube provocation in 12 patients with cold urticaria |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | Review of aetiology, management and treatment options in chronic urticaria |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Review | Allergy | Review of ebastine (another antihistamine) in allergic rhinitis and chronic idiopathic urticaria; indirect relevance |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case report | Qatar Med J | Cold-induced urticaria following black ant bite anaphylaxis; background only |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0304010ABAAAAAA | Desloratadine 5 mg tablets | Tablet | Not available |

The identifier above is a BNF-style product code rather than a standard PL number. The BNF section (0304, antihistamines) is consistent with the drug class. Dosage form and approved indication text are not recorded in the data compiled for this report.

## Safety Considerations

**Contraindications (knowledge-graph associations, not label text):** The TxGNN knowledge graph links desloratadine with the following conditions. These should be verified against the SmPC before use:
- Cardiovascular: hypertension, coronary artery disease, atherosclerosis
- Renal and hepatic: kidney disease, liver disease, gallbladder disease
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperthyroidism (Graves disease, thyrotoxicosis)
- Other: benign prostatic hyperplasia, angle-closure glaucoma

**Drug Interactions:** The interaction screen returned 100 potential interactions, but none has a graded severity. Examples include cimetidine, omeprazole, pantoprazole, lansoprazole, metformin, morphine, simvastatin, doxycycline, epinephrine and prednisone. Their clinical significance has not been established from the data available.

For full safety information, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 4 trials and three RCTs support dose-dependent efficacy of desloratadine in acquired cold urticaria, with a plausible H1-mediated mechanism. The studies are small, there is no Phase 3 evidence, and the effective doses exceed the standard 5 mg, so this is a modest level of evidence (L2).

Other predictions (nasal cavity disease, acute laryngopharyngitis, recalcitrant atopic dermatitis, atopic IgE responsiveness, rosacea conjunctivitis) have little or no supporting evidence and should be held.

**To proceed, the following is needed:**
- SmPC warnings and contraindications to complete the safety review, as label-based safety data are not available
- Verification of the knowledge-graph contraindication signals against the SmPC
- A safety assessment of doses of 10–20 mg, including cardiac and sedation considerations and any off-label prescribing governance
- Confirmation of the dosage form, authorised indications and PL number for the UK product
- Mechanism of action data from DrugBank
- Larger confirmatory trials, ideally Phase 3, in cold urticaria
- Review of the NICE and British Association of Dermatologists guidance on urticaria management
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

