---
layout: default
title: Nisoldipine
parent: 僅模型預測 (L5)
nav_order: 416
evidence_level: L5
indication_count: 5
---

# Nisoldipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Nisoldipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Nisoldipine is a dihydropyridine calcium channel blocker conventionally used to treat hypertension.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia**,
but the current evidence base consists only of general hypoxia-pathophysiology literature rather than studies specific to nisoldipine or this indication, and **no clinical trials** have been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no licence text available). Nisoldipine is pharmacologically classified as a dihydropyridine calcium channel blocker, a class conventionally indicated for hypertension — requires formal confirmation |
| Predicted New Indication | Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a data gap). Based on established pharmacological classification, nisoldipine is a second-generation dihydropyridine calcium channel blocker (CCB), acting via inhibition of L-type calcium channels in vascular smooth muscle to produce vasodilation. This class effect is not restricted to the systemic circulation — dihydropyridine and non-dihydropyridine CCBs (e.g. nifedipine, amlodipine) have historically been trialled, and used off-label in selected vasoreactive patients, for pulmonary arterial hypertension. This provides a plausible pharmacological rationale for why a knowledge-graph model might link nisoldipine to a pulmonary hypertension phenotype.

However, the literature returned for this prediction does **not** directly test nisoldipine, CCBs as a class, or pulmonary hypertension treatment. It largely comprises general reviews on hypoxia pathophysiology across unrelated organ systems (brain ageing, cancer biology, multiple sclerosis, headache). The mechanistic overlap is therefore indirect — the shared concept is "hypoxia" rather than a demonstrated drug–disease relationship — and should be treated as a hypothesis-generating signal only, not as supportive evidence in itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Describes the four basic mechanisms of hypoxaemia (low ambient O₂, hypoventilation, V/Q mismatch, right-to-left shunt) — general respiratory physiology, not drug-specific |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | Overview of cellular hypoxia-sensing and its role in vascular disease, inflammation and cancer |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Review | Journal of Applied Physiology | Narrative update on hypoxia physiology research; no pulmonary hypertension or CCB content |
| [27423661](https://pubmed.ncbi.nlm.nih.gov/27423661/) | 2016 | Review | Cell and Tissue Research | Role of hypoxia/HIF-1 signalling in tissue repair and fibrosis |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Review | Annual Review of Immunology | Hypoxia's role in innate immune and inflammatory responses |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Clinical evidence and molecular mechanisms of hypoxia-induced cognitive impairment |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Hypoxia's dual role in neurodegeneration versus neuroprotection with brain ageing |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Interplay between hypoxia and multiple sclerosis pathology |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Revista Medica del IMSS | Hypobaric (altitude) hypoxia and physiological adaptation |
| [27146279](https://pubmed.ncbi.nlm.nih.gov/27146279/) | 2017 | Review | Cephalalgia | Possible role of hypoxia in migraine and cluster headache |

**Note:** none of the above studies evaluate nisoldipine, calcium channel blockers, or pulmonary hypertension treatment directly. They establish that hypoxia is a broadly studied pathophysiological driver across specialties but do not constitute direct supportive evidence for this repurposing candidate.

---

## UK Market Information

Nisoldipine currently holds **no UK marketing authorisation** (market status: Not Marketed; 0 licences on record). No product, dosage form, or approved indication data is available to summarise.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(Key warnings, contraindications and drug–drug interaction data for nisoldipine were not available in this evidence pack and are flagged as a blocking data gap — see Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but supporting evidence is weak and indirect: there are no clinical trials, and the retrieved literature addresses hypoxia biology in general rather than nisoldipine or pulmonary hypertension specifically. Combined with the drug's absence from the UK market and missing core safety data, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- MHRA/SmPC-sourced warnings, contraindications and DDI data (currently a blocking data gap)
- Confirmed mechanism of action via DrugBank (currently a data gap)
- Direct preclinical or clinical evidence linking nisoldipine (or the dihydropyridine CCB class) to pulmonary hypertension outcomes, rather than general hypoxia-pathophysiology literature
- Clarification of nisoldipine's licensing pathway/status before any UK market entry can be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

