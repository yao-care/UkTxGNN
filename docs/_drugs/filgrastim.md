---
layout: default
title: Filgrastim
parent: Model Prediction Only (L5)
nav_order: 288
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-06
description: "Filgrastim: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Constitutional neutropenia"
monitor_inn: "Filgrastim"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "fetal and neonatal alloimmune thrombocytopenia", "platelet-type bleeding disorder"]
---

# Filgrastim
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

## Filgrastim: From Severe Congenital Neutropenia to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Filgrastim is a granulocyte colony-stimulating factor (G-CSF), originally used for constitutional and severe congenital neutropenia, cyclic haematopoiesis and chronic familial neutropenia.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but this is a model prediction only, with **no clinical trials** and **no publications** supporting this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constitutional neutropenia; severe congenital neutropenia; cyclic haematopoiesis; chronic familial neutropenia |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (26 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 26 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known pharmacology, filgrastim acts through the G-CSF receptor on neutrophil-lineage progenitors, promoting their proliferation, differentiation and release. Its efficacy in neutropenia is well established.

Primary release disorder of platelets is a qualitative platelet function defect, in which platelets fail to secrete their granule contents. This is not expected to respond to stimulation of the granulocyte lineage. No plausible mechanistic link was identified from the data compiled for this report, and the very high TxGNN score is not backed by any trial or publication.

The same applies to the other top-ranked predictions, which are all inherited bleeding or protein-disorder conditions with no apparent connection to G-CSF signalling:

- Pseudo-von Willebrand disease (score 1.0000)
- Glanzmann thrombasthenia (99.996%)
- Scott syndrome (99.956%)
- Haemorrhagic disorder due to constitutional thrombocytopenia (99.911%). This has only a weak, indirect rationale, since G-CSF mobilises haematopoietic progenitors but is not a recognised thrombopoietic agent.

---

## Clinical Trial Evidence

Currently no clinical trials are registered for the top-ranked predicted indication, primary release disorder of platelets.

For the related, lower-ranked prediction **platelet-type bleeding disorder** (score 0.9969), seven trials were linked. All were graded as having low relevance. They are stem cell transplantation studies in haematological malignancies or marrow failure, in which filgrastim is at most a supportive or mobilisation agent. Their listing under this indication is likely an ontology-mapping artefact.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00296023](https://clinicaltrials.gov/study/NCT00296023) | NA | Completed | 25 | Low-dose allogeneic PBSC transplant in high-risk low-grade haematological malignancies |
| [NCT00004232](https://clinicaltrials.gov/study/NCT00004232) | Phase 1 | Completed | Not stated | CD34-enriched PBSC to augment bone marrow in allogeneic transplant |
| [NCT00054236](https://clinicaltrials.gov/study/NCT00054236) | Phase 1 | Completed | 55 | Multiple cord blood unit transplant after non-myeloablative conditioning |
| [NCT00301912](https://clinicaltrials.gov/study/NCT00301912) | Phase 2 | Withdrawn | 0 | Busulfan/fludarabine preparative therapy; no participants enrolled, so no evidence |
| [NCT00295997](https://clinicaltrials.gov/study/NCT00295997) | NA | Unknown | 35 | Non-myeloablative allogeneic SCT from matched unrelated donors |
| [NCT00080925](https://clinicaltrials.gov/study/NCT00080925) | Phase 1 | Completed | 20 | T-cell depleted reduced-intensity haploidentical SCT |
| [NCT00004904](https://clinicaltrials.gov/study/NCT00004904) | Phase 1 | Completed | Not stated | T-cell depleted partially matched related donor HSCT with CD34 "veto" cells |

---

## UK Market Information

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0901060I0AAAPAP | Filgrastim 12million units/0.2ml inj pre-filled syringes | Filgrastim |
| 0901060I0AAALAL | Filgrastim 30million units/0.5ml inj pre-filled syringes | Filgrastim |
| 0901060I0AAAAAA | Filgrastim 30million units/1ml solution for injection vials | Filgrastim |
| 0901060I0AAAMAM | Filgrastim 48million units/0.5ml inj pre-filled syringes | Filgrastim |
| 0901060I0AAANAN | Filgrastim 48million units/0.8ml inj pre-filled syringes | Filgrastim |
| 0901060I0AAABAB | Filgrastim 48million units/1.6ml inj vials | Filgrastim |
| 0901060I0AAAQAQ | Filgrastim 70million units/0.73ml inj pre-filled syringes | Filgrastim |
| 0901060I0BGACAP | Accofil 12million units/0.2ml inj pre-filled syringes | Filgrastim |
| 0901060I0BGAAAL | Accofil 30million units/0.5ml inj pre-filled syringes | Filgrastim |
| 0901060I0BGABAM | Accofil 48million units/0.5ml inj pre-filled syringes | Filgrastim |
| 0901060I0BGADAQ | Accofil 70million units/0.73ml inj pre-filled syringes | Filgrastim |
| 0901060I0BBAAAA | Neupogen 30million units/1ml solution for injection vials | Filgrastim |
| 0901060I0BBABAB | Neupogen 48million units/1.6ml solution for injection vials | Filgrastim |
| 0901060I0BBAEAL | Neupogen Singleject 30million units/0.5ml inj pfs | Filgrastim |
| 0901060I0BBAFAM | Neupogen Singleject 48million units/0.5ml inj pfs | Filgrastim |
| 0901060I0BEAAAP | Nivestim 12million units/0.2ml inj pre-filled syringes | Filgrastim |
| 0901060I0BEABAL | Nivestim 30million units/0.5ml inj pre-filled syringes | Filgrastim |
| 0901060I0BEACAM | Nivestim 48million units/0.5ml inj pre-filled syringes | Filgrastim |
| 0901060I0BCAAAL | Ratiograstim 30million units/0.5ml inj pre-filled syringes | Filgrastim |
| 0901060I0BCABAN | Ratiograstim 48million units/0.8ml inj pre-filled syringes | Filgrastim |

Showing 20 of 26 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

The authorisation number above is as listed in the compiled data and does not follow the usual MHRA "PL" format, so it should be verified against the MHRA register.

---

## Safety Considerations

**Drug Interactions:** The interaction screen returned 100 interacting drugs, all classified as Moderate. Examples shown include:

- Radiopharmaceuticals and radioimmunotherapy: iobenguane (I-131), fludeoxyglucose (18F), ibritumomab tiuxetan, tositumomab, tositumomab (I-131)
- Cytotoxic and antineoplastic agents: paclitaxel, mercaptopurine, trimetrexate, azacitidine, bendamustine, altretamine, arsenic trioxide, asparaginase (*Escherichia coli*), abemaciclib
- Other agents: levamisole, acalabrutinib, aldesleukin, alemtuzumab, avapritinib, belantamab mafodotin

Please refer to the SmPC and BNF for full safety information, including warnings and contraindications. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no relevant trials or publications, and no plausible mechanism links G-CSF to platelet release disorders. The only trials found for a related platelet indication are transplant studies unrelated to this question.

**To proceed, the following is needed:**
- Confirmed mechanism of action data, and a mechanistic case for G-CSF activity in platelet function disorders
- Preclinical or case-level evidence of any effect on platelet function
- Review of the ontology mapping that linked the transplant trials to platelet bleeding disorders
- Full UK SmPC and BNF safety information (warnings and contraindications), and approved indication text for the listed authorisation
- Verification of the marketing authorisation number against the MHRA register
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

