---
layout: default
title: Etoricoxib
parent: Model Prediction Only (L5)
nav_order: 268
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
description: "Etoricoxib: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available in the compiled data (the product's clinical use is gen…"
monitor_inn: "Etoricoxib"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis", "pulmonary hypertension", "benign prostatic hyperplasia (disease)", "kyphoscoliotic heart disease", "headache disorder", "trigeminal autonomic cephalalgia"]
---

# Etoricoxib
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

## Etoricoxib: From Musculoskeletal and Inflammatory Pain to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Etoricoxib is a selective COX-2 inhibitor marketed in the UK as a 60 mg tablet, and its original indication text is not available in the data compiled for this report. The TxGNN model predicts it may be useful for **migraine disorder**, with a very high score. However, **no clinical trials** and only **1 supporting publication** (a scoping review that is not specific to etoricoxib) back this prediction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the product's clinical use is generally rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, gout and acute pain) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

**Other predictions of note.** Headache disorder (score 0.9931) and trigeminal autonomic cephalalgia (score 0.9915) are supported by small case-level literature (L4, "Research Question"). They are the most evidence-supported of the ten predictions, even though they rank lower by score.

---

## Why is This Prediction Reasonable?

Etoricoxib selectively inhibits COX-2, which reduces the synthesis of prostaglandin E2 (PGE2). PGE2 contributes to neurogenic inflammation and trigeminovascular sensitisation in migraine, so the mechanism is plausible. Detailed mechanism-of-action data were not available in the compiled data beyond COX-2 (PTGS2) as the target.

A preclinical study (PMID 29209105) found that NSAIDs, including etoricoxib, affected the release of CGRP and PGE2 from rat trigeminal ganglia. Both molecules are implicated in migraine, which supports the biological rationale. This is not human clinical evidence.

The only literature item linked directly to the top prediction (PMID 42841395) is a scoping review of fasting-induced headache during Ramadan. It does not provide etoricoxib-specific efficacy data in migraine. The high TxGNN score should therefore be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder.

---

## Literature Evidence

Publications for the top prediction (migraine disorder) and the closely related predictions are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35277974](https://pubmed.ncbi.nlm.nih.gov/35277974/) | 2022 | Case series/Observational | Headache | Etoricoxib and celecoxib helped patients with indomethacin-responsive headaches (including some trigeminal autonomic cephalalgias) and may offer a better-tolerated alternative to indomethacin |
| [36893522](https://pubmed.ncbi.nlm.nih.gov/36893522/) | 2023 | Case report | Clinical Neurology and Neurosurgery | Two patients with secondary cough headache responded to etoricoxib |
| [18171381](https://pubmed.ncbi.nlm.nih.gov/18171381/) | 2008 | Case report | European Journal of Neurology | Primary stabbing headache was responsive to etoricoxib |
| [17883876](https://pubmed.ncbi.nlm.nih.gov/17883876/) | 2007 | Case report | Journal of Medical Case Reports | Etoricoxib used to treat an idiopathic stabbing headache |
| [29209105](https://pubmed.ncbi.nlm.nih.gov/29209105/) | 2017 | Preclinical (rat) | Mediators of Inflammation | Nimesulide, etoricoxib and ketoprofen affected CGRP and PGE2 release from rat trigeminal ganglia |
| [42841395](https://pubmed.ncbi.nlm.nih.gov/42841395/) | 2026 | Review | Pain Management | Scoping review of fasting-induced headache in Ramadan; not specific to etoricoxib |
| [25229174](https://pubmed.ncbi.nlm.nih.gov/25229174/) | 2014 | Case report (adverse event) | Clinical Neuropharmacology | Reversible cerebral vasoconstriction syndrome possibly induced by etoricoxib (safety signal) |

None of these is a controlled trial in migraine. The evidence is anecdotal or indirect.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010AJAAAAAA | Etoricoxib Tab 60mg | Tablet | Not available in the compiled data |

One valid single-ingredient authorisation is recorded. Please check the current MHRA record and the BNF for the full licensed indications and the product's formal licence (PL) number.

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed, but it returned only pharmacology target information (COX-2 / PTGS2) and no specific interacting drugs.
- **Safety signals from the literature**: A case report describes life-threatening hyperkalaemia and acute kidney dysfunction with etoricoxib in a patient taking telmisartan on a potassium-rich low-sodium diet (PMID 21373319). Another describes possible reversible cerebral vasoconstriction syndrome (PMID 25229174). Selective COX-2 inhibitors are also associated with cardiovascular risk, fluid retention and blood pressure elevation.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction rests on a model score and a plausible COX-2/prostaglandin mechanism, with no clinical trials and no etoricoxib-specific migraine literature (L5). Case-level reports for other primary headaches (stabbing headache, indomethacin-responsive headaches) are more encouraging, but they are not enough for a recommendation.

**To proceed, the following is needed:**
- Systematic review of existing randomised evidence on COX-2 inhibitors and NSAIDs in acute and preventive migraine treatment
- Confirmation of the licensed UK indications and the SmPC safety information for the authorised product
- Detailed mechanism-of-action data
- A cardiovascular, renal and blood-pressure risk assessment for the intended population
- If pursued, prioritising indomethacin-responsive headaches and trigeminal autonomic cephalalgias as the better-supported research question, ideally through a prospective controlled study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

