---
layout: default
title: Carbimazole
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 3
---

# Carbimazole
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

# Carbimazole: From Hyperthyroidism to Resistance to Thyroid Hormone (THRβ Mutation)

## One-Sentence Summary

Carbimazole is a thionamide antithyroid agent, originally established for the treatment of hyperthyroidism including Graves' disease. The TxGNN model predicts it may be effective for **Resistance to Thyroid Hormone due to a Mutation in Thyroid Hormone Receptor Beta (RTH-β)**, with **0 clinical trials** and **1 publication** currently supporting this direction.

> ⚠️ This report is intended for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperthyroidism (Graves' disease, toxic nodular goitre) |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| UK Market Status | Not currently marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

> **Data note:** The MHRA marketing authorisation database returned zero records for Carbimazole in this evidence pack. Clinicians should verify directly via the [MHRA Product Licence Search](https://products.mhra.gov.uk/) or the current BNF, as this may reflect a data collection gap rather than the true regulatory position.

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Carbimazole is a prodrug that is rapidly converted in vivo to its active metabolite methimazole. Methimazole inhibits thyroid peroxidase (TPO), the enzyme responsible for the iodination and coupling steps in thyroid hormone (T3 and T4) biosynthesis. Its efficacy in reducing circulating thyroid hormone levels in primary hyperthyroidism has been well established over decades of clinical use.

Resistance to thyroid hormone due to a mutation in the thyroid hormone receptor beta gene (THRB) — commonly abbreviated RTH-β — is a rare autosomal dominant condition in which pituitary and peripheral tissues display relative insensitivity to thyroid hormone signalling. As a physiological compensation, affected individuals typically present with persistently elevated free T4 (and often free T3) alongside non-suppressed or frankly elevated TSH. This biochemical picture closely mimics primary hyperthyroidism on routine thyroid function testing, and has historically led to misdiagnosis and inappropriate initiation of antithyroid therapy, including carbimazole.

The TxGNN prediction is mechanistically plausible in that carbimazole would lower circulating free T4 concentrations; however, in RTH-β those elevated hormones represent a compensatory response to impaired receptor sensitivity. Reducing thyroid hormone synthesis risks worsening hypothyroid symptoms in peripheral tissues whilst paradoxically driving further TSH-mediated thyroid enlargement. The single identified publication in this evidence pack illustrates precisely this diagnostic pitfall rather than a therapeutic success. Clinical context and molecular confirmation of THRB pathogenic variants are therefore essential before any treatment decision.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Case Report | *BMJ Case Reports* | A young man with persistently elevated free T4 (25–35.7 pmol/L) and non-suppressed TSH (6.78–22.1 mIU/L) was intermittently treated with carbimazole over ten years without adequate response; the case highlights the risk of misidentifying RTH-β as primary hyperthyroidism and illustrates why antithyroid drugs may be ineffective or harmful in this context |

---

## UK Market Information

According to the data available in this evidence pack, Carbimazole holds no current MHRA marketing authorisations in the United Kingdom. No licensed products, dosage forms, or approved indications were returned.

> Clinicians should cross-reference with the MHRA Product Licence Search, the Electronic Medicines Compendium (eMC), and the current edition of the BNF (Section 6.2.2 — Antithyroid drugs) to obtain authoritative prescribing information.

---

## Safety Considerations

No specific safety data (warnings, contraindications, or drug interactions) were available in this evidence pack.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the **Yellow Card Scheme** at [yellowcard.mhra.gov.uk](https://yellowcard.mhra.gov.uk/).

> **Known class-level considerations (thionamides, for clinical reference):** Agranulocytosis is a rare but serious adverse effect of both carbimazole and propylthiouracil; patients should be advised to seek urgent medical attention if they develop sore throat, mouth ulcers, or fever. Carbimazole has also been associated with congenital abnormalities (including aplasia cutis and choanal atresia) when used in the first trimester of pregnancy — propylthiouracil is generally preferred in this period. These observations are from published clinical literature and should be confirmed against the current SmPC.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole identified publication describes a case in which carbimazole was used *erroneously* over a decade in a patient subsequently found to have RTH-β — illustrating a diagnostic trap rather than a therapeutic benefit. No registered clinical trials exist for this indication, and the underlying mechanistic rationale raises genuine concerns that reducing thyroid hormone synthesis could be counterproductive or harmful in confirmed RTH-β.

**To proceed, the following is needed:**

- **Mechanistic clarification:** Does lowering circulating T4 via TPO inhibition confer any net clinical benefit in RTH-β patients, or does it worsen peripheral hypothyroid symptoms and exacerbate TSH-driven goitre?
- **Prospective observational data:** Case series or registry data specifically in genetically confirmed RTH-β patients who have received antithyroid therapy, with documented clinical and biochemical outcomes
- **Patient stratification:** THRB genotyping and phenotype characterisation to determine whether any RTH-β subpopulation (e.g., those with predominant pituitary resistance) might derive benefit
- **Full MOA data:** Retrieval from DrugBank API and SmPC to complete the mechanistic analysis
- **Regulatory verification:** Confirmation of current MHRA marketing authorisation status via eMC or MHRA Product Licence Search
- **Safety profile review:** Full SmPC and BNF review, including teratogenicity data and haematological monitoring requirements, before any clinical exploration

---

*Report generated: 5 April 2026 | Evidence data cut-off: 5 April 2026 | Candidate ID: TW-DB00389-multi (v4)*
*This report is for research purposes only and does not constitute clinical guidance or a recommendation for prescribing.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

