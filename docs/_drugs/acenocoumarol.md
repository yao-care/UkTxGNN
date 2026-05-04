---
layout: default
title: Acenocoumarol
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 3
---

# Acenocoumarol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Acenocoumarol: From Anticoagulation to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Acenocoumarol is a coumarin-class vitamin K antagonist (VKA) anticoagulant, pharmacologically analogous to warfarin, used for the prevention and treatment of thromboembolic disorders; it does not currently hold an MHRA marketing authorisation in the United Kingdom.
The TxGNN model predicts it may have therapeutic relevance in **Heparin Cofactor 2 Deficiency**, a rare inherited thrombophilia characterised by impaired thrombin neutralisation.
However, there are currently **no registered clinical trials** and **no supporting publications** for this specific pairing, meaning the evidence base rests entirely on computational prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No MHRA marketing authorisation on record; drug class is oral anticoagulant (VKA) |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, acenocoumarol is a member of the 4-hydroxycoumarin (VKA) anticoagulant class, its efficacy in thromboembolic prophylaxis and treatment has been well-established clinically, and mechanistically it may be applicable to conditions characterised by excessive or poorly regulated thrombin generation—including hereditary thrombophilias such as heparin cofactor 2 deficiency.

Heparin Cofactor 2 (HC2, encoded by *SERPIND1*) is a serine protease inhibitor that irreversibly inactivates thrombin, functioning as a secondary anticoagulant checkpoint independent of antithrombin. In HC2 deficiency, impaired thrombin neutralisation may theoretically shift the haemostatic balance towards a prothrombotic state. Acenocoumarol addresses this imbalance indirectly: by inhibiting the hepatic synthesis of vitamin K-dependent coagulation factors (II, VII, IX, and X), it reduces the upstream generation of thrombin (Factor IIa) itself, thereby partially compensating for the downstream loss of HC2-mediated thrombin clearance.

There are, however, two important limitations that constrain the strength of this prediction. First, VKA therapy cannot replace HC2 protein function—it is a compensatory upstream intervention rather than a disease-targeted therapy; notably, direct oral anticoagulants (DOACs) targeting Factor Xa or thrombin directly may offer more mechanistically precise alternatives. Second, and critically, the clinical significance of isolated HC2 deficiency as an independent risk factor for venous thromboembolism (VTE) remains contested in the literature: several large prospective cohort studies have failed to demonstrate a strong, independent association with thrombosis, raising questions about whether pharmacological anticoagulation in asymptomatic HC2-deficient individuals would confer a meaningful net clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## UK Market Information

Acenocoumarol holds no current MHRA marketing authorisation in the United Kingdom. In UK clinical practice, **warfarin** is the predominant VKA listed in the British National Formulary (BNF, Section 2.8.2 — Oral anticoagulants). Acenocoumarol (brand name Sinthrome) is licensed in a number of European countries (e.g. the Netherlands, Belgium, Switzerland) and other international markets but is not routinely available through NHS supply chains.

> No MHRA marketing authorisations are on record for acenocoumarol. Should an import licence or named-patient supply be considered, this would require separate MHRA authorisation under the Human Medicines Regulations 2012.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for acenocoumarol in heparin cofactor 2 deficiency is confined to a single TxGNN computational prediction (Evidence Level L5), with no registered clinical trials or published literature to support clinical translation. The mechanistic link, whilst biologically coherent, is indirect and substantially weakened by the unresolved question of whether HC2 deficiency constitutes a clinically meaningful independent thrombophilia.

**To proceed, the following is needed:**

- **Clinical significance review**: Commission or identify a systematic review or meta-analysis evaluating HC2 deficiency as an independent VTE risk factor, to determine whether anticoagulant therapy would confer net clinical benefit in this population
- **Mechanism of action data**: Retrieve full MOA documentation for acenocoumarol from DrugBank and the current SmPC, including pharmacokinetic parameters (notably the short half-life of 8–11 hours versus warfarin's 36–42 hours, which affects INR stability and monitoring burden)
- **Safety profile**: Obtain MHRA SmPC data on contraindications, key warnings, drug–drug interactions, and teratogenicity; the absence of this information currently constitutes a blocking data gap (DG001)
- **Comparator assessment**: Evaluate whether DOACs (e.g. apixaban or rivaroxaban, which directly inhibit Factor Xa) would represent a more mechanistically targeted and practically preferable anticoagulant option in HC2-deficient patients compared with VKA
- **Regulatory pathway**: Determine whether any named-patient, compassionate use, or unlicensed import route would be required given acenocoumarol's absence from the UK market, and assess feasibility before any clinical investigation is initiated

> **Note on additional TxGNN predictions:** Two further indications were ranked by TxGNN—*Factor 5 Excess with Spontaneous Thrombosis* (rank 2, 99.78%, L5, Hold) and *Antithrombin Deficiency Type 2* (rank 3, 99.77%, L4, Research Question). Of these, antithrombin deficiency type 2 carries the strongest mechanistic rationale, with class-level evidence supporting VKA use in AT3-deficient patients (warfarin is referenced in ACCP guidelines); this indication may merit a dedicated evidence review as a higher-priority repurposing candidate.

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This document should be reviewed in conjunction with current MHRA guidance, the BNF, and applicable NICE technology appraisals.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

