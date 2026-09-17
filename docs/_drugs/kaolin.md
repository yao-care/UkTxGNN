---
layout: default
title: Kaolin
parent: Model Prediction Only (L5)
nav_order: 323
evidence_level: L5
indication_count: 10
---

# Kaolin
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

# Kaolin: From No Documented Indication to Thrombotic Disease

## One-Sentence Summary

> Kaolin has no original UK-approved indication or marketing authorisation recorded in this evidence pack, and its known pharmacological role is as a contact-activation procoagulant (Factor XII activator) used as a reagent in kaolin-activated thromboelastography (TEG) and in topical haemostatic dressings.
> The TxGNN model predicts it may be effective for **Thrombotic Disease**, but the underlying evidence — **3 clinical trials** and **20 publications** — consists entirely of studies using kaolin as a diagnostic reagent or haemostatic wound-care material, not as a therapeutic anticoagulant.
> This is very likely a **spurious model prediction**, as the proposed indication is mechanistically opposite to kaolin's known procoagulant action.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack; no UK marketing authorisation on record |
| Predicted New Indication | Thrombotic Disease |
| TxGNN Prediction Score | 94.70% |
| Evidence Level | L5 (model prediction only; no therapeutic studies) |
| UK Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Kaolin is not available in DrugBank (marked as a data gap). However, the evidence pack's own trial and literature review consistently describes kaolin as a **contact-activation pathway procoagulant** — it activates Factor XII (the intrinsic coagulation cascade), which is precisely why it is used as the standard activating reagent in kaolin-activated thromboelastography (TEG) for measuring clotting, and as the active mineral component in haemostatic dressings such as kaolin-coated gauze and QuikClot.

This mechanism is **directionally opposite** to what would be required to treat thrombotic disease, which requires reducing — not promoting — coagulation. The clinical trials and literature retrieved for this indication overwhelmingly involve kaolin-activated TEG as a *monitoring tool* for other anticoagulants (e.g. rivaroxaban, heparin, dabigatran) or for diagnosing hypercoagulable states, rather than any interventional use of kaolin itself to treat thrombosis. The reviewers' own relevance grading (Grade C, "kaolin as reagent, not therapeutic intervention") supports this interpretation.

