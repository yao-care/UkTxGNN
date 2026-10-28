---
layout: default
title: Alprostadil
parent: Model Prediction Only (L5)
nav_order: 42
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Alprostadil: predicted new indication Aortic malformation (evidence level L4). Approved use: Erectile dysfunction"
monitor_inn: "Alprostadil"
predicted_indications: ["aortic malformation", "congenital tricuspid stenosis", "congenital valvular dysplasia", "tricuspid valve agenesis", "straddling or overriding tricuspid valve", "tricuspid valve prolapse (disease)", "anomaly of the tricuspid subvalvular apparatus", "double outlet right ventricle with atrioventricular septal defect, pulmonary stenosis, heterotaxy", "heart septal defect", "endemic goiter"]
---

# Alprostadil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Alprostadil: From Erectile Dysfunction and Ductal-Dependent Congenital Heart Disease to Aortic Malformation
{: .text-alpha }

## One-Sentence Summary

Alprostadil (prostaglandin E1) was originally used for erectile dysfunction and to keep the ductus arteriosus open in neonates with certain congenital heart defects.
The TxGNN model predicts it may be effective for **aortic malformation**, but this is largely a broader category of an existing indication (aortic coarctation), and the evidence is limited to **0 registered clinical trials** and **8 publications**, mostly case reports and perioperative studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erectile dysfunction; congenital heart defects such as tricuspid atresia, aortic coarctation and tetralogy of Fallot (the UK authorisation record has no indication text) |
| Predicted New Indication | Aortic malformation |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold (treat as a research question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known pharmacology, alprostadil is a prostaglandin E1 analogue that relaxes the smooth muscle of the ductus arteriosus. Infusion keeps the ductus open in newborns whose circulation depends on it, which maintains pulmonary or systemic blood flow until surgery.

Aortic coarctation and interrupted aortic arch are already among alprostadil's original indications, so "aortic malformation" is largely a broader label for something already covered. The high TxGNN score is consistent with this overlap, and this is **not a truly novel repurposing signal**.

Separate perioperative and animal data suggest alprostadil may also have anti-inflammatory and cytoprotective effects. These include a reduced inflammatory response and lung injury after cardiopulmonary bypass in children with congenital heart disease, and attenuated ischaemia-reperfusion injury in rat skeletal muscle. None of these findings is specific to aortic malformation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | Clinical evaluation/Review | Pharmacotherapy | Alprostadil infusion dilates the ductus, increases pulmonary blood flow and supports infants with congenital heart lesions that depend on a patent ductus |
| [19080093](https://pubmed.ncbi.nlm.nih.gov/19080093/) | 2008 | Clinical study (perioperative) | Zhonghua Yi Xue Za Zhi | Effects of alprostadil and ulinastatin on inflammatory response and lung injury after cardiopulmonary bypass in children with congenital heart disease |
| [15362549](https://pubmed.ncbi.nlm.nih.gov/15362549/) | 2004 | Review | Kyobu Geka | Transposition of the great arteries: the ductus is kept patent with alprostadil alfadex to prevent deterioration of left ventricular performance before arterial switch |
| [19068708](https://pubmed.ncbi.nlm.nih.gov/19068708/) | 2008 | Case report | Kyobu Geka | Neonate with interrupted aortic arch type B managed with alprostadil to keep the ductus open, then single-stage repair and continuous haemodiafiltration; survived |
| [30184041](https://pubmed.ncbi.nlm.nih.gov/30184041/) | 2018 | Case report | Braz J Cardiovasc Surg | Complex aortopulmonary window in a 9-year-old; milrinone and alprostadil used before surgery to counteract high lung pressure |
| [41167776](https://pubmed.ncbi.nlm.nih.gov/41167776/) | 2025 | Cohort | Zhonghua Fu Chan Ke Za Zhi | Retrospective review of delivery mode and timing in 123 fetuses with complex congenital heart disease |
| [42469655](https://pubmed.ncbi.nlm.nih.gov/42469655/) | 2026 | Cohort | BMC Pregnancy Childbirth | Retrospective study of pregnancy and perinatal management of complex fetal congenital heart disease |
| [20029353](https://pubmed.ncbi.nlm.nih.gov/20029353/) | 2009 | Preclinical animal study | Minerva Chir | Alprostadil tested for attenuating ischaemia-reperfusion injury in rat skeletal muscle |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0704050B0AABABA (BNF-style code) | Alprostadil urethral stick 500 micrograms | Urethral stick (dosage form not recorded) | Not recorded in the data compiled for this report |

Only one authorisation record was found. It is a BNF classification code rather than a standard MHRA PL number, and the manufacturer and indication text are not recorded.

---

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from drug-disease links in the TxGNN knowledge graph, not from label text, so check them against the SmPC):
- **Respiratory:** newborn respiratory distress syndrome, acute respiratory distress syndrome, lung disease
- **Haematological:** sickle cell anaemia and related haemoglobinopathies, blood coagulation disease, polycythaemia, thrombocytosis, plasma cell myeloma, leukaemias (lymphoid, acute lymphoblastic and myeloid)
- **Cardiovascular:** hypotensive disorder
- **Genitourinary (relevant to urethral use):** priapism, urethral stricture, Peyronie disease and penile fibromatosis, balanitis, balanoposthitis, balanitis xerotica obliterans, urethritis
- **Gastrointestinal:** pyloric stenosis

**Safety signals in the literature:**
- Prolonged prostaglandin E1 infusion in neonates has been linked to gastric outlet obstruction (antral foveolar hyperplasia and hypertrophic pyloric stenosis).
- Iatrogenic pseudo-Bartter syndrome has been reported during prostaglandin infusion.

**Drug interactions:** The interaction search returned 59 records. Six are rated Moderate: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, lorcaserin and sapropterin. Many others have no assigned severity, including morphine, metformin, simvastatin, prednisolone, atropine, vancomycin, amphotericin B, potassium chloride and the proton pump inhibitors omeprazole, lansoprazole and pantoprazole.

For label warnings and contraindications, refer to the SmPC and BNF. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold (research question only)**

**Rationale:**
The predicted "aortic malformation" overlaps heavily with alprostadil's established use in ductal-dependent lesions, so it is not a genuinely new indication. There are no registered trials, and the supporting literature consists of case reports, perioperative studies and one preclinical study. The other nine predictions (congenital tricuspid and valvular disorders, heart septal defect, endemic goitre) rest on model scores alone or on weak evidence. Endemic goitre in particular has no plausible mechanism and is likely a TxGNN model (deep learning) artefact.

**To proceed, the following is needed:**
- Mechanism of action data, to support the mechanistic-link analysis
- SmPC and BNF warnings and contraindications for the UK-licensed product, which are required before safety screening
- A clear UK authorisation record, including the PL number, dosage form and approved indication (the current urethral stick record is unlikely to cover neonatal ductal-dependent use)
- A defined, narrower target population within ductal-dependent lesions, with prospective or well-designed observational data
- A safety monitoring plan for prolonged neonatal infusion (gastric outlet obstruction, apnoea, electrolyte disturbance)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

