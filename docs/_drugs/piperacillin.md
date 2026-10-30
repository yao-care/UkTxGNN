---
layout: default
title: Piperacillin
parent: Model Prediction Only (L5)
nav_order: 500
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
description: "Piperacillin: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not available in the data compiled for this report (piperacillin is a…"
monitor_inn: "piperacillin"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "sclerosing cholangitis", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "WHIM syndrome"]
---

# Piperacillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Piperacillin: From Bacterial Infection to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Piperacillin is a beta-lactam antibiotic, marketed in the UK as an injectable (including the piperacillin/tazobactam combination product Tazocin).
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but **no clinical trials** and only **15 publications** (almost all case reports in which piperacillin treated an infection in patients who happened to have RA) were found.
There is no credible evidence that piperacillin treats rheumatoid arthritis, and the prediction should be regarded as a computational artefact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (piperacillin is an antibacterial for bacterial infections) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (2 of 2) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Piperacillin is, however, a well-established beta-lactam antibiotic that inhibits bacterial cell wall synthesis.

This mechanism has no known anti-inflammatory or immunomodulatory action relevant to rheumatoid arthritis, an autoimmune disease. The high score (0.9994) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The retrieved literature supports this view. The papers describe RA patients who developed infections or treatment complications (for example, methotrexate-induced pancytopenia or infections under immunosuppression), where piperacillin was used to treat the infection. This reflects co-occurrence in patients, not an effect on RA itself.

Other predictions in the list (for example colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, diabetic nephropathy and WHIM syndrome) also lack any mechanistic rationale or clinical evidence. Sclerosing cholangitis has only a speculative link through gut microbiome modulation by antibiotics, with no supporting studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications tests piperacillin as a treatment for RA. The most relevant are listed below (all are case reports or cohort studies; no RCTs were found).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Case report | Orthopadie (Heidelberg) | Prosthetic knee joint infection with *Haemophilus influenzae* in an RA patient; piperacillin/tazobactam used for pneumonia |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Case report | BMJ Case Reports | Purulent pericarditis in an RA patient on etanercept; empirical piperacillin-tazobactam started |
| [41268563](https://pubmed.ncbi.nlm.nih.gov/41268563/) | 2025 | Case report | Frontiers in Immunology | Severe atypical bullous erysipelas caused by *E. coli* in an immunosuppressed patient with long-standing RA |
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2026 | Cohort | British Journal of Clinical Pharmacology | Predictive model for eosinophilia in patients treated with ampicillin/sulbactam or piperacillin/tazobactam |
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Cohort | Annals of Translational Medicine | Prevalence and clinical features of antibiotic-associated drug-induced liver injury |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Case report | Proceedings (Baylor Univ. Med. Center) | Low-dose methotrexate toxicity with pancytopenia in an RA patient; leucovorin rescue |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Case report | Cureus | Pancytopenia from low-dose methotrexate in RA |
| [36945293](https://pubmed.ncbi.nlm.nih.gov/36945293/) | 2023 | Case report | Cureus | Recurrent pleural effusions in an RA patient in remission for nine years |
| [40119266](https://pubmed.ncbi.nlm.nih.gov/40119266/) | 2025 | Case report/Review | BMC Infectious Diseases | Septic shock caused by drug-resistant *Edwardsiella tarda* |
| [1921823](https://pubmed.ncbi.nlm.nih.gov/1921823/) | 1991 | Case report | Medical Journal of Australia | Pancytopenia after accidental methotrexate overdose in RA |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501014S0BBABAB | Tazocin Inj 4.5g Vl | Injection (vial) | Not available in the data compiled for this report |
| 0501014S0AAABAB | Piperacillin/Tazobactam Inj 4g/0.5g Vl | Injection (vial) | Not available in the data compiled for this report |

Both authorisations are valid single-ingredient entries. The identifiers shown are BNF-style codes (BNF section 5.1.1.4, antipseudomonal penicillins), not PL numbers, so the licence details should be verified against the MHRA register and the SmPC.

---

## Safety Considerations

- **Drug Interactions**: 81 potential interactions were identified. The main ones by severity are:
  - **Major**: vancomycin
  - **Moderate**: doxycycline, tetracycline, minocycline, kanamycin, streptomycin, picosulfuric acid
  - **Minor**: clarithromycin
  - Several others (for example pantoprazole, morphine, prednisolone, prednisone, simvastatin, potassium chloride) have unclassified severity.

No warning or contraindication data were available in the data compiled for this report. Please refer to the SmPC and BNF for full safety information, including renal dose adjustment. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5). There are no trials, the literature reflects antibiotic use for infections in RA patients rather than any benefit for RA, and there is no plausible mechanistic link between a bacterial cell wall inhibitor and an autoimmune joint disease.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis for an effect on RA, supported by preclinical data
- Mechanism of action data and licensed indication text for the UK products
- Warnings and contraindications from the SmPC and BNF
- Evidence from controlled studies, none of which currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

