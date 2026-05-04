---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: From Gout and Hyperuricaemia to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase (XO) inhibitor with a long-established role in the management of gout, chronic hyperuricaemia, and uric acid nephropathy prevention.
The TxGNN model predicts it may be effective for **Hepatic Porphyria**, with **no registered clinical trials** and **2 publications** currently providing indirect mechanistic support — representing an early-stage hypothesis that warrants dedicated investigation before any clinical application.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout; chronic hyperuricaemia; uric acid nephropathy prevention (MHRA licence data not retrieved — see UK Market Information) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| UK Market Status | No MHRA licence data retrieved (likely a data collection gap) |
| Number of Marketing Authorisations | 0 (data not retrieved) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Allopurinol is best known as a xanthine oxidase inhibitor — it blocks the final steps of uric acid synthesis, making it the cornerstone of long-term gout management. Beyond its effect on uric acid, allopurinol has been reported to inhibit 5-aminolevulinate synthase (ALAS), the rate-limiting enzyme governing hepatic haem biosynthesis. This secondary pharmacological property is the key mechanistic link underpinning the TxGNN prediction.

Acute hepatic porphyrias — including Acute Intermittent Porphyria (AIP), Variegate Porphyria (VP), and Hereditary Coproporphyria (HCP) — share a common pathological driver: overactivation of ALAS, leading to the toxic accumulation of haem precursors such as aminolevulinic acid (ALA) and porphobilinogen (PBG). If allopurinol can meaningfully suppress ALAS activity, it may theoretically reduce precursor overproduction during acute attacks. Additionally, XO inhibition reduces the generation of superoxide radicals (O₂⁻), which may provide secondary hepatoprotection by attenuating oxidative stress in the already-compromised porphyric liver.

It should be noted that detailed mechanism of action data was not available in this evidence pack. The precise molecular pathway by which allopurinol modulates ALAS activity — and whether this effect is clinically relevant at standard therapeutic doses — has not been confirmed in controlled human studies. The relationship of this proposed mechanism to established porphyria treatments (haematin infusion, givosiran) must also be carefully considered before any clinical conclusions are drawn.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis / Mechanistic Review | Medical Hypotheses | Proposes that inhibiting haem utilisation by tryptophan 2,3-dioxygenase (TDO) — or supplementing tryptophan itself — may suppress hepatic ALAS activity and reduce porphyrin precursor accumulation in acute hepatic porphyrias; provides a detailed biochemical rationale for ALAS as a therapeutic target |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal Study (rat) | Biochemical Pharmacology | Examined how carbamazepine exacerbates hepatic porphyria via disruption of haem metabolism in rat liver, using a validated screening model; contextually relevant as a reference framework for assessing drug effects on the haem regulatory pathway |

---

## UK Market Information

No MHRA marketing authorisation data was retrieved for allopurinol in this evidence pack. This is almost certainly a data collection gap: allopurinol is a long-established generic medicine widely available in the United Kingdom, classified under **BNF Section 10.1.4 (Gout and Hyperuricaemia)**, and multiple manufacturers hold MHRA product licences.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|---------------------|
| *Not retrieved* | Allopurinol (various generics) | Tablet (100 mg, 300 mg) | Gout; hyperuricaemia; uric acid nephropathy (see SmPC) |

UK prescribers should consult the current BNF entry and the relevant SmPC directly. This section will be updated once MHRA licence data is retrieved.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> ⚠️ **Additional note from evidence review:** One ranked indication in this evidence pack — immune-mediated necrotising myopathy (rank 8) — highlights that allopurinol itself is a recognised cause of drug-induced myositis. This safety signal should be borne in mind across all repurposing investigations for this drug, particularly for immune-mediated or inflammatory conditions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction rests on a mechanistically coherent hypothesis — allopurinol's documented capacity to inhibit ALAS directly addresses the core pathological driver of acute hepatic porphyrias. However, the current evidence base consists of two indirectly relevant publications (one mechanistic hypothesis paper, one animal pharmacology study), with no clinical trials and no direct human evidence of allopurinol efficacy in porphyria. The evidence level of L4 is insufficient to justify clinical progression without further targeted investigation.

**To proceed, the following is needed:**

- **MHRA licence data retrieval**: Confirm UK regulatory status, approved indications, and licensed dosage forms to complete the regulatory picture
- **Detailed MOA confirmation**: Obtain DrugBank API data and primary literature confirming allopurinol's ALAS inhibitory potency and clinically achievable effect at standard doses (100–300 mg/day)
- **Focused historical literature search**: Search for case reports and older clinical observations of allopurinol in porphyria patients, including pre-1990 literature not captured by the current PubMed query
- **Porphyria guidelines review**: Determine whether the European Porphyria Network (EPNET) or British and Irish Porphyria Network (BIPNET) have previously evaluated or contraindicated allopurinol in porphyria management
- **Safety assessment**: Confirm that allopurinol itself does not precipitate porphyric attacks (some drugs are known porphyrinogenic); this is a prerequisite before any clinical use
- **Proof-of-concept study design**: If preclinical validation supports the ALAS inhibition hypothesis, consider a small Phase 2 mechanistic study measuring ALA/PBG levels in porphyria patients receiving allopurinol

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. Generated: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

