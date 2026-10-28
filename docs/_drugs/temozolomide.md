---
layout: default
title: Temozolomide
parent: Model Prediction Only (L5)
nav_order: 602
evidence_level: L5
indication_count: 1
monitor_inn: "Temozolomide"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-10-23
description: "Temozolomide: predicted new indication Cauda equina neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Temozolomide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Temozolomide: Cauda equina neoplasm
{: .text-alpha }

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy agent, with relations recorded in the knowledge graph for anaplastic astrocytoma, astrocytoma (excluding glioblastoma) and brain glioblastoma.
The TxGNN model predicts it may be effective for **cauda equina neoplasm**, but there are **no registered clinical trials** and only **3 publications** (all case reports, one directly relevant), so the evidence is very limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cauda equina neoplasm |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Temozolomide is an oral alkylating agent. It methylates DNA (at O6-guanine, N7-guanine and N3-adenine), producing cytotoxic lesions and apoptosis in dividing cells. Its activity is greatest in tumours with MGMT promoter silencing. Detailed mechanism of action data are not available in the data compiled for this report, so this description is based on general pharmacological knowledge.

Cauda equina neoplasms are mostly myxopapillary ependymomas. These are glial tumours of the central nervous system. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The MGMT status of these tumours is not established in the data compiled, and the TxGNN score is a computational prediction, not clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | Case report | European Spine Journal | Remarkable response to temozolomide in a relapsed spinal myxopapillary ependymoma with multiple recurrence and cerebrospinal dissemination |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | Case report | Medicine | Nasal NUT carcinoma with repeated responses during multimodal treatment including radiotherapy; not a cauda equina tumour |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | Case report | Neuro-Chirurgie | Neuromeningeal cryptococcosis in an immunocompromised child treated for pontine glioma; not relevant to efficacy in cauda equina tumours |

Only one report (a single case of spinal myxopapillary ependymoma) is close to the predicted disease, and it does not constitute a study of cauda equina neoplasm as a group.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0801050Y0AAADAD | Temozolomide capsule 20 mg | Not recorded | Not recorded |

The list contains one single-ingredient authorisation record, and it is complete. No approved indication text is available in the data compiled, so the original indications above are not confirmed licence wording.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions. Knowledge-graph contraindication relations include thrombocytopenia, neutropenia, pancytopenia and aplastic anaemia, indicating haematological toxicity is a key concern |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Handling Protection | Follow local cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindication relations recorded in the knowledge graph (not label text):** liver failure, thrombocytopenia, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, pneumocystosis, pancytopenia, lymphopenia, myelodysplastic syndrome, idiopathic aplastic anaemia and aplastic anaemia.
- **Drug interactions:** 100 interactions were found in the interaction database. Of those shown, naltrexone is rated Moderate and levofloxacin Minor. The remainder shown (for example pantoprazole, omeprazole, lansoprazole, metformin, morphine, prednisone, hydrocortisone and doxycycline) have no assigned severity level.

Please refer to the SmPC and BNF for authoritative safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials are registered, and the only directly relevant publication is a single case report in spinal myxopapillary ependymoma. The prediction therefore rests on model output and mechanistic reasoning, which places it at evidence level L5. The product has an established UK presence, but its safety profile includes significant haematological toxicity.

**To proceed, the following is needed:**
- Case series, registry data or prospective studies of temozolomide in myxopapillary ependymoma and other cauda equina tumours
- MGMT promoter status data for these tumours
- Detailed mechanism of action data
- Licence indication text and SmPC warnings and contraindications for the UK product
- A haematological monitoring and safety plan for use outside the current indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

