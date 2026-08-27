---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 7
---

# Felodipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Using the Evidence Pack provided, here is the evaluation report.

# Felodipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Felodipine is a dihydropyridine calcium channel blocker whose established use is the treatment of hypertension (and, off-label, angina). The TxGNN model predicts it may be effective for **Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia**, but this direction is currently supported only by **0 clinical trials** and **20 publications**, none of which study felodipine directly in this indication — they address the general biology of hypoxia. Given a blocking data gap on MHRA safety information and no confirmed UK marketing authorisation in this dataset, the evidence base is not yet sufficient to progress this candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (established indication for the dihydropyridine calcium-channel-blocker class; specific UK licence wording not available in this dataset) |
| Predicted New Indication | Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| UK Market Status | Not Marketed (no marketing authorisation record in this dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this dataset (flagged as a High-severity data gap). Based on established pharmacological knowledge, felodipine is a dihydropyridine calcium-channel blocker that is highly vascular-selective — it inhibits L-type calcium channels in vascular smooth muscle with minimal effect on cardiac contractility, producing potent peripheral and, in principle, pulmonary vasodilation. Its efficacy in systemic hypertension is well established, and mechanistically a vasodilator of this class could plausibly lower pulmonary vascular resistance in patients whose pulmonary hypertension arises from chronic lung disease and/or hypoxia (so-called Group 3 pulmonary hypertension).

However, this mechanistic plausibility needs an important caveat that a reviewer should weigh carefully: current pulmonary hypertension management guidance generally **advises against** calcium-channel blockers in Group 3 (lung disease/hypoxia-associated) pulmonary hypertension, because hypoxic pulmonary vasoconstriction is a protective mechanism that helps match ventilation to perfusion. A non-selective pulmonary vasodilator such as felodipine risks blunting this protective response and worsening ventilation–perfusion mismatch and hypoxaemia — the opposite of the intended benefit. This is a well-recognised distinction from Group 1 pulmonary arterial hypertension, where CCBs benefit a small subset of vasoreactive-positive patients.

None of the 20 literature items retrieved for this predicted indication actually studies felodipine in pulmonary hypertension; they are general reviews and mechanistic papers on hypoxia biology (neurodegeneration, oncology, immunology, altitude physiology, etc.) that establish background plausibility for a hypoxia-driven disease process but do not test the drug. This weakens the strength of the repurposing signal considerably relative to a purely score-based reading.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Reviews the mechanisms of hypoxaemia (ventilation-perfusion mismatch, shunt, hypoventilation, diffusion limitation); background respiratory physiology, not felodipine-specific |
| [27423661](https://pubmed.ncbi.nlm.nih.gov/27423661/) | 2016 | Review | Cell and Tissue Research | Discusses hypoxia and HIF-1 signalling in tissue repair and fibrosis; general mechanistic relevance to hypoxic lung pathology |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Review | Journal of Applied Physiology | Overview of hypoxia research progress in respiratory/exercise physiology |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | General review of hypoxia-mediated cellular adaptation mechanisms |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Reviews therapeutic modification of tumour hypoxia; oncology-focused, tangential relevance |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Review | Annual Review of Immunology | Reviews hypoxia and innate immune/inflammatory signalling (HIFs) |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Reviews hypoxia's role in brain ageing and neurodegeneration |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Reviews cognitive impairment caused by acute/chronic hypoxia |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Reviews the role of hypoxia in multiple sclerosis pathology |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Revista Medica del Instituto Mexicano del Seguro Social | Discusses hypobaric hypoxia and altitude physiology |

**Note:** None of the above literature directly evaluates felodipine in pulmonary hypertension; all items support only the general biological plausibility of hypoxia as a disease mechanism. Ten further items retrieved were even more tangential (oncology-specific hypoxia biology unrelated to pulmonary vasculature) and have been omitted from this table.

---

## UK Market Information

No UK marketing authorisation records are available in the current dataset (total licences: 0; market status: Not Marketed). This should be independently verified against the MHRA Products database, as felodipine is a long-established antihypertensive in UK clinical use — its absence here most likely reflects a data-collection gap (see DG001) rather than genuine absence from the UK market, and should be confirmed before further evaluation.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

In addition, reviewers should note the mechanistic safety concern discussed above: calcium-channel blockers, including felodipine, are generally not recommended in pulmonary hypertension associated with chronic lung disease and/or hypoxia (Group 3), owing to the risk of worsening hypoxaemia through inhibition of hypoxic pulmonary vasoconstriction. This is a pharmacological consideration based on established clinical knowledge of the drug class, not a finding extracted from the evidence pack, and should be verified against current specialist pulmonary hypertension guidance before any further action.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A blocking data gap on MHRA warnings/contraindications (DG001) prevents even an initial (S1) safety assessment, and the mechanism-of-action data needed to assess the biological rationale is also missing (DG002).
- The top-ranked predicted indication has no supporting clinical trials, and its literature evidence is indirect (general hypoxia biology) rather than felodipine-specific.
- A recognised class-level safety concern — that CCBs may worsen hypoxaemia in lung-disease-associated pulmonary hypertension — argues for caution rather than straightforward extrapolation from the antihypertensive indication.
- UK market status is recorded as not marketed in this dataset, which itself needs confirmation before any repurposing pathway could be considered.

**To proceed, the following is needed:**
- MHRA SmPC data: warnings, contraindications, and drug interactions (resolves DG001)
- Structured mechanism-of-action data from DrugBank (resolves DG002)
- Confirmation of felodipine's actual current UK marketing authorisation status
- Felodipine-specific (not general hypoxia) clinical or pharmacodynamic studies in Group 3 pulmonary hypertension populations
- A specialist clinical pharmacology opinion on the hypoxic-pulmonary-vasoconstriction risk before any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

