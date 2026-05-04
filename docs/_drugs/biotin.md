---
layout: default
title: Biotin
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 2
---

# Biotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Biotin: From Vitamin B7 Deficiency Correction to Dyspepsia

## One-Sentence Summary

Biotin (vitamin B7) is a water-soluble vitamin serving as an essential cofactor for multiple carboxylase enzymes, with established clinical use in correcting biotin deficiency states; no formal MHRA marketing authorisation currently exists for any indication in the United Kingdom.
The TxGNN model predicts it may be effective for **Dyspepsia**, with **2 clinical trials** and **7 publications** identified in evidence queries; however, neither trial directly investigates biotin for dyspepsia, and the supporting literature is largely indirect or anecdotal in nature.
Overall evidence remains at Level **L4** (preclinical or mechanistic), and the current body of data does not support progression beyond the exploratory research stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Biotin (vitamin B7) deficiency correction — no formal MHRA-approved indication on record |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L4 |
| UK Market Status | Not marketed (no MHRA marketing authorisation) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not formally documented within this evidence pack. Based on established nutritional pharmacology, biotin (vitamin B7) functions as an essential cofactor for five key carboxylase enzymes — including pyruvate carboxylase, acetyl-CoA carboxylase, propionyl-CoA carboxylase, 3-methylcrotonyl-CoA carboxylase, and β-methylmalonyl-CoA decarboxylase — all of which play central roles in energy metabolism, gluconeogenesis, fatty acid synthesis, and amino acid catabolism. These metabolic pathways are critically important for maintaining the integrity and turnover of rapidly dividing cells, including gastrointestinal epithelial cells lining the stomach and duodenum.

The mechanistic rationale for biotin in dyspepsia remains theoretical at this stage. Biotin's role in gastrointestinal epithelial energy metabolism may theoretically support mucosal barrier integrity, and preclinical animal model data suggest that biotin can modulate gut microbiota composition — a factor increasingly implicated in functional gastrointestinal disorders, including functional dyspepsia. Additionally, one published case report (PMID 15863846) describes an infant whose clinical presentation included dyspepsia alongside confirmed biotin deficiency, suggesting a potential bidirectional relationship between biotin status and upper gastrointestinal function — though this represents a single low-quality observation rather than causal evidence.

It is important to contextualise the TxGNN model's high prediction score (99.43%) as reflecting structural connectivity within its knowledge graph, rather than direct clinical corroboration. No human pharmacological studies have specifically investigated biotin as a treatment for dyspepsia, and the mechanistic rationale remains speculative. Clinicians should interpret this prediction as a hypothesis-generating signal requiring prospective validation before any clinical application is considered.

---

## Clinical Trial Evidence

> ⚠️ **Important caveat**: Both retrieved trials were assessed as **low-relevance (Grade C)** by the evidence pipeline. Neither directly investigates biotin for dyspepsia; they are included here for transparency and completeness.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | Unknown | 150 | Oxycodone vs pregabalin as preemptive analgesia for post-operative pain in elective surgery (laparoscopic cholecystectomy, submucosal resection, breast lumpectomy, median laparotomy) — **not relevant** to biotin or dyspepsia; likely a data pipeline matching error and should be excluded from evaluation |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Serum micronutrient concentrations following transdermal vitamin patch use in post-bariatric surgery patients — provides background on transdermal B-vitamin (potentially including biotin) absorption kinetics; primary endpoint is not dyspepsia efficacy and biotin is not singled out |

