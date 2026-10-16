---
layout: default
title: Acetic Acid
parent: Model Prediction Only (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Acetic Acid: predicted new indication Post-bacterial disorder (evidence level L5). Approved use: Otitis externa"
---

# Acetic Acid
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

# Acetic Acid: From Otitis Externa to Post-Bacterial Disorder

## One-Sentence Summary

Acetic acid is a topical acidifying antiseptic, originally used for otitis externa and other external ear disease.
The TxGNN model predicts it may be effective for **post-bacterial disorder**, but there are currently **no clinical trials** and **no relevant publications** supporting this prediction.
A more evidence-supported secondary direction is **tinea corporis** (indirect, mostly historical reports only), described below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Otitis externa; external ear disease (taken from the knowledge-graph indication data, as no approved indication text is available for the UK product) |
| Predicted New Indication | Post-bacterial disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acetic acid is a topical antiseptic and acidifying agent with antibacterial activity. Its use in otitis externa is consistent with lowering local pH and inhibiting microbial growth.

The top-ranked prediction, post-bacterial disorder, refers to non-specific sequelae that follow a bacterial infection. A topical antiseptic acting at the surface of an infected site has no clear route to preventing or treating such sequelae. The link is therefore **not supported** by the data compiled for this report, despite the high model score.

Most of the other top-ranked predictions (post-infectious vasculitis, Chagas cardiomyopathy, infection-related haemolytic uraemic syndrome, drug-induced osteoporosis) are systemic or immune-mediated conditions. A topical acidifier has no plausible mechanism for these, and no clinical evidence was found. The one exception is **tinea corporis** (rank 9), where topical antifungal action through acidification is plausible and consistent with its established ear-infection use. It is the only prediction with some indirect supporting literature (L4), so it is discussed in the sections below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for either the top prediction or the tinea corporis prediction.

---

## Literature Evidence

**For the top prediction (post-bacterial disorder):** Currently no related literature available.

**For tinea corporis (the best-supported secondary prediction):** All evidence is indirect, old, or uncontrolled.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26857689](https://pubmed.ncbi.nlm.nih.gov/26857689/) | 2016 | In vitro study | Mycoses | Seven commercial topical nail products compared with amorolfine in an onychomycosis model against *Trichophyton mentagrophytes* (indirect support) |
| [31049344](https://pubmed.ncbi.nlm.nih.gov/31049344/) | 2019 | Clinical report | Skin Appendage Disorders | Chemical peeling as an alternative to oral antifungals for onychomycosis in elderly or diabetic patients |
| [20256868](https://pubmed.ncbi.nlm.nih.gov/20256868/) | 1947 | Historical case series | Urologic and Cutaneous Review | Iodine plus dilute acetic acid for tinea capitis in a larger patient series |
| [20996178](https://pubmed.ncbi.nlm.nih.gov/20996178/) | 1946 | Historical clinical report | JAMA | Iodine plus dilute acetic acid for tinea capitis |
| [20983383](https://pubmed.ncbi.nlm.nih.gov/20983383/) | 1946 | Historical clinical report | Archives of Dermatology and Syphilology | Treatment of tinea capitis with iodine and dilute acetic acid |
| [13616002](https://pubmed.ncbi.nlm.nih.gov/13616002/) | 1958 | Historical clinical report | Vestnik Dermatologii i Venerologii | Foot epidermophytosis treated with increasing concentrations of acetic acid |
| [16233325](https://pubmed.ncbi.nlm.nih.gov/16233325/) | 2002 | In vitro study | J Biosci Bioeng | Lactic acid bacteria fermentation product showed antifungal activity against tinea under low-pH conditions (indirect) |
| [37256034](https://pubmed.ncbi.nlm.nih.gov/37256034/) | 2023 | Case series (safety) | Archives of Plastic Surgery | Burns caused by folk remedies, a safety concern for topical use |

Note: none of these studies is a controlled trial of acetic acid in tinea corporis. A systematic review of animal models of post-infectious irritable bowel syndrome (PMID 20848144) was also retrieved for "post-infectious syndrome" but does not study acetic acid and is not relevant evidence.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1201010B0AAAFAF | Acetic Acid_Ear Spy 2% 5ml | Not stated | Not stated |

One single-ingredient authorisation is recorded as valid. Dosage form and approved indication text are not available in the data compiled for this report. Please check the current MHRA record and the BNF for the full product details.

---

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text):** inherited porphyria, porphyrin metabolism disease, porphyria, herpes simplex infection, and geniculate herpes zoster. These should be verified against the SmPC.
- **Local tolerability:** one case series (PMID 37256034) describes burns from folk remedies, which supports caution with concentrated or unsupervised topical use. Acetic acid is also an irritant, so use near the eye (for example in blepharitis) would be a particular concern.

No drug interaction data were found. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported by a high model score only, with no trials, no relevant literature, and no plausible mechanism. Tinea corporis is a reasonable research question (L4) but rests on indirect, historical, uncontrolled data and raises a topical safety concern.

**To proceed, the following is needed:**
- Mechanism of action data for acetic acid
- Full SmPC safety information (warnings, contraindications), which is currently missing and would be needed before any safety screening
- For tinea corporis: a controlled in vitro or clinical study of defined acetic acid concentrations against dermatophytes, with skin-tolerability assessment
- Confirmation of the dosage form and approved indication for the UK authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

