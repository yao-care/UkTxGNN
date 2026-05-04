---
layout: default
title: Carteolol
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 1
---

# Carteolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Carteolol: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Carteolol is a non-selective β1/β2-adrenergic receptor antagonist (β-blocker), established in ophthalmology for reducing intraocular pressure (IOP) in open-angle glaucoma and ocular hypertension, and used systemically for hypertension and cardiac arrhythmias.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
however there are currently **no registered clinical trials** and **no supporting publications** for this specific indication — the prediction rests on pharmacological plausibility and mechanistic inference alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / ocular hypertension (established pharmacological use; no UK marketing authorisation on record) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (mechanistic reasoning; no clinical studies identified) |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Carteolol is a non-selective β1/β2-adrenergic receptor antagonist. Its ocular mechanism is well understood: by blocking β2 receptors in the ciliary body, it suppresses aqueous humour production, thereby lowering intraocular pressure (IOP). This mechanism is a cornerstone of medical management for open-angle glaucoma and ocular hypertension, and is shared by other β-blockers such as timolol and betaxolol.

The TxGNN model's prediction is therefore mechanistically plausible in a narrow sense: primary hereditary glaucoma (also referred to as primary congenital or juvenile open-angle glaucoma) is characterised by chronically elevated IOP, and IOP reduction remains the principal therapeutic target regardless of aetiology. In that respect, carteolol's pharmacological effect — reducing aqueous humour production — is directly relevant to the elevated-IOP component of the disease, and forms the basis of this prediction.

However, the mechanistic link is indirect and symptomatic rather than disease-modifying. Primary hereditary glaucoma is fundamentally a structural and genetic disorder: the underlying pathology is trabeculodysgenesis (maldevelopment of the trabecular meshwork and anterior chamber angle), driven by mutations in genes such as *MYOC*, *CYP1B1*, and *LTBP2*. IOP elevation is a secondary consequence of impaired aqueous outflow through a structurally abnormal drainage system. Carteolol reduces IOP by suppressing aqueous production, but cannot correct the structural defect or modify the disease at the genetic level. The mechanistic connection should therefore be characterised as **adjunctive / symptomatic** rather than curative or disease-modifying.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Carteolol in primary hereditary glaucoma.

---

## Literature Evidence

Currently no related literature available for Carteolol in primary hereditary glaucoma.

---

## UK Market Information

Carteolol currently holds **no MHRA marketing authorisation** in the United Kingdom. No licensed products are on record with the UK medicines register. This means there is no approved Summary of Product Characteristics (SmPC) for a UK-licensed carteolol product, and no BNF listing under a current UK authorisation.

> **Note for clinicians:** Carteolol ophthalmic preparations are licensed and used in other jurisdictions (including Japan and France). Any use in the UK would require assessment under unlicensed/off-label frameworks, including compliance with NHS England guidance on the prescribing of unlicensed medicines.

---

## Safety Considerations

Please refer to the SmPC (from a reference jurisdiction, e.g., the European Public Assessment Report or equivalent) and the BNF for safety information. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

> As a β-blocker, carteolol carries class-level considerations relevant to ophthalmic use, including potential systemic absorption and effects in patients with asthma, chronic obstructive pulmonary disease, bradycardia, heart block, or uncontrolled heart failure. Clinicians should consult the relevant SmPC before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Carteolol's mechanism of lowering IOP is pharmacologically relevant to primary hereditary glaucoma, but the evidence base is entirely absent — no clinical trials or publications have been identified for this specific indication. Furthermore, carteolol has no UK marketing authorisation, limiting any near-term clinical pathway. The connection is mechanistically adjunctive (symptom control) rather than disease-modifying, which further tempers the strength of this repurposing signal.

**To proceed, the following is needed:**

- **Mechanism of action data (DrugBank full record):** Retrieve the complete DrugBank MOA entry for DB00521 to confirm receptor binding profile, pharmacokinetics, and known ocular penetration.
- **Comparative effectiveness data:** A targeted literature search to assess whether any ophthalmic β-blocker (class evidence) has been studied specifically in primary hereditary glaucoma or congenital glaucoma — this would establish whether the class effect is transferable.
- **UK regulatory pathway assessment:** Since no UK MA exists, clarify whether the clinical context would require a Specials licence, a clinical trial authorisation (CTA), or a named-patient basis — and whether a marketing authorisation application (MAA) via the MHRA would be warranted.
- **Safety profile review:** Obtain the TFDA/EMA SmPC or equivalent to populate key warnings and contraindications; this is currently a blocking data gap (DG001).
- **Genetic subtype stratification:** Determine whether IOP-lowering therapy (β-blocker class) offers meaningful benefit in *CYP1B1*- or *MYOC*-mutation carriers specifically, as paediatric congenital glaucoma is primarily surgical — understanding the patient population is critical before committing to any trial design.

---

*This report is generated for research reference purposes only and does not constitute medical advice. Any repurposing candidate requires clinical validation before therapeutic application. All content is subject to the YMYL disclaimer applicable to drug repurposing research.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