No clinical trials directly investigating biotin for dyspepsia have been identified in ClinicalTrials.gov or the WHO ICTRP registry.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Clinical Study | *Minerva Gastroenterol Dietol* | Open multicentre study of a multi-component food supplement (sodium alginate, calcium carbonate, pineapple, papaya, ginger, α-galactosidase, fennel — branded "Perdiges, Bioten") for functional dyspepsia following H. pylori eradication; suggests benefit in symptom relief, but biotin is not an isolated variable and the product name "Bioten" does not confirm biotin content |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case Report | *J Dermatology* | A 5-month-old Japanese infant diagnosed with dyspepsia and fed exclusively on amino acid formula developed classic biotin deficiency (alopecia, periorificial dermatitis, subnormal serum and urinary biotin); suggests an association between amino acid formula feeding, dyspepsia context, and biotin depletion — causal directionality unclear |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Review/Intervention | *Exp Clin Gastroenterol* | A multi-component supplement (inulin, oligofructose, vitamins C, B1, B6, B12, E, PP, folic acid, pantothenic acid, **biotin**, zinc, selenium) evaluated for gut microbiota correction in patients with bronchopulmonary disease on antibiotics — biotin is one of many components; indirect relevance to gut flora modulation |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observational | *Int J Mol Med* | Quantitative immunohistochemistry of stomach antral endocrine cells in 76 IBS patients — demonstrates enteroendocrine cell abnormalities in functional gut disorders; no biotin involvement |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observational | *World J Gastrointest Endosc* | Endocrine cell types in the oxyntic mucosa of IBS patients — provides mechanistic background on gastric neuroendocrine dysregulation in functional GI disease; no biotin connection |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Immunohistochemistry | *J Clin Pathol* | IL-10 localisation in H. pylori-associated gastritis and its counter-inflammatory role — relevant to gastric mucosal immunology; no biotin involvement |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Immunohistochemistry | *Kidney Int* | Small bowel T cells, HLA class II antigen DR, and GroEL stress proteins in IgA nephropathy — intestinal mucosal inflammation in a renal condition; minimal relevance to biotin or dyspepsia |

> ⚠️ **Note**: Of the seven publications retrieved, only PMID 15863846 and PMID 25384804 show any plausible connection to biotin and dyspepsia, and both are of low evidential quality (single case report and indirect multi-component supplement study, respectively). The remaining five are background literature on functional gastrointestinal conditions with no direct biotin relevance.

---

## UK Market Information

Biotin (DB00121) currently holds **no MHRA marketing authorisation** in the United Kingdom and is not listed as a licensed medicinal product in the BNF or subject to any NICE technology appraisal in a therapeutic context.

Biotin is widely available in the UK as a food supplement regulated under food law (rather than the Human Medicines Regulations 2012), typically in formulations of 10–10,000 µg for hair, skin, and nail support. This food supplement status does not constitute a marketing authorisation for medicinal use. Any proposed therapeutic application for dyspepsia would require a full MHRA marketing authorisation application (or, for high-dose investigational use, a Clinical Trial Authorisation).

> No MHRA-licensed products to display.

---

## Safety Considerations

No formal safety data — including key warnings, contraindications, or drug interactions — are available within this evidence pack.

Please refer to the Summary of Product Characteristics (SmPC) and the British National Formulary (BNF) for relevant safety information. Suspected adverse reactions should be reported via the **Yellow Card Scheme** at [https://yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's high prediction score for biotin in dyspepsia is not currently supported by any direct clinical evidence — retrieved clinical trials are unrelated to this repurposing hypothesis (Grade C relevance), the published literature consists entirely of case reports and indirect observational studies, and formal mechanistic data are absent. With no MHRA marketing authorisation, an evidence level of L4, and all safety data categorised as unavailable, this candidate cannot progress beyond the research hypothesis stage at this time.

**To proceed, the following is needed:**

- **Mechanistic documentation**: Formally retrieve and document biotin's mechanism of action (MOA) from DrugBank API or peer-reviewed pharmacology literature, particularly its role in gastrointestinal epithelial metabolism
- **Targeted literature review**: Commission a systematic review specifically examining biotin status, supplementation, and functional gastrointestinal outcomes in human subjects
- **Proof-of-concept study**: At minimum, a well-designed pilot study (n ≥ 30) examining the effect of oral biotin supplementation on validated dyspepsia symptom scores (e.g., Leeds Dyspepsia Questionnaire, ROME IV criteria)
- **Safety data collection**: Document key warnings, contraindications, and drug-drug interaction profile; obtain SmPC or equivalent pharmacovigilance records
- **Regulatory pathway clarification**: Seek MHRA advice on whether high-dose therapeutic biotin would be classified as a medicinal product or food supplement, and whether a Clinical Trial Authorisation would be required for a dyspepsia indication study
- **Dose selection rationale**: Define the proposed therapeutic dose range (standard nutritional doses of 30–300 µg/day versus high-dose regimens of 100–300 mg/day as explored in neurological conditions such as progressive multiple sclerosis)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

