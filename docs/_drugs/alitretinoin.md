---
layout: default
title: Alitretinoin
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Alitretinoin
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

# Alitretinoin: From Chronic Hand Eczema to Acne

## One-Sentence Summary

Alitretinoin (9-cis-retinoic acid) is an oral retinoid with established approval in several jurisdictions (including via the EMA) for severe chronic hand eczema refractory to potent topical corticosteroids.
The TxGNN model predicts it may be effective for **Acne**, supported by **1 registered trial** and **5 publications** — including a direct clinical comparison demonstrating equivalent sebosuppressive activity to isotretinoin (PMID 8884148).
Note: TxGNN's highest-ranked prediction (amenorrhea, 99.99%) has been assessed as a confounded adverse-effect signal with no therapeutic rationale and is classified **Hold**; acne (99.92%) is the most clinically actionable candidate and is the focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe chronic hand eczema (known EMA-approved indication; no MHRA licence on record in this Evidence Pack) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.92% (TxGNN rank 2; selected as primary candidate over rank 1 due to mechanistic support and available evidence) |
| Evidence Level | L3 |
| UK Market Status | Not marketed (0 MHRA authorisations on record) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. From published sources, Alitretinoin is the 9-cis isomer of retinoic acid and is a pan-retinoid receptor agonist, activating both retinoic acid receptors (RAR-α/β/γ) and retinoid X receptors (RXR-α/β/γ). Through these nuclear receptors it suppresses sebaceous gland proliferation, normalises keratinocyte differentiation, and attenuates AP-1-driven inflammation — all recognised as central mechanisms in the pathogenesis of acne vulgaris.

The repurposing rationale is particularly compelling because isotretinoin (13-cis-retinoic acid), a structural analogue, is already the established gold-standard oral therapy for severe acne. Alitretinoin shares this class-effect mechanism and additionally carries stronger RXR-binding activity. Critically, a direct clinical comparison by Ott et al. (1996; PMID 8884148) demonstrated that 9-cis-RA is as active as 13-cis-RA in inhibiting cultured human sebocyte proliferation and reducing hamster sebaceous gland size — the accepted surrogate endpoints for anti-acne activity.

**Note on TxGNN's top-ranked prediction:** Amenorrhea ranked first by TxGNN score (99.99%). However, retinoids cause menstrual irregularities and amenorrhoea as adverse effects, not as therapeutic targets. This prediction is biologically confounded, has no clinical evidence, and has been designated Hold at decision stage S0. Acne — ranked second by TxGNN score but supported by mechanistic evidence and a direct comparative study — is the actionable focus of this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04663906](https://clinicaltrials.gov/study/NCT04663906) | N/A | Unknown | 300 | Observational study investigating whether **isotretinoin** (13-cis-RA, not alitretinoin) increases COVID-19 infection risk via nasal mucosal dryness; does not assess alitretinoin efficacy for acne |

