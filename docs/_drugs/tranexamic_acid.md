---
layout: default
title: Tranexamic Acid
parent: Model Prediction Only (L5)
nav_order: 633
evidence_level: L5
indication_count: 1
---

# Tranexamic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Tranexamic Acid: From Endometriosis to Amenorrhoea

## One-Sentence Summary

Tranexamic acid is an antifibrinolytic medicine. The knowledge graph records its original indication as endometriosis, although it is best known clinically for heavy menstrual bleeding.
The TxGNN model predicts it may be effective for **amenorrhoea**, but there are **no registered clinical trials** and only **2 publications** (both narrative reviews), and these do not directly support the prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (as recorded in the TxGNN knowledge graph; no approved indication text is available in the UK licence data) |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L4 (see note below) |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

*Note on evidence level:* Strictly, the grading rules would place this at L5 (model prediction only), because there are no clinical trials and only narrative reviews. L4 is retained here from the underlying assessment, but it rests on general pharmacology, not on studies of this indication.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug in the data compiled for this report. Based on general pharmacology, tranexamic acid is an antifibrinolytic. It inhibits plasminogen activation and so reduces fibrinolysis-mediated breakdown of the endometrium. It is an established treatment for heavy menstrual bleeding, which gives a plausible indirect link to menstrual suppression.

However, **suppressing menses is not the same as treating amenorrhoea**, which is the absence of menses. Amenorrhoea is usually hormonal or structural in origin, and an antifibrinolytic would not be expected to restore menstruation. The high TxGNN score probably reflects network proximity to menstrual disorders rather than a true therapeutic relationship.

The two publications retrieved concern abnormal uterine bleeding and menses suppression in haematology patients. In that setting, reducing bleeding is the goal, so they do not show benefit in amenorrhoea itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause | Evidence-based review of drug therapies for abnormal uterine bleeding. Non-hormonal options (including NSAIDs, which reduce bleeding by 25–35%) are effective and generally well tolerated. Choice depends on cause, bleeding volume, contraception and fertility needs, and perimenopausal status. |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | J Oncol Pharm Pract | Systematic approach to menses prophylaxis and suppression in pre-menopausal women with haematological cancers, where cytopenias make menstrual bleeding hazardous. Comparative data between agents are scarce. |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0211000P0AAACAC | Tranexamic Acid Tab 500mg | Not specified | Not specified |

Only one authorisation (single-ingredient, valid) is recorded, and its dosage form and approved indication text are not available in the data compiled for this report. Please check the MHRA register, the BNF and the current SmPC for licensed indications. The record does not follow the usual UK "PL" numbering format, so the identifier should be verified.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from drug-disease network links, not from label text, and should be verified against the SmPC):
- Cardiovascular and thrombotic: thrombophlebitis, coronary artery disease, stroke, cerebrovascular disorder, hypertension
- Hormone-sensitive cancers: female breast carcinoma, endometrial cancer and related uterine neoplasms
- Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperlipidaemia, hypertriglyceridaemia, obesity
- Hepatic and porphyria: liver disease, gallbladder disease, porphyria
- Neurological and psychiatric: migraine, brain oedema, anxiety and neurotic disorders, dysthymic disorder

**Drug Interactions:** 35 interactions were identified. Examples of those listed:
- **Major:** oestrogen-containing products (ethinylestradiol, estradiol, conjugated oestrogens, estrone, diethylstilbestrol and others), progestogens (norethisterone, drospirenone, etonogestrel), anti-inhibitor coagulant complex, factor IX complex (human) and carfilzomib. The main concern with hormonal products and procoagulant agents is additive thrombotic risk.
- **Moderate:** thrombolytics (alteplase, anistreplase), which have opposing pharmacological effects.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and a loose mechanistic link to menstrual bleeding. There are no clinical trials, and the only publications are narrative reviews of bleeding control, which is the opposite of the clinical need in amenorrhoea. The drug's antifibrinolytic action gives no clear reason to expect restoration of menses.

**To proceed, the following is needed:**
- Clarification of whether a bleeding-related indication (for example, menses suppression or heavy menstrual bleeding) is the more appropriate target than amenorrhoea
- Detailed mechanism of action data and a clearer mechanistic argument for the new indication
- Verified UK licence details (dosage form and approved indication) from the MHRA register and SmPC
- Review of label-based warnings and contraindications, particularly thrombotic risk and interactions with hormonal products
- Any clinical or observational data in the target population before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

