---
layout: default
title: Selegiline
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 4
---

# Selegiline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Selegiline: From Parkinson's Disease to Schizophrenia

---

## One-Sentence Summary

Selegiline is a selective, irreversible MAO-B (monoamine oxidase type B) inhibitor, approved in multiple countries for Parkinson's Disease (oral formulation) and major depressive disorder (transdermal formulation), as confirmed by published literature.

The TxGNN model generated four repurposing predictions; the highest-ranked by score (rank 1: polymicrogyria with cerebellar hypoplasia and arthrogryposis) has no supporting evidence and is on hold. The most evidenced prediction — and the focus of this report — is **Schizophrenia** (negative symptoms, rank 2), with **1 registered clinical trial** and **20 publications** supporting this direction, corresponding to a TxGNN score of **99.14%** and an evidence level of **L2**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's Disease (oral); Major Depressive Disorder (transdermal) — sourced from published literature; not present in UK MHRA dataset |
| Predicted New Indication | Schizophrenia (negative symptoms) |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L2 |
| UK Market Status | Not found in MHRA marketing authorisation dataset (verification recommended) |
| Number of Marketing Authorisations | 0 (per current MHRA dataset) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current UK regulatory dataset for selegiline. Based on published literature — including the systematic review and meta-analysis by Rossano et al. (PMID 37087864) — selegiline is an irreversible, selective inhibitor of monoamine oxidase type B (MAO-B), the mitochondrial enzyme primarily responsible for oxidative deamination of dopamine in the basal ganglia and prefrontal cortex. Its efficacy in Parkinson's Disease, where progressive dopaminergic neuronal loss is the defining pathology, is well established. At standard oral doses (5–10 mg/day), selectivity for MAO-B is maintained; at doses ≥20 mg/day, selectivity is lost and non-selective MAOI activity emerges.

The mechanistic rationale for schizophrenia centres on the **hypodopaminergic hypothesis of negative symptoms**. Negative symptoms — flat affect, alogia, avolition, and anhedonia — are associated with insufficient dopaminergic tone in mesocortical pathways, particularly the prefrontal cortex. This is precisely the circuit that conventional D2-antagonist antipsychotics fail to adequately address, and may inadvertently worsen. By inhibiting MAO-B at selective doses, selegiline raises dopamine concentrations in these mesocortical regions, directly targeting the mechanistic deficit underlying negative symptoms. Two secondary mechanisms further support this rationale: first, reduced degradation of phenylethylamine (an endogenous trace amine independently implicated in schizophrenic negative symptoms); and second, antioxidant neuroprotection through attenuation of free-radical-mediated damage to dopaminergic neurones — a mechanism consistent with growing evidence that oxidative stress contributes to neuroprogression in schizophrenia.

