---
layout: default
title: Nitrazepam
parent: 僅模型預測 (L5)
nav_order: 419
evidence_level: L5
indication_count: 3
---

# Nitrazepam
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

# Nitrazepam: From Benzodiazepine Sedative-Hypnotic to Insomnia (Difficulty Initiating and Maintaining Sleep)

## One-Sentence Summary

Nitrazepam is a benzodiazepine; the Evidence Pack does not record a specific original indication or detailed mechanism of action (both flagged as data gaps). The TxGNN model's top prediction is **Insomnia (sleep disorder, initiating and maintaining sleep)** — notably, this is consistent with nitrazepam's long-established clinical use as a hypnotic rather than a genuinely novel repurposing target. Evidence currently consists of **20 published articles** (including two historical double-blind comparative studies) and **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Evidence Pack (no licences on file; historically nitrazepam is a benzodiazepine hypnotic) |
| Predicted New Indication | Insomnia (sleep disorder, initiating and maintaining sleep) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| UK Market Status | Not marketed (per Evidence Pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on general pharmacological knowledge, nitrazepam belongs to the benzodiazepine class, acting as a positive allosteric modulator at GABA-A receptors to produce sedative, hypnotic, anxiolytic, anticonvulsant and muscle-relaxant effects. This class-level pharmacology is directly consistent with a hypnotic role in insomnia.

The Evidence Pack records no original indication for nitrazepam, which limits a formal comparison between "original" and "new" use. However, it is worth flagging explicitly: the top-ranked predicted indication (insomnia) overlaps with nitrazepam's well-documented historical use as a hypnotic (e.g. PMID 4892037, 1969, describing it as "a safe hypnotic" compared with butobarbitone). This suggests the model may be reaffirming an established indication rather than identifying a novel repurposing opportunity — a distinction that should be clarified before this candidate is treated as "new."

Two lower-ranked predictions (acute encephalopathy with biphasic seizures, and Wernicke-Korsakoff syndrome) were also generated but carry weak or absent supporting evidence; the latter was scored by the pipeline as L5/Hold, with the rationale noting no direct mechanistic link between nitrazepam's GABA-A activity and the thiamine-deficiency pathology underlying Wernicke-Korsakoff syndrome.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (neither `clinical_trials` nor `ictrp_trials` returned results for this indication).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | RCT (double-blind) | British Medical Journal | Nitrazepam 5mg as effective as butobarbitone as a hypnotic; safe even in acute overdose up to 80 tablets |
| [6135296](https://pubmed.ncbi.nlm.nih.gov/6135296/) | 1983 | RCT (double-blind cross-over) | Acta Psychiatrica Scandinavica | Nitrazepam 5mg vs triazolam 0.25mg in 26 geriatric inpatients; similar sleep quantity/quality, no significant psychomotor differences |
| [14960254](https://pubmed.ncbi.nlm.nih.gov/14960254/) | 2004 | RCT/HTA | Health Technology Assessment | CBT package vs continued hypnotic use in long-term hypnotic users in general practice |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Review | BMJ Clinical Evidence | Up to 40% of adults have insomnia; prevalence increases with age; risk factors include stress and hyperarousal |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | Review | Clinical Pharmacokinetics | Clinical pharmacokinetic review of nitrazepam |
| [1125532](https://pubmed.ncbi.nlm.nih.gov/1125532/) | 1975 | Case report | British Journal of Psychiatry | Reported case of nitrazepam (Mogadon) dependence |
| [15089115](https://pubmed.ncbi.nlm.nih.gov/15089115/) | 2004 | Review | CNS Drugs | Reviews residual "hangover" effects of hypnotics, including daytime sleepiness and psychomotor impairment |
| [10804040](https://pubmed.ncbi.nlm.nih.gov/10804040/) | 2000 | Review | Drugs | Zolpidem efficacy noted as comparable to benzodiazepines including nitrazepam in treatment of insomnia |
| [39231170](https://pubmed.ncbi.nlm.nih.gov/39231170/) | 2024 | Observational | PLoS One | Consumption patterns and factors associated with inappropriate benzodiazepine prescribing in primary care |
| [10612270](https://pubmed.ncbi.nlm.nih.gov/10612270/) | 1999 | Review | Drug Safety | 15-year risk/benefit review of zopiclone, contextualised against benzodiazepine hypnotics |

---

## UK Market Information

No UK marketing authorisation is currently recorded in this Evidence Pack (0 licences on file, market status "not marketed"). This should be independently verified against the MHRA product database and BNF, as it may reflect a data gap in the source dataset rather than the true regulatory position.

---

## Safety Considerations

A **blocking data gap (DG001)** exists: SmPC/label warnings and contraindications for nitrazepam were not available at the time of this Evidence Pack (data cutoff 2026-09-10), and this must be resolved before any safety (S1) assessment can proceed. No drug-drug interaction data was found (`query_status: not_found`).

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap (missing label warnings/contraindications, DG001) prevents completion of the S1 safety review, regardless of the strength of the efficacy signal. In addition, no registered clinical trials support the insomnia indication, and the predicted "new" indication appears to substantially overlap with nitrazepam's already-established hypnotic use, raising the question of whether this represents genuine repurposing.

**To proceed, the following is needed:**
- Resolve DG001: obtain SmPC/label warnings and contraindications (e.g. from MHRA)
- Resolve DG002: confirm mechanism of action and, ideally, the drug's originally licensed indication(s)
- Formal classification of the 20 literature items (study type/tier) to confirm the L3 evidence level
- Confirmation of current UK marketing authorisation status for nitrazepam
- Clarification on whether "insomnia" should be treated as a novel repurposing candidate or as recognition of existing use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