In short, this prediction appears to reflect a **literature co-occurrence artefact** — kaolin is textually associated with thrombosis-related research because it is the standard laboratory reagent used to study clotting, not because it has any plausible therapeutic role in thrombotic disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02887820](https://clinicaltrials.gov/study/NCT02887820) | N/A | Terminated | 15 | Pilot study of TEG-guided transfusion/coagulation management in ECMO patients; kaolin used solely as the TEG activation reagent, not as a treatment |
| [NCT04246307](https://clinicaltrials.gov/study/NCT04246307) | N/A | Unknown | 50 | Compared ClotPro® vs kaolin-activated TEG® for assessing haemostasis during liver transplantation; a diagnostic comparison study, not a treatment trial |
| [NCT02271126](https://clinicaltrials.gov/study/NCT02271126) | Phase 1 | Completed | 42 | Compared TEG vs aPTT for monitoring heparin anticoagulation during ECMO; kaolin again used only as the TEG assay reagent |

**Note:** None of the identified trials evaluate kaolin as a therapeutic intervention for thrombotic disease. All use kaolin-activated TEG purely as a diagnostic/monitoring assay.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38396728](https://pubmed.ncbi.nlm.nih.gov/38396728/) | 2024 | Cohort | Int J Mol Sci | Compared TEG and conventional coagulation markers in COPD exacerbation vs stable phase; not a kaolin treatment study |
| [32496878](https://pubmed.ncbi.nlm.nih.gov/32496878/) | 2020 | Cohort | Clin Appl Thromb Hemost | Compared TEG with conventional coagulation tests in severe liver disease; kaolin used as TEG reagent |
| [34861681](https://pubmed.ncbi.nlm.nih.gov/34861681/) | 2022 | Cohort | Blood Advances | Investigated Factor XII and contact pathway activation in COVID-19-associated thrombosis; mechanistic background only |
| [9624740](https://pubmed.ncbi.nlm.nih.gov/9624740/) | 1997 | Review | Br J Biomed Sci | Reviews lupus anticoagulant diagnosis, including kaolin clotting time (KCT) as a laboratory test |
| [3931480](https://pubmed.ncbi.nlm.nih.gov/3931480/) | 1985 | pending | Am J Obstet Gynecol | Discusses lupus anticoagulant identification via kaolin clotting time in pregnancy-related thrombosis |
| [39067844](https://pubmed.ncbi.nlm.nih.gov/39067844/) | 2025 | pending | Ann Vasc Surg | Examined HbA1c and coagulation parameters in peripheral artery disease; no kaolin intervention |
| [6788212](https://pubmed.ncbi.nlm.nih.gov/6788212/) | 1981 | pending | BMJ | Described hypercoagulation states in glomerulonephritis using clotting assays |
| [26633836](https://pubmed.ncbi.nlm.nih.gov/26633836/) | 2016 | pending | Thromb Haemost | RCT of dabigatran effects on coagulation in patients on dual antiplatelet therapy; kaolin not the study drug |
| [32342930](https://pubmed.ncbi.nlm.nih.gov/32342930/) | 2020 | pending | Malays J Pathol | Reviewed lupus anticoagulant testing practice, including kaolin-based assays |
| [36813431](https://pubmed.ncbi.nlm.nih.gov/36813431/) | 2023 | pending | Gastroenterol Clin North Am | Review of diarrhoea in COVID-19; only tangentially retrieved, no relevance to thrombosis or kaolin therapy |

**Note:** All retrieved literature relates to kaolin's role as a coagulation-testing reagent (kaolin clotting time / kaolin-activated TEG) or to unrelated thrombosis research where kaolin was not the studied intervention. No publication reports kaolin as a treatment for thrombotic disease.

---

## UK Market Information

Kaolin currently holds **no MHRA marketing authorisations** and is recorded as **Not Marketed** in the UK regulatory dataset (0 licenses). No product-level information (brand name, dosage form, approved indication) is available in this evidence pack.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

*(No key warnings, contraindications, or drug interaction data are available in this evidence pack — all fields returned as data gaps.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted mechanism is directionally contradictory: kaolin is a Factor XII–activating procoagulant, whereas thrombotic disease requires anticoagulant/antithrombotic therapy. All supporting trials and literature use kaolin solely as a diagnostic reagent (kaolin-activated TEG/KCT) or as a topical haemostatic material, not as a systemic therapeutic agent.
- Evidence level is L5 — model prediction only, with zero interventional trials and zero literature supporting therapeutic use in this indication.
- The same "Hold" conclusion applies across all ten TxGNN-predicted indications for kaolin in this evidence pack (thrombotic disease, bronchitis, heparin cofactor 2 deficiency, antithrombin deficiency, factor 5 excess, vein disease, thrombophilia, interventricular septum aneurysm, Jeune syndrome, heart disease) — each is either mechanistically contradictory or lacks any therapeutic evidence, consistent with a knowledge-graph noise pattern rather than a genuine repurposing signal.

**To proceed, the following would be needed (not currently justified given the mechanistic contradiction):**
- Confirmed original indication(s) and DrugBank MOA data for Kaolin (currently data gaps, DG001/DG002)
- Any preclinical or pharmacodynamic data showing an antithrombotic (rather than procoagulant) effect, which would need to override the current mechanistic contradiction
- TFDA/MHRA safety labelling data (warnings, contraindications) before any further evaluation stage

Given the mechanistic contradiction and complete absence of therapeutic evidence, this candidate should not advance beyond Hold without a substantive re-evaluation of the underlying TxGNN signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

