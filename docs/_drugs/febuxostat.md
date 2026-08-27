---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 3
---

# Febuxostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using the evidence pack provided, here is the evaluation report.

---

# Febuxostat: From Hyperuricaemia (Gout) to Renal Hypouricaemia

## One-Sentence Summary

Febuxostat is a xanthine oxidase inhibitor whose established pharmacological role is lowering serum uric acid in patients with hyperuricaemia and gout. The TxGNN model predicts a possible link to **Renal Hypouricaemia** — a condition of *abnormally low* urate — with **1 clinical trial** and **2 publications** currently identified, none of which directly confirm a therapeutic benefit for this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricaemia / gout (established pharmacological use; not captured as licence data in this evidence pack) |
| Predicted New Indication | Renal Hypouricaemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 (limited — one case report and one narrative review; no controlled trial in the target population) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack (flagged as a High-severity data gap). Based on the supporting literature, febuxostat is a **non-purine selective xanthine oxidoreductase inhibitor** — it blocks the enzyme xanthine oxidase, reducing both uric acid production and the generation of reactive oxygen species during purine catabolism. Its proven original use is lowering serum urate in hyperuricaemia and gout.

The relationship to the predicted indication is not a simple "same disease, lower dose" link — it is directionally paradoxical. Renal hypouricaemia (RHUC) is a genetic disorder (typically URAT1 transporter mutations) causing *excessive* urate loss, i.e. abnormally *low* serum urate, the opposite of what febuxostat is designed to treat. The mechanistic rationale identified in the literature is more specific: patients with renal hypouricaemia are prone to exercise-induced acute kidney injury (EIAKI), thought to be driven by xanthine oxidase-mediated oxidative stress in the renal tubules during intense anaerobic exercise. Febuxostat's inhibition of xanthine oxidase may therefore protect against EIAKI in this population — not by correcting the underlying hypouricaemia, but by suppressing a downstream oxidative injury pathway.

This is a plausible but narrow mechanistic hypothesis, currently supported only by a single case report. It should not be interpreted as evidence that febuxostat treats renal hypouricaemia itself; rather, it is a candidate prophylactic strategy for a specific complication (EIAKI) in a specific, rare patient subgroup. Separately, it is worth noting that TxGNN also flagged two related purine-metabolism disorders (HPRT partial deficiency and Lesch-Nyhan syndrome, ranks 2–3) — both of which cause *hyperuricaemia*, a direction fully consistent with febuxostat's established mechanism, and a stronger mechanistic fit than the rank-1 prediction reviewed here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study examining whether uric-acid-lowering control affects stone recurrence and renal function in patients with hyperuricaemia-associated renal calculi. Studies hyperuricaemia (not renal hypouricaemia), so relevance to the predicted indication is indirect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case report | Internal Medicine (Tokyo) | Describes a 16-year-old athlete with familial renal hypouricaemia (URAT1 mutations) and recurrent exercise-induced acute kidney injury; proposes febuxostat as prophylaxis by suppressing xanthine oxidoreductase-driven oxidative injury. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricaemia aetiology and clinical relevance for rheumatologists; general background on the condition, not febuxostat-specific. |

---

## UK Market Information

Febuxostat does not currently hold a marketing authorisation in the UK within this evidence pack (0 authorisations on record; market status "Not marketed"). No product-specific licence, brand name, or dosage form data is available.

---

## Safety Considerations

SmPC warnings and contraindications data for febuxostat were not available in this evidence pack (flagged as a **Blocking** data gap — this prevents the drug from entering the initial safety screening stage). No drug–drug interaction data was returned by the interaction query.

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic link to renal hypouricaemia is indirect and narrow (protection against a downstream complication, not treatment of the condition itself), and is currently supported by only a single case report and a general review — insufficient for L1/L2-level confidence despite the very high TxGNN score.
- A Blocking data gap exists for SmPC warnings/contraindications, which prevents this candidate from completing even the initial (S1) safety pre-assessment.

**To proceed, the following is needed:**
- SmPC warnings, contraindications, and full prescribing information for febuxostat (resolves Blocking gap DG001)
- Confirmed mechanism-of-action documentation (resolves High-severity gap DG002)
- Dedicated studies of febuxostat specifically in renal hypouricaemia / exercise-induced acute kidney injury prevention, beyond the single case report currently available
- Assessment of the regulatory pathway, given febuxostat is not currently marketed in the UK
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

