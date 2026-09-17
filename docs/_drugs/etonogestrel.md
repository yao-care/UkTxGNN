---
layout: default
title: Etonogestrel
parent: Moderate Evidence (L3-L4)
nav_order: 250
evidence_level: L4
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a progestogen-only hormone used in long-acting contraceptive implants; no UK marketing authorisation is currently recorded for it in this evidence pack.
The TxGNN model predicts a possible association with **Amenorrhea**, but this is supported by only **1 clinical trial** of low direct relevance and **2 publications**, with a significant caveat that the signal may reflect a known side effect rather than a therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (progestogen-only implant) — no formal UK licensed indication text is available in this evidence pack |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack. Based on what is known, etonogestrel is a single progestogen that suppresses the hypothalamic-pituitary-gonadal axis (inhibiting the LH surge, thickening cervical mucus, and inhibiting ovulation) to achieve its contraceptive effect.

Importantly, amenorrhea is a well-recognised **side effect** of etonogestrel implants — roughly 20–30% of users experience amenorrhea after a year of use — rather than an indication the drug is used to treat. The evidence pack's own repurposing rationale flags this directly: the high TxGNN score is likely learned from drug-adverse-effect association data (etonogestrel *causing* amenorrhea) rather than from evidence of etonogestrel *treating* amenorrhea. This distinction is critical and should be treated as a strong caveat on the prediction, not a confirmation of therapeutic value.

The four lower-ranked candidates in this pack (breast fibrocystic disease, blunt duct adenosis, apocrine adenosis, benign mammary dysplasia) show near-identical scores (0.992–0.996) with zero supporting trials or literature, suggesting a clustered graph-similarity artefact around benign breast/hormonal conditions rather than five independent signals.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | Completed | 498 | Evaluated contraceptive efficacy and safety of the etonogestrel implant used beyond the approved 3-year duration, up to 5 years. **Not designed to test treatment of amenorrhea**; relevance graded C (indirect safety-database source only) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Compared Implanon (etonogestrel) vs Norplant contraceptive implants for efficacy, tolerability and bleeding patterns; no pregnancies over ~340/329 woman-years. Relates to bleeding pattern effects, not amenorrhea treatment |
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT (protocol) | Trials | Study protocol for BIO101 in COVID-19 pneumonia — **unrelated to etonogestrel or amenorrhea**; likely a search/retrieval artefact in this evidence pack |

---

## UK Market Information

No UK marketing authorisation is currently recorded for Etonogestrel in this evidence pack (0 licences, market status "not marketed"). This should be verified directly against the MHRA product database and BNF before further evaluation, as it materially affects feasibility of any repurposing pathway.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is low (L4), the single available trial and literature do not directly test etonogestrel for amenorrhea treatment, and the mechanistic rationale suggests the TxGNN signal likely reflects a known adverse effect (drug-induced amenorrhea) rather than a therapeutic association. Combined with the absence of a UK marketing authorisation and complete absence of safety/label data, this candidate does not currently support progression.

**To proceed, the following is needed:**
- Mechanism-of-action data confirming whether any pharmacological basis exists for *treating* amenorrhea (as opposed to causing it)
- Confirmation of UK regulatory/marketing status directly from the MHRA (this evidence pack shows none on record)
- SmPC-level warnings, contraindications and interaction data (currently a blocking data gap)
- Dedicated clinical evidence specifically evaluating etonogestrel as a treatment for amenorrhea, distinct from its known role as a contraceptive side effect
- Clarification of whether the TxGNN model can distinguish causal (adverse-effect) from therapeutic drug-disease relationships, given the pattern seen here and across the four related lower-ranked breast-condition candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

