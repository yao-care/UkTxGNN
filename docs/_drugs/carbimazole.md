---
layout: default
title: Carbimazole
parent: Model Prediction Only (L5)
nav_order: 133
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Carbimazole: predicted new indication Neonatal thyrotoxicosis (evidence level L5). Approved use: Hyperthyroidism, Graves' disease, thyrotoxicosis"
monitor_inn: "Carbimazole"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia"]
---

# Carbimazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Carbimazole: From Hyperthyroidism to Neonatal Thyrotoxicosis

## One-Sentence Summary

Carbimazole is an antithyroid drug (a prodrug of methimazole) originally used to treat hyperthyroidism, Graves' disease and thyrotoxicosis.
The TxGNN model's top-ranked prediction is resistance to thyroid hormone beta, but this looks like a network artefact. The most clinically plausible prediction is **neonatal thyrotoxicosis**, supported by **0 registered clinical trials** and **13 publications** (reviews, cohorts and case reports).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperthyroidism, Graves' disease, thyrotoxicosis (the approved indication text is not available in the licence data) |
| Predicted New Indication | Neonatal thyrotoxicosis (the top-scoring prediction, resistance to thyroid hormone due to a thyroid hormone receptor beta mutation, is judged not credible; see below) |
| TxGNN Prediction Score | 99.41% (neonatal thyrotoxicosis); 99.71% for resistance to thyroid hormone beta; 99.21% for hyperthyroxinaemia |
| Evidence Level | L3 (neonatal thyrotoxicosis: reviews, cohorts and case reports only) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Proceed with Guardrails (neonatal thyrotoxicosis only); Hold for the other two predictions |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Carbimazole is, however, a well-known prodrug of methimazole. It inhibits thyroid peroxidase and so reduces the synthesis of thyroid hormone. This is why it works in hyperthyroidism and Graves' disease.

**Neonatal thyrotoxicosis (most plausible).** This condition usually results from transplacental passage of maternal TSH-receptor stimulating antibodies in Graves' disease, driving excess thyroid hormone production. Blocking hormone synthesis directly matches this pathophysiology. Carbimazole is already used in this setting, so the prediction is essentially an extension of the existing hyperthyroidism use to a special population. The published evidence is limited to case reports, small series and reviews.

**Resistance to thyroid hormone beta (not supported).** The defect lies in the receptor, with raised T4/T3 and non-suppressed TSH. Lowering hormone synthesis would remove negative feedback and raise TSH further, risking goitre enlargement and worsening hypothyroidism in receptor-resistant tissues. The high score is probably a network-proximity artefact from shared thyroid-axis terms, and antithyroid drugs are generally not recommended here.

**Hyperthyroxinaemia (not a distinct target).** This is a laboratory finding with several causes. Where it reflects true hormone overproduction, it is already covered by the existing indication. With binding-protein abnormalities (such as familial dysalbuminaemic hyperthyroxinaemia) antithyroid treatment is not indicated, and in TSH-secreting pituitary adenoma carbimazole does not address the cause and may raise TSH further.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the three predicted indications.

---

## Literature Evidence