The use of selegiline as an **augmentation** to existing antipsychotic therapy is pharmacologically coherent: it targets a complementary mechanism rather than duplicating existing D2 blockade, addressing a gap that standard treatment leaves unmet. This rationale is empirically supported by a multicentre, double-blind, placebo-controlled RCT (PMID 15677608), a further double-blind RCT augmenting risperidone (PMID 17972359), and a 2023 systematic review and meta-analysis spanning multiple psychiatric indications (PMID 37087864).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00456976](https://clinicaltrials.gov/study/NCT00456976) | Early Phase 1 | Completed | 70 | Randomised, placebo-controlled trial of selegiline augmentation of antipsychotic medication in inpatients with chronic schizophrenia. Primary endpoint: reduction in negative symptom scores. Design consistent with an augmentation proof-of-concept study; results should be reviewed alongside the published double-blind RCT (PMID 15677608), with which this trial may have methodological overlap. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15677608](https://pubmed.ncbi.nlm.nih.gov/15677608/) | 2005 | RCT (double-blind, placebo-controlled, multicentre) | American Journal of Psychiatry | Selegiline augmentation of antipsychotics in schizophrenia outpatients with moderate-to-severe negative symptoms; the primary pivotal reference for this repurposing indication |
| [17972359](https://pubmed.ncbi.nlm.nih.gov/17972359/) | 2008 | RCT | Human Psychopharmacology | 8-week double-blind, randomised, placebo-controlled trial of selegiline added to risperidone in chronic schizophrenia with prominent negative symptoms |
| [8627275](https://pubmed.ncbi.nlm.nih.gov/8627275/) | 1996 | Controlled study | Journal of Nervous and Mental Disease | Open pilot of low-dose selegiline (5 mg twice daily) augmentation in 21 patients with chronic schizophrenia or schizoaffective disorder; improvement in negative symptoms without significant adverse effects, providing early proof of concept |
| [8102552](https://pubmed.ncbi.nlm.nih.gov/8102552/) | 1993 | RCT | Biological Psychiatry | Placebo-controlled 6-week trial of selegiline 10 mg/day in 33 patients for neuroleptic-induced tardive dyskinesia; secondary assessment of positive and negative symptom scores |
| [37087864](https://pubmed.ncbi.nlm.nih.gov/37087864/) | 2023 | Systematic review & meta-analysis | European Neuropsychopharmacology | Comprehensive appraisal of oral and transdermal selegiline across psychiatric conditions; synthesises evidence from multiple formulations and indications including schizophrenia |
| [26848926](https://pubmed.ncbi.nlm.nih.gov/26848926/) | 2016 | Cochrane systematic review | Cochrane Database of Systematic Reviews | Reviews antioxidant treatments for schizophrenia; discusses selegiline's secondary neuroprotective mechanism via oxidative stress reduction as a rationale for its use in schizophrenia |
| [17405823](https://pubmed.ncbi.nlm.nih.gov/17405823/) | 2007 | Review | Annals of Pharmacotherapy | Evaluates the clinical evidence for selegiline specifically in the treatment of negative symptoms in schizophrenia; contextualises available trial data for clinical practice |
| [16930948](https://pubmed.ncbi.nlm.nih.gov/16930948/) | 2006 | Systematic review | Schizophrenia Research | Systematic review of pharmacological options for primary negative symptoms; places selegiline augmentation in the context of available treatment strategies |
| [10080262](https://pubmed.ncbi.nlm.nih.gov/10080262/) | 1999 | Case series | Comprehensive Psychiatry | Three patients with DSM-IV schizophrenia in a continuing day treatment programme showed significant improvement in negative symptoms and overall functioning following selegiline addition to antipsychotic regimen; no adverse effects observed |
| [7831475](https://pubmed.ncbi.nlm.nih.gov/7831475/) | 1994 | Review | Progress in Neurobiology | Mechanistic review of MAO-B inhibitors including selegiline; discusses pharmacological basis for applications in neurological and psychiatric disorders beyond Parkinson's Disease |

---

## Safety Considerations

Detailed UK-specific safety data — including MHRA-approved warnings, contraindications, and drug interaction information — were not available in this Evidence Pack.

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

**Additional safety considerations specific to this repurposing context:**

- **Dose-dependent selectivity**: At oral doses ≤10 mg/day, selegiline retains MAO-B selectivity and dietary tyramine restrictions are generally not required. At doses ≥20 mg/day, selectivity is lost, necessitating dietary and drug interaction precautions applicable to non-selective MAOIs. Augmentation studies have consistently used the selective range (5–10 mg/day).
- **Serotonergic interactions**: Combination with serotonergic antidepressants (SSRIs, SNRIs, TCAs) carries a risk of serotonin syndrome — clinically important given the frequency of comorbid depression in schizophrenia and common co-prescription.
- **Interaction with pethidine**: Contraindicated in combination with pethidine (opioid analgesic); this is a class effect of MAOIs and should be communicated to the clinical team.
- **Polypharmacy monitoring**: Patients with schizophrenia are frequently prescribed multiple psychoactive agents; a full medicines reconciliation is essential before initiating selegiline augmentation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The pharmacological basis for selegiline augmentation in schizophrenia is mechanistically coherent and empirically supported by multiple randomised controlled trials — including a multicentre, double-blind, placebo-controlled RCT published in the *American Journal of Psychiatry* (PMID 15677608), a further double-blind RCT of selegiline added to risperidone (PMID 17972359), and a 2023 systematic review and meta-analysis (PMID 37087864) — directly addressing the unmet clinical need of negative symptoms that current antipsychotic monotherapy fails to adequately treat.

**To proceed, the following is needed:**

- **Verify UK licensing status**: Conduct a direct search of the MHRA's Interactive Product Information database and BNF. Selegiline-containing products may hold current UK marketing authorisations not captured in this dataset; unlicensed use protocols would apply if absent.
- **Obtain and review the SmPC**: Confirm current contraindications, warnings, and approved posology for the UK-licensed formulation.
- **Define the augmentation protocol**: Confirm dose (5–10 mg/day oral to maintain MAO-B selectivity), titration schedule, and duration based on the published RCT designs.
- **Conduct a full drug interaction review**: Assess all co-prescribed medications for serotonergic and MAOI interaction potential; liaise with clinical pharmacy.
- **Review NICE guidance on schizophrenia (NG185)**: Determine whether off-label use requires a shared care agreement, individual funding request, or formal governance approval.
- **Establish a safety monitoring plan**: Specify monitoring parameters, frequency of review, and stopping criteria for augmentation use in a real-world UK clinical setting.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