> **Interpretive note:** The single identified trial involves isotretinoin — a related but distinct molecule — and addresses an adverse-event safety question rather than therapeutic efficacy. No registered trials of oral alitretinoin specifically for acne were identified in ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [8884148](https://pubmed.ncbi.nlm.nih.gov/8884148/) | 1996 | Clinical Comparative Study | *Dermatology* | Direct head-to-head: 9-cis-RA (alitretinoin) equally active to 13-cis-RA (isotretinoin) in inhibiting human sebocyte proliferation and reducing sebaceous gland size — strongest direct evidence for the repurposing hypothesis |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Review | *Clinics in Dermatology* | Comprehensive review of vitamin A and retinoids in dermatology; confirms alitretinoin among oral retinoids used as therapeutic agents, with RAR/RXR pan-agonist profile described |
| [11586072](https://pubmed.ncbi.nlm.nih.gov/11586072/) | 2001 | Expert Review | *Skin Pharmacology and Applied Skin Physiology* | Retinoids' pleiotropic dermatological effects via RAR/RXR nuclear receptors; supports mechanistic basis for sebaceous gland targeting and keratinocyte normalisation |
| [8884149](https://pubmed.ncbi.nlm.nih.gov/8884149/) | 1996 | Clinical Study | *Dermatology* | Oral all-trans-retinoic acid reduces sebum excretion rate in young male subjects; supports class-effect sebosuppression shared by systemic retinoids |
| [10521699](https://pubmed.ncbi.nlm.nih.gov/10521699/) | 1999 | Mechanistic Review | *Biochimica et Biophysica Acta* | Retinoid receptor binding and metabolism; provides the mechanistic framework for retinoid activity in epithelial differentiation and sebaceous tissue regulation |

---

## UK Market Information

No MHRA marketing authorisations for Alitretinoin are recorded in this Evidence Pack (market status: not marketed in the UK at time of data snapshot). For reference, Alitretinoin 10 mg and 30 mg capsules (Toctino®, Stiefel/GSK) received European Medicines Agency (EMA) approval in 2008 for severe chronic hand eczema refractory to potent topical corticosteroids; prescribers should verify current MHRA authorisation status, NICE guidance, and BNF listing independently, as the UK regulatory position following the end of the EMA mutual recognition period may differ from this snapshot.

---

## Cytotoxicity

Alitretinoin (DB00523) is classified as an antineoplastic agent in DrugBank, owing to its approval as a topical gel (Panretin®) for AIDS-related Kaposi's sarcoma cutaneous lesions. The following applies to systemic/oral use; cytotoxic precautions are not required at dermatological doses.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted retinoid (RAR/RXR pan-agonist); not a conventional cytotoxic agent. Antineoplastic classification derives from Kaposi's sarcoma topical use |
| Myelosuppression Risk | Low — oral retinoids at dermatological doses are not myelosuppressive |
| Emetogenicity Classification | Low to minimal at dermatological dosing levels |
| Monitoring Items | FBC, LFTs, fasting lipid profile (triglycerides and total cholesterol), renal function, and mandatory pregnancy tests for females of childbearing potential |
| Handling Protection | Standard pharmaceutical handling is sufficient at dermatological doses; pregnant or potentially pregnant staff should avoid direct handling given the teratogenic class-effect |

---

## Safety Considerations

No specific safety data (SmPC warnings, contraindications, or drug interaction records) is available in this Evidence Pack.

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

> **Critical known safety concern (from published literature):** Alitretinoin is a potent teratogen. All oral retinoid prescribing in the UK requires compliance with the mandatory Retinoid Pregnancy Prevention Programme (PPP), including effective contraception, monthly pregnancy testing, and a 30-day contraception-confirmed dispensing limit. This requirement is non-negotiable for any repurposing trial or off-label use in females of childbearing potential and must be addressed before any clinical development proceeds.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alitretinoin shares the proven sebosuppressive mechanism of isotretinoin, and a direct clinical comparison study demonstrates equivalent activity against sebocyte proliferation — the key surrogate for anti-acne efficacy. However, no completed RCT of oral alitretinoin specifically for acne has been identified, and critical safety data (including the mandatory Pregnancy Prevention Programme requirements) must be formally documented before any clinical application proceeds.

**To proceed, the following is needed:**

- Confirm current MHRA authorisation and BNF listing for Alitretinoin (Toctino) — UK regulatory position following EMA transition requires independent verification
- Retrieve full SmPC to document contraindications, teratogenicity programme requirements, and drug interactions (Data Gap DG001 — currently Blocking)
- Obtain DrugBank MOA data (Data Gap DG002) to formally document RAR/RXR receptor-binding profile for inclusion in any regulatory submission
- Design a Phase 2 RCT comparing oral alitretinoin vs isotretinoin for moderate-to-severe acne to establish non-inferiority or superiority with UK patient data
- Assess NICE Technology Appraisal coverage of oral retinoids for acne (e.g., TA 77) and determine whether existing appraisals cover off-label alitretinoin use
- Develop a Pregnancy Prevention Programme compliance plan aligned with MHRA guidance for any trial or off-label prescribing programme

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All prescribing decisions should reference the current SmPC, BNF, and applicable NICE guidance.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

