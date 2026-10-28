---
layout: default
title: Perphenazine
parent: Model Prediction Only (L5)
nav_order: 488
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Perphenazine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Schizophrenia"
monitor_inn: "Perphenazine"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "hydranencephaly (disease)", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "atypical glycine encephalopathy"]
---

# Perphenazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Perphenazine: From Schizophrenia to retinal dystrophy with or without extraocular anomalies (Prediction-Only)
{: .text-alpha }

## One-Sentence Summary

Perphenazine is a phenothiazine antipsychotic, originally used to treat schizophrenia and mixed anxiety and depressive disorder.
The TxGNN model's top-ranked prediction is **retinal dystrophy with or without extraocular anomalies**, but there are **no clinical trials** and only **1 publication** (a case report of drug-induced retinal toxicity from a different drug), so this prediction is not supported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia; mixed anxiety and depressive disorder (the UK authorisation record has no indication text) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, perphenazine is a phenothiazine antipsychotic whose efficacy in schizophrenia is established. It acts mainly as a dopamine D2 antagonist, with additional activity at 5-HT2A and other receptors.

For the top prediction, **the rationale is weak**. The only literature record (PMID 14129300, 1964) describes pigmentary retinopathy caused by **thioridazine**, a different phenothiazine. This is a retinal toxicity signal for the drug class, not evidence of benefit. No plausible therapeutic mechanism for perphenazine in inherited retinal dystrophy has been identified. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions are similarly unsupported: syndromic myopia, perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis, hydranencephaly, Charcot-Marie-Tooth disease type 1G, X-linked myopia, a congenital disorder of glycosylation, and atypical glycine encephalopathy. They are mostly congenital structural, genetic or metabolic conditions, and none has trials or literature. The speculation that dopaminergic signalling is involved in myopia is not backed by direct evidence.


---

## Clinical Trial Evidence

For the top prediction (retinal dystrophy), no trials are registered: currently no related clinical trials registered.

For anxiety disorder, one trial was identified:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | Terminated | 407 | Multicentre pharmacovigilance study of psychopharmacological treatment and adverse drug reaction rates in elderly psychiatric inpatients. It is a safety-monitoring study, not an efficacy trial for anxiety. |

---

## Literature Evidence

**Retinal dystrophy (top prediction):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14129300](https://pubmed.ncbi.nlm.nih.gov/14129300/) | 1964 | Case report | Am J Psychiatry | Pigmentary retinopathy with thioridazine (a different drug) at very high doses. This is a safety signal, not supportive evidence. |

**Anxiety disorder (most relevant selection from 20 publications):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | J Clin Psychiatry | Review of typical and atypical antipsychotics for primary and comorbid anxiety. |
| [4867598](https://pubmed.ncbi.nlm.nih.gov/4867598/) | 1968 | Double-blind study | Psychosomatics | Perphenazine-amitriptyline in anxiety and depression accompanying physical disorders. |
| [4554486](https://pubmed.ncbi.nlm.nih.gov/4554486/) | 1972 | Controlled study | Psychopharmacologia | Doxepin versus amitriptyline-perphenazine in mixed anxious-depressed outpatients. |
| [14249358](https://pubmed.ncbi.nlm.nih.gov/14249358/) | 1964 | Clinical study | J Med Assoc Georgia | Combined amitriptyline and perphenazine in combined depression and anxiety. |
| [14144440](https://pubmed.ncbi.nlm.nih.gov/14144440/) | 1964 | Clinical study | Am J Psychiatry | Effects of the perphenazine-amitriptyline combination. |
| [14401911](https://pubmed.ncbi.nlm.nih.gov/14401911/) | 1959 | Comparative study | J Ment Sci | Perphenazine compared with sodium amylobarbitone and placebo in anxious and depressed outpatients. |
| [4886995](https://pubmed.ncbi.nlm.nih.gov/4886995/) | 1969 | Double-blind study | Dis Nerv Syst | Thiothixene versus perphenazine-amitriptyline in psychotic and psychoneurotic depression. |
| [27372312](https://pubmed.ncbi.nlm.nih.gov/27372312/) | 2016 | Review (safety) | CNS Drugs | Incidence and management of antipsychotic-induced somnolence. |

Most of this evidence is old, uses the perphenazine-amitriptyline combination, and cannot isolate the contribution of perphenazine.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0402010Q0AAACAC (BNF-style code, not a PL number) | Perphenazine tablets 2 mg | Tablet | Indication text not available in the compiled record |

One valid single-ingredient authorisation is recorded. The BNF section code (0402010) corresponds to antipsychotic drugs.

---

## Safety Considerations

No label-based warnings or contraindications were available. The following come from knowledge-graph contraindication links and interaction screening, and should be checked against the SmPC and BNF.

- **Contraindication signals (knowledge graph, not label text):**
  - Cardiac and QT: long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, myocardial infarction and coronary thrombosis.
  - Blood pressure: orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy.
  - Neurological: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm.
  - Haematological: neutropenia, agranulocytosis, thrombocytopenia, anaemia, haemoglobinopathy.
  - Other: liver disease, gallbladder disease, hyperglycaemia, open-angle glaucoma, benign prostatic hyperplasia, manic bipolar disorder, substance abuse/dependence, breast carcinoma, obesity.
- **Drug interactions:** 100 interactions were found. Major-level examples include **bupropion**, **morphine** and **potassium citrate**. Moderate-level examples include antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, chlorpropamide, albiglutide), anticholinergics (atropine, hyoscyamine, glycopyrronium), epinephrine, famotidine, clarithromycin, loperamide, lorcaserin, bisacodyl and picosulfuric acid.
- **Class-related concerns:** sedation/somnolence and extrapyramidal effects. Phenothiazine-associated retinopathy has been reported for thioridazine, which is relevant to any proposal involving eye disease.

Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction (retinal dystrophy) and the other high-scoring predictions rest on model scores alone (Evidence Level L5). The only related literature points to a retinal safety risk, not a benefit.
- Anxiety disorder has more evidence (L3), but it is mostly old combination-product studies, and the only trial is a terminated pharmacovigilance study. This overlaps with the existing licence and is not a new repurposing opportunity.

**To proceed, the following is needed:**
- Mechanism of action data, to assess biological plausibility.
- Full SmPC warnings and contraindications from the MHRA/BNF record, plus the approved indication text for the UK authorisation.
- For anxiety disorder: modern randomised trials of perphenazine alone, with a clear benefit-risk assessment in view of the QT, sedation, extrapyramidal and interaction burden.
- For retinal dystrophy: preclinical or mechanistic evidence before any further consideration, with an explicit review of phenothiazine retinal toxicity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

