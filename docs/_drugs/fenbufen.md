---
layout: default
title: Fenbufen
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Fenbufen
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

# Fenbufen: From Rheumatic Disease (Historical NSAID Use) to Osteoarthritis

## One-Sentence Summary

Fenbufen is a phenylalkanoic acid NSAID that was historically marketed internationally (e.g. as Cinopal/Lederfen) for pain and inflammation in rheumatoid arthritis and osteoarthritis, though it currently holds no UK marketing authorisation and formal regulatory indication data is unavailable. The TxGNN model's top-ranked prediction — **Osteoarthritis** (score 99.00%) — largely re-identifies this drug's own historically established use rather than a genuinely novel indication, supported by **20 PubMed publications** (several 1970s–1980s RCTs) but **no registered clinical trials** in ClinicalTrials.gov or ICTRP.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in UK regulatory records (drug not currently marketed); historical literature indicates use for rheumatic/inflammatory pain (osteoarthritis, rheumatoid arthritis) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L1 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, regulator-confirmed mechanism of action data is not available for Fenbufen (DrugBank field flagged as a data gap). However, the accompanying literature evidence is informative: Fenbufen is a pro-drug phenylalkanoic acid derivative with analgesic, antipyretic and anti-inflammatory activity. Pharmacological studies cited in the evidence base indicate that fenbufen itself has little direct effect on cyclooxygenase, and that its major active metabolite, biphenylacetic acid, is the potent COX-1/COX-2 inhibitor responsible for its therapeutic effect — a classic NSAID mechanism.

This mechanism is directly applicable to osteoarthritis, where prostaglandin-mediated joint inflammation and pain are core pathological features. Notably, the "predicted new indication" here is not truly novel: multiple double-blind RCTs from the late 1970s and early 1980s (predating modern trial registries) already established fenbufen's efficacy in osteoarthritis, comparing it favourably to aspirin, indomethacin and piroxicam. A 1983 review further notes that fenbufen was evaluated in 155 clinical trials, including 53 specifically in osteoarthritis.

In other words, TxGNN's knowledge graph appears not to have this historical indication encoded, so the "prediction" is best understood as a high-confidence rediscovery of an already-proven pharmacological relationship, rather than a mechanistically speculative repurposing hypothesis. This strengthens confidence in the biological plausibility of the signal, but it also means the finding offers limited *new* clinical information — the open question is regulatory and commercial (i.e., whether/how the drug could re-enter UK practice), not mechanistic.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no entries in ClinicalTrials.gov or ICTRP). The supporting evidence below predates modern trial registries and derives entirely from published literature.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [377471](https://pubmed.ncbi.nlm.nih.gov/377471/) | 1979 | RCT | Scand J Rheumatol Suppl | Double-blind crossover RCT (53 patients, knee/hip OA); fenbufen 600 mg/day vs aspirin 3.6 g/day over 4 weeks each — both produced significant improvement in OA activity measures |
| [7044804](https://pubmed.ncbi.nlm.nih.gov/7044804/) | 1982 | RCT | Eur J Rheumatol Inflamm | Long-term double-blind, randomised parallel-group study (110 patients) comparing fenbufen vs indomethacin in OA, assessing both long-term efficacy and safety |
| [7051052](https://pubmed.ncbi.nlm.nih.gov/7051052/) | 1982 | RCT (placebo-controlled) | Pharmacology | Short-term double-blind, placebo-controlled, parallel-group study of fenbufen in osteoarthritis (abstract not available) |
| [6242958](https://pubmed.ncbi.nlm.nih.gov/6242958/) | 1981 | RCT (crossover) | Eur J Rheumatol Inflamm | Single-blind crossover comparison of fenbufen 600 mg nocte vs piroxicam 20 mg nocte in osteoarthritis (abstract not available) |
| [6356911](https://pubmed.ncbi.nlm.nih.gov/6356911/) | 1983 | Review | Am J Med | Summarises 155 clinical trials of fenbufen (102 RA, 53 OA), including 12 pivotal double-blind controlled protocols (4 weeks–1 year duration) |
| [7009135](https://pubmed.ncbi.nlm.nih.gov/7009135/) | 1981 | Review | Drugs | Pharmacological review: fenbufen 600–1000 mg/day comparable in efficacy to aspirin 3–4 g, indomethacin 75–100 mg or phenylbutazone 300–400 mg, generally with fewer side effects |
| [35818275](https://pubmed.ncbi.nlm.nih.gov/35818275/) | 2022 | Review (safety) | Cell Mol Biol (Noisy-le-Grand) | Investigated immunomodulatory and toxic potential of fenbufen in cell-mediated and humoral immunity models; notes contemporary use for pain, pyrexia, OA and RA |
| [347241](https://pubmed.ncbi.nlm.nih.gov/347241/) | 1978 | Clinical Study | Modern Medicine of Asia | Early clinical study of fenbufen in osteoarthritis (abstract not available) |
| [331427](https://pubmed.ncbi.nlm.nih.gov/331427/) | 1977 | Comparative Trial | Revista Medica de Chile | Comparison of fenbufen and acetylsalicylic acid in the treatment of osteoarthritis (abstract not available) |
| [11496378](https://pubmed.ncbi.nlm.nih.gov/11496378/) | 1979 | Clinical Study (non-English) | Acta Rhumatologica | "Fenbufen in osteoarthritis" — non-English clinical study (abstract not available) |

---

## UK Market Information

Fenbufen currently has no UK marketing authorisation on record (0 licences; market status: **not marketed**). No product-level dosage form, brand name, or approved indication text is available for this drug in the evidence pack.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

No structured warnings, contraindications, or drug–drug interaction data were returned for Fenbufen in this evidence pack (safety query status: not found), and this has been flagged as a **blocking** data gap for safety pre-assessment. Note, separately, that the surrounding literature base (outside the formal safety dataset queried here) includes isolated post-marketing case reports historically associated with fenbufen — including pulmonary eosinophilia/rash and pure red cell aplasia — which should be formally verified against the SmPC before any clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic and historical literature evidence for fenbufen in osteoarthritis is strong (L1, multiple RCTs), the candidate cannot currently proceed: Fenbufen holds no UK marketing authorisation, and formal safety data (SmPC warnings, contraindications, DDI) is an unresolved **blocking** data gap that prevents entry into initial safety assessment (S1).

**To proceed, the following is needed:**
- MHRA/regulatory safety documentation (warnings, contraindications, DDI) to close the blocking data gap
- Confirmation of current UK/EU marketing and licensing status, and pathway for reintroduction if none exists
- Formal DrugBank-confirmed mechanism of action data
- Independent verification of historical post-marketing safety signals (e.g. hypersensitivity/pulmonary eosinophilia, red cell aplasia) noted in the literature but not captured in structured safety data

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates identified here require clinical validation before any application in practice.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

