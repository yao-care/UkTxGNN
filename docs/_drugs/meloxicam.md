---
layout: default
title: Meloxicam
parent: Model Prediction Only (L5)
nav_order: 389
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Meloxicam is a COX-2-preferential non-steroidal anti-inflammatory drug (NSAID), originally used for rheumatoid arthritis, osteoarthritis and related joint conditions.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, spondyloarthropathy (UK licence indication text not available in the data compiled for this report) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, meloxicam is a COX-2-preferential NSAID that reduces prostaglandin-mediated inflammation and pain. Its efficacy in inflammatory and degenerative joint disease is established.

The predicted condition is a rare skeletal dysplasia caused by loss-of-function variants in *CDMP1/GDF5*. Meloxicam has no known link to GDF5 or BMP signalling, and COX inhibition does not address the underlying genetic defect. The high score most likely reflects proximity in the knowledge graph to arthropathy and skeletal phenotypes rather than a plausible mechanism. At best, meloxicam might offer symptomatic relief of joint pain, which would be an indirect benefit and not disease modification.

**Other predictions in the top 10** (all with no clinical trials):

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Brachyolmia-amelogenesis imperfecta syndrome | 99.92% | L5 | Genetic (LTBP3-related); no mechanistic link to COX inhibition |
| Myosclerosis | 99.90% | L5 | Rare congenital myopathy; no disease-modifying role |
| Brachyolmia | 99.89% | L5 | Genetic skeletal dysplasia; mechanism unrelated |
| Pseudoachondroplasia | 99.81% | L5 | Possible symptomatic relief of secondary joint degeneration only |
| Spondyloarthropathy, susceptibility to | 99.52% | L5 | Near-duplicate of an existing indication, not a true repurposing candidate |
| Rheumatoid nodulosis | 99.51% | L5 | May relieve joint symptoms; does not treat nodules |
| Rheumatoid factor-positive polyarticular JIA | 99.44% | L4 | Subtype of an existing indication; indirect evidence only |
| WHIM syndrome | 99.38% | L5 | CXCR4 gain-of-function immunodeficiency; no plausible link |
| Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.36% | L5 | Extremely rare; no plausible link |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction.

For the eighth-ranked prediction (rheumatoid factor-positive polyarticular juvenile idiopathic arthritis), one indirect paper was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Safety registry study (design not confirmed) | Pediatric Rheumatology Online Journal | Long-term safety and developmental data for celecoxib and non-selective NSAIDs in juvenile idiopathic arthritis. Meloxicam is not specifically assessed. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1001010AAAAAAAA | Meloxicam tablets 7.5 mg | Not stated | Not stated |

The data compiled for this report lists one valid single-ingredient authorisation. The identifier is not in standard MHRA "PL" format, and dosage form, manufacturer and indication text are not available. Please verify against the MHRA product database, the SmPC and the BNF (musculoskeletal and joint diseases, NSAIDs section).

## Safety Considerations

**Contraindications and cautions suggested by the knowledge graph** (these are graph-derived associations, not label text):
- Cardiovascular: hypertension, congestive heart failure, myocardial infarction, coronary thrombosis, stroke and cerebrovascular disorders, cardiovascular and heart disease
- Gastrointestinal: active peptic ulcer disease, gastritis
- Renal: kidney disease, impaired renal function
- Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperlipidaemia (including familial)
- Haematological: blood coagulation disease, anaemia (including macrocytic), haemoglobinopathy
- Other: substance abuse/dependence

**Drug interactions** (100 recorded; examples shown, most rated Moderate):
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
- Antidiabetic agents: metformin, glimepiride, chlorpropamide
- Other NSAIDs and aminosalicylates: acetylsalicylic acid, mesalazine, balsalazide
- Aminoglycosides and glycopeptides: kanamycin, vancomycin
- Potassium salts and bowel preparations: potassium citrate, potassium bicarbonate, sodium sulfate, picosulfuric acid, polyethylene glycol with electrolytes
- Aprepitant (Moderate)
- Linaclotide (Minor)

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by the model score alone (L5), with no trials or publications, and no plausible mechanistic link between COX inhibition and the GDF5-related defect in Hunter-Thompson type acromesomelic dysplasia. NSAID exposure also carries cardiovascular, gastrointestinal and renal risks that would need justification in a rare-disease population.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological hypothesis linking meloxicam to GDF5/BMP signalling or the disease phenotype
- Preclinical or case-based evidence of benefit
- Confirmation of UK licence details (product, dosage form, approved indications) and SmPC warnings and contraindications
- A clinical rationale for symptomatic use only, if pursued, with a safety plan for children and for patients with cardiovascular, renal or gastrointestinal risk
- Review of the near-duplicate predictions (spondyloarthropathy susceptibility, rheumatoid factor-positive polyarticular JIA), which fall within existing indications and may be better treated as label clarifications than as repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

