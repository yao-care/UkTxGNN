---
layout: default
title: Midodrine
parent: Model Prediction Only (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Midodrine"
predicted_indications: ["variably protease-sensitive prionopathy", "faciodigitogenital syndrome", "attention deficit-hyperactivity disorder", "hypotensive disorder", "attention deficit hyperactivity disorder, inattentive type", "sinoatrial node disease", "monogenic obesity", "specific developmental disorder", "obsolete hypertelorism (disease)", "sinoatrial block"]
description: "Midodrine: predicted new indication Variably protease-sensitive prionopathy (evidence level L5). Approved use: Not recorded in the local data"
---

# Midodrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Midodrine: Variably protease-sensitive prionopathy
{: .text-alpha }

## One-Sentence Summary

The TxGNN model predicts it may be effective for **hypotensive disorder**, with **1 clinical trial** and **18 publications** currently supporting this direction.
This prediction largely overlaps with the existing indication, so it is not a true novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Variably protease-sensitive prionopathy |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, midodrine is a prodrug whose active metabolite, desglymidodrine, is a peripheral alpha-1 agonist. It increases arterial and venous vascular tone and raises blood pressure.

Orthostatic hypotension and the broader category of hypotensive disorder share the same underlying problem: inadequate blood pressure regulation. A pressor mechanism is therefore directly applicable. A Phase 2 trial has examined normalising blood pressure in hypotensive people with spinal cord injury, and several guidelines and reviews cover midodrine in orthostatic hypotension management.

Because this prediction overlaps with the existing labelled use, it should be treated as an extension or confirmation of known use rather than a novel repurposing opportunity. The evidence level is capped at L2 because the only listed trial is a single Phase 2 study (n=21), with no Phase 3 RCT identified.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02893553](https://clinicaltrials.gov/study/NCT02893553) | Phase 2 | Completed | 21 | Effect of normalising blood pressure on cerebral blood flow in hypotensive individuals with spinal cord injury (2016-12 to 2021-12). Relevant to hypotension and pressor-based treatment, but the small sample and cerebral blood flow endpoint limit generalisability. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25644760](https://pubmed.ncbi.nlm.nih.gov/25644760/) | 2015 | Randomised trial | Hepatology | Terlipressin plus albumin compared with midodrine and octreotide plus albumin for hepatorenal syndrome |
| [38205630](https://pubmed.ncbi.nlm.nih.gov/38205630/) | 2024 | Scientific statement | Hypertension | AHA statement on orthostatic hypotension in adults with hypertension |
| [38123372](https://pubmed.ncbi.nlm.nih.gov/38123372/) | 2024 | Review / expert position | Revue Neurologique | Review and expert position on orthostatic hypotension, including difficult cases with supine hypertension |
| [28050656](https://pubmed.ncbi.nlm.nih.gov/28050656/) | 2017 | Consensus panel | Journal of Neurology | Recommendations for screening, diagnosis and treatment of neurogenic orthostatic hypotension and associated supine hypertension |
| [41941194](https://pubmed.ncbi.nlm.nih.gov/41941194/) | 2026 | Review | JAMA Internal Medicine | Management of orthostatic hypotension, including coexisting supine hypertension and postprandial hypotension |
| [32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/) | 2020 | Review | Autonomic Neuroscience | Pharmacological treatment of neurogenic orthostatic hypotension |
| [31996627](https://pubmed.ncbi.nlm.nih.gov/31996627/) | 2020 | Review | Continuum | Management of orthostatic hypotension, with emphasis on the neurogenic form |
| [35029940](https://pubmed.ncbi.nlm.nih.gov/35029940/) | 2022 | Review | American Family Physician | Practical approach to orthostatic hypotension |
| [42635998](https://pubmed.ncbi.nlm.nih.gov/42635998/) | 2026 | Review | JAMA | Review of postural orthostatic tachycardia syndrome (POTS) |
| [37978969](https://pubmed.ncbi.nlm.nih.gov/37978969/) | 2024 | Clinical practice update | Gastroenterology | AGA update on vasoactive drugs and albumin in cirrhosis |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0207020Y0AAADAD | Midodrine HCl tablets 5 mg | Tablet (not specified in the data) | Not specified in the data compiled for this report |

One valid single-ingredient authorisation is recorded. Details of the approved indication, dosage form and manufacturer should be confirmed against the MHRA record, the SmPC and the BNF.

---

## Safety Considerations

- **Knowledge-graph contraindications** (from drug–disease contraindication links, not label text): phaeochromocytoma (adrenal gland), sympathetic paraganglioma, thyrotoxicosis, hyperthyroidism, Graves' disease, and several cancers (duodenum, small intestine, heart, adrenal gland).
- **Drug interactions:** 81 interactions are recorded. Examples of moderate-level interactions include:
  - other sympathomimetics and vasoconstrictors: epinephrine (including ophthalmic and topical forms), ephedrine, phentermine, diethylpropion, mazindol, sibutramine, isometheptene
  - others: bupropion, lorcaserin, trospium, rolapitant, glycerol phenylbutyrate
  - Minor-level examples: ranitidine, cimetidine, metformin
- **Clinical cautions** (from general pharmacology): supine hypertension, urinary retention and reflex bradycardia. Caution is especially warranted in patients with sinus node dysfunction, and with beta-blockers or cardiac glycosides.

Please refer to the SmPC and BNF for complete safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is direct and biologically coherent, and a completed Phase 2 trial plus multiple guidelines and reviews support pressor-based management of hypotension. However, this overlaps with midodrine's existing use, and the supporting trial is small (n=21), so evidence is limited to L2.

**To proceed, the following is needed:**
- Confirmation of the approved indication, dosage form and manufacturer for the UK authorisation (MHRA / SmPC)
- Label-based warnings and contraindications from the SmPC and BNF
- Mechanism of action data (DrugBank)
- Phase 3 RCT evidence, or a clear definition of which hypotensive population would be targeted beyond the current indication
- A monitoring plan for supine hypertension, heart rate and urinary retention, and a review of interacting medicines

---

*Other predicted indications (variably protease-sensitive prionopathy, faciodigitogenital syndrome, ADHD and its inattentive subtype, sinoatrial node disease and block, monogenic obesity, specific developmental disorder, hypertelorism) have model predictions only, with no supporting trials or no plausible mechanism, and are recommended as **Hold**. Midodrine's bradycardic effect makes the sinoatrial conditions a potential safety concern rather than an opportunity.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

