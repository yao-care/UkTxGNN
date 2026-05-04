---
layout: default
title: Cetrorelix
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Cetrorelix
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cetrorelix: From Controlled Ovarian Stimulation to Hypertrichosis

## One-Sentence Summary

Cetrorelix is a GnRH (gonadotropin-releasing hormone) receptor antagonist, approved in multiple jurisdictions for the prevention of premature LH surges during controlled ovarian stimulation in women undergoing assisted reproductive technology (ART).
The TxGNN model predicts it may have therapeutic potential in **hypertrichosis**, however there are currently **no clinical trials** and **no published literature** directly supporting this indication.
At evidence level L5 (model prediction only), a **Hold** decision is recommended until credible mechanistic and safety evidence can be established.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Controlled ovarian stimulation (prevention of premature LH surge during ART) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| UK Market Status | No MHRA authorisations identified in current dataset |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cetrorelix is a synthetic decapeptide that competitively and reversibly blocks GnRH receptors at the anterior pituitary. Unlike GnRH agonists — which initially stimulate the HPG axis before causing receptor downregulation — Cetrorelix produces an immediate and dose-dependent suppression of LH and FSH release. This leads to a rapid reduction in gonadal sex hormone production, including androgens in both males and females.

The proposed mechanistic basis for this prediction rests on the relationship between androgen excess and hair growth. In androgen-sensitive forms of hypertrichosis, elevated circulating androgens — particularly testosterone and dihydrotestosterone (DHT) — promote increased hair follicle activity across non-sexual body sites. By suppressing the HPG axis, Cetrorelix could theoretically reduce androgen levels and thereby attenuate androgen-mediated stimulation of hair follicles. This indirect pathway (GnRH antagonism → ↓LH/FSH → ↓gonadal androgens → ↓hair follicle stimulation) is the most likely basis for the TxGNN model's high prediction score.

However, this mechanistic link is considered weak and indirect. Hypertrichosis is an aetiologically heterogeneous condition: a substantial proportion of cases are genetic, congenital, or drug-induced, and are not driven by androgen excess. Where androgens are implicated, therapies with more direct anti-androgenic mechanisms — such as spironolactone, cyproterone acetate, or eflornithine (for localised facial hair) — are already established first-line options. Critically, no preclinical models or clinical studies have specifically evaluated Cetrorelix in hypertrichosis. The high TxGNN score most likely reflects indirect ontological proximity in the knowledge graph (GnRH axis → androgens → hair follicle growth) rather than a validated therapeutic relationship, and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.98%), there is no supporting clinical or preclinical evidence for Cetrorelix in hypertrichosis, the mechanistic link is indirect and non-specific, and the drug's MHRA authorisation status and full safety profile have not yet been retrieved for this Evidence Pack.

**To proceed, the following is needed:**

- **Regulatory verification**: Cetrotide (cetrorelix 0.25 mg powder for solution for injection) is believed to hold a valid MHRA authorisation in the UK — the regulatory dataset should be re-queried to confirm current licence status, approved indications, and prescribing restrictions
- **Safety data retrieval**: Obtain the Cetrorelix SmPC to document key warnings, contraindications, special population restrictions (particularly pregnancy and renal impairment), and known drug interactions before any further evaluation
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank (DB00050) to support a formal mechanistic plausibility assessment
- **Subtype stratification**: Identify androgen-dependent hypertrichosis subtypes (e.g., hypertrichosis associated with polycystic ovary syndrome or congenital adrenal hyperplasia) where HPG axis suppression may be most relevant, and distinguish these from genetic or congenital subtypes where GnRH antagonism would have no rational basis
- **Preclinical hypothesis generation**: Seek evidence from existing GnRH antagonist studies in hyperandrogenism models that may indirectly support a hair-growth endpoint
- **Alternative prioritisation**: Across the full TxGNN prediction set for Cetrorelix, **central precocious puberty (rank 10)** carries the strongest mechanistic rationale — CPP is GnRH-dependent, and GnRH class agents are already standard of care — and should be considered the higher-priority candidate for further feasibility assessment; **aromatase excess syndrome (rank 9)** also warrants investigation as a secondary hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

