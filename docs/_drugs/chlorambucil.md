---
layout: default
title: Chlorambucil
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 8
---

# Chlorambucil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Chlorambucil: From Chronic Lymphocytic Leukaemia to IgHV-Mutated CLL/SLL

---

## One-Sentence Summary

Chlorambucil is a nitrogen mustard alkylating agent with a long-established historical role in treating chronic lymphocytic leukaemia (CLL) and other lymphoid malignancies.
The TxGNN model predicts it may be effective for **CLL/Small Lymphocytic Lymphoma with Immunoglobulin Heavy Chain Variable-Region Gene (IgHV) Somatic Hypermutation** — a molecularly defined, typically indolent subtype of CLL with a distinct biological profile.
There are currently **no clinical trials** and **no publications** directly addressing this specific molecular subtype, placing this prediction at evidence level **L5**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Lymphocytic Leukaemia and lymphoid malignancies (no current UK MHRA authorisation on record) |
| Predicted New Indication | CLL/SLL with IgHV Somatic Hypermutation |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on widely published pharmacological knowledge, Chlorambucil is a bifunctional alkylating agent of the nitrogen mustard class. It acts by covalently cross-linking DNA strands at guanine residues, disrupting DNA replication and transcription and triggering apoptosis in dividing cells — including the malignant B-lymphocytes that accumulate in CLL. This mechanism of action is not disease-stage specific and is broadly applicable across lymphoid malignancies characterised by clonal B-cell proliferation.

IgHV-mutated CLL/SLL is biologically distinct from its unmutated counterpart: the presence of somatic hypermutation in the immunoglobulin heavy chain variable-region gene indicates the malignant clone has undergone germinal centre maturation. This subtype is associated with a more indolent clinical course, longer time to first treatment, and historically superior responses to chemoimmunotherapy including alkylating agent-based regimens. The landmark Phase 3 RESONATE-2 trial enrolled predominantly elderly, treatment-naïve CLL patients without del(17p) — a population substantially enriched for IgHV-mutated disease — and used Chlorambucil as the active comparator arm, demonstrating measurable haematological efficacy in this group.

The TxGNN prediction is therefore biologically plausible: Chlorambucil's mechanism of inducing cytotoxic DNA damage is consistent with the biology of slowly cycling malignant B-lymphocytes characteristic of IgHV-mutated CLL. However, no dedicated evidence for this molecularly defined subtype exists in the current data, and modern treatment guidelines increasingly favour BTK inhibitors (ibrutinib, acalabrutinib) and BCL-2 inhibitors (venetoclax) even for IgHV-mutated patients, reflecting the shift away from conventional alkylating chemotherapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for CLL/SLL with IgHV somatic hypermutation specifically.

---

## Literature Evidence

Currently no related literature available for CLL/SLL with IgHV somatic hypermutation specifically.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrogen mustard alkylating agent |
| Myelosuppression Risk | High — Bone marrow suppression is the primary dose-limiting toxicity. Neutropenia, thrombocytopenia, and anaemia are well documented at therapeutic doses; cumulative myelosuppression may occur with prolonged use |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count (FBC) with differential before and at regular intervals during treatment; liver function tests; renal function; monitoring for signs of infection |
| Handling Protection | Must follow cytotoxic drug handling regulations. Although Chlorambucil is administered orally, preparation, dispensing, and disposal must comply with local cytotoxic safety policies |

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Note that Chlorambucil does not currently hold an MHRA marketing authorisation in the United Kingdom; any clinical use would require access via a Specials Manufacturing Licence or Named Patient Programme. Report any suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Chlorambucil has clear biological plausibility for CLL treatment broadly, but there is no direct clinical evidence for the specific predicted indication (IgHV-mutated CLL/SLL) in this Evidence Pack, and the drug currently holds no MHRA marketing authorisation in the United Kingdom, creating both evidential and regulatory barriers to progression.

**To proceed, the following is needed:**

- **MOA data**: Retrieve confirmed mechanism of action data from DrugBank (DB00291) to formally document the alkylating agent classification and support mechanistic reasoning
- **Regulatory history**: Clarify whether Leukeran® (chlorambucil) previously held a UK marketing authorisation, its current MHRA status, and the applicable regulatory pathway for any new indication (including whether re-authorisation or a variation would be required)
- **IgHV-stratified evidence**: Obtain subgroup analyses from existing large CLL trials stratified by IgHV mutation status (e.g., RESONATE-2, CLL11/GAO trial) to quantify comparative efficacy of Chlorambucil specifically in this molecular subtype
- **Safety profile**: Retrieve contraindications, warnings, and clinically significant drug interactions from historical SmPC documentation or published systematic reviews to fill current data gaps
- **Guideline review**: Assess current NICE (NG144), ESMO, and iwCLL clinical guidelines to determine whether Chlorambucil retains a defined role in IgHV-mutated CLL alongside or in preference to BTK inhibitors and venetoclax-based regimens
- **Patient population definition**: Clarify the target patient population (e.g., elderly patients unfit for intensive regimens, resource-limited settings) where Chlorambucil may retain relevance given its low cost and oral availability

---

> ⚠️ *This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All clinical decisions should be made by qualified healthcare professionals with reference to current NICE guidance, BNF, and SmPC documentation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

