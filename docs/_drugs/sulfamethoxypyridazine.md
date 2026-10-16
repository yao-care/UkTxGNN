---
layout: default
title: Sulfamethoxypyridazine
parent: Model Prediction Only (L5)
nav_order: 581
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sulfamethoxypyridazine: predicted new indication Gout (evidence level L5). Approved use: Not stated in the licence data compiled for this report (classed as a…"
monitor_inn: "Sulfamethoxypyridazine"
predicted_indications: ["gout", "allergic asthma", "diabetic nephropathy", "brain small vessel disease 1 with or without ocular anomalies", "intrinsic asthma", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "Raynaud disease", "type 1 diabetes mellitus", "bronchitis", "chronic kidney disease"]
---

# Sulfamethoxypyridazine
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

# Sulfamethoxypyridazine: From Bacterial Infection to Gout (Top Prediction)

## One-Sentence Summary

Sulfamethoxypyridazine is a long-acting sulfonamide antibacterial, currently listed as marketed in the UK as a 500 mg tablet.
The TxGNN model ranks **gout** as its top predicted new indication, but this is a computational prediction only, with **no clinical trials** and **no publications** supporting it.
The only indication with any published literature is **bronchitis** (rank 9), and that evidence is limited to seven papers from 1962-1964.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data compiled for this report (classed as a sulfonamide antibacterial) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

Other predicted indications, all scoring between 95.8% and 97.7%, are allergic asthma, diabetic nephropathy, brain small vessel disease 1, intrinsic asthma, a COL4A1-related hematuria-retinal syndrome, Raynaud disease, type 1 diabetes mellitus, bronchitis and chronic kidney disease. Only bronchitis has any literature (evidence level L4); the rest are L5.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Sulfamethoxypyridazine is a long-acting sulfonamide antibacterial, and no established mechanism links it to urate lowering or to the inflammation of gout.

The gout score is therefore best read as a pattern found in the knowledge graph, not as a pharmacological rationale. The same applies to most of the other predictions. For example, the two COL4A1-related rare disorders most likely reflect network proximity rather than any real drug effect.

Bronchitis is the one biologically plausible prediction. As an antibacterial, the drug could in principle be used for bacterial respiratory infections and for reducing exacerbations of chronic bronchitis. However, current antibiotic options and resistance patterns have changed substantially since the 1960s, and this sulfonamide has largely been superseded.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for gout, or for any of the other predicted indications.

---

## Literature Evidence

No literature is available for gout. The only literature found relates to the lower-ranked prediction of **bronchitis**. All items are from 1962-1964, mostly non-English, and none has an abstract available.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14102014](https://pubmed.ncbi.nlm.nih.gov/14102014/) | 1964 | Clinical study | British Medical Journal | Compared daily penicillin, tetracycline, erythromycin and sulphamethoxypyridazine for their influence on exacerbations of bronchitis (British Tuberculosis Association research committee report) |
| [14218248](https://pubmed.ncbi.nlm.nih.gov/14218248/) | 1964 | Review/clinical report | Deutsche Medizinische Wochenschrift | Long-term antibiotic therapy in chronic bronchitis |
| [14216736](https://pubmed.ncbi.nlm.nih.gov/14216736/) | 1964 | Observational study | Minerva Otorinolaringologica | Cytological and bacteriological sputum study in tracheo-bronchitis in laryngeal cancer and laryngectomised patients treated with a new synthetic preparation |
| [14468600](https://pubmed.ncbi.nlm.nih.gov/14468600/) | 1962 | Clinical study | La Riforma Medica | Combination of sulfamethoxypyridazine, tripyraphene and methamizole in respiratory disorders |
| [14097704](https://pubmed.ncbi.nlm.nih.gov/14097704/) | 1963 | Clinical report | Minerva Pediatrica | Combination of oxolamine citrate, aminophenazone and sulfamethoxypyridazine in paediatric practice |
| [14236503](https://pubmed.ncbi.nlm.nih.gov/14236503/) | 1964 | Case report (safety) | Zeitschrift fur Arztliche Fortbildung | Methaemoglobinaemia in young infants due to sulfamethoxypyridazine |
| [14084454](https://pubmed.ncbi.nlm.nih.gov/14084454/) | 1963 | Case report (safety) | Rivista di Anatomia Patologica e di Oncologia | Bullous erythroderma with epidermolysis (Lyell-type syndrome) attributed to sulfamethoxypyridazine |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501080T0AAAAAA (BNF-style product code, not a PL number) | Sulfamethoxypyridazine 500 mg tablets | Tablet | Not stated in the data compiled for this report |

One single-ingredient product is recorded as valid. Dosage form, manufacturer and indication text are missing from the data, so they should be checked against the SmPC and the BNF.

---

## Safety Considerations

No label-derived warnings, contraindications or drug interaction data were available for this drug. The following points come from the published reports and general sulfonamide class knowledge, and should be verified against the SmPC:

- **Hypersensitivity:** the literature includes a case of severe bullous skin reaction (Lyell-type syndrome). Sulfonamide hypersensitivity is also a concern in atopic patients, which is relevant to the asthma predictions.
- **Methaemoglobinaemia:** reported in young infants.
- **Renal effects:** sulfonamides are renally cleared, with a known risk of crystalluria and renal toxicity. This argues for caution in the diabetic nephropathy and chronic kidney disease predictions.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gout prediction rests on a model score alone, with no trials, no publications and no plausible mechanism. The only indication with any literature (bronchitis) relies on 1960s low-quality reports and is of limited relevance to current practice. The safety profile of sulfonamides also raises concerns for several predicted renal and atopic indications.

**To proceed, the following is needed:**
- Mechanism of action data, to test whether any link to urate handling or inflammation exists
- SmPC and BNF safety information (warnings, contraindications, interactions), plus the approved indication text and dosage form for the UK product
- Preclinical or mechanistic studies for gout before any clinical consideration
- For bronchitis, a comparison against current antibiotic options and resistance patterns, if this remains a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

