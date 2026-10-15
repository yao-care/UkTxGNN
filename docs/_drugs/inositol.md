---
layout: default
title: Inositol
parent: Model Prediction Only (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
---

# Inositol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Inositol: From Lipid Disorders and Vitamin-Deficiency Conditions to Idiopathic Copper-Associated Cirrhosis

## One-Sentence Summary

Inositol is a vitamin-like compound whose original indications in the data compiled for this report include pellagra, beriberi and several lipid disorders (such as hypertriglyceridaemia and familial combined hyperlipidaemia). The TxGNN model gives its top-ranked prediction, **idiopathic copper-associated cirrhosis**, a very high score, but **no clinical trials and no publications** support this prediction. The only predicted indications with any literature are congestive heart failure and hyperlipoproteinaemia, and neither provides evidence that inositol is effective.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the UK authorisation record; the knowledge graph lists pellagra, beriberi, hypertriglyceridaemia, familial combined hyperlipidaemia and hypoalphalipoproteinaemia |
| Predicted New Indication | Idiopathic copper-associated cirrhosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Inositol is a naturally occurring sugar alcohol that takes part in intracellular signalling (for example, the inositol phosphate and IP3 calcium pathways). Its link to the original lipid-related indications is historical, since inositol esters such as inositol nicotinate were used for lipid lowering.

For idiopathic copper-associated cirrhosis, **no mechanistic rationale is supported by the data compiled for this report**. The score is a model output only. Several liver and portal-hypertension-related diseases (early-onset familial noncirrhotic portal hypertension, hepatopulmonary syndrome, hepatoportal sclerosis, primitive portal vein thrombosis) share exactly the same score. This suggests a common graph-based signal rather than disease-specific evidence, so the score should be treated with caution.

Other predictions with some literature:

- **Congestive heart failure (L4):** Plasma myo-inositol is raised in heart failure and carries prognostic significance (PMID 39121579). This is a biomarker association, and it may even point to a harmful role, so it does not support inositol as a treatment. IP3-dependent calcium signalling is also implicated in cardiac pathology, but only in preclinical and review papers.
- **Hyperlipoproteinaemia (L3):** Several old studies (1976–1983) tested clofibrate combined with inositol nicotinate. The combination confounds any attribution to inositol, and this overlaps with the original lipid indications, so it is not a true repurposing candidate.
- **Acute pulmonary heart disease (L4):** Only indirect literature on calcium signalling and lung injury.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, or for any of the other nine predictions reviewed.

---

## Literature Evidence

There is no literature for the top-ranked prediction, idiopathic copper-associated cirrhosis. The most relevant publications found for the other predicted indications are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39121579](https://pubmed.ncbi.nlm.nih.gov/39121579/) | 2024 | Cohort/Biomarker | EBioMedicine | Plasma myo-inositol is elevated in heart failure (HFrEF and HFpEF) and has prognostic significance; an association only, not evidence of benefit |
| [22834797](https://pubmed.ncbi.nlm.nih.gov/22834797/) | 2012 | Review | Current Medicinal Chemistry | IP3-dependent calcium signalling and chromogranins in cardiomyopathy and heart failure |
| [30971818](https://pubmed.ncbi.nlm.nih.gov/30971818/) | 2019 | Preclinical | Nature | Nitrosative stress drives HFpEF in a mouse model; does not test inositol |
| [6683558](https://pubmed.ncbi.nlm.nih.gov/6683558/) | 1983 | Clinical study | Arzneimittel-Forschung | Clofibrate plus inositol nicotinate over 16 weeks in 20 patients with hyperlipoproteinaemia types IIa, IV and V; confounded by the combination |
| [1253701](https://pubmed.ncbi.nlm.nih.gov/1253701/) | 1976 | Clinical study | Deutsche Medizinische Wochenschrift | Clofibrate plus inositol nicotinate lowered cholesterol by about 20% and triglycerides by about 40%; no significant difference from double-dose clofibrate alone |
| [203832](https://pubmed.ncbi.nlm.nih.gov/203832/) | 1978 | Clinical study | Medizinische Klinik | Long-term clofibrate plus m-inositol nicotinate reduced triglycerides, especially VLDL; phenotype shifts were not avoided by the combination |
| [196436](https://pubmed.ncbi.nlm.nih.gov/196436/) | 1976 | Clinical study | Verhandlungen der Deutschen Gesellschaft für Innere Medizin | Lipoprotein phenotype changes under clofibrate plus m-inositol nicotinate therapy |
| [41253746](https://pubmed.ncbi.nlm.nih.gov/41253746/) | 2025 | Preclinical | Signal Transduction and Targeted Therapy | Targeting endothelial calcium signalling accelerates lung injury resolution; does not test inositol |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 090602800BBJGA0 | IP6 + Inositol powder | Not stated | Not stated |

Only one single-ingredient authorisation is recorded, and it is currently valid. The dosage form and approved indication text are not available in the data compiled for this report.

---

## Safety Considerations

The knowledge graph links inositol to the following conditions as potential contraindications. These come from graph relationships, not from product label text, and should be verified against the SmPC and BNF:

- **Liver and gallbladder:** liver disease, gallbladder disease
- **Blood and coagulation:** thrombocytopenia, blood coagulation disease, haemoglobinopathy
- **Metabolic:** hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, gout, hypophosphataemia
- **Cardiovascular and cerebrovascular:** acute coronary syndrome, coronary artery disease, coronary thrombosis, myocardial infarction, stroke and cerebrovascular disorders, cerebral infarction, cerebral artery occlusion, brain stem infarction, hypotensive disorder
- **Other:** peptic ulcer disease, substance abuse/dependence

Several of these (liver disease, coagulation disorders, cardiovascular disease) overlap with the predicted new indications, which warrants particular care. No drug interaction data were found.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests on a model score alone, with no trials, no publications and no supportable mechanism. The score is shared with several unrelated liver and portal-vascular conditions. The indications with some literature (heart failure, hyperlipoproteinaemia) offer only biomarker associations, preclinical work or old confounded combination studies. The knowledge-graph contraindications include liver and cardiovascular disease, which are relevant to the predicted uses.

**To proceed, the following is needed:**
- Mechanism of action data for inositol (currently unavailable)
- A biological rationale linking inositol to copper-associated cirrhosis, with preclinical or clinical evidence
- Confirmation of the approved indication, dosage form and manufacturer for the UK authorisation
- Label-based warnings and contraindications from the SmPC and BNF
- If heart failure is pursued, work to establish whether raised myo-inositol is protective or harmful before considering any supplementation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

