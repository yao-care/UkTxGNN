---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 569
evidence_level: L5
indication_count: 7
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Theophylline: From Obstructive Airway Disease to Thrombotic Disease

## One-Sentence Summary

Theophylline is a long-established xanthine bronchodilator used in asthma and chronic obstructive pulmonary disease (COPD), although this original indication is not recorded in the regulatory data supplied for this evaluation. The TxGNN model's top-ranked new-indication candidate is **Thrombotic Disease** (score 99.62%), but this candidate is supported by **zero clinical trials** and only **tangential literature** (19 publications, mostly assay-development or unrelated cohort studies), and the evidence pack's own review flags it as a probable false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied regulatory data; theophylline is an established bronchodilator for asthma/COPD (obstructive airway disease) — see Safety/MOA notes below |
| Predicted New Indication | Thrombotic Disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 (model prediction only; no supporting clinical or mechanistic studies) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for theophylline in this evidence pack (flagged as a High-severity data gap, DG002). Based on the wider literature captured here, theophylline is known to act as a non-selective phosphodiesterase inhibitor and adenosine receptor antagonist, mechanisms relevant to bronchodilation and airway anti-inflammatory activity — not to platelet function or coagulation.

The supporting literature for "thrombotic disease" does not establish a therapeutic link. Most publications concern platelet-biomarker assay methodology (e.g., platelet factor 4, soluble CLEC-2, microRNA quantification) in which theophylline appears only incidentally, for example as a component of an anticoagulant buffer used during blood sampling, or as the analyte in an unrelated biosensor-development paper. None of the retrieved studies test theophylline as a treatment for thrombosis.

The evidence pack's own repurposing rationale is explicit on this point: there is no clear mechanistic support, and the high TxGNN score most likely reflects semantic proximity between graph nodes (platelet biology, vascular disease terminology) rather than genuine pharmacological plausibility. This is corroborated by the very low candidate rank (4,243 out of the full disease universe), indicating the model itself places limited confidence in this prediction relative to tens of thousands of alternatives.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clinical Pharmacokinetics | Reviews the antiplatelet drug ticlopidine's pharmacokinetics in arterial thrombosis; theophylline is not evaluated as a therapeutic agent |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Cohort | Rheumatology (Oxford) | Examines platelet/neutrophil activation in Behçet's disease by age and sex; no theophylline intervention studied |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Cohort | Inflammatory Bowel Diseases | Investigates platelet-leukocyte aggregate formation in IBD relative to disease activity; theophylline not administered |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Assay development | Analytica Chimica Acta | Describes a gold-nanoparticle electrochemical biosensor for measuring theophylline blood levels — a detection method, not a thrombosis treatment study |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | General review of prostaglandin/thromboxane biology in platelet aggregation and atherosclerosis; theophylline not discussed |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Method paper | British Journal of Haematology | Describes a radioimmunoassay for platelet factor 4; theophylline is mentioned only as a component of the sample anticoagulant, not as a treatment |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Method paper | Platelets | Develops an assay for soluble CLEC-2 as a platelet-activation marker; theophylline not evaluated therapeutically |
| [14231672](https://pubmed.ncbi.nlm.nih.gov/14231672/) | 1964 | Case discussion | Zeitschrift für die gesamte innere Medizin | Discusses chronic cor pulmonale secondary to thromboembolic disease; no direct theophylline efficacy data for thrombosis |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Cohort | Cor et Vasa | Studies T-lymphocyte subsets in vascular disease patients; "theophylline-resistant" T-cells are used only as an immunological marker classification, unrelated to drug efficacy |
| [197665](https://pubmed.ncbi.nlm.nih.gov/197665/) | 1977 | Review | Stroke | Reviews brain oedema classification in stroke; unrelated to theophylline treatment of thrombotic disease |

## UK Market Information

No UK marketing authorisations are currently recorded for theophylline in this evidence pack (market status: Not marketed; total licenses: 0).

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trials and no mechanistically relevant literature support theophylline for thrombotic disease; the retrieved publications are either methodological (assay/biomarker development) or incidental mentions. The evidence pack's own assessment independently concludes this is likely a false-positive prediction driven by knowledge-graph node proximity rather than pharmacological plausibility, consistent with the L5 evidence level and low model rank (4,243).

**To proceed, the following is needed:**
- Resolution of the Blocking data gap (DG001): TFDA/MHRA SmPC warnings and contraindications, without which no safety pre-screening (S1) can begin.
- Resolution of the High-severity data gap (DG002): a documented mechanism of action for theophylline, to properly assess mechanistic plausibility for any new indication.
- Confirmation of the drug's original indication and UK licensing status, which are currently absent from the regulatory data.
- If this candidate is to be pursued further, dedicated preclinical or clinical studies directly testing theophylline in thrombotic disease, as none currently exist.
- Note: within the same evidence pack, other predicted indications (obstructive lung disease, tracheal disease, nasal cavity disease) carry substantially stronger evidence (L1–L3) and may warrant separate, dedicated evaluation reports.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

