---
layout: default
title: Mefenamic Acid
parent: High Evidence (L1-L2)
nav_order: 388
evidence_level: L2
indication_count: 8
last_modified_at: 2026-10-15
description: "Mefenamic Acid: predicted new indication Rheumatoid arthritis (evidence level L2). Approved use: Not available in the data compiled for this report"
---

# Mefenamic Acid
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **8** 
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

# Mefenamic Acid: From Pain and Inflammation to Rheumatoid Arthritis

## One-Sentence Summary

Mefenamic acid is a non-steroidal anti-inflammatory drug (NSAID) that is already marketed in the UK as an oral capsule.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, supported by **no registered clinical trials** but **several older double-blind trials among 20 publications** (1966-1979).
This is closer to an on-class use of an NSAID than true repurposing, and the evidence supports symptom relief only, not disease modification.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Mefenamic acid is an NSAID that inhibits cyclo-oxygenase (COX-1 and COX-2) and so reduces prostaglandin synthesis. Prostaglandins mediate pain and inflammation in rheumatoid arthritis.

Because mefenamic acid is already an established analgesic and anti-inflammatory agent, the prediction is mechanistically plausible. Older double-blind comparator and crossover trials found it comparable to ibuprofen, and superior to placebo, for symptom control. There is no evidence that it modifies the course of the disease.

Better-tolerated NSAIDs are available, and the literature reports gastrointestinal toxicity and autoimmune haemolytic anaemia with mefenamic acid. These limit its appeal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

The supporting studies are older published trials that were not registered. They are listed below.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [373989](https://pubmed.ncbi.nlm.nih.gov/373989/) | 1979 | RCT (double-blind crossover) | Curr Med Res Opin | 24 patients; mefenamic acid 1500 mg/day, sulindac and flurbiprofen were all significantly better than placebo for pain, joint tenderness and morning stiffness |
| [796645](https://pubmed.ncbi.nlm.nih.gov/796645/) | 1976 | RCT (double-blind crossover) | Med J Aust | Mefenamic acid 1500 mg/day compared favourably with ibuprofen 1200 mg/day; side effects were mild and mostly gastrointestinal |
| [330287](https://pubmed.ncbi.nlm.nih.gov/330287/) | 1977 | RCT (double-blind, within-patient) | J Int Med Res | 40 patients; analgesic and anti-inflammatory effects not significantly different from ibuprofen |
| [326491](https://pubmed.ncbi.nlm.nih.gov/326491/) | 1977 | Double-blind crossover | Curr Med Res Opin | 18 patients; mefenamic acid and indomethacin both significantly better than placebo on most parameters |
| [4294443](https://pubmed.ncbi.nlm.nih.gov/4294443/) | 1967 | Clinical study | Ann Rheum Dis | Early clinical study of mefenamic acid in rheumatoid arthritis (no abstract available) |
| [5920657](https://pubmed.ncbi.nlm.nih.gov/5920657/) | 1966 | Comparative study | Br Med J | Mefenamic and flufenamic acid compared with aspirin and phenylbutazone (no abstract available) |
| [1455792](https://pubmed.ncbi.nlm.nih.gov/1455792/) | 1992 | Clinical study | Vopr Kurortol Fizioter Lech Fiz Kult | Electrophoresis of mefenamic acid in 125 patients; complete or partial response in 75% (non-standard delivery route) |
| [5676955](https://pubmed.ncbi.nlm.nih.gov/5676955/) | 1968 | Case report (safety) | Br Med J | Three patients developed autoimmune haemolytic anaemia during mefenamic acid therapy; all recovered on withdrawal |
| [377958](https://pubmed.ncbi.nlm.nih.gov/377958/) | 1979 | Review | Am J Hosp Pharm | Overview of antirheumatic agents, including mefenamic acid |
| [5333309](https://pubmed.ncbi.nlm.nih.gov/5333309/) | 1966 | Review/Monograph | Br Med J | Monograph on mefenamic acid |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010N0AAAAAA | Mefenamic Acid Capsules 250 mg | Capsule | Not stated in the data compiled for this report |

The data compiled for this report list one valid single-ingredient authorisation. The identifier shown appears to be a BNF-style product code rather than a standard PL number. Please check it against the MHRA register.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** hypertension, kidney disease, liver disease, gallbladder disease, active peptic ulcer disease, blood coagulation disorders, myocardial infarction and other cardiovascular or heart disease, and haemoglobinopathy. These should be checked against the SmPC.
- **Drug interactions:** The interaction screen returned 100 interactions, and 20 are listed in the data compiled for this report. They were mostly Moderate and some were Minor. Moderate interactions include:
  - corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
  - aspirin
  - metformin and chlorpropamide
  - mesalazine and balsalazide
  - aprepitant
  - potassium citrate and potassium bicarbonate
  - bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes)
  
  Minor interactions include famotidine, ranitidine, cimetidine, dapagliflozin and linaclotide.
- **Literature-reported safety signals:** gastrointestinal toxicity, autoimmune haemolytic anaemia, and enteropathy with villous atrophy in prolonged use.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several small double-blind trials show symptomatic benefit comparable to other NSAIDs in rheumatoid arthritis. However, they are old, small and unregistered, and show no disease modification. The drug is already an established NSAID, so the incremental value is limited.

**To proceed, the following is needed:**
- The approved indication text and product details from the SmPC, which are missing from the data compiled for this report
- Confirmation of the mechanism of action data
- The warnings and contraindications from the SmPC and BNF, which are currently missing
- A comparison against currently preferred NSAIDs and a review of whether it adds value in current UK practice
- A gastrointestinal, cardiovascular, renal and haematological safety monitoring plan

---

### Other predicted indications (for information)

| Predicted Indication | Evidence Level | Note |
|------|------|------|
| Migraine disorder | L2 | Double-blind trials in acute, prophylactic and menstrual migraine; small, older studies |
| Headache disorder | L2 | Evidence is mostly migraine-specific |
| Migraine with brainstem aura | L4 | Indirect evidence only |
| Osteoarthritis susceptibility | L5 | A genetic risk concept and not a treatable condition; no studies |
| Trigeminal autonomic cephalalgia | L5 | Speculative link; no studies |
| Colobomatous microphthalmia-rhizomelic dysplasia syndrome | L5 | Likely a model artefact |
| Brachydactyly-syndactyly syndrome | L5 | Likely a model artefact |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

