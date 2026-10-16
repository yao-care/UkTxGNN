---
layout: default
title: Quetiapine
parent: Model Prediction Only (L5)
nav_order: 530
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Quetiapine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Bipolar disorder, major affective disorder…"
---

# Quetiapine
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

# Quetiapine: From Schizophrenia and Bipolar Disorder to Retinal Dystrophy

## One-Sentence Summary

Quetiapine is an atypical antipsychotic, originally used to treat schizophrenia and bipolar disorder.
The TxGNN model's top-ranked prediction is **retinal dystrophy with or without extraocular anomalies**, but this is a model prediction only, with **no clinical trials** and **no publications** supporting it.
The best-supported candidate among the top 10 is **trichotillomania**, which has **6 publications** (case reports and reviews only) and no registered trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bipolar disorder, major affective disorder, manic bipolar affective disorder, schizophrenia |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies (rank 1); trichotillomania (rank 8) is the only candidate with any supporting literature |
| TxGNN Prediction Score | 99.57% (rank 1); 99.38% (trichotillomania) |
| Evidence Level | L5 (rank 1); L4 (trichotillomania) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, quetiapine is an atypical antipsychotic whose receptor pharmacology involves serotonin 5-HT2A, dopamine D2 and histamine H1 antagonism. Its efficacy in schizophrenia and bipolar disorder is established.

**For the top-ranked prediction (retinal dystrophy):** the data compiled for this report show no mechanistic link. Inherited retinal degeneration is not plausibly addressed by monoaminergic receptor antagonism. The high score (0.996) reflects the model's prediction alone. The same holds for the other top-ranked candidates, which are mostly genetic or developmental conditions (congenital glycosylation disorder, hydranencephaly, 17p13.3 microdeletion syndrome, polymicrogyria, X-linked myopias, Charcot-Marie-Tooth type 1G). None has trials or literature.

**For trichotillomania (rank 8):** a plausible link exists. Trichotillomania is a body-focused repetitive behaviour related to the obsessive-compulsive spectrum, in which serotonergic and dopaminergic dysregulation is implicated. Atypical antipsychotics are sometimes used as augmentation in this spectrum. The evidence is limited to case reports and small series, and one report describes quetiapine exacerbating obsessive-compulsive symptoms in a patient with trichotillomania.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Evidence below relates to trichotillomania (rank 8), the only predicted indication with literature. The abstracts available were truncated, so findings are summarised cautiously.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12405081](https://pubmed.ncbi.nlm.nih.gov/12405081/) | 2002 | Review / case report | Psychiatry | Overview of trichotillomania and its treatment; case report of a favourable response to quetiapine in a 33-year-old woman |
| [19142421](https://pubmed.ncbi.nlm.nih.gov/19142421/) | 2008 | Case report/series | Rev Bras Psiquiatr | Quetiapine for the treatment of trichotillomania (no abstract available) |
| [11212595](https://pubmed.ncbi.nlm.nih.gov/11212595/) | 2001 | Case report/Review | J Psychiatry Neurosci | Review of atypical antipsychotic-induced obsessive-compulsive symptoms; first report of quetiapine exacerbating OCS in a patient with OCD, trichotillomania and bipolar disorder |
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | Review | Int J Dermatol | Review of pharmacological treatment of trichotillomania; notes lack of guidelines and common treatment strategy |
| [20833945](https://pubmed.ncbi.nlm.nih.gov/20833945/) | 2010 | Case report/Review | Psychosomatics | Treatment of recurrent Rapunzel syndrome and trichotillomania; background context only |
| [27840761](https://pubmed.ncbi.nlm.nih.gov/27840761/) | 2016 | Case report | Case Rep Psychiatry | Trichotillomania as a manifestation of dementia; limited direct relevance to quetiapine |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0402010ABAAABAB (BNF-style code) | Quetiapine tablets 25 mg | Tablet | Not stated in the data compiled |

One valid single-ingredient authorisation is recorded. BNF chapter 4.2.1 (antipsychotic drugs) is the relevant classification, as suggested by the code prefix.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text; verify against the SmPC): hypertension, orthostatic hypotension, long QT syndrome and torsades de pointes, epilepsy, liver disease, diabetes mellitus and diabetic ketoacidosis, hyperglycaemia, neutropenia and agranulocytosis, hypothyroidism, hyperlipidaemia and hypertriglyceridaemia, obesity, myocardial infarction, and several movement and other disorders.
- **Drug Interactions:** 100 interactions were identified. Examples flagged **Major**: bupropion and morphine. Many **Moderate** interactions were also listed, including antidiabetic drugs (metformin, pioglitazone, alogliptin, canagliflozin, acarbose, albiglutide, chlorpropamide), anticholinergics (atropine, hyoscyamine, glycopyrronium, clidinium), epinephrine, famotidine, loperamide, aprepitant, dexamethasone, bisacodyl and lorcaserin.
- **Metabolic and sedation burden:** the knowledge-graph signals and the interactions with antidiabetic drugs point to metabolic risk that matters for any new long-term use.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predictions, including retinal dystrophy, rest on model scores alone (L5) with no mechanistic, trial or literature support. Trichotillomania has a plausible mechanism but only case-level evidence (L4), and quetiapine carries notable metabolic, cardiac and interaction risks.

**To proceed, the following is needed:**
- Mechanism of action data for quetiapine
- Full MHRA SmPC warnings and contraindications, and approved indication text for the UK authorisation
- For trichotillomania: a systematic review of antipsychotic use, then a controlled trial against established options (e.g. habit reversal therapy, N-acetylcysteine)
- A risk-benefit assessment covering metabolic monitoring, QT risk and the interaction burden
- No further work on the other top-ranked candidates unless supporting biological or clinical evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

