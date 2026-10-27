---
layout: default
title: Trifluoperazine
parent: Model Prediction Only (L5)
nav_order: 640
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Trifluoperazine: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Schizophrenia, anxiety"
monitor_inn: "Trifluoperazine"
predicted_indications: ["manic bipolar affective disorder"]
---

# Trifluoperazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Trifluoperazine: From Schizophrenia and Anxiety to Manic Bipolar Affective Disorder
{: .text-alpha }

## One-Sentence Summary

Trifluoperazine is a phenothiazine antipsychotic, originally used to treat schizophrenia and anxiety.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**,
but there are **no registered clinical trials** and the **20 publications** compiled for this report are mostly indirect, so the evidence is currently model-based only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia, anxiety (from the knowledge graph; no approved indication text is available in the UK licence record) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 (model prediction only; the supporting literature is indirect and no trials are registered) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

*Note: the structured scoring in the data compiled for this report lists L4. In my assessment the literature contains no preclinical or mechanism study of trifluoperazine in mania, so L5 is the better fit under the grading rules. This should be confirmed at review.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general knowledge of the drug class (not from the supplied data), trifluoperazine is a phenothiazine antipsychotic whose main pharmacology is dopamine D2 receptor antagonism. D2 blockade is the mechanism shared by antipsychotics used to treat acute mania, which makes the prediction plausible.

Schizophrenia and manic episodes of bipolar disorder both involve psychotic and behavioural symptoms that respond to antipsychotics. The high TxGNN score probably reflects trifluoperazine's similarity to other antipsychotics already used in mania. It is a computational prediction and not clinical evidence for trifluoperazine itself. None of the supplied records shows trifluoperazine tested specifically in bipolar mania.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications below is a randomised trial of trifluoperazine in mania. Most are reviews, case reports or historical studies that mention the drug or the wider antipsychotic class. Only the most relevant are listed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | J Clin Psychiatry | Reviewed the efficacy of typical and atypical antipsychotics for anxiety symptoms, including in bipolar disorder |
| [11279762](https://pubmed.ncbi.nlm.nih.gov/11279762/) | 2001 | Review | Cochrane Database Syst Rev | Clotiapine for acute psychotic illness with agitation; a different drug, so only indirectly relevant |
| [40926568](https://pubmed.ncbi.nlm.nih.gov/40926568/) | 2026 | Review | J Appl Toxicol | Phenothiazine derivatives and apoptosis; notes use in schizophrenia and mania in bipolar disorder |
| [30601177](https://pubmed.ncbi.nlm.nih.gov/30601177/) | 2021 | Review | Am J Ther | Safety scoring of psychotropic drugs in lactation, including for bipolar mood episodes |
| [19461391](https://pubmed.ncbi.nlm.nih.gov/19461391/) | 2009 | Review | J Psychiatr Pract | Use and safety of antipsychotics in pregnancy |
| [39202628](https://pubmed.ncbi.nlm.nih.gov/39202628/) | 2024 | Review | Medicina (Kaunas) | Systematic review of drug-induced oral vertical dyskinesia ("rabbit" syndrome) |
| [24943390](https://pubmed.ncbi.nlm.nih.gov/24943390/) | 2014 | Cohort | J Clin Psychopharmacol | Prescribing patterns for psychotic disorders in Ugandan hospitals |
| [14084030](https://pubmed.ncbi.nlm.nih.gov/14084030/) | 1963 | Double-blind study | Curr Ther Res | Withdrawal of trifluoperazine in patients on tranylcypromine plus trifluoperazine (no abstract available) |
| [13761179](https://pubmed.ncbi.nlm.nih.gov/13761179/) | 1961 | Clinical report | Am J Psychiatry | Tranylcypromine plus trifluoperazine in agitated depression (no abstract available) |
| [14309092](https://pubmed.ncbi.nlm.nih.gov/14309092/) | 1965 | Clinical report | Int J Neuropsychiatry | Haloperidol in schizophrenic and manic patients; a different drug (no abstract available) |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0402010X0AAAHAH (a BNF-style product code, not a PL number) | Trifluoperazine tablets 1 mg | Tablet | Not available in the data compiled for this report |

The licence record gives no dosage form or approved indication text. The product sits in BNF chapter 4 (central nervous system), antipsychotic drugs. Please check the current SmPC and any NICE guidance for authorised indications.

---

## Cytotoxicity

Not applicable. Trifluoperazine is not an antineoplastic drug.

---

## Safety Considerations

**Contraindications suggested by the knowledge graph (not label text):** the TxGNN knowledge graph links trifluoperazine to the following conditions. These are drug-disease edges and need verification against the SmPC.
- **Haematological:** neutropenia, agranulocytosis, thrombocytopenia, anaemia (including macrocytic anaemia)
- **Hepatic:** liver disease, cirrhosis, fatty liver disease, hepatitis, gallbladder disease
- **Neurological:** epilepsy, Alzheimer disease, tardive dyskinesia, lingual-facial-buccal dyskinesia, neuroleptic malignant syndrome, multiple system atrophy
- **Cardiovascular and autonomic:** orthostatic hypotension, hypotensive disorder, postural orthostatic tachycardia syndrome
- **Eye:** glaucoma, vision disorder, blindness, retinal disease, retinitis
- **Other:** benign prostatic hyperplasia, female breast carcinoma

**Drug interactions:** 100 interactions were found in the interaction database; 20 were returned in detail.
- **Major:** bupropion, morphine
- **Moderate (examples):** epinephrine, hydrocortisone, atropine, glycopyrronium, hyoscyamine, loperamide, amphotericin B, and several antidiabetic drugs (metformin, pioglitazone, alogliptin, canagliflozin, chlorpropamide, acarbose, albiglutide)

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and class-level pharmacology. No clinical trials are registered, and none of the literature directly tests trifluoperazine in mania. Established alternatives already exist, and the knowledge-graph safety signals (haematological, hepatic and neurological) need careful review.

**To proceed, the following is needed:**
- Mechanism of action data for trifluoperazine (currently missing)
- SmPC warnings and contraindications (currently missing), as well as the authorised indications and dosage form for the UK product
- A targeted literature search for trifluoperazine in acute mania, including comparative trials against current standard treatments
- A comparison with existing NICE-recommended options for bipolar mania to establish whether there is any added value
- A safety assessment covering the knowledge-graph contraindications and the major interactions, including monitoring of blood counts and liver function
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

