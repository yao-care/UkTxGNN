---
layout: default
title: Flutamide
parent: 僅模型預測 (L5)
nav_order: 282
evidence_level: L5
indication_count: 10
---

# Flutamide
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

# Flutamide: From Prostate Cancer (Antiandrogen Therapy) to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Flutamide is a first-generation nonsteroidal antiandrogen, clinically established as a component of combined androgen blockade for hormone-dependent prostate cancer. The TxGNN model additionally predicts a link to a composite label, **"prostate cancer/brain cancer susceptibility"**, but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — the score is high, but the direct evidence base is empty.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (advanced/hormone-dependent), as part of combined androgen blockade — not recorded in UK regulatory licence data, as flutamide is not currently marketed in the UK |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for flutamide is not available in this evidence pack. However, literature retrieved elsewhere in the pack (e.g. PMID 8252497, "Mechanism of action and pure antiandrogenic properties of flutamide") confirms it acts as a competitive androgen receptor (AR) antagonist, blocking testosterone/dihydrotestosterone signalling at the target tissue.

The predicted new indication is a composite TxGNN disease label combining two distinct concepts. The "prostate cancer" component is mechanistically coherent with flutamide's known AR-antagonist action — but the model's own rationale notes that this specific knowledge-graph node has no attached trials or literature of its own. The "brain cancer susceptibility" component has no known AR-signalling-driven mechanism, and the rationale explicitly flags it as an unresolved comorbidity/susceptibility edge in the knowledge graph requiring manual semantic review before this label can be treated as a genuine clinical hypothesis.

It is worth noting that flutamide's use in classic (androgen-dependent) prostate cancer itself is not a novel repurposing signal — TxGNN separately scores "male reproductive organ cancer" (rank 6) with L1 evidence (50 clinical trials, 20 publications), reflecting flutamide's already-established, decades-long clinical use in that setting rather than a new hypothesis. The rank-1 composite label reviewed here is a distinct, much weaker signal that should not be conflated with that established use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## UK Market Information

Flutamide currently holds no UK marketing authorisation (0 licences on file; market status: not marketed). No product-level dosage form or approved-indication data is available for this evidence pack.

---

## Cytotoxicity

Flutamide is used clinically as a hormonal antineoplastic agent (androgen receptor antagonist) in prostate cancer, so this section is included, though it is a hormonal therapy rather than conventional cytotoxic chemotherapy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal antineoplastic (androgen receptor antagonist) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Liver function tests — literature in this evidence pack (PMID 16540588) reports that flutamide metabolites have been associated with severe hepatic dysfunction in some patients; renal function and FBC as per standard oncology monitoring |
| Handling Protection | No cytotoxic-handling requirement identified in this evidence pack (oral hormonal agent, not a parenteral cytotoxic); please refer to the SmPC |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The composite predicted indication carries a high TxGNN score but zero directly attached clinical trials or literature, and the model's own rationale flags the "brain cancer susceptibility" component as an unverified knowledge-graph artefact requiring manual review. Combined with the drug's unlicensed status in the UK, this is insufficient to progress beyond a research question.

**To proceed, the following is needed:**
- MHRA/SmPC-equivalent label data on warnings, contraindications and interactions (currently blocking — no safety data available for S1 assessment)
- Confirmed mechanism-of-action documentation from DrugBank
- Manual clinical/semantic review of the "brain cancer susceptibility" component of the disease label
- Dedicated preclinical or clinical evidence specifically addressing AR signalling in a CNS/brain tumour context, rather than relying on prostate cancer data by extrapolation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

