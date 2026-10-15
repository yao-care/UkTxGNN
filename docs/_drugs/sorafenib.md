---
layout: default
title: Sorafenib
parent: High Evidence (L1-L2)
nav_order: 573
evidence_level: L2
indication_count: 10
---

# Sorafenib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Sorafenib: From Hepatocellular Carcinoma to Liposarcoma

## One-Sentence Summary

Sorafenib is an oral multikinase inhibitor, originally used to treat hepatocellular carcinoma, renal cell carcinoma and thyroid carcinoma.
The TxGNN model predicts it may be effective for **liposarcoma**, with **1 clinical trial** (a Phase 2 study in soft tissue sarcomas generally) and **8 publications** currently supporting this direction. Most of this evidence concerns soft tissue sarcomas as a group rather than liposarcoma specifically.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatocellular carcinoma (also renal cell carcinoma and thyroid carcinoma) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

The original indication is taken from the knowledge-graph indication list, because the licence record compiled for this report contains no approved-indication text.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, sorafenib is a multikinase inhibitor acting on RAF, VEGFR, PDGFR and KIT. By blocking these pathways it may suppress MAPK signalling and tumour angiogenesis.

Its efficacy has been established in hepatocellular and renal cell carcinoma, both of which are highly vascular tumours. Soft tissue sarcomas, including dedifferentiated liposarcoma, also depend on growth-factor signalling. Preclinical work in dedifferentiated liposarcoma xenograft models (including PTEN down-regulation and response to PI3K pathway inhibition) and in cell lines supports biological plausibility.

However, histology-specific benefit in liposarcoma has not been clearly shown. The clinical data come from mixed soft tissue sarcoma populations, so the prediction is an extrapolation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Single-arm trial of sorafenib in advanced soft tissue sarcomas. It is relevant to the sarcoma class but not liposarcoma-specific, and has no randomised comparator. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 trial (SWOG S0505) | Cancer | Intergroup phase 2 trial of sorafenib, a multitargeted tyrosine kinase inhibitor, in advanced soft tissue sarcomas. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Ann Surg Oncol | Neoadjuvant conformal radiotherapy plus sorafenib in locally advanced extremity soft tissue sarcoma. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | Histology-driven treatment of soft tissue sarcomas. Trabectedin is highlighted for liposarcoma, particularly myxoid liposarcoma. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magy Onkol | Treatment of soft tissue sarcomas by histological subtype. |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Mol Cancer Ther | Sorafenib inhibited growth and MAPK signalling in malignant peripheral nerve sheath tumour and dedifferentiated liposarcoma cell lines. |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical | Am J Pathol | Dedifferentiated liposarcoma xenograft models show PTEN down-regulation and response to PI3K pathway inhibition. |

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0801050AJAAAAAA | Sorafenib Tablets 200 mg | Tablet (200 mg) | Not stated in the compiled data |

One valid single-ingredient authorisation is recorded. Please check the current MHRA record, BNF and SmPC for the authorisation number format, indications and any NICE appraisals.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC. FBC, liver function, blood pressure and electrolytes (including phosphate) are suggested by the knowledge-graph contraindication signals below. |
| Handling Protection | Please refer to the SmPC and local cytotoxic handling policy |

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text)**: The knowledge graph links sorafenib to hypertension, liver failure, thrombocytopenia, neutropenia, agranulocytosis, blood coagulation disorders, acute coronary syndrome, coronary artery disease and myocardial infarction or ischaemia, anaemia, hypophosphataemia, pancreatitis, and anxiety and related mood disorders. These should be verified against the SmPC.
- **Drug Interactions**: 100 interactions were identified.
  - **Major**: dolasetron.
  - **Moderate** (examples): clarithromycin, dexamethasone, levofloxacin, famotidine, loperamide, palonosetron, naltrexone and several laxatives or bowel preparations (bisacodyl, lactulose, lactitol, sodium picosulfate, polyethylene glycol, sodium sulfate).
  - **Minor** (examples): metronidazole, dapagliflozin, naloxegol.

Label warnings were not available in the compiled data. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score is high, but the only direct clinical evidence is a small, single-arm Phase 2 trial in mixed soft tissue sarcomas, with no liposarcoma-specific efficacy data and no Phase 3 trials.
- Established treatments for liposarcoma exist, such as trabectedin.
- Label safety data are also missing from the data compiled for this report.

**To proceed, the following is needed:**
- Subgroup results for liposarcoma from the Phase 2 soft tissue sarcoma trials (NCT00217620 and SWOG S0505).
- Mechanism of action data and SmPC-based warnings and contraindications, with a safety review of the knowledge-graph signals (cardiovascular, haematological, hepatic).
- The approved indication text for the UK authorisation.
- A liposarcoma-specific prospective study, ideally in dedifferentiated disease, before any clinical positioning.

## Other Predicted Indications (for Context)

The data also include lower-ranked predictions, summarised briefly:

- **Female breast carcinoma (L2, Research Question)**: Several completed Phase 1/2 combination trials exist, including NCT00828074, NCT00634634 and NCT00548899. The one randomised Phase 2 trial (NCT00573755) was terminated with 4 patients. There is no Phase 3 evidence and efficacy signals are modest.
- **Renal pelvis carcinoma (L2, Hold)**: Small Phase 2 urothelial cancer trials (NCT00112905, NCT00112671) showed no convincing single-agent activity.
- **Dermatofibrosarcoma protuberans (L4, Research Question)**: A coherent PDGFR-based rationale and one case report of response (PMID 23557478), but imatinib is the established option.
- **Unclassified renal cell carcinoma (L4, Research Question)**: Only case reports and descriptive literature exist.
- **Ovarian myxoid liposarcoma, Xp11.2/TFE3-associated renal cell carcinoma, renal cell carcinoma associated with neuroblastoma, childhood kidney cell carcinoma and vulva sarcoma (all L5, Hold)**: These have no trials or literature.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

