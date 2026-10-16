---
layout: default
title: Arginine
parent: Model Prediction Only (L5)
nav_order: 70
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Arginine: predicted new indication Gastroparesis (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Arginine"
predicted_indications: ["gastroparesis (disease)"]
---

# Arginine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Arginine: From an Unspecified Original Indication to Gastroparesis

## One-Sentence Summary

Arginine is an amino acid that is marketed in the UK in single-ingredient liquid and powder products, although no approved indication text is available in the data compiled for this report.
The TxGNN model predicts it may be useful for **gastroparesis**, but there are **no registered clinical trials** and the **9 publications** identified are mostly preclinical or unrelated to arginine itself.
Evidence is therefore limited to a model prediction plus a plausible mechanistic rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for arginine is not available in the data compiled for this report. Based on known biochemistry, arginine is the substrate for neuronal nitric oxide synthase (nNOS), which produces nitric oxide (NO). NO is the main inhibitory neurotransmitter responsible for gastric fundic accommodation and pyloric relaxation.

Preclinical work in mice (PMID 25057793) found that glucocorticoid-induced gastroparesis was associated with depletion of L-arginine, and that L-arginine supplementation reversed the delayed gastric emptying. Other animal studies describe impaired nitrergic relaxation of the pyloric sphincter in a Parkinson's disease rat model (PMID 35380456) and myenteric neuropathy in diabetic rats (PMID 18312542). These are consistent with nitrergic dysfunction being a common feature of gastroparesis.

There are important caveats. No human clinical evidence exists, and the very high TxGNN score is a computational prediction only. In diabetic gastroparesis, NO deficiency may result from loss of nNOS-expressing neurons, so supplying more substrate may not be enough to restore function.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Only publications with some relevance to arginine or the nitrergic mechanism are highlighted first. All are preclinical or case-level; none is a human trial.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057793](https://pubmed.ncbi.nlm.nih.gov/25057793/) | 2014 | Preclinical (mouse) | Endocrinology | Glucocorticoids induced gastroparesis in mice via depletion of L-arginine; supplementation reversed the effect |
| [35380456](https://pubmed.ncbi.nlm.nih.gov/35380456/) | 2022 | Preclinical (rat) | Am J Physiol Gastrointest Liver Physiol | Impaired nitrergic relaxation of the pyloric sphincter in a Parkinson's disease rat model |
| [18312542](https://pubmed.ncbi.nlm.nih.gov/18312542/) | 2008 | Preclinical (rat) | Neurogastroenterol Motil | Myenteric neuropathy and nNOS changes in the jejunum of diabetic BB-rats |
| [18322959](https://pubmed.ncbi.nlm.nih.gov/18322959/) | 2008 | Preclinical (mouse) | World J Gastroenterol | Gastric motor effects of ghrelin and GHRP-6 in diabetic mice with gastroparesis (not arginine-specific) |
| [21193530](https://pubmed.ncbi.nlm.nih.gov/21193530/) | 2011 | Preclinical (rat) | Am J Physiol Gastrointest Liver Physiol | Hyperglycaemia inhibits gastric motility via nodose ganglia KATP channels (not arginine-specific) |
| [19023028](https://pubmed.ncbi.nlm.nih.gov/19023028/) | 2009 | Preclinical (animal) | Am J Physiol Gastrointest Liver Physiol | Synchronised gastric electrical stimulation improved vagotomy-induced impaired accommodation via the nitrergic pathway (device study) |
| [31984783](https://pubmed.ncbi.nlm.nih.gov/31984783/) | 2020 | Preclinical (rat) | Am J Physiol Gastrointest Liver Physiol | Sacral nerve stimulation increased gastric accommodation (device study) |
| [8194696](https://pubmed.ncbi.nlm.nih.gov/8194696/) | 1994 | Preclinical (rat) | Gastroenterology | Gastric motor response to food protein-induced anaphylaxis (not arginine-specific) |
| [33867519](https://pubmed.ncbi.nlm.nih.gov/33867519/) | 2021 | Case report | Am J Case Rep | Lifestyle changes normalised serum lactate in an m.3243A>G carrier (not directly relevant) |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 091101000AADJDJ | Arginine Liq Spec 500mg/5ml | Not specified | Not specified |
| 091101000AAFIFI | L-Arginine Pdr | Not specified | Not specified |

Both products are listed as valid, single-ingredient authorisations. Dosage form and approved indication text were not available in the data compiled for this report.

## Safety Considerations

- **Disease associations flagged as potential contraindications (knowledge graph, not label text):** The TxGNN knowledge graph links arginine with contraindication-type relationships to a range of conditions. These should be verified against the SmPC and are grouped below:
  - **Renal:** kidney disease, chronic kidney disease, chronic renal failure, end-stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, renal tubular acidosis
  - **Metabolic and acid-base:** metabolic acidosis, acidosis disorders, phenylketonuria and other disorders of phenylalanine metabolism
  - **Calcium and bone:** hypercalcaemia, humoral hypercalcaemia of malignancy, hyperparathyroidism, osteitis fibrosa, sarcoidosis, lytic metastatic bone lesions, phosphorus metabolism disorders
  - **Cardiovascular:** heart disease, cardiovascular disease, digitalis poisoning, ventricular fibrillation
  - **Haematological:** sickle cell anaemia, hereditary persistence of fetal haemoglobin
  - **Other:** constipation, pyoureter

Please refer to the SmPC and BNF for authoritative safety information, including warnings, contraindications and drug interactions. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score and animal data, with no registered trials and no human evidence. The nitrergic rationale is plausible, but may not hold in diabetic gastroparesis where nNOS-expressing neurons are lost. Safety data from the product labels is also missing.

**To proceed, the following is needed:**
- The SmPC and BNF safety information (warnings, contraindications, interactions) for the UK-authorised arginine products
- Approved indication, dosage form and manufacturer details for the two UK authorisations
- Mechanism of action data confirmed from a source such as DrugBank
- Human evidence, such as a small proof-of-concept study of gastric emptying in patients with gastroparesis, ideally stratified by cause (diabetic, idiopathic, drug-induced)
- A review of the renal, metabolic and cardiovascular conditions flagged above, given that many gastroparesis patients have diabetes and renal impairment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

