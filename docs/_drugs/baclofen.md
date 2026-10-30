---
layout: default
title: Baclofen
parent: Model Prediction Only (L5)
nav_order: 92
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
description: "Baclofen: predicted new indication Attention deficit-hyperactivity disorder (evidence level L5). Approved use: Muscle spasticity"
monitor_inn: "Baclofen"
predicted_indications: ["attention deficit-hyperactivity disorder", "nicotine dependence"]
---

# Baclofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Baclofen: From Spasticity to Attention Deficit-Hyperactivity Disorder
{: .text-alpha }

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist, widely used to treat muscle spasticity. The TxGNN model predicts it may be useful for **attention deficit-hyperactivity disorder (ADHD)**, but **no clinical trials** and **no ADHD-specific publications** currently support this prediction. The evidence is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Muscle spasticity (the MHRA record compiled for this report carries no indication text; this is taken from the literature) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 0.9932 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Baclofen is known to be a GABA-B receptor agonist. GABA is the brain's main inhibitory neurotransmitter, and baclofen's effect on spasticity comes from dampening excitatory signalling in the spinal cord.

A plausible link to ADHD is that GABA-B stimulation may modulate dopamine and glutamate signalling in frontostriatal circuits, which are involved in attention and impulse control. This is a hypothesis, not a demonstrated effect.

The supplied literature does not test baclofen in ADHD. The articles concern Tourette syndrome (where ADHD is a common comorbidity), rodent studies of impulsivity and decision-making, EEG work in a rat model, and methylphenidate prescribing in adults. The high TxGNN score is likely driven by network associations rather than direct clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these publications tests baclofen in people with ADHD.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Clinical report/Review | J Child Neurol | Baclofen with botulinum toxin A reported for tics in 450 patients with tic disorders or Tourette syndrome. Not an ADHD study. |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | Int Rev Neurobiol | Emerging treatments for Tourette syndrome, with ADHD noted as a common comorbidity |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatr Drugs | Clinical features and management of Tourette syndrome, including comorbid psychiatric conditions |
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Review/Meta-analysis | Cureus | Behavioural therapy, antipsychotics and alpha agonists for tics. Not specific to ADHD. |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Observational | L'Encephale | Supervised off-label methylphenidate prescribing in adult ADHD. Baclofen not involved. |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Preclinical | Brain Res | EEG responses to neurotransmitter agonists in a rat ADHD model |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Preclinical | Psychopharmacology | Alpha-2A noradrenergic stimulation in the ventral hippocampus reduced impulsive decision-making in rodents |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Preclinical | Neuropsychopharmacology | Brain regions involved in effort-based decision-making in rodents |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Preclinical | Eur J Neurosci | Habenula function in social play behaviour in rats |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1002020C0AAABAB | Baclofen oral solution 5mg/5ml sugar free | Oral solution | Not listed in the record |

Check the current BNF entry and the SmPC for the licensed indications. No NICE appraisal of baclofen for ADHD is included in the data compiled for this report.

---

## Safety Considerations

**Knowledge-graph contraindication signals** (derived from drug-disease links in the TxGNN knowledge graph, not from product label text):
- Epilepsy
- Kidney disease
- Psychotic and related disorders (psychotic disorder, schizophrenia, schizophreniform disorder, schizoaffective disorder, mental disorder)
- Stroke and cerebrovascular disorders (including cerebral infarction)
- Autonomic nervous system disorders (including autonomic dysreflexia and Horner syndrome)
- Bladder-neck and urinary tract conditions (disease of neck of urinary bladder, pyoureter)

Epilepsy and psychotic disorders are the most relevant to an ADHD population, because both may co-occur with ADHD.

**Drug Interactions** (100 interactions recorded; main ones shown):
- **Major:** morphine, liposomal morphine
- **Moderate:** dronabinol, nabilone, metoclopramide, opium, sibutramine, difenoxin, diphenoxylate

Several of these are central nervous system depressants or opioids, so additive sedation and respiratory depression should be considered.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ADHD prediction rests on a model score alone, with no registered trials and no ADHD-specific publications. Epilepsy and psychotic disorders are also relevant to this population.

**To proceed, the following is needed:**
- Direct preclinical or clinical evidence of baclofen in ADHD
- Detailed mechanism of action data linking GABA-B signalling to ADHD pathophysiology
- Review of the SmPC warnings and contraindications for paediatric and adult ADHD populations
- A safety plan covering sedation and co-prescribed medicines

**Note on the second-ranked prediction:** Baclofen is also predicted for **nicotine dependence** (score 0.9919, evidence level L2). Three Phase 2 trials exist (NCT01228994, NCT00257894, NCT01821560): two were terminated early and one was completed, and none reported results in the data compiled. Rodent studies also support an effect on nicotine reward and withdrawal. This is a more evidence-supported research question than ADHD and could be assessed in a separate report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

