---
noindex: true
sitemap: false
layout: default
title: Celiprolol Hcl
parent: Model Prediction Only (L5)
nav_order: 147
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Celiprolol Hcl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **0** 
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

## Celiprolol HCL: Repurposing Evaluation — No Prediction Data Available
{: .text-alpha }

## One-Sentence Summary

The TxGNN model returned **no predicted indications** for this candidate, and the underlying Evidence Pack contains critical data gaps in original indication, mechanism of action, and safety profile.
As a result, **no evidence-based repurposing recommendation** can be made at this time.

<!-- review:begin uk-lic-20261106-celiprolol_hcl-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Celiprolol HCL is a beta-adrenoceptor blocking agent not currently authorised for marketing in the United Kingdom. / The TxGNN model returned **no predicted indications** for this candidate, and the underlying Evidence Pack contains critical data gaps in original indication, mechanism of action, and safety profile." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 5 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-celiprolol_hcl-1 -->

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | No TxGNN prediction available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model prediction only (no predictions returned) |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (5 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 5 |
| Recommended Decision | **Hold** |

---

## UK Market Information

<!-- licenses:begin -->

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 020400060AAAAAA | Celiprolol 200mg tablets | Celiprolol hydrochloride |
| 020400060AAACAC | Celiprolol 200mg/5ml oral suspension | Celiprolol hydrochloride |
| 020400060AAABAB | Celiprolol 400mg tablets | Celiprolol hydrochloride |
| 020400060BBAAAA | Celectol 200mg tablets | Celiprolol hydrochloride |
| 020400060BBABAB | Celectol 400mg tablets | Celiprolol hydrochloride |

Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

<!-- licenses:end -->

> **Note for clinicians:** Celiprolol is available in certain other European markets (e.g., France, Germany) for cardiovascular indications.

<!-- review:begin uk-lic-20261106-celiprolol_hcl-3 -->

> **Review correction (2026-11-06)**: Originally stated: "> **Note for clinicians:** Celiprolol is available in certain other European markets (e.g., France, Germany) for cardiovascular indications. However, in the absence of a UK marketing authorisation, any clinical use would require a Specials licence or named-patient basis application via the MHRA, and standard BNF/NICE guidance does not apply." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 5 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-celiprolol_hcl-3 -->

---

## Safety Considerations

No safety data is available in this Evidence Pack. Please refer to the current SmPC (if sourced from another jurisdiction), the BNF, and relevant MHRA guidance before considering any clinical use.

Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Celiprolol HCL is incomplete across all critical domains — TxGNN returned no predicted indications, the mechanism of action is unrecorded, and no safety profile has been retrieved. There is currently no basis on which to evaluate or recommend a repurposing pathway.

<!-- review:begin uk-lic-20261106-celiprolol_hcl-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The Evidence Pack for Celiprolol HCL is incomplete across all critical domains — TxGNN returned no predicted indications, the mechanism of action is unrecorded, the drug has no UK marketing authorisation, and no safety profile has been retrieved." Removed: it treated BNF prescribing codes as MHRA licences or stated a licence status or count; this site's market data is the NHSBSA BNF prescribing code list, rebuilt by ingredient on 2026-11-06, which lists NHS prescribing codes and does not include MHRA licence status. This drug has 5 BNF presentation codes in that list; the Quick Overview and the table under UK Market Information show the current figures. Source: [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification).

<!-- review:end uk-lic-20261106-celiprolol_hcl-2 -->

**To proceed, the following is needed:**

- **TxGNN prediction run**: Re-run the TxGNN pipeline with a confirmed DrugBank ID for Celiprolol (DrugBank DB01353) to generate ranked disease predictions.
- **Mechanism of action**: Retrieve MOA data from DrugBank or literature (celiprolol is understood to be a cardioselective β₁-blocker with partial β₂-agonist activity, but this must be confirmed from source data).
- **Original indication confirmation**: Populate `original_indications` from MHRA Specials records, EMA authorisations, or published pharmacopoeial data.
- **Safety data retrieval**: Download and parse the relevant SmPC (e.g., from the French or German medicines agency) to populate key warnings, contraindications, and drug interaction profile.
- **DrugBank ID linkage**: Confirm and record the DrugBank ID so that DDI queries, category classification, and MOA extraction can proceed correctly.
- **UK pathway assessment**: If a TxGNN prediction is subsequently generated, assess whether a Specials licence or a full MHRA application would be the appropriate UK regulatory route.

---

*This report was generated on 2026-04-05. All findings are based solely on the data provided in Evidence Pack version v4 (candidate ID: TW-UNKNOWN-multi). This report is intended for research purposes only and does not constitute medical advice or a clinical recommendation. Any repurposing candidate requires prospective clinical validation before therapeutic application.*

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the official data this site uses (the NHSBSA BNF prescribing code list; MHRA licence status is not included in it). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Celiprolol HCL is a beta-adrenoceptor blocking agent not currently authorised for marketing in the United Kingdom" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "the drug has no UK marketing authorisation" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |
| 2026-11-06 | Removed: "However, in the absence of a UK marketing authorisation, any clinical use would require a Specials licence or named-patient basis applicatio" | Corrected | [NHSBSA BNF code information](https://www.nhsbsa.nhs.uk/prescription-data/understanding-our-data/bnf-classification) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

