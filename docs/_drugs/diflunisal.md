---
layout: default
title: Diflunisal
parent: Model Prediction Only (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Diflunisal: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis"
monitor_inn: "Diflunisal"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "spondyloarthropathy, susceptibility to", "myosclerosis", "ankylosing spondylitis", "brachyolmia", "hypermobility of coccyx", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "inflammatory spondylopathy"]
---

# Diflunisal
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Diflunisal: From Rheumatoid Arthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Diflunisal is a salicylate-derived non-steroidal anti-inflammatory drug (NSAID), originally used for rheumatoid arthritis and osteoarthritis.
The TxGNN model ranks **acromesomelic dysplasia, Hunter-Thompson type** as its top prediction, but this is a graph-based prediction only, with **no clinical trials** and **no publications** supporting it.
The only predicted indication with direct clinical evidence is **ankylosing spondylitis**, a lower-ranked prediction that is covered below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis (from the knowledge graph; the UK authorisation record has no indication text) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known pharmacology, diflunisal is an NSAID that inhibits cyclo-oxygenase (COX-1 and COX-2) and reduces prostaglandin-mediated inflammation and pain. It is also known to stabilise transthyretin.

For the top-ranked prediction, **no plausible mechanistic link has been identified**. Acromesomelic dysplasia, Hunter-Thompson type, is a rare genetic skeletal disorder linked to the CDMP1/GDF5 pathway. Neither COX inhibition nor transthyretin stabilisation addresses this underlying genetic defect. The very high TxGNN score reflects patterns in the knowledge graph rather than biological or clinical rationale.

Other highly ranked predictions show the same pattern. Brachyolmia, brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, and colobomatous microphthalmia-rhizomelic dysplasia syndrome are rare genetic or developmental conditions with no mechanistic rationale and no supporting studies.

The more credible predictions are those close to diflunisal's existing use:
- **Ankylosing spondylitis** (rank 5, score 99.98%): NSAIDs are established first-line therapy, so the mechanism is coherent. This is effectively an extension within the NSAID class rather than a novel repurposing.
- **Inflammatory spondylopathy** (rank 10): overlaps with ankylosing spondylitis and cites the same literature, so it should be treated as a duplicate or parent category rather than independent evidence.
- **Spondyloarthropathy, susceptibility to** (rank 3): conceptually relevant, but this is a genetic susceptibility term rather than a treatable clinical condition.
- **Rheumatoid vasculitis** (rank 8): indirect only, because it is managed with immunosuppression and NSAIDs are unlikely to modify the disease.
- **Hypermobility of coccyx** (rank 7): at most symptomatic pain relief is conceivable, and it is speculative.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication, or for any other predicted indication in the data compiled for this report.

---

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication.

For context, the following publications were retrieved for the best-supported alternative prediction, **ankylosing spondylitis**:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3524970](https://pubmed.ncbi.nlm.nih.gov/3524970/) | 1986 | Double-blind randomised comparative trial | Clin Rheumatol | In 38 men with ankylosing spondylitis, diflunisal 500 mg twice daily and phenylbutazone 200 mg twice daily were both effective over 12 weeks, with benefit maintained over a 36-week open extension. Diflunisal initially had a more pronounced and rapid analgesic effect. |
| [3546687](https://pubmed.ncbi.nlm.nih.gov/3546687/) | 1986 | Cohort | J Rheumatol | Lung function study in 33 men with active ankylosing spondylitis treated with diflunisal or phenylbutazone. It examined the influence of disease activity and NSAID treatment, and is not specific to diflunisal. |
| [4062389](https://pubmed.ncbi.nlm.nih.gov/4062389/) | 1985 | Prospective cohort | Ann Rheum Dis | In 38 men receiving phenylbutazone or diflunisal, serum IgA levels correlated with disease activity measures. It is not a drug-efficacy study. |
| [6772422](https://pubmed.ncbi.nlm.nih.gov/6772422/) | 1980 | Review | Drugs | Review of diclofenac in rheumatic diseases and pain, not of diflunisal. |
| [387372](https://pubmed.ncbi.nlm.nih.gov/387372/) | 1979 | Review | Drugs | Review of naproxen in rheumatic diseases and pain states, not of diflunisal. |
| [3539573](https://pubmed.ncbi.nlm.nih.gov/3539573/) | 1986 | Review | Drugs | Review of pirprofen, another NSAID, including its use in ankylosing spondylitis. |
| [2670397](https://pubmed.ncbi.nlm.nih.gov/2670397/) | 1989 | Review | Clin Pharm | Review of diclofenac sodium pharmacology and efficacy, not of diflunisal. |

Only one of these papers (PMID 3524970) provides direct evidence for diflunisal, and it is dated and small. The remainder are reviews of other NSAIDs or studies of disease characteristics.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010D0AAAAAA | Diflunisal tablets 250 mg | Tablet | Not stated in the data compiled for this report |

One single-ingredient authorisation is recorded as valid. The listed number does not follow the usual PL format, so please verify the authorisation details against the MHRA record.

---

## Safety Considerations

**Contraindications flagged by the knowledge graph** (derived from drug-disease graph links rather than label text, so they should be confirmed against the SmPC):
- Cardiovascular: hypertension, hypertensive disorder, myocardial infarction, coronary thrombosis, cardiovascular disease, heart disease
- Gastrointestinal: peptic ulcer disease, active peptic ulcer disease
- Renal, hepatic and biliary: kidney disease, pyoureter, liver disease, gallbladder disease
- Haematological: blood coagulation disease, haemoglobinopathy

**Drug Interactions:** 100 interactions were identified, and the 20 shown in the data are all rated Moderate. They include:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
- Other salicylates and aminosalicylates: acetylsalicylic acid, mesalazine, balsalazide
- Antidiabetic agents: metformin, chlorpropamide, glimepiride, and insulins (aspart, degludec, detemir, glargine)
- Bowel preparations and potassium or citrate agents: picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate, potassium citrate, potassium bicarbonate

Label-based warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, acromesomelic dysplasia, Hunter-Thompson type, rests on a model score alone (evidence level L5), with no mechanistic link, trials or literature. The only credible signal is for ankylosing spondylitis (L3), which is an extension within the NSAID class and is supported by a single dated study. It could be taken forward as a research question, but it is not a novel repurposing.

**To proceed, the following is needed:**
- Label-based warnings and contraindications from the SmPC and BNF, because safety screening cannot proceed without them
- Mechanism of action data
- The approved indication text and dosage form for the UK authorisation
- For ankylosing spondylitis, modern comparative evidence against current NSAIDs or biologics, and review of its place in current UK guidance
- Review of the knowledge-graph contraindications (cardiovascular, gastrointestinal, renal, hepatic and bleeding risks) before any new-population use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

