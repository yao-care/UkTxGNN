---
layout: default
title: Chlorpromazine
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 10
---

# Chlorpromazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Chlorpromazine: From Schizophrenia to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Chlorpromazine is a first-generation phenothiazine antipsychotic with over 70 years of clinical use, established for the management of schizophrenia, acute mania, and severe agitation.
The TxGNN model's highest-ranked prediction is **Retinal Dystrophy with or without Extraocular Anomalies** (score 99.95%); however, this prediction is critically undermined by existing evidence demonstrating that chlorpromazine is itself a recognised cause of phenothiazine-induced retinopathy — not a treatment for retinal disease.
There are **no registered clinical trials** and **no directly supportive publications** for this indication; the most clinically actionable prediction in this Evidence Pack is **Early-Onset Schizophrenia** (rank 10), supported by **1 observational study** and **8 publications**, which aligns with the drug's well-established pharmacology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no MHRA marketing authorisation record found in dataset) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| UK Market Status | Not marketed (0 MHRA authorisations in dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, chlorpromazine is a phenothiazine derivative that acts primarily as a D2 dopamine receptor antagonist across mesolimbic and mesocortical pathways, with additional activity at D1, D3, D4, serotonin (5-HT2), histamine (H1), muscarinic, and alpha-adrenergic receptors.

The TxGNN model most likely established a connection to retinal dystrophy via the retinal dopaminergic signalling pathway: D4 receptors are expressed in retinal photoreceptors and modulate retinal physiology, including light adaptation. The knowledge graph may have identified this receptor-level overlap as a potential therapeutic link between chlorpromazine's dopaminergic profile and retinal disease.

**This prediction is, however, strongly contraindicated by existing clinical evidence.** Phenothiazine retinopathy — characterised by pigmentary degeneration of the retinal epithelium — is a recognised adverse effect of chlorpromazine, particularly at high cumulative doses (PMID 5647013). The biological association captured by TxGNN reflects a toxic relationship, not a therapeutic one. Prescribing chlorpromazine with the intent of treating retinal dystrophy would carry a direct risk of worsening or inducing retinal damage. This highlights an important limitation of purely graph-based predictions: the model identifies dopamine–retina network proximity without distinguishing therapeutic from iatrogenic mechanisms.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for chlorpromazine in retinal dystrophy with or without extraocular anomalies.

---

## Literature Evidence

The 15 publications retrieved for this indication do not support a therapeutic role for chlorpromazine in retinal dystrophy. They cover general extraocular anomalies, congenital ocular conditions, and orbital pathologies retrieved via broad keyword matching. The single entry with direct drug relevance documents phenothiazine-induced retinal toxicity — the inverse of a therapeutic effect.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [5647013](https://pubmed.ncbi.nlm.nih.gov/5647013/) | 1968 | Case Series | *Ophthalmologica* | Phenothiazine-retinopathy: chlorpromazine documented as a cause of retinal pigmentary damage, **not** a treatment |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | *Pediatric Radiology* | Differential diagnosis and imaging of paediatric orbital and ocular pathologies; no chlorpromazine relevance |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | *Taiwan Journal of Ophthalmology* | Congenital anomalies of lens shape; no drug therapy relevance |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Original Research | *Int J Molecular Sciences* | Optic nerve and retinal abnormalities in congenital fibrosis of extraocular muscles (CFEOM); genetic basis (KIF21A, TUBB3) |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Clinical Study | *American Journal of Ophthalmology* | Pathogenesis of maculopathy associated with cavitary optic disc anomalies; no pharmacotherapy content |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | *J Neuro-Ophthalmology* | Congenital trochlear-oculomotor synkinesis in a 6-year-old; structural anomaly, not drug-related |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | *Klin Monatsbl Augenheilkd* | Congenital ptosis: surgical management; no pharmacotherapy relevance |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Clinical Review | *Seminars in Neurology* | Systematic approach to diplopia evaluation; no drug treatment content |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | *Optometry and Vision Science* | Variable synergistic divergence in congenital fibrosis of extraocular muscles |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review/Case Series | *Archives of Ophthalmology* | Clinical features and management of orbital arteriovenous malformations |

---

## UK Market Information

No MHRA marketing authorisations for chlorpromazine were found in this dataset.

> **Note for clinicians:** Chlorpromazine hydrochloride (brand name Largactil, and generic preparations) has a long history of availability in the UK as a licensed antipsychotic. The absence of records in this dataset likely reflects a data retrieval limitation rather than genuine market absence. Current authorisation status, indications, and prescribing information should be confirmed directly via the [MHRA Product Licences database](https://products.mhra.gov.uk/) and the BNF (Section 4.2.1: Antipsychotic drugs).

---

## Safety Considerations

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

> **Critical safety alert relevant to this prediction:** Chlorpromazine carries a well-documented risk of **phenothiazine retinopathy** (pigmentary degeneration of the retinal epithelium) at high or prolonged doses. This makes the primary TxGNN prediction of benefit in retinal dystrophy not only unsupported but potentially harmful. Prescribers should consider baseline and periodic ophthalmic review for patients on long-term chlorpromazine therapy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction is mechanistically inverted: chlorpromazine is a recognised cause of retinal toxicity and cannot be recommended as a therapeutic candidate for retinal dystrophy. Predictions ranked 1 through 9 all carry evidence level L5 (model prediction only, no supporting clinical or preclinical data), and several involve irreversible structural congenital conditions (hydranencephaly, polymicrogyria) where pharmacological intervention has no plausible disease-modifying mechanism.

**Most actionable finding — Rank 10: Early-Onset Schizophrenia (L3, Proceed with Guardrails)**

The only prediction in this Evidence Pack with actionable evidence is early-onset schizophrenia (rank 10, TxGNN score 99.47%). Chlorpromazine's D2 antagonism is directly relevant to the dopaminergic hyperactivity hypothesis of schizophrenia, and the mechanism is identical across adult-onset and early-onset subtypes. Pharmacogenetic studies (PMID 18408624; PMID 17915974) further support chlorpromazine's pharmacological relevance in this population. This represents an extension to a paediatric/early-onset subpopulation rather than classical repurposing, but warrants structured evaluation given the unmet need in treatment-resistant early-onset cases.

**To proceed with any further evaluation, the following is needed:**

- Confirm current UK marketing authorisation status via MHRA and BNF — particularly whether any existing licence covers early-onset or paediatric indications
- Retrieve full MOA data from DrugBank (DB00477) to strengthen mechanistic rationale
- For early-onset schizophrenia: obtain paediatric dosing, pharmacokinetic, and extrapyramidal side-effect data (young patients have heightened sensitivity to tardive dyskinesia and acute dystonic reactions)
- Conduct a systematic literature review specifically for chlorpromazine in paediatric psychosis to establish whether L2 or L1 evidence already exists outside this dataset
- For rank 1 prediction (retinal dystrophy): formally record this as a **contraindicated direction** in the project's candidate database, to prevent recurrence in future automated scoring cycles

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require formal clinical validation before therapeutic application. Adverse events should be reported via the MHRA Yellow Card Scheme.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

