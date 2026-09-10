---
layout: default
title: Cyproheptadine
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 4
---

# Cyproheptadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the report structure already specified in the task (no additional skill needed — this is a direct content-generation task from a provided evidence pack, not a coding/repo task). Here's the report:

---

# Cyproheptadine: From Historical Antihistamine Use to Allergic Urticaria

## One-Sentence Summary

Cyproheptadine is a first-generation H1-antihistamine with additional anti-serotonergic activity; this evidence pack does not document a specific original approved indication or any current UK marketing authorisation for the drug. The TxGNN model predicts potential efficacy in **Allergic Urticaria**, but the supporting **2 clinical trials** and **19 publications** relate almost entirely to *other* (second-generation) antihistamines rather than cyproheptadine itself, so this should currently be read as a class-effect hypothesis rather than direct evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack — no marketing authorisation or approved indication text is on file |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for cyproheptadine is not currently available in this evidence pack. Based on its known pharmacological classification, cyproheptadine is a first-generation H1-receptor antagonist that also carries notable anti-serotonergic (5-HT2) activity.

H1-receptor antagonism is the core pharmacological mechanism underlying treatment of allergic urticaria, and cyproheptadine possesses this activity, so the prediction is theoretically plausible. However, all clinical trials and literature captured for this candidate concern second-generation antihistamines — loratadine, desloratadine, rupatadine and bilastine — rather than cyproheptadine itself. This evidence can therefore only be treated as an indirect, class-effect inference: cyproheptadine's sedation and anticholinergic profile differs materially from these newer agents, so efficacy and safety cannot be directly extrapolated from them.

No original indication or UK licensing history is recorded for this drug in the evidence pack, and a Blocking data gap has been flagged for missing SmPC warnings/contraindications — meaning a formal safety pre-assessment cannot yet be completed. Both factors weigh against treating this as a strong repurposing signal at this stage, despite the biologically sound mechanistic rationale.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT07101445](https://clinicaltrials.gov/study/NCT07101445) | Phase 4 | Recruiting | 94 | Compares methylprednisolone vs dexamethasone premedication to prevent allergic reaction to motixafortide (Aphexda) in stem cell mobilisation — does not involve cyproheptadine; graded low relevance (class C) |
| [NCT00762983](https://clinicaltrials.gov/study/NCT00762983) | N/A | Completed | 1,003 | Post-marketing drug-use survey of Claritin (loratadine) in paediatric patients — does not involve cyproheptadine; graded low relevance (class C) |

Neither trial provides direct evidence for cyproheptadine in allergic urticaria.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39549290](https://pubmed.ncbi.nlm.nih.gov/39549290/) | 2024 | RCT | Iran J Allergy Asthma Immunol | Compared mometasone nasal spray with different doses of desloratadine and montelukast in childhood allergic rhinitis; not cyproheptadine-specific |
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | Comparative study | Asian Pac J Allergy Immunol | Double-blind cross-over study; cyproheptadine shown effective for cold urticaria in Thai children, comparable to ketotifen |
| [35396016](https://pubmed.ncbi.nlm.nih.gov/35396016/) | 2022 | Review | Profiles Drug Subst Excip Relat Methodol | Comprehensive profile of loratadine, used for chronic urticaria/rhinitis/asthma |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Review | Drugs | Bilastine efficacy in allergic rhinitis and urticaria (Phase III trial summary) |
| [27500993](https://pubmed.ncbi.nlm.nih.gov/27500993/) | 2016 | Review | Expert Opin Drug Saf | Global safety evaluation of rupatadine in allergic rhinitis and urticaria |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Review | Clin Pharmacokinet | Comparative pharmacokinetics/pharmacodynamics of desloratadine, fexofenadine, levocetirizine |
| [18339040](https://pubmed.ncbi.nlm.nih.gov/18339040/) | 2008 | Review | Allergy | Rupatadine's role in allergic rhinitis and chronic urticaria |
| [21162645](https://pubmed.ncbi.nlm.nih.gov/21162645/) | 2011 | Review | Expert Rev Clin Immunol | Rupatadine for allergic rhinitis and urticaria |
| [11398910](https://pubmed.ncbi.nlm.nih.gov/11398910/) | 2001 | Review | Drugs | Desloratadine pharmacology and safety review |
| [33198523](https://pubmed.ncbi.nlm.nih.gov/33198523/) | 2021 | Review | Expert Opin Pharmacother | Second-generation H1-antihistamines in children's allergic rhinitis/urticaria, focus on rupatadine |

Only PMID 7488341 involves cyproheptadine directly, and it concerns cold urticaria rather than allergic urticaria specifically.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*Note: A Blocking data gap (DG001) is recorded — MHRA/manufacturer warnings and contraindications have not yet been retrieved, so no formal safety pre-assessment (S1) can be completed for this candidate.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (H1-antagonism) is sound, but all supporting trial and literature evidence concerns other antihistamines rather than cyproheptadine itself, giving an evidence level of only L4. Combined with a Blocking gap in essential safety data and the absence of any current UK marketing authorisation, this candidate is not ready to advance.

**To proceed, the following is needed:**
- MHRA/SmPC warnings, contraindications and drug-interaction data for cyproheptadine (Blocking — DG001)
- Confirmed mechanism of action documentation (DG002)
- Cyproheptadine-specific clinical evidence in allergic urticaria (rather than class-effect extrapolation from second-generation antihistamines)
- Clarification of regulatory pathway, given the drug currently holds no UK marketing authorisation

---

### Additional Note: Other Predicted Indications in This Evidence Pack

This evidence pack (candidate ID `TW-DB00434-multi`) evaluated four predicted indications for cyproheptadine. Notably, **cold urticaria** is supported by considerably stronger, drug-specific evidence than the top-ranked candidate above and may warrant separate evaluation:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Allergic Urticaria | 99.96% | L4 | S1 | Research Question |
| 2 | Cold Urticaria | 99.76% | L2 | S3 | Proceed with Guardrails |
| 3 | Nasal Cavity Disease | 99.21% | L4 | S0 | Hold |
| 4 | Acute Laryngopharyngitis | 99.13% | L5 | S0 | Hold |

Cold urticaria is supported by multiple direct cyproheptadine RCTs/cohort studies (e.g. PMID 334082, 6480953, 6102102, 5287036) spanning the 1970s–1990s and is considered a well-established, textbook indication rather than a novel TxGNN discovery — it may merit its own dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

