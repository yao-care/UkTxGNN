---
layout: default
title: Carbamazepine
parent: Model Prediction Only (L5)
nav_order: 131
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "Carbamazepine: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (also partial epilepsy, bipolar disorder…"
monitor_inn: "Carbamazepine"
predicted_indications: ["trigeminal nerve neoplasm", "beta-ketothiolase deficiency", "Rett syndrome, congenital variant"]
---

# Carbamazepine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Carbamazepine: From Epilepsy to Trigeminal Nerve Neoplasm
{: .text-alpha }

## One-Sentence Summary

Carbamazepine is an established antiseizure medicine, originally used for epilepsy, bipolar disorder and trigeminal neuralgia.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm** (score 1.0000), but **no clinical trials** are registered and the 18 publications retrieved are mostly case reports and reviews of tumour-related neuralgia, not treatment of the tumour itself. The evidence is therefore weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (also partial epilepsy, bipolar disorder, Lennox-Gastaut syndrome, trigeminal and glossopharyngeal neuralgia) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (1 of 1) – MHRA licence status is not included in this data |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Carbamazepine is widely known to block voltage-gated sodium channels, which reduces abnormal repetitive neuronal firing. This is the basis of its use in epilepsy and trigeminal neuralgia.

The predicted indication is probably a semantic artefact. Trigeminal neuralgia is a listed original indication, and the retrieved papers describe neuralgia that is *secondary to* tumours or masses (schwannoma, lipoma, meningioma, dermoid cyst, lymphoma). In these reports carbamazepine controls the pain symptomatically, and in several cases it failed or was poorly tolerated. This is symptom control, not an antineoplastic effect. The high TxGNN score (1.0000) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as "trigeminal nerve neoplasm" and "trigeminal neuralgia", not biological evidence.


---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The most relevant publications retrieved (none is an RCT):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clin Croat | Treatment options for trigeminal neuralgia, including tumour-related causes |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Medical and surgical treatments for trigeminal neuralgia |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case report | Br J Neurosurg | Primary lymphoma of the trigeminal nerve; carbamazepine did not relieve symptoms |
| [25142539](https://pubmed.ncbi.nlm.nih.gov/25142539/) | 2014 | Case report | Rinsho Shinkeigaku | Lymphoma spreading along the trigeminal nerve; initial pain improvement with carbamazepine, then loss of effect |
| [15235745](https://pubmed.ncbi.nlm.nih.gov/15235745/) | 2004 | Case report | Arq Neuropsiquiatr | Primary melanoma of Meckel's cave; pain not relieved by carbamazepine |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | Case report | No Shinkei Geka | Cerebellopontine angle lipoma; pain poorly controlled on carbamazepine because of side effects |
| [33989821](https://pubmed.ncbi.nlm.nih.gov/33989821/) | 2021 | Case report | World Neurosurg | Petroclival meningioma causing trigeminal neuralgia; treated surgically |
| [11286444](https://pubmed.ncbi.nlm.nih.gov/11286444/) | 2001 | Survey | Br J Oral Maxillofac Surg | UK survey of trigeminal neuralgia investigation and carbamazepine monitoring practice |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Preclinical | Exp Neurol | Carbamazepine inhibited spontaneous activity in experimental rat neuromas |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0408010C0AAABAB | Carbamazepine Tab 100mg | Not specified | Not specified |

One valid single-ingredient authorisation is recorded. Dosage form and indication text are not available in the compiled data, and the identifier is not in the usual PL format. Please check the MHRA register and the BNF (Section 4.8.1, antiepileptic drugs) for current licensed products and indications.

---

## Safety Considerations

**Contraindications and conditions of concern (from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence, and not label text):**
- **Haematological:** neutropenia, agranulocytosis, pancytopenia, thrombocytopenia, anaemia, and congenital or cyclic neutropenia syndromes
- **Cardiovascular:** atrioventricular block and heart conduction disease, coronary artery disease, sudden cardiac arrest, hypertension
- **Hepatic and renal:** liver disease, kidney disease, impaired renal function, gallbladder disease
- **Other:** glaucoma and ocular hypertension, inappropriate ADH secretion (SIADH), absence epilepsy, anxiety and neurotic disorders

**Drug interactions (100 recorded; examples):**
- **Major:** clarithromycin, eliglustat
- **Moderate:** doxycycline, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), bupropion, aprepitant, morphine, metronidazole, cimetidine, pioglitazone, canagliflozin, vitamin D analogues, dronabinol, activated charcoal

Carbamazepine is a strong enzyme inducer, so interactions are numerous. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has only model-score support. No trials exist, and the literature shows symptomatic pain control in tumour-associated neuralgia rather than any effect on the neoplasm. Carbamazepine's established role in trigeminal neuralgia is not new repurposing. The seizure-related predictions are plausible but mostly overlap with its existing epilepsy indication, supported by animal or case-level evidence only.

**To proceed, the following is needed:**
- Mechanism of action data and any rationale for antitumour activity (none currently supported)
- Reframing of the question: either symptomatic neuralgia control in tumour patients, or the reflex epilepsy syndromes (e.g. startle epilepsy, where a clinical series reported carbamazepine response)
- Controlled clinical data in whichever indication is chosen
- Full UK licence details (dosage forms, indications) from the MHRA and SmPC
- A haematological, hepatic, cardiac and interaction monitoring plan, including HLA-B*1502 and HLA-A*3101 screening per SmPC where applicable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

