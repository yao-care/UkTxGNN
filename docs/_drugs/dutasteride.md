---
layout: default
title: Dutasteride
parent: Model Prediction Only (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dutasteride: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
monitor_inn: "Dutasteride"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "familial isolated trichomegaly"]
---

# Dutasteride
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

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a 5-alpha-reductase inhibitor, originally used to treat benign prostatic hyperplasia.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but there are **no clinical trials and no publications** supporting this prediction. It is a graph-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (from the knowledge graph; no approved indication text is available in the UK licence data) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Dutasteride inhibits type 1 and type 2 5-alpha-reductase, the enzymes that convert testosterone to dihydrotestosterone (DHT). Lowering DHT shrinks the prostate in benign prostatic hyperplasia. Detailed mechanism of action data is not otherwise available in the data compiled for this report.

The link to the predicted indication is weak. Ambras syndrome is a congenital disorder associated with genomic rearrangements affecting regulation of the *TRPS1* gene. It is not primarily driven by DHT, so 5-alpha-reductase inhibition has no clear reason to help. The very high TxGNN score reflects proximity in the knowledge graph, not demonstrated biology.

Other predictions in the top ten (hypertrichosis, hair shaft abnormalities, hypotrichosis simplex of the scalp, diffuse alopecia areata and others) are also hair-related or unrelated disorders. Most have no trials or literature and a weak or speculative mechanistic rationale. For example, hypertrichosis is by definition androgen-independent. The only literature retrieved for any of them is a 2026 narrative review of androgenetic alopecia in women, linked to diffuse alopecia areata. It gives indirect context only and does not show efficacy in alopecia areata, which is autoimmune rather than DHT-driven.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction (Ambras type hypertrichosis universalis congenita).

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0604020B0AAAAAA (BNF-style code; no PL number in the data) | Dutasteride capsules 500 microgram | Capsule (as named in the product description) | Not stated in the data |

Only one single-ingredient authorisation is recorded, and it is valid. Please confirm the full authorisation details and licensed indications in the MHRA records and the BNF.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver disease, gallbladder disease, priapism and intraoperative floppy iris syndrome. These should be checked against the SmPC.
- **Drug Interactions:** 100 interactions were found in total. Those rated moderate are aprepitant, cimetidine, clarithromycin, clotrimazole and miconazole. Others, rated unknown, include pantoprazole, omeprazole, lansoprazole, metformin, glimepiride, rosiglitazone, simvastatin, morphine, doxycycline, prednisone, hydrocortisone, triamcinolone, calcitriol, mesalazine and lactulose.
- **Developmental concern:** 5-alpha-reductase inhibitors affect androgen-dependent development, which raises concerns in any use in developmental or congenital conditions.

Please refer to the SmPC and BNF for full warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on knowledge-graph proximity alone, with no trials or literature. The mechanistic rationale is weak, because Ambras syndrome is a genetic disorder that is not primarily DHT-driven. Evidence level is L5.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence that 5-alpha-reductase inhibition or DHT reduction is relevant to *TRPS1*-related hair overgrowth
- Complete mechanism of action data
- Safety data from the SmPC and BNF (warnings and contraindications are currently missing), including the developmental concerns noted above
- Confirmation of the licensed indication and authorisation details from MHRA records
- If any hair-related indication is pursued, prioritise androgen-driven conditions where the mechanism is plausible, and review the predictions with literature support first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

