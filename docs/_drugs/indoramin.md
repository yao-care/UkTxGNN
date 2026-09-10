---
layout: default
title: Indoramin
parent: 僅模型預測 (L5)
nav_order: 314
evidence_level: L5
indication_count: 10
---

# Indoramin
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

# Indoramin: From Hypertension to Benign Prostatic Hyperplasia

## One-Sentence Summary

Indoramin is a selective α1-adrenergic receptor antagonist historically used to treat hypertension (and, in the UK, licensed for benign prostatic hyperplasia/enlargement under the brand name Doralese, now discontinued). The TxGNN model predicts it may be effective for **Benign Prostatic Hyperplasia**, with **0 clinical trials** and **8 publications** currently supporting this direction — all class-level (α1-blocker) reviews and cohort studies rather than indoramin-specific trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no active licence on file); literature indicates historical use as an antihypertensive and, in the UK, for BPH/BPE |
| Predicted New Indication | Benign Prostatic Hyperplasia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is currently unavailable (data gap). However, the literature included in this evidence pack consistently and independently describes indoramin as a selective postsynaptic **α1-adrenergic receptor antagonist**, originally developed for hypertension. Notably, one of the retrieved reviews (PMID 11829730) explicitly lists "indoramin (Doralese)" alongside prazosin, doxazosin and terazosin as α1-blockers used in the treatment of benign prostatic enlargement — indicating indoramin held a UK licence for BPH under this brand name in the past.

The mechanistic link to BPH is well established at the class level: α1A-receptor blockade relaxes smooth muscle in the prostate and bladder neck, reducing the dynamic component of bladder outlet obstruction. This is the same mechanism underlying currently licensed BPH agents (tamsulosin, terazosin, doxazosin, alfuzosin), making indoramin's predicted repositioning to BPH pharmacologically coherent rather than a spurious knowledge-graph signal.

That said, the supporting literature for this specific indication (9 papers, tier 2–3) consists entirely of general BPH/α-blocker reviews and cohort studies — none report indoramin-specific randomised trial data in a BPH population. The evidence therefore supports plausibility by drug class rather than confirmed drug-specific efficacy, and indoramin currently has no active UK marketing authorisation (0 licences on file), which is a material constraint on repurposing feasibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15082205](https://pubmed.ncbi.nlm.nih.gov/15082205/) | 2004 | RCT | European urology | Compared 5-alpha reductase inhibition vs α-blockade for preventing acute urinary retention and BPH-related surgery in real-world practice |
| [9143856](https://pubmed.ncbi.nlm.nih.gov/9143856/) | 1997 | Review | Drugs & aging | Practical treatment guidelines for symptomatic BPH, covering surgical and medical (α-blocker) options |
| [8918007](https://pubmed.ncbi.nlm.nih.gov/8918007/) | 1996 | Review | East African medical journal | Overview of medical management of BPH, noting α-adrenergic antagonists as a major treatment advance |
| [8880886](https://pubmed.ncbi.nlm.nih.gov/8880886/) | 1996 | Review | Pharmacological research | Overview of α1-adrenoceptor antagonists in the pharmacological management of BPH |
| [11829730](https://pubmed.ncbi.nlm.nih.gov/11829730/) | 2002 | Review | Expert opinion on pharmacotherapy | Reviews α1-adrenoceptor antagonists (including indoramin/Doralese) in lower urinary tract disease |
| [11111208](https://pubmed.ncbi.nlm.nih.gov/11111208/) | 2000 | Cohort | European urology | UK GPRD-based study on real-life progression and management of LUTS/BPH, 1992–1998 |
| [14641795](https://pubmed.ncbi.nlm.nih.gov/14641795/) | 2003 | Cohort | Journal of internal medicine | Association between α-blocker use and risk of hip/femur fractures |
| [11275742](https://pubmed.ncbi.nlm.nih.gov/11275742/) | 2001 | Cohort | European urology | Triumph project: UK general practice database analysis of LUTS/BPH management and treatment effectiveness |

---

## UK Market Information

No active UK marketing authorisation is currently on file (total licences: 0; market status: Not marketed). Literature within this evidence pack indicates indoramin was historically marketed in the UK as **Baratol** (hypertension) and **Doralese** (benign prostatic hyperplasia/enlargement); both appear to have been discontinued. Confirmation of current MHRA licence status and discontinuation history is needed before further evaluation.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for indoramin in BPH is sound (established α1-blocker class effect, and indoramin previously held a UK BPH licence as Doralese), but the current evidentiary base is class-level only — no indoramin-specific clinical trials for BPH are registered, and the drug has no active UK marketing authorisation.

**To proceed, the following is needed:**
- Confirmed mechanism of action data from DrugBank (currently a data gap)
- MHRA/SmPC safety data — key warnings, contraindications, drug interactions (currently all data gaps)
- Clarification of historical Doralese licence withdrawal reason, and any barriers to reintroduction
- Indoramin-specific efficacy/safety data in a BPH population, or a formal bridging argument from class-effect evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

