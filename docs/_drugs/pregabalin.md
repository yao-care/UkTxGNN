---
layout: default
title: Pregabalin
parent: Model Prediction Only (L5)
nav_order: 516
evidence_level: L5
indication_count: 6
---

# Pregabalin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Pregabalin: From Anxiety Disorder, Fibromyalgia and Neuropathic Pain to Tendinitis

## One-Sentence Summary

Pregabalin is a gabapentinoid, originally used for anxiety disorder, fibromyalgia, myofascial pain syndrome and postherpetic neuralgia.
The TxGNN model predicts it may be effective for **tendinitis**, but there are **no clinical trials** and **no publications that test pregabalin as a treatment for tendon inflammation**. The prediction is supported by mechanistic plausibility only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder, fibromyalgia, myofascial pain syndrome, postherpetic neuralgia (from the TxGNN knowledge graph, as no indication text is recorded in the UK licence data) |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 (mechanistic plausibility only; no tendinitis-specific studies) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Pregabalin is generally understood to bind the alpha2-delta subunit of voltage-gated calcium channels. This reduces the release of excitatory neurotransmitters and may relieve neuropathic and nociceptive pain.

Its established uses are pain-dominant conditions (fibromyalgia, myofascial pain, postherpetic neuralgia). Tendinitis is a painful musculoskeletal condition, so a pain-pathway overlap is plausible. The high TxGNN score probably reflects this overlap rather than any tendinopathy-specific evidence.

The retrieved literature does not show that pregabalin treats tendon inflammation itself. It concerns postoperative pain after shoulder surgery, nerve impingement and a drug-associated disability syndrome. Any benefit would most likely be symptomatic pain relief, not disease modification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for tendinitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Compared perioperative oral pregabalin with interscalene brachial plexus block after arthroscopic rotator cuff repair, looking at postoperative pain, opioid use and satisfaction. The abstract reports the aim only, not results. This is surgical analgesia, not tendinitis treatment. |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Retrospective cohort | J Orthop Sci | Assessed analgesic efficacy and opioid-sparing effect of pregabalin after rotator cuff repair. Earlier studies on opioid sparing have conflicting results. |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Case report/Review | Praxis | Fluoroquinolone-associated disability after ciprofloxacin. Tendinopathy is a fluoroquinolone side effect; this is not about pregabalin treatment. |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial | Arthroscopy | Piriformis syndrome and its diagnosis and surgical release. No direct pregabalin evidence. |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case report | Pain Pract | Posterior femoral cutaneous nerve impingement after a marathon, with hamstring tendonitis as the cause. Not about pregabalin efficacy. |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclinical (animal) | Adv Pharmacol Pharm Sci | Plant extract reduced vincristine-induced neuropathy in rats. Not about pregabalin or tendinitis. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0408010AEAAAAAA (as recorded; a code rather than a standard PL number) | Pregabalin 25 mg capsules | Capsule | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN graph, not from label text, so they must be checked against the SmPC): anxiety disorder, neurotic disorder, dysthymic disorder, thrombocytopenia, angioedema (including acquired, hereditary, non-histaminic and RAAS-blocker-induced forms), myopathy and other muscle diseases, familial periodic paralysis, rhabdomyolysis, nodular fasciitis, impaired renal function and atrioventricular block.
- **Drug interactions**: The interaction database returned 100 records. Of the 20 reviewed, the main ones are:
  - **Major**: morphine and liposomal morphine.
  - **Moderate**: pioglitazone, rosiglitazone, troglitazone, difenoxin, diphenoxylate, dronabinol, nabilone, metoclopramide, opium and sibutramine.
  - Other entries are of unknown severity.
- **Reported adverse effects in the retrieved literature**: sexual dysfunction (mostly dose-related) and sedation.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The very high model score is a computational signal only. No trials or tendinitis-specific studies support it, and the retrieved literature addresses perioperative pain and unrelated conditions. The knowledge-graph contraindication signals (muscle disease, rhabdomyolysis) also warrant caution in a musculoskeletal setting.

**To proceed, the following is needed:**
- Controlled studies of pregabalin in tendinopathy or tendinitis, with pain and function outcomes
- Mechanism-of-action data and SmPC-based warnings and contraindications
- UK licence details (approved indications and formulations) for the authorisation recorded
- Review of the muscle-related contraindication signals and the major opioid interaction

**Note on other predictions:** In the same candidate list, **migraine disorder** has stronger support (evidence level L2). It has randomised trials in paediatric migraine prophylaxis against propranolol and sodium valproate, and a network meta-analysis. The only Phase 3 registration (NCT00447369) was withdrawn and provides no data. Migraine may merit a separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

