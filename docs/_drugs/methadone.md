---
layout: default
title: Methadone
parent: Moderate Evidence (L3-L4)
nav_order: 398
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Methadone: predicted new indication Tourette syndrome (evidence level L4). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Methadone"
predicted_indications: ["Tourette syndrome", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "headache disorder", "manic bipolar affective disorder", "trigeminal autonomic cephalalgia", "common cold", "migraine disorder", "fibromyalgia", "idiopathic granulomatous myositis"]
---

# Methadone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Methadone: From Opioid Dependence to Tourette Syndrome

## One-Sentence Summary

Methadone is a long-acting opioid agonist, marketed in the UK as a 5 mg tablet. The TxGNN model predicts it may be effective for **Tourette syndrome**, but no clinical trials are registered. Only **4 publications** were retrieved, and just one (a 1992 report) addresses methadone in Tourette's disorder directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L4 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Methadone is generally recognised as a mu-opioid receptor agonist with NMDA receptor antagonist activity. The original indication is not recorded in the UK licence data, so the link between the original and new indication cannot be assessed from this dataset.

The proposed rationale is that opioid modulation of dopaminergic and serotonergic (5-HT2A/C) circuits may influence tics and compulsive behaviours. A review of atypical opiates in obsessive-compulsive disorder (OCD) notes that opiates have been reported as effective in treatment-refractory OCD and Tourette syndrome.

The supporting evidence is weak. The only direct report is a small, old, uncontrolled publication from 1992, and no trials are registered. The very high TxGNN score is not backed by clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1728167](https://pubmed.ncbi.nlm.nih.gov/1728167/) | 1992 | Case report/small series | Am J Psychiatry | Methadone treatment of Tourette's disorder (no abstract available) |
| [17102981](https://pubmed.ncbi.nlm.nih.gov/17102981/) | 2007 | Preclinical/Review | Psychopharmacology | Atypical opiates in OCD; 5-HT2A-related behaviour is linked to tics and compulsions, and opiates are reported effective in refractory OCD and Tourette syndrome |
| [15247538](https://pubmed.ncbi.nlm.nih.gov/15247538/) | 2004 | Review | Curr Opin Neurol | Non-genetic causes of chorea; general differential diagnosis, only indirectly relevant |
| [39086469](https://pubmed.ncbi.nlm.nih.gov/39086469/) | 2024 | Review | Palliat Care Soc Pract | Novel analgesics for neuropathic pain in advanced cancer; not specific to Tourette syndrome |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0407020M0AAAEAE | Methadone HCl Tablets 5 mg | Tablet | Not stated in the data compiled |

Methadone is listed in the data as a single-ingredient product with a valid status. The listed number is a product code rather than a standard PL number. Please check the current MHRA record and the BNF for the authorised indications and formulations.

---

## Safety Considerations

**Contraindication signals from the knowledge graph.** These come from drug-disease links in the TxGNN knowledge graph, not from label text. They include:
- **Cardiac:** long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease
- **Respiratory:** respiratory failure, asthma
- **Neurological:** epilepsy, raised intracranial pressure (intracranial hypertension, pseudotumor cerebri)
- **Gastrointestinal:** paralytic ileus, intestinal obstruction, inflammatory bowel disease, *Clostridium difficile* colitis, necrotising enterocolitis
- **Organ function:** kidney disease, liver disease, gallbladder disease
- **Other:** hypothyroidism, hypotension, benign prostatic hyperplasia, urethral stricture, substance-related disorders

**Drug interactions.** The interaction screen returned 100 interactions in total. Those flagged as **Major** among the first 20 reviewed are:
- Alvimopan
- Bupropion
- Morphine
- Dexamethasone
- Clarithromycin
- Cisapride
- Picosulfuric acid
- Polyethylene glycol (3350 with electrolytes)

Moderate interactions include famotidine, cimetidine, loperamide, aprepitant, and several anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine, clidinium).

**Evidence-based harm signals from the literature:**
- Methadone-induced bradycardia has been reported.
- Cluster headache induction or exacerbation has been reported in patients treated for opioid addiction.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Other Predicted Indications (Context)

The remaining top-ranked predictions are not supported by clinical evidence, and several suggest harm or mechanistic opposition:

| Predicted Indication | Evidence Level | Comment |
|------|------|------|
| Nephrogenic syndrome of inappropriate antidiuresis | L5 | Prediction only; no literature |
| Trichotillomania | L5 | Opioid antagonists, not agonists, are studied; mechanistically opposite |
| Headache disorder | L5 | Literature is about opioid use disorder and perioperative care; opioids risk medication-overuse headache |
| Manic bipolar affective disorder | L4 | Dated small study (1982) and indirect evidence only |
| Trigeminal autonomic cephalalgia | L4 | Only report suggests harm (cluster headache induction) |
| Common cold | L5 | Literature is keyword matches on cold-pressor pain testing |
| Migraine disorder | L3 | One prospective cohort of low-dose methadone in refractory chronic migraine with medication-overuse headache; risk-benefit unfavourable for general use |
| Fibromyalgia | L4 | No methadone-specific data; guidelines generally advise against opioids |
| Idiopathic granulomatous myositis | L5 | Prediction only |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Tourette syndrome prediction rests on a single small 1992 uncontrolled report plus indirect mechanistic discussion, with no registered trials. Methadone also carries significant cardiac, respiratory and dependence risks, and many major drug interactions, which make an unsupported repurposing difficult to justify.

**To proceed, the following is needed:**
- Mechanism of action data and a clear statement of the original UK-authorised indications
- A systematic literature search for methadone or opioid use in Tourette syndrome, in comparison with current standard treatments
- A preclinical or small controlled study design with strict QT and respiratory monitoring
- Full SmPC and BNF safety information, including warnings and contraindications
- A risk-benefit assessment covering dependence, misuse and diversion potential in a young patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

