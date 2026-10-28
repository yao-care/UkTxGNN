---
layout: default
title: Dienogest
parent: Model Prediction Only (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Dienogest: predicted new indication Amenorrhoea (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "dienogest"
predicted_indications: ["amenorrhea (disease)", "primary ovarian failure", "breast fibrocystic disease", "isolated growth hormone deficiency", "symptomatic form of fragile X syndrome in female carrier", "blepharophimosis-epicanthus inversus-ptosis", "hypogonadotropic hypogonadism with or without anosmia", "partial trisomy/tetrasomy of the short arm of chromosome 5", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 18"]
---

# Dienogest
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Dienogest: From Hormonal Contraception/Gynaecological Use to Amenorrhoea
{: .text-alpha }

## One-Sentence Summary

Dienogest is a progestin used in combination oral preparations (including estradiol valerate + dienogest), and the data compiled for this report do not list a specific original indication.
The TxGNN model predicts it may be relevant to **amenorrhoea**, but there are **no registered clinical trials** and only **7 publications**, none of which directly tests dienogest as a treatment for amenorrhoea.
Amenorrhoea is better understood as an expected pharmacological effect of dienogest than as an established treatment target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the licence indication text is empty) |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 (preclinical/mechanistic and indirect literature only; no clinical trials) |
| UK Market Status | Marketed (valid licences: 2 of 2) |
| Number of Marketing Authorisations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known pharmacology, dienogest is a progestin with strong effects on the endometrium and mild antigonadotropic activity. It suppresses ovulation and endometrial proliferation, which commonly leads to amenorrhoea or a markedly altered bleeding pattern, as seen when it is used for endometriosis.

This explains why the model links dienogest to amenorrhoea. However, the link is largely circular: amenorrhoea is an expected effect or side effect of treatment, not a recognised disease target that dienogest is used to correct. In addition, dienogest lowers estradiol. In secondary amenorrhoea caused by oestrogen deficiency, this effect would be a concern rather than a benefit.

The other nine predictions (for example primary ovarian failure, hypogonadotropic hypogonadism, and several chromosomal or genetic syndromes) have no supporting evidence. Several are mechanistically counterproductive, because dienogest suppresses the hypothalamic-pituitary-gonadal axis and lowers oestrogen. They are most likely artefacts of network proximity to sex-hormone pathways.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic review / Bayesian meta-analysis | BMC Pharmacol Toxicol | Summarises adverse events and their prevalence during dienogest treatment for endometriosis and adenomyosis |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Retrospective cohort (514 women) | Reprod Sci | Long-term (>12 months) dienogest 2 mg daily for ovarian endometrioma; assessed efficacy, safety and recurrence |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Rev Endocr Metab Disord | Endocrine background of hormonal treatments for endometriosis; amenorrhoea is a treatment aim in this context |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Clinical/laboratory study | Eur J Contracept Reprod Health Care | Further evidence for dienogest 2 mg in endometriosis treatment |
| [42438810](https://pubmed.ncbi.nlm.nih.gov/42438810/) | 2026 | Case report | JCEM Case Rep | Primary hyperparathyroidism unmasked after dienogest-altered oestrogen dynamics, with implications for calcium homeostasis |

The data also include a case report of an ovarian granulosa cell tumour (PMID 34918698) and a review of imaging of Müllerian anomalies (PMID 40543564). Both are unrelated to dienogest therapy and are not summarised here.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0703010R0BBAAAA | Qlaira (C/Pk Tab) | Not specified | Not specified |
| 0703010R0AAAAAA | Estradiol / Estradiol + Dienogest (C/Pk Tab) | Not specified | Not specified |

Both authorisations are valid. Dosage form and indication text are not recorded in the data compiled for this report. The identifiers shown above are as recorded and do not follow the standard MHRA PL number format, so they should be verified against the MHRA register and the BNF.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** The TxGNN knowledge graph links dienogest to the following conditions, which must be checked against the SmPC:
  - Cardiovascular and thrombotic: hypertension, thrombophlebitis
  - Hormone-sensitive malignancy: female breast carcinoma
  - Hepatic and biliary: liver disease, gallbladder disease
  - Renal: kidney disease
  - Metabolic and endocrine: diabetes mellitus and diabetic ketoacidosis, hypertriglyceridaemia, hypothyroidism, hypercalcaemia
  - Other: porphyria, epilepsy, asthma, systemic lupus erythematosus, anxiety and related mood disorders
- **Drug Interactions:** 37 interactions were identified. Those flagged as **Major** include sugammadex, griseofulvin, bexarotene, brigatinib, dabrafenib and encorafenib. Moderate interactions include linaclotide, metreleptin, prucalopride, miltefosine and several biologics (for example adalimumab, anakinra, canakinumab, certolizumab pegol).
- A case report (PMID 42438810) describes primary hyperparathyroidism emerging after dienogest-altered oestrogen dynamics, suggesting attention to calcium homeostasis.

Label warnings and contraindications were not available. Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. Amenorrhoea is an expected pharmacological effect of dienogest rather than a validated therapeutic target, there are no clinical trials, and the supporting literature concerns endometriosis rather than amenorrhoea. Where amenorrhoea results from oestrogen deficiency, dienogest's oestradiol-lowering effect could be unhelpful.

**To proceed, the following is needed:**
- Label warnings and contraindications from the SmPC and BNF, which are currently missing and block safety screening
- Mechanism of action data (for example from DrugBank)
- Licence indication and dosage form details for both authorisations
- A clear clinical question defining which type of amenorrhoea (if any) would be treated, and why a progestin that suppresses oestradiol would be appropriate
- Clinical or observational studies in the proposed population before any further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

