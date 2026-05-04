---
layout: default
title: Amlodipine
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

# Amlodipine: From Hypertension to Brain Stem Infarction

## One-Sentence Summary

Amlodipine is a long-acting dihydropyridine calcium channel blocker, clinically established for hypertension and stable angina pectoris.
The TxGNN model predicts it may be effective for **Brain Stem Infarction** (rank 1, score 99.94%),
however **no registered clinical trials** and **no publications** currently support this specific indication directly.
Notably, a closely related cerebrovascular candidate — intracerebral haemorrhage (rank 10) — carries substantially stronger evidence, including a completed Phase 3 trial (n = 1,671), and may represent a more immediately actionable repurposing opportunity within the same evidence pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; stable angina pectoris (MHRA licensing data not retrieved in this evidence pack — based on established pharmacology) |
| Predicted New Indication | Brain Stem Infarction |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| UK Market Status | Not available in evidence pack (data gap — see UK Market Information section) |
| Number of Marketing Authorisations | Not available in evidence pack (data gap) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved in this evidence pack. Based on established pharmacology, Amlodipine is a long-acting L-type calcium channel blocker (CCB) of the dihydropyridine class. Its antihypertensive efficacy is well proven across decades of clinical use, and mechanistically it may be relevant to brain stem infarction through two theoretically plausible pathways.

Hypertension is the principal modifiable risk factor for small-vessel cerebrovascular disease, including perforating artery disease of the brainstem. By reducing systemic vascular resistance through peripheral vasodilation, Amlodipine could theoretically lower the incidence or severity of hypertensive small-vessel injury leading to brainstem lacunar infarction. Furthermore, L-type calcium channel blockade has been demonstrated in multiple preclinical ischaemia models to attenuate post-ischaemic intracellular calcium overload — a key trigger of calcium-mediated neuronal apoptosis — suggesting a neuroprotective mechanism that extends beyond blood pressure lowering alone.

It should be emphasised, however, that the TxGNN high prediction score for brain stem infarction most likely reflects Amlodipine's broad cerebrovascular protection associations within the knowledge graph (shared with hypertension, stroke, and related vascular phenotypes), rather than any independent clinical signal specific to this diagnosis. No clinical trials or publications directly investigating Amlodipine in brain stem infarction were identified in the evidence search.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for brain stem infarction.

---

## Literature Evidence

Currently no related literature available for brain stem infarction.

---

## UK Market Information

MHRA marketing authorisation data was not retrieved in this evidence pack (0 licences recorded). This appears to represent a data collection gap, as Amlodipine is a well-established antihypertensive agent with multiple authorised products in the United Kingdom. Clinicians should consult:

- The **MHRA Product Licence Register** for current authorised indications and licence holders
- The **British National Formulary (BNF), Chapter 2.6** (Nitrates, calcium-channel blockers, and other antianginal drugs) for prescribing information
- The relevant **Summary of Product Characteristics (SmPC)** for dosing, contraindications, and warnings

Remediation of this data gap is required before a complete regulatory assessment can be performed.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns brain stem infarction its highest prediction score in this evidence pack (99.94%), yet this signal is entirely unsupported by clinical trial data or published literature. The high rank most plausibly reflects indirect knowledge-graph associations with Amlodipine's well-established cerebrovascular risk-reduction properties, rather than a drug–disease relationship specific to brain stem infarction.

**To proceed, the following is needed:**

- **Regulatory data retrieval**: Obtain MHRA marketing authorisation details, SmPC, and approved UK indications for Amlodipine via the MHRA PL register; this is currently a blocking data gap
- **Mechanism of action data**: Query DrugBank API (DB00381) to populate MOA fields and support mechanistic rationale for any indication
- **Safety profile review**: Retrieve contraindications and key warnings from the SmPC, particularly regarding hypotension risk in the acute stroke setting
- **Brainstem-specific preclinical evidence**: Commission a targeted literature search (MEDLINE, EMBASE) for Amlodipine or CCBs in brainstem ischaemia animal models before any clinical feasibility discussion
- **Prioritisation review**: Consider escalating the evaluation of **intracerebral haemorrhage (rank 10, L2, "Proceed with Guardrails")**, which is supported by a completed Phase 3 RCT (TRIDENT, n = 1,671) and an actively recruiting trial (NCT07458880), and may represent the most actionable cerebrovascular repurposing candidate in this evidence pack
- **Blood pressure target safety assessment**: Any neuroprotection study in acute brainstem infarction must account for the haemodynamic risks of CCB-induced hypotension in the acute ischaemic period
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

