---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
---

# Etoposide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Etoposide: From Small Cell Lung Cancer to Well-Differentiated Fetal Adenocarcinoma of the Lung

## One-Sentence Summary

Etoposide is a topoisomerase II inhibitor established as chemotherapy for small cell lung cancer, germ cell tumours and lymphomas. The TxGNN model predicts it may also be effective for **well-differentiated fetal adenocarcinoma of the lung** (the low-grade epithelial component of pulmonary blastoma), but this is currently supported by **0 clinical trials** and only **1 case-report publication**, so the evidence base is very thin.

*(Note: this evidence pack — candidate ID `TW-DB00773-multi` — contains 10 TxGNN-predicted indications for Etoposide. This report follows the standard format for the top-ranked prediction; a summary of the other 9 candidates is provided in a supplementary table before the conclusion.)*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Small cell lung cancer, germ cell tumours and lymphomas (per literature evidence, PMID 1984834; no UK marketing authorisation record available in this pack) |
| Predicted New Indication | Well-differentiated fetal adenocarcinoma of the lung |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| UK Market Status | Not marketed (per data available in this evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for Etoposide was flagged as a data gap in this evidence pack. Based on information available across the supporting literature and trial records, Etoposide is a **topoisomerase II inhibitor** (epipodophyllotoxin class): it stabilises the DNA–topoisomerase II cleavage complex, producing double-strand DNA breaks and triggering apoptosis in rapidly dividing cells. This mechanism underlies its long-standing use in small cell lung cancer, germ cell tumours and a wide range of lymphomas and sarcomas, as reflected throughout the trial and publication evidence in this pack (e.g. PMID 1984834, PMID 8070034).

Well-differentiated fetal adenocarcinoma of the lung is the low-grade, low-mitotic-index epithelial component of **classic biphasic pulmonary blastoma** — a very rare primary lung malignancy that also contains a primitive mesenchymal (sarcomatous) component. Because it is a lung tumour sharing anatomical origin with small cell lung cancer, and because pulmonary blastoma as a whole is a highly proliferative, mixed-histology tumour, there is a plausible mechanistic rationale for cytotoxic, DNA-damaging agents such as Etoposide to have activity here.

However, the supporting evidence is indirect: the single literature record identified (PMID 33107372) describes a case of *classic biphasic* pulmonary blastoma (the combined epithelial/mesenchymal tumour) treated with nedaplatin plus paclitaxel — not Etoposide specifically, and not the isolated well-differentiated fetal adenocarcinoma subtype. No trial or publication in this pack directly evaluates Etoposide in this specific histological subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Case Report | The Journal of International Medical Research | Case of classic biphasic pulmonary blastoma (which includes well-differentiated fetal adenocarcinoma as its epithelial component) treated with adjuvant chemotherapy after surgical resection; illustrates the chemosensitivity of this tumour family but does not test Etoposide directly. |

---

## Cytotoxicity

Etoposide is a conventional cytotoxic chemotherapy agent (topoisomerase II inhibitor, epipodophyllotoxin class), as evidenced throughout the trial and literature records in this pack (e.g. its role as the "E" in EPOCH, ICE, VDC/IE and BEACOPP regimens).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase II inhibitor / epipodophyllotoxin class) |
| Myelosuppression Risk | High — multiple Etoposide-containing regimens in this evidence pack required G-CSF/filgrastim prophylaxis and thrombopoietin-agonist supportive care for febrile neutropenia and thrombocytopenia (e.g. PMID 34962714; NCT01459653) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Full blood count with differential (given the neutropenia/thrombocytopenia signal in the supporting evidence), plus renal and hepatic function as standard for cytotoxic chemotherapy |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Other Predicted Indications in This Evidence Pack

This evidence pack scored Etoposide against 10 candidate indications. The table below summarises the other 9 for context, since several have materially stronger evidence than the top-ranked prediction above.

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|------|------|------|------|
| 2 | Primary pulmonary lymphoma | 99.94% | L2 | S2 | Proceed with Guardrails |
| 3 | Pulmonary blastoma | 99.94% | L4 | S1 | Research Question |
| 4 | Ewing sarcoma | 99.85% | L1 | S3 | Proceed with Guardrails |
| 5 | Botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.80% | L4 | S0 | Hold |
| 6 | Rhabdomyosarcoma (disease) | 99.79% | L1 | S3 | Proceed with Guardrails |
| 7 | Embryonal extrahepatic bile duct rhabdomyosarcoma | 99.76% | L5 | S0 | Hold |
| 8 | Parameningeal embryonal rhabdomyosarcoma | 99.76% | L4 | S1 | Research Question |
| 9 | Extrahepatic bile duct rhabdomyosarcoma | 99.75% | L5 | S0 | Hold |
| 10 | Prostate embryonal rhabdomyosarcoma | 99.74% | L4 | S1 | Research Question |

Note: for rank 4 (Ewing sarcoma) and rank 6 (rhabdomyosarcoma), the evidence pack's own rationale indicates these reflect **confirmation of existing standard-of-care use** (Etoposide/Ifosfamide within VDC/IE and related regimens) rather than novel repurposing — the L1 evidence level and multiple Phase 3 RCTs (e.g. PMID 12594313, PMID 36522207, PMID 11846301) support long-established practice rather than a new indication.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
- The top-ranked TxGNN prediction (well-differentiated fetal adenocarcinoma of the lung) has a very high model score but only L4 evidence — a single indirect case report, with no trials and no subtype-specific data — so it does not yet support a repurposing decision.
- Two other candidates in this pack (Ewing sarcoma, rhabdomyosarcoma) have L1 evidence, but represent extension/confirmation of Etoposide's established chemotherapy role rather than new repurposing opportunities.

**To proceed, the following is needed:**
- UK product labelling/SmPC data (currently blocking — DG001: no warnings, contraindications or DDI data available for safety screening)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- A prospective case series or trial specifically evaluating Etoposide-containing regimens in pulmonary blastoma/well-differentiated fetal adenocarcinoma
- Confirmation of current UK marketing authorisation status, since this pack records 0 licences on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

