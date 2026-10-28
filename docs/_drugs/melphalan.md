---
layout: default
title: Melphalan
parent: Model Prediction Only (L5)
nav_order: 390
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
monitor_inn: "Melphalan"
predicted_indications: ["female breast carcinoma", "rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma"]
description: "Melphalan: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Melphalan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Melphalan: Female breast carcinoma
{: .text-alpha }

## One-Sentence Summary

Melphalan is an alkylating chemotherapy agent, originally used for ovarian cancer.
The TxGNN model predicts it may be effective for **gonadal germ cell tumour**,
with **7 clinical trials** (mostly small, early-phase or mixed-tumour transplant protocols, with melphalan given as part of combination regimens) and **1 publication** (a 1964 paper of limited relevance) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 (one completed Phase 2 trial, but melphalan is part of a combination regimen) |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails (research question only) |

---

## Why is This Prediction Reasonable?

Melphalan is a nitrogen mustard DNA alkylating agent. It forms interstrand crosslinks in DNA, which causes cell death in rapidly dividing cells. Detailed mechanism of action data were not available in the data compiled for this report, so this description is based on general pharmacological knowledge of the drug class.

Ovarian cancer and gonadal germ cell tumours are both tumours arising in the gonads, and germ cell tumours are generally highly chemosensitive to DNA-damaging agents. High-dose melphalan with autologous stem cell rescue has been explored as salvage therapy for relapsed or poor-prognosis disease. This is the only clinical setting in which melphalan has been tested for this indication.

In the available trials, melphalan is usually one component of a multi-drug regimen, so its individual contribution cannot be separated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | Two cycles of high-dose chemotherapy (gemcitabine, docetaxel, melphalan, carboplatin, then ifosfamide, carboplatin, etoposide) for poor-prognosis relapsed germ-cell tumours. The most direct evidence, but melphalan is one component of a combination. |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose melphalan with autologous stem cell support and amifostine cytoprotection in cancer patients, including solid tumours. |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Eight high-dose chemotherapy regimens with autologous transplant for haematological malignancies and selected solid tumours. Germ cell tumours are only a subset. |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | Pilot of busulfan, melphalan and topotecan followed by autologous stem cell transplant in advanced or recurrent tumours. |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | N/A | Completed | 174 | Different high-dose chemotherapy regimens, with or without total-body irradiation, before autologous transplant. Not specific to germ cell tumours. |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Focus on the chemoprotectant amifostine with autologous transplant in paediatric solid and brain tumours. Weak relevance to melphalan efficacy. |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan for recurrent neoplastic meningitis. Different route and clinical setting. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Other | Acta Unio Int Contra Cancrum | Study of the effect of hormonal and alkylating drugs on pituitary follicle-stimulating function. No abstract available, and limited direct relevance to germ cell tumour treatment. |

Literature for related ovarian germ cell tumours is limited to a single case report (PMID 9251739, 1997) describing successful mega-dose chemotherapy with peripheral blood progenitor cell rescue in a metastatic ovarian primitive neuroectodermal tumour.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0801010S0AAABAB (a product code, not a standard PL number) | Melphalan tablets 2 mg | Tablet (inferred from product name) | Indication text not available in the data compiled for this report |

Only one valid single-ingredient authorisation was recorded. Please check the current MHRA record, the SmPC and the BNF for the licensed indications.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High. Bone marrow suppression is the dose-limiting toxicity, and it is more pronounced at high doses requiring stem cell rescue. |
| Emetogenicity Classification | Low to moderate at oral doses; higher with high-dose intravenous regimens |
| Monitoring Items | Full blood count with differential, renal and liver function |
| Handling Protection | Must follow local cytotoxic drug handling regulations |

Please refer to the SmPC warnings and precautions for full detail.

---

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** kidney disease, thrombocytopenia, anaemia (including macrocytic and haemolytic anaemia), leukopenia, agranulocytosis, neutropenia and congenital neutropenia syndromes, interstitial lung disease, pulmonary fibrosis, drug-induced liver injury and vasculitis. These should be checked against the SmPC.
- **Drug interactions:** 100 interactions were recorded. Those listed include moderate interactions with amphotericin B (including the lipid complex, cholesteryl sulfate and liposomal formulations), and minor interactions with cimetidine, levofloxacin, zinc sulfate and zinc gluconate. Several others, including proton pump inhibitors, metformin, vancomycin and prednisone, are of unknown severity.
- Long-term risk of second malignancies, mainly acute leukaemia, is described for alkylating agents in the literature.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (research question only)**

**Rationale:**
There is one completed Phase 2 trial in relapsed germ cell tumours (n=64), but melphalan was part of a multi-drug high-dose regimen and its individual effect cannot be isolated. The remaining trials are small, early-phase or mixed-tumour protocols. Melphalan carries significant myelosuppression risk, so any use should stay within a specialist research or transplant setting. Other predicted indications, such as ovarian primitive germ cell tumour (L3) and female breast carcinoma (L2), have limited or historical evidence. The mucinous adenocarcinoma predictions (rectum, colon, gallbladder, cervix, endometrium), choriocarcinoma of ovary and malignant non-epithelial ovarian tumour are prediction-only (L5) and should be held.

**To proceed, the following is needed:**
- Published results from NCT00936936, including the specific contribution of melphalan and outcomes compared with standard salvage regimens
- Detailed mechanism of action data and the licensed indication text from the MHRA record and SmPC
- A review of the safety profile in this population, including renal function, myelosuppression and secondary malignancy risk
- Confirmation of the formulation and route required (high-dose intravenous melphalan versus the oral 2 mg tablet), since route compatibility has not yet been assessed
- Specialist oncology and NICE guidance review before any clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

