---
layout: default
title: Betaxolol
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 1
---

# Betaxolol
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

# Betaxolol: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Betaxolol is a selective β₁-adrenoceptor antagonist, approved in multiple jurisdictions (as Betoptic®) for adult open-angle glaucoma and ocular hypertension, though it currently holds no UK marketing authorisation.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
with a prediction confidence score of **99.74%**; however, this is a mechanistic subtype extension rather than a wholly novel indication, and at present **no dedicated clinical trials or publications** specifically supporting this subtype exist.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / ocular hypertension (approved in other jurisdictions; no UK marketing authorisation held) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Betaxolol is a cardioselective (β₁-preferring) adrenoceptor antagonist. When applied topically to the eye, it acts on β₁ receptors in the ciliary body epithelium to suppress cAMP synthesis, thereby reducing active aqueous humour secretion and lowering intraocular pressure (IOP) by approximately 20–35%. This IOP-lowering mechanism is the pharmacological basis for its established use in adult open-angle glaucoma, and it is the same pathophysiological node — elevated IOP — that is central to all forms of glaucoma, including hereditary subtypes.

Primary hereditary glaucoma (PHG) is a group of genetically determined conditions (most commonly caused by mutations in *CYP1B1* or *MYOC*) in which structural maldevelopment of the trabecular meshwork and Schlemm's canal impairs aqueous outflow. Although the root cause is developmental, the resulting IOP elevation drives progressive optic nerve damage by the same mechanism as in sporadic open-angle glaucoma. Betaxolol's ability to reduce aqueous production upstream of the outflow defect therefore provides a rational pharmacological intervention, particularly as a bridging or adjunctive measure before, or in cases not amenable to, surgical correction (trabeculotomy / goniotomy).

Compared with non-selective β-blockers such as timolol, betaxolol's β₁ selectivity reduces interference with β₂-mediated bronchodilation — a clinically meaningful advantage in the paediatric population in whom PHG most frequently presents. It is important to note that the TxGNN model is predicting a *subtype extension* of an indication for which betaxolol already has regulatory approval elsewhere (adult open-angle glaucoma), rather than a genuinely novel therapeutic area; this substantially strengthens the biological plausibility of the prediction. Formal mechanism-of-action data from DrugBank was not available in the source Evidence Pack; the mechanistic reasoning above is drawn from the repurposing rationale provided and established pharmacological literature.

---

## Clinical Trial Evidence

Currently no clinical trials specifically investigating betaxolol in primary hereditary glaucoma are registered on ClinicalTrials.gov or the WHO ICTRP.

---

## Literature Evidence

Currently no published literature specifically addressing betaxolol in primary hereditary glaucoma is available in PubMed.

---

## UK Market Information

Betaxolol currently holds **no marketing authorisation in the United Kingdom**. No MHRA-approved products are on the UK market. Prescribers wishing to use betaxolol would need to consider an unlicensed/off-label supply route (e.g., Specials, named-patient import), subject to appropriate governance.

> **Note for clinicians**: Betaxolol ophthalmic solution (Betoptic®) is authorised in a number of other jurisdictions (including the EU, United States, and Taiwan) for open-angle glaucoma and ocular hypertension in adults. The BNF does not currently list betaxolol as a marketed UK preparation. Clinicians should verify current availability via the MHRA products database before initiating any prescribing pathway.

---

## Safety Considerations

Formal SmPC and MHRA-approved warnings and contraindications data were not available in the source Evidence Pack, and no drug interaction data were retrieved.

> Please refer to the SmPC from an equivalent jurisdiction (e.g., the EMA-approved Betoptic® SmPC) and the BNF for safety information before use. Class-effect cautions for β-blockers applied topically include: systemic absorption causing bradycardia, bronchospasm, and hypotension; particular caution is required in patients with asthma, COPD, second- or third-degree AV block, or decompensated heart failure. In the paediatric PHG population, systemic β-blockade following ocular administration carries heightened risk; weight-adjusted dosing and monitoring are essential. Report suspected adverse reactions via the **Yellow Card Scheme** (https://yellowcard.mhra.gov.uk/).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction is biologically highly plausible — betaxolol's established IOP-lowering mechanism directly addresses the central pathophysiology of primary hereditary glaucoma, and this represents a subtype extension rather than a truly novel indication. However, the complete absence of specific clinical trial or published evidence for this hereditary subtype, combined with betaxolol having no current UK marketing authorisation, means that clinical adoption requires careful governance scaffolding before proceeding.

**To proceed, the following is needed:**

- **Regulatory pathway scoping**: Engage with MHRA to clarify whether a new paediatric indication application, an off-label use policy, or a named-patient supply framework is the appropriate route for the PHG population in the UK.
- **Safety dossier assembly**: Retrieve the full SmPC (e.g., EMA Betoptic® SmPC), MHRA Yellow Card data, and DrugBank safety data to complete a formal safety assessment — particularly for the neonatal/paediatric age group most affected by PHG.
- **Mechanism of action (MOA) confirmation**: Obtain structured DrugBank API data for DB00195 to formally document the receptor pharmacology, supporting regulatory submissions.
- **Evidence gap review**: Commission a targeted systematic literature review of betaxolol and β-blocker eye drops in paediatric or hereditary glaucoma subtypes; even indirect evidence (e.g., timolol in congenital glaucoma) would inform a bridging rationale.
- **Paediatric safety monitoring plan**: Given the PHG patient population (predominantly infants and young children), a protocol for monitoring systemic β-blockade effects (heart rate, respiratory function) during topical ophthalmic use is essential before any clinical use is initiated.
- **Clinical expert consultation**: Involve a paediatric ophthalmologist and a clinical pharmacologist to review the proposed use case and validate the repurposing rationale in a UK clinical context.

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All UK prescribing decisions must comply with current MHRA guidance and relevant legislation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

