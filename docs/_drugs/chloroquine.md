---
layout: default
title: Chloroquine
parent: Model Prediction Only (L5)
nav_order: 156
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
description: "Chloroquine: predicted new indication Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (evidence level L4). Approved use: Rheumatoid arthritis, systemic and discoid lupus erythe…"
monitor_inn: "chloroquine"
predicted_indications: ["rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis", "juvenile chronic polyarthritis", "juvenile idiopathic arthritis"]
---

# Chloroquine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Chloroquine: From Rheumatoid Arthritis and Malaria to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis
{: .text-alpha }

## One-Sentence Summary

Chloroquine is an antimalarial that is also used in rheumatoid arthritis and lupus. The TxGNN model predicts it may be effective for **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (JIA)**, but **no clinical trials** and only **1 indirectly relevant publication** support this specific prediction, so the evidence is largely computational.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, systemic and discoid lupus erythematosus, malaria (Plasmodium vivax, falciparum, ovale, malariae) |
| Predicted New Indication | Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| UK Market Status | Listed in NHSBSA BNF presentation codes (2 of 2) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 2 (valid: 2) |
| Recommended Decision | Hold |

*Note: the original indications are taken from the TxGNN model (deep learning), as no approved indication text was available in the UK licence data. The scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.*

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the known pharmacology of chloroquine, it has immunomodulatory activity: it inhibits lysosomal function, reduces antigen processing and Toll-like receptor signalling, and lowers pro-inflammatory cytokine production.

Chloroquine is already used in adult rheumatoid arthritis. RF-positive polyarticular JIA resembles adult seropositive rheumatoid arthritis, so a plausible mechanistic link exists. However, the TxGNN score is a computational prediction. The one publication retrieved for this exact disease concerns leflunomide, not chloroquine, and so gives no direct evidence for chloroquine here.

Related predictions for broader JIA terms (juvenile chronic polyarthritis, juvenile idiopathic arthritis) have more literature, including older reports on chloroquine dosing in children. These are historical, mostly uncontrolled, and do not provide prospective efficacy data. Current standard care, such as methotrexate and biologics, is better evidenced.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the predicted indication itself:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Cohort | The Journal of Rheumatology | Long-term real-life experience with leflunomide in JIA. It does not evaluate chloroquine. |

For closely related JIA terms, the most relevant publications involving chloroquine are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18021335](https://pubmed.ncbi.nlm.nih.gov/18021335/) | 2007 | Cohort | Journal of Clinical Pharmacy and Therapeutics | Compared methotrexate pharmacokinetics in JIA patients on methotrexate alone or with chloroquine. |
| [2047820](https://pubmed.ncbi.nlm.nih.gov/2047820/) | 1991 | Review | Schweizerische medizinische Wochenschrift | Therapeutic strategy in 119 patients with juvenile chronic arthritis, with chloroquine discussed among disease-modifying drugs. |
| [7409700](https://pubmed.ncbi.nlm.nih.gov/7409700/) | 1980 | Review | Fortschritte der Medizin | Review of drug therapy in juvenile chronic polyarthritis, including benefits and adverse effects of chloroquine. |
| [4608161](https://pubmed.ncbi.nlm.nih.gov/4608161/) | 1974 | Clinical study | Scandinavian Journal of Rheumatology | Dosage of chloroquine and hydroxychloroquine in children with juvenile rheumatoid arthritis and lupus, with serum concentrations measured. |
| [9523387](https://pubmed.ncbi.nlm.nih.gov/9523387/) | 1998 | Case report | Revue du Rhumatisme | Third-degree atrioventricular block in a patient with juvenile-onset arthritis on long-term chloroquine (safety signal). |
| [1450810](https://pubmed.ncbi.nlm.nih.gov/1450810/) | 1992 | Case report | British Journal of Rheumatology | Chloroquine-induced vitiligo in a patient with juvenile-onset rheumatoid arthritis. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0504010Z0BBAAAA (BNF code) | Paludrine/Avloclor tablets 100/250 mg | Tablet | Not available in the data compiled |
| 0504010Z0AAAAAA (BNF code) | Chloroquine/Proguanil tablets 250/100 mg | Tablet | Not available in the data compiled |

Both entries are single-ingredient authorisations with valid status. They are listed here by BNF classification code (antimalarials, section 5.4.1); PL numbers and approved indication wording were not available.

## Cytotoxicity

Not applicable. Chloroquine is not an antineoplastic drug.

## Safety Considerations

- **Contraindications and conditions flagged in the knowledge graph** (these are graph-derived associations, not label text): epilepsy, porphyria (including inherited forms), liver disease, gallbladder disease, psoriasis, neutropenia, agranulocytosis, leukopenia, anaemia (including macrocytic), G6PD deficiency, glycogen storage disease, cystinuria, galactosaemia, substance abuse/dependence, and eye, retinal, vision and hearing disorders (including retinitis, scotoma and blindness).
- **Drug interactions:** 467 interactions were identified. Major-level examples include agalsidase beta, bupropion, cisapride, clarithromycin, dolasetron and granisetron (several are QT-prolonging agents). Moderate-level examples include antacids (aluminium hydroxide, calcium carbonate), cimetidine, famotidine, metronidazole, loperamide, aprepitant, sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide) and insulin, where glucose-lowering effects may be affected.
- **Signals in the retrieved literature:** a case of third-degree atrioventricular block on chloroquine, and chloroquine-induced vitiligo in juvenile-onset arthritis. Retinal toxicity and cardiac conduction risks warrant particular caution in children.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials and no direct chloroquine evidence for RF-positive polyarticular JIA. Related literature is old, uncontrolled or indirect, and established therapies (methotrexate, biologics) are better supported, while the ocular and cardiac risks are a concern in children.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Label-level warnings and contraindications from the SmPC/BNF, and approved indication text and PL numbers for the UK authorisations
- Controlled efficacy data (or a systematic review) for chloroquine in polyarticular JIA, compared with current standard care
- A paediatric dosing and safety monitoring plan, including retinal screening and cardiac (ECG) assessment
- A review of the main interacting drugs likely to be co-prescribed in JIA, such as methotrexate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

