---
layout: default
title: Hydromorphone
parent: Moderate Evidence (L3-L4)
nav_order: 325
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-15
description: "Hydromorphone: predicted new indication Pharyngitis (evidence level L4). Approved use: Common cold"
monitor_inn: "Hydromorphone"
predicted_indications: ["pharyngitis", "allergic urticaria", "nasal cavity disease", "acute laryngopharyngitis", "headache disorder", "trigeminal autonomic cephalalgia"]
---

# Hydromorphone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Hydromorphone: From Common Cold to Pharyngitis

## One-Sentence Summary

Hydromorphone is a strong opioid analgesic (mu-opioid agonist). The knowledge graph lists its original indications as common cold and nasopharyngitis.
The TxGNN model predicts it may be useful for **pharyngitis**, but the **3 linked clinical trials** study post-tonsillectomy pain rather than pharyngitis, and **no publications** were found for this prediction. Evidence is therefore very limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Common cold; nasopharyngitis (from the knowledge graph; no approved indication text is available for the UK product) |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hydromorphone is a mu-opioid receptor agonist that acts centrally to relieve pain and suppress cough. Its original indications in the knowledge graph (common cold, nasopharyngitis) are upper respiratory conditions, and pharyngitis is closely related to both.

The link is probably symptomatic only. Hydromorphone has no antimicrobial or anti-inflammatory action against the cause of pharyngitis. The three linked trials involve pain after tonsillectomy, which is surgical pain and not pharyngitis as a disease. The high TxGNN score most likely reflects the closeness of pharyngitis to the cold and nasopharyngitis indications in the network, and not trial data on pharyngitis itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04230681](https://clinicaltrials.gov/study/NCT04230681) | Early Phase 1 | Completed | 189 | Hydromorphone vs fentanyl for pain after tonsillectomy or adenotonsillectomy in children. The condition is surgical pain, not pharyngitis. |
| [NCT05244226](https://clinicaltrials.gov/study/NCT05244226) | Phase 2 | Completed | 66 | Short-acting opioids (fentanyl/hydromorphone) vs methadone for paediatric post-tonsillectomy pain. Hydromorphone is not the studied intervention. |
| [NCT06576830](https://clinicaltrials.gov/study/NCT06576830) | Phase 4 | Recruiting | 440 | Single-dose intraoperative methadone vs short-acting opioids (fentanyl/hydromorphone) in paediatric tonsillectomy. Little relevance to hydromorphone for pharyngitis. |

All three trials were graded as having low relevance (grade C) to this prediction.

---

## UK Market Information

One valid single-ingredient marketing authorisation is recorded for hydromorphone. The data compiled for this report contain no dosage form or approved indication text for it.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 040702050AAADAD | Hydromorphone HCl capsule 2.6 mg | Capsule | Not available |

---

## Safety Considerations

**Contraindications (from knowledge graph drug-disease edges, not label text):** the knowledge graph links hydromorphone with the following conditions, which warrant caution or avoidance:
- Hepatic and renal: liver failure, liver disease, kidney disease
- Respiratory and cardiovascular: respiratory failure, hypotensive disorder, sudden cardiac arrest, heart conduction disease
- Neurological: epilepsy
- Endocrine: hypothyroidism (including myxedema and congenital hypothyroidism), and adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia)
- Gastrointestinal: inflammatory bowel disease, ulcerative colitis, constipation, gallbladder disease
- Genitourinary: benign prostatic hyperplasia, pyoureter
- Other: substance-related disorder and drug dependence, butyrylcholinesterase deficiency

**Drug Interactions:** 100 interactions were identified. The major-level interactions in the listed results are:
- Alvimopan
- Bupropion
- Morphine
- Naltrexone

Moderate-level interactions include anticholinergics (hyoscyamine, atropine, glycopyrronium, dicyclomine, trospium), loperamide, eluxadoline, naloxone, cimetidine, cannabinoids (dronabinol, nabilone), 5-HT3 antagonists (dolasetron, palonosetron) and bowel-preparation agents.

For full safety information, please refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Other Predicted Indications (for context)

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Allergic urticaria | 99.81% | L5 | No evidence. Opioids can release histamine and cause urticaria, so worsening is more likely than benefit. |
| Nasal cavity disease | 99.80% | L5 | No evidence and no defined mechanism. |
| Acute laryngopharyngitis | 99.75% | L5 | No evidence. Central antitussive effect may ease cough but does not treat the underlying condition. |
| Headache disorder | 99.65% | L3 | The only prediction with a completed trial (NCT02389829, Phase 4, n=127) and published studies. Hydromorphone was less effective than prochlorperazine plus diphenhydramine, and guidelines advise against routine opioid use for acute migraine. This is a real but unfavourable use, not a recommended repurposing. |
| Trigeminal autonomic cephalalgia | 99.58% | L5 | No evidence. Opioids are not recommended for cluster headache, and established therapies exist. |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pharyngitis prediction rests on a high model score alone. The linked trials address post-tonsillectomy pain, not pharyngitis, and no literature supports it. Hydromorphone also carries significant risks (respiratory depression, dependence, many interactions), which are hard to justify for a usually self-limiting condition with safer symptomatic options.

**To proceed, the following is needed:**
- Trials or literature that directly assess hydromorphone in pharyngitis (not post-surgical pain)
- Mechanism of action data and a clear rationale beyond symptomatic analgesia
- Approved indication text, dosage form and SmPC warnings and contraindications for the UK product
- A benefit-risk assessment against established first-line options for sore throat
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

