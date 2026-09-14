---
layout: default
title: Oxitriptan
parent: 僅模型預測 (L5)
nav_order: 436
evidence_level: L5
indication_count: 10
---

# Oxitriptan
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

# Oxitriptan: From No Marketed Indication to Insomnia

## One-Sentence Summary

Oxitriptan (5-hydroxytryptophan, 5-HTP) currently holds no UK marketing authorisation and no approved indication is on record; historically it has been available as a dietary supplement and studied as a direct serotonin precursor for mood, sleep and pain-related conditions.
The TxGNN model predicts it may be effective for **Insomnia**, with **6 clinical trials** and **7 publications** identified — though none of these directly confirm therapeutic efficacy for insomnia, and one trial highlights a serious historical safety signal (eosinophilia-myalgia syndrome) linked to contaminated 5-HTP batches.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None on record — not currently marketed for any approved indication |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source dataset (DrugBank MOA field is a data gap). Based on the pharmacological literature returned in the evidence pack, oxitriptan is the metabolic intermediate between tryptophan and serotonin: it is decarboxylated directly to 5-hydroxytryptamine (5-HT), which is further converted to melatonin. Because 5-HT and melatonin are central regulators of the sleep–wake cycle, raising 5-HT synthesis is mechanistically plausible as a route to improving sleep.

However, the drug has no established original indication to compare against — it has never held a UK marketing authorisation. The available evidence is overwhelmingly indirect: animal models of pharmacologically-induced insomnia (e.g. PCPA-induced insomnia in cats/rats) show that 5-HTP restores sleep architecture, and isolated human case reports from the 1970s–80s (Morvan's disease, post-traumatic insomnia) describe favourable responses. There is, notably, no completed RCT in the pack that tests 5-HTP specifically as a treatment for a clinically diagnosed insomnia population.

A further complication is a well-documented historical safety signal: contaminated batches of L-tryptophan/L-5-HTP supplements caused an outbreak of eosinophilia-myalgia syndrome (EMS) in the late 1980s, a potentially fatal condition. This means any repurposing pathway must address manufacturing purity and impurity control before efficacy questions are even considered.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06718452](https://clinicaltrials.gov/study/NCT06718452) | N/A | Not yet recruiting | 100 | Tinnitus/neuroinflammation trial (umPEA/LUT) — no direct link to 5-HTP or insomnia (relevance: C) |
| [NCT04078724](https://clinicaltrials.gov/study/NCT04078724) | N/A | Completed | 33 | RCT of 5-HTP supplementation on sleep quality and gut microbiome in older adults with normal cognition vs. MCI (relevance: C) |
| [NCT03364101](https://clinicaltrials.gov/study/NCT03364101) | N/A | Completed | 60 | "PowerOff" study exploring sleep quality vs. placebo; title alone insufficient to confirm 5-HTP involvement (relevance: C) |
| [NCT00001918](https://clinicaltrials.gov/study/NCT00001918) | N/A | Completed | 20 | Clinical evaluation of L-5-HTP-related eosinophilia-myalgia syndrome (EMS) — an important **safety** signal rather than efficacy evidence (relevance: B) |
| [NCT06893822](https://clinicaltrials.gov/study/NCT06893822) | N/A | Recruiting | 20 | Griffonia simplicifolia (natural 5-HTP source) on pain sensitisation; primary endpoint is pain, not sleep (relevance: C) |
| [NCT06365801](https://clinicaltrials.gov/study/NCT06365801) | N/A | Not yet recruiting | 100 | Acupuncture study in irritable bowel syndrome; unrelated to insomnia (relevance: C) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2962265](https://pubmed.ncbi.nlm.nih.gov/2962265/) | 1987 | Review | Revue médicale de la Suisse romande | Overview of indications for L-5-HTP in neurology |
| [33634088](https://pubmed.ncbi.nlm.nih.gov/33634088/) | 2021 | Review (biosynthesis) | Frontiers in Bioengineering and Biotechnology | Advances in microbial production of 5-HTP; notes its use in depression, insomnia, migraine |
| [38403005](https://pubmed.ncbi.nlm.nih.gov/38403005/) | 2024 | Animal study | Journal of Ethnopharmacology | Chinese herbal formula (GHYSJ) improves sleep in sleep-deprived mice via NLRP3/Caspase1/GSDMD pathway; not a direct 5-HTP efficacy study |
| [40350945](https://pubmed.ncbi.nlm.nih.gov/40350945/) | 2025 | Animal study | China Journal of Chinese Materia Medica | Fushen Decoction affects 5-HT/GABA systems in PCPA-induced insomnia mouse model |
| [32006050](https://pubmed.ncbi.nlm.nih.gov/32006050/) | 2020 | Biosynthesis study | Applied Microbiology and Biotechnology | Industrial production optimisation of 5-HTP via engineered tryptophan pathway; not a clinical study |
| [4548556](https://pubmed.ncbi.nlm.nih.gov/4548556/) | 1974 | Case report / cohort | Revue Neurologique | Polygraphic/metabolic study of persistent insomnia with hallucinations (Morvan's fibrillar chorea) |
| [4128428](https://pubmed.ncbi.nlm.nih.gov/4128428/) | 1974 | Case report | Electroencephalography and Clinical Neurophysiology | Single case of 4-month agrypnia in Morvan's disease with favourable response to 5-HTP |

## UK Market Information

Oxitriptan currently holds **no UK marketing authorisation** and no licences are recorded in the source dataset (0 licences; market status: Not Marketed). No brand product, dosage form, or approved indication text is therefore available for this drug in this jurisdiction.

## Safety Considerations

- **Historical safety signal (from evidence, not structured safety data):** In the late 1980s, contaminated batches of L-tryptophan and L-5-hydroxytryptophan supplements caused an outbreak of **eosinophilia-myalgia syndrome (EMS)**, a potentially fatal condition affecting over 1,500 people, with fatalities reported. NCT00001918 was set up specifically to clinically evaluate this signal. Any future development of oxitriptan for a therapeutic indication would need to demonstrate robust manufacturing purity controls to exclude recurrence of this risk.
- No structured key warnings, contraindications, or drug-drug interaction data are currently available for this compound (flagged as a **Blocking** data gap — DG001, TFDA/UK label warnings not yet obtained). Please refer to the SmPC and BNF once available, and report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (serotonin precursor → sleep-wake regulation) is biologically plausible, but the evidence base is limited to animal models, single-patient case reports from the 1970s–80s, and trials where 5-HTP is a secondary/incidental exposure rather than an active intervention tested for insomnia. No completed RCT in a diagnosed insomnia population exists in the current evidence pack, and a serious historical manufacturing-related safety signal (EMS) has not been resolved.

**To proceed, the following is needed:**
- TFDA/UK-equivalent product labelling — warnings, contraindications and DDI data (Blocking gap DG001)
- Confirmed mechanism of action documentation (High-priority gap DG002)
- A purpose-designed RCT in a diagnosed insomnia population with validated sleep outcome measures
- Manufacturing/purity assurance data addressing the EMS contamination risk before any clinical development is considered
- Note: among the other TxGNN-predicted indications for this drug, **anxiety** (rank 3, evidence level L3) has comparatively stronger evidence, including a Cochrane systematic review and a double-blind RCT (PMID 3312397), and may warrant separate evaluation as a higher-priority candidate than insomnia.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

