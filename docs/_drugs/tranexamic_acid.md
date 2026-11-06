---
layout: default
title: Tranexamic Acid
parent: Model Prediction Only (L5)
nav_order: 633
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-06
monitor_inn: "Tranexamic acid"
predicted_indications: ["amenorrhea (disease)"]
description: "Tranexamic Acid: predicted new indication Amenorrhea (disease) (evidence level L5). Approved use: Not recorded in the local data"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Tranexamic Acid: Amenorrhea (disease)
{: .text-alpha }

## One-Sentence Summary

Tranexamic acid is an antifibrinolytic medicine. Its original indication is endometriosis, although it is best known clinically for heavy menstrual bleeding.
The TxGNN model predicts it may be effective for **amenorrhoea**, but there are **no registered clinical trials** and only **2 publications** (both narrative reviews), and these do not directly support the prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 0.9919 |
| Evidence Level | L5 (see note below) |
| UK Market Status | Listed in the NHSBSA BNF prescribing code list (26 presentation codes) – MHRA licence status is not included in this data |
| Number of BNF Presentation Codes | 26 |
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

| BNF presentation code | BNF presentation | BNF chemical substance |
|------|------|------|
| 0211000P0AAAQAQ | Tranexamic acid 100mg/5ml oral solution | Tranexamic acid |
| 0211000P0AABFBF | Tranexamic acid 150mg/5ml oral solution | Tranexamic acid |
| 0211000P0AABGBG | Tranexamic acid 1g granules sachets | Tranexamic acid |
| 0211000P0AABHBH | Tranexamic acid 1g/100ml infusion polyethylene bottles | Tranexamic acid |
| 0211000P0AAAJAJ | Tranexamic acid 1g/5ml oral solution | Tranexamic acid |
| 0211000P0AAAKAK | Tranexamic acid 2.5g/5ml oral solution | Tranexamic acid |
| 0211000P0AABABA | Tranexamic acid 225mg/5ml oral solution | Tranexamic acid |
| 0211000P0AAAZAZ | Tranexamic acid 240mg/5ml oral solution | Tranexamic acid |
| 0211000P0AAAIAI | Tranexamic acid 250mg/5ml oral solution | Tranexamic acid |
| 0211000P0AABEBE | Tranexamic acid 250mg/5ml oral suspension | Tranexamic acid |
| 0211000P0AAAUAU | Tranexamic acid 25mg/5ml oral solution | Tranexamic acid |
| 0211000P0AAARAR | Tranexamic acid 300mg/5ml oral solution | Tranexamic acid |
| 0211000P0AAAWAW | Tranexamic acid 350mg/5ml oral solution | Tranexamic acid |
| 0211000P0AAANAN | Tranexamic acid 400mg/5ml oral solution | Tranexamic acid |
| 0211000P0AAAXAX | Tranexamic acid 425mg/5ml oral solution | Tranexamic acid |
| 0211000P0AABDBD | Tranexamic acid 5% mouthwash | Tranexamic acid |
| 0211000P0AAACAC | Tranexamic acid 500mg tablets | Tranexamic acid |
| 0211000P0AABIBI | Tranexamic acid 500mg/50ml infusion polyethylene bottles | Tranexamic acid |
| 0211000P0AABBBB | Tranexamic acid 500mg/5ml oral solution | Tranexamic acid |
| 0211000P0AABCBC | Tranexamic acid 500mg/5ml oral suspension | Tranexamic acid |

Showing 20 of 26 BNF presentation codes. Source: NHSBSA BNF code information (NHS prescribing codes). These are not MHRA licences, and MHRA licence status is not included in this data.

Please check the MHRA register, the BNF and the current SmPC for licensed indications.

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