Most relevant publications for neonatal thyrotoxicosis (the highest-value prediction):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24251220](https://pubmed.ncbi.nlm.nih.gov/24251220/) | 2013 | Review | Indian J Endocrinol Metab | Fetal thyrotoxicosis is rare, with mortality of 12-20%, mostly from heart failure. It results from placental transfer of thyroid-stimulating immunoglobulins. |
| [24622372](https://pubmed.ncbi.nlm.nih.gov/24622372/) | 2013 | Review | Lancet Diabetes Endocrinol | Hyperthyroidism in pregnancy: distinguishing it from physiological changes, and the risks to mother and offspring. |
| [7523202](https://pubmed.ncbi.nlm.nih.gov/7523202/) | 1994 | Retrospective cohort | Eur J Obstet Gynecol Reprod Biol | 32 pregnancies complicated by hyperthyroidism, managed with carbimazole or propylthiouracil. |
| [1971773](https://pubmed.ncbi.nlm.nih.gov/1971773/) | 1990 | Cohort | Clin Endocrinol | In 44 women with Graves' disease treated with PTU or carbimazole, maternal and neonatal thyroid function was related to TSH receptor antibodies and thionamide dose. |
| [11298090](https://pubmed.ncbi.nlm.nih.gov/11298090/) | 2001 | Case series | Clin Endocrinol | Congenital thyrotoxicosis in premature infants. Maternal history and TSH receptor antibody levels help predict adverse outcomes. |
| [41191399](https://pubmed.ncbi.nlm.nih.gov/41191399/) | 2025 | Case report | Endocrinol Diabetes Metab Case Rep | Neonatal hypercalcaemia secondary to transient thyrotoxicosis; the thyrotoxicosis responded to carbimazole. |
| [25952662](https://pubmed.ncbi.nlm.nih.gov/25952662/) | 2015 | Case report | Indian J Pediatr | Intrauterine carbimazole treatment of fetal hyperthyroidism in two siblings. |
| [12124735](https://pubmed.ncbi.nlm.nih.gov/12124735/) | 2002 | Case report | Am J Med Genet | Choanal atresia after maternal carbimazole treatment (safety signal). |
| [27747714](https://pubmed.ncbi.nlm.nih.gov/27747714/) | 2015 | Case report | Drug Saf Case Rep | A newborn treated with carbimazole and propranolol developed severe hypotension after amlodipine. |
| [2315685](https://pubmed.ncbi.nlm.nih.gov/2315685/) | 1990 | Case report | Scott Med J | Neonatal thyrotoxicosis responded to carbimazole in the infant of a mother with relapsed Graves' disease and TSH receptor antibodies. |

Other predictions: resistance to thyroid hormone beta has one case discussion ([24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/), 2013, BMJ Case Reports), which describes a patient with raised free T4 and non-suppressed TSH who was intermittently treated with carbimazole. For hyperthyroxinaemia there are only case reports, a review and a laboratory study (for example [24847468](https://pubmed.ncbi.nlm.nih.gov/24847468/) and [3708869](https://pubmed.ncbi.nlm.nih.gov/3708869/)), with no controlled data.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0602020D0AAAAAA (BNF code 0602020D0, antithyroid drugs) | Carbimazole tablets 5 mg | Tablet (not specified in the data) | Not specified in the data; please check the SmPC |

---

## Safety Considerations

- **Teratogenic signal:** Case reports describe choanal atresia after in-utero carbimazole exposure. Possible associations with aplasia cutis have also been noted.
- **Overtreatment:** Fetal or neonatal hypothyroidism and goitre can occur if the dose is too high.
- **Drug interactions:** Case reports describe severe hypotension when amlodipine was added in a neonate treated with carbimazole and propranolol. Dedicated interaction data are not available.
- **Resistance to thyroid hormone beta:** Antithyroid drugs are generally not recommended, as they may raise TSH and worsen goitre or hypothyroidism.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (neonatal thyrotoxicosis only). Hold for resistance to thyroid hormone beta and hyperthyroxinaemia.**

**Rationale:**
- For neonatal thyrotoxicosis, the mechanism matches the pathophysiology and carbimazole is already used clinically in this setting, but the evidence is limited to reviews, cohorts and case reports (L3), with no registered trials.
- The resistance to thyroid hormone beta prediction is probably an artefact and may be harmful. Hyperthyroxinaemia is a laboratory finding rather than a distinct target.

**To proceed, the following is needed:**
- The approved indication text and SmPC safety data (warnings and contraindications) for the UK licence
- Mechanism of action data from DrugBank
- Review against NICE and BNF guidance on antithyroid drugs in pregnancy and the neonatal period
- A structured review of dosing, monitoring (thyroid function, blood counts) and teratogenicity risk for fetal and neonatal use
- Formal clinical specialist (paediatric endocrinology) input on any evidence gaps that prospective or registry data could address
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

