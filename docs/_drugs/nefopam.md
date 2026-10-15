---
layout: default
title: Nefopam
parent: Model Prediction Only (L5)
nav_order: 438
evidence_level: L5
indication_count: 10
---

# Nefopam
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

# Nefopam: From Analgesia to Lumbar Spinal Stenosis (Perioperative Pain)

## One-Sentence Summary

Nefopam is a centrally acting non-opioid analgesic marketed in the UK as a 30 mg tablet.
The TxGNN model's top-ranked predictions are cataract-related conditions (mature cataract and others), none of which has any supporting evidence. The only prediction with published literature is **lumbar spinal stenosis**, with **0 registered clinical trials** and **4 publications** (mostly perioperative pain studies).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (nefopam is a non-opioid analgesic) |
| Predicted New Indication | Mature cataract (top-ranked prediction, no supporting evidence). The only prediction with literature is lumbar spinal stenosis (rank 10), discussed below |
| TxGNN Prediction Score | 99.98% (mature cataract); 99.97% (lumbar spinal stenosis) |
| Evidence Level | L5 for mature cataract and the other cataract predictions; L4 for lumbar spinal stenosis |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold (cataract predictions); lumbar spinal stenosis is a research question only |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, nefopam is a centrally acting non-opioid analgesic. It inhibits serotonin, noradrenaline and dopamine reuptake and modulates voltage-gated sodium and calcium channels.

**Cataract predictions (ranks 1-9).** No mechanistic link has been established. Nothing in nefopam's pharmacology is known to affect lens opacification, whether age-related, diabetic, syndromic or tetanic. The uniformly high scores across the cataract group (99.97-99.98%) most likely reflect a shared disease-class signal in the knowledge graph rather than a pharmacological rationale. These should be regarded as model artefacts.

**Lumbar spinal stenosis (rank 10).** The link here is indirect but plausible. Monoamine reuptake inhibition and ion channel modulation may help neuropathic-type pain, dysesthesia and postoperative pain in patients undergoing spine surgery. However, the evidence concerns symptom control around surgery, not modification of the underlying disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

All publications below relate to lumbar spinal stenosis. No literature was available for any cataract prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38068520](https://pubmed.ncbi.nlm.nih.gov/38068520/) | 2023 | Randomised, double-blind study | Journal of Clinical Medicine | 73 patients with lumbar spinal stenosis undergoing spine surgery received nefopam 20 mg or saline before surgery; outcomes were dysesthesia, postoperative pain and satisfaction (results not shown in the available abstract) |
| [41937571](https://pubmed.ncbi.nlm.nih.gov/41937571/) | 2026 | Randomised, double-blind, placebo-controlled trial | Asian Spine Journal | Evaluated the opioid-sparing effect of continuous postoperative intravenous nefopam in multilevel degenerative lumbar spinal fusion (results not shown in the available abstract) |
| [31166320](https://pubmed.ncbi.nlm.nih.gov/31166320/) | 2019 | Clinical study | Zhurnal Voprosy Neirokhirurgii imeni N. N. Burdenko | Compared multimodal perioperative analgesia regimens in spinal stenosis surgery and their effect on failed back surgery syndrome (design not confirmed) |
| [25535527](https://pubmed.ncbi.nlm.nih.gov/25535527/) | 2014 | Case report | Journal of Korean Neurosurgical Society | Status epilepticus in a 71-year-old man after nefopam given around lumbar spinal stenosis surgery; a seizure-risk safety signal |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0407010P0AAABAB (BNF product code, not a PL number) | Nefopam HCl Tab 30mg | Tablet | Not stated in the data compiled |

BNF classification code 0407010 corresponds to the non-opioid analgesics section. Only one valid single-ingredient authorisation is recorded.

---

## Safety Considerations

- **Seizure risk:** The literature includes a case report of status epilepticus associated with nefopam ([PMID 25535527](https://pubmed.ncbi.nlm.nih.gov/25535527/)). Published neurological adverse reactions include confusion, hallucinations, delirium and convulsions, and other reported effects are anticholinergic and cardiovascular.

Please refer to the SmPC and BNF for full warnings, contraindications and drug interaction information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold** (for all cataract predictions); lumbar spinal stenosis is a research question only.

**Rationale:**
- The nine cataract predictions have no trials, no literature and no plausible mechanism, so they rest on model score alone (L5).
- For lumbar spinal stenosis, the evidence supports perioperative analgesia rather than treatment of the disease itself. Study designs have not been fully verified, so it remains L4 and is not graded as RCT-level evidence. The seizure signal also calls for caution.

**To proceed, the following is needed:**
- Mechanism of action data confirmed from DrugBank
- SmPC warnings and contraindications (currently a blocking gap for safety screening)
- Full-text review of the two randomised studies (PMIDs 38068520 and 41937571) to confirm designs, endpoints and results
- Clarification of whether perioperative analgesia in spinal stenosis surgery falls within nefopam's existing analgesic use, which would make it a use-extension question rather than true repurposing
- A seizure-risk assessment for patients undergoing spine surgery
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

