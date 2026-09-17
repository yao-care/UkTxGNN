---
layout: default
title: Progesterone
parent: Moderate Evidence (L3-L4)
nav_order: 485
evidence_level: L3
indication_count: 10
---

# Progesterone
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

Using no additional skill — this is a direct report-generation task governed entirely by the CLAUDE.md prompt spec already provided, so I'll follow that template exactly.

# Progesterone: From Reproductive Endocrine Therapy to Amenorrhea

## One-Sentence Summary

> Progesterone is an endogenous steroid hormone with established roles across reproductive endocrinology, but this evidence pack contains no recorded UK marketing authorisation or approved indication text for the product.
> The TxGNN model predicts strong applicability to **Amenorrhea**,
> with **50 clinical trials** and **18 publications** reviewed, although most reflect progesterone's long-standing textbook use (the progesterone challenge test and cyclic therapy) rather than a genuinely novel pharmacological mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack — no marketing authorisation or approved indication text on file (`original_indications` empty) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.9996% |
| Evidence Level | L3 |
| UK Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this DrugBank entry (DB00396). Based on known pharmacology, progesterone is a natural steroid hormone that regulates the hypothalamic-pituitary-ovarian axis and the proliferative/secretory transformation of the endometrium; this is reflected in the literature evidence returned (e.g. PMID 38652231, PMID 22283375).

No original indication is recorded in this evidence pack, so a formal "original → new indication" comparison cannot be made from the regulatory data alone. However, the repurposing rationale attached to this candidate is explicit: progesterone withdrawal induces endometrial shedding and bleeding, and this is the physiological basis of the progesterone challenge test used to distinguish anatomical from hormonal causes of secondary amenorrhea, as well as cyclic progesterone therapy for withdrawal bleeding. This is described in the evidence pack as "a well-established mechanism representing an existing clinical use rather than a novel pharmacological discovery" — i.e. the TxGNN prediction is recovering a known, textbook clinical application rather than identifying a genuinely new mechanism.

This distinction matters for decision-making: the prediction is mechanistically sound and clinically plausible, but the strength of the "repurposing" claim is lower than it would be for a truly novel indication, since progesterone's use in amenorrhea diagnosis and management is already part of standard gynaecological practice.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01942668](https://clinicaltrials.gov/study/NCT01942668) | Phase 3 | Completed | 1,845 | Estradiol + progesterone combination for vasomotor symptoms in postmenopausal women with an intact uterus |
| [NCT01185782](https://clinicaltrials.gov/study/NCT01185782) | Phase 3 | Completed | 300 | Comparative study of gonadotropin therapy in subjects with Amenorrhea I / anovulatory cycles (relevance grade B — endocrine axis relevant, not direct progesterone test) |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | Completed | 42 | Tests whether progesterone-induced endometrial withdrawal bleeding is necessary before ovulation induction with clomiphene in women with oligo-/amenorrhea |
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | Terminated | 60 | Post-ablation medroxyprogesterone acetate effect on endometrial amenorrhea rates (heavy menstrual bleeding) |
| [NCT05312190](https://clinicaltrials.gov/study/NCT05312190) | N/A | Unknown | 330 | Progesterone capsules vs a Chinese herbal formula (alone and combined) for menstrual disorders |
| [NCT06533865](https://clinicaltrials.gov/study/NCT06533865) | Phase 3 | Recruiting | 114 | Romosozumab as adjunct to physiologic oestrogen replacement plus cyclic progesterone in functional hypothalamic amenorrhea with low bone density |
| [NCT01674426](https://clinicaltrials.gov/study/NCT01674426) | N/A | Completed | 17 | Randomised pilot of cognitive behavioural therapy vs observation for functional hypothalamic amenorrhea (relevance grade C — pathogenesis study, not a drug trial) |
| [NCT03740204](https://clinicaltrials.gov/study/NCT03740204) | Phase 2 | Recruiting | 120 | Transdermal estradiol with cyclic progesterone vs placebo in hypoestrogenaemic adolescents/young adults with an eating disorder (relevance grade C — tests oestrogen, progesterone is background regimen only) |
| [NCT00088153](https://clinicaltrials.gov/study/NCT00088153) | Phase 2/3 | Completed | 110 | Effects of anorexia nervosa on peak bone mass; oestrogen administration to maintain bone development in adolescents |
| [NCT02858336](https://clinicaltrials.gov/study/NCT02858336) | N/A | Completed | 38 | CaREFREE study — diet, exercise and environmental effects on functional hypothalamic amenorrhea |

A further 40 trials were identified in the underlying dataset but relate mainly to related conditions (PCOS, uterine fibroids, ovarian insufficiency) rather than direct progesterone intervention in amenorrhea, and are not shown here.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Reviews in Endocrine & Metabolic Disorders | Diagnostic and therapeutic use of oral micronised progesterone in endocrinology, including its role via hypothalamic kisspeptin/neurokinin B/dynorphin neurons |
| [35525789](https://pubmed.ncbi.nlm.nih.gov/35525789/) | 2022 | Review | Current Problems in Pediatric and Adolescent Health Care | Etiology and management of amenorrhoea in adolescent and young adult women, including HPO-axis dysfunction |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | American Family Physician | Evaluation of amenorrhoea; practical diagnostic approach including progesterone challenge testing |
| [35463307](https://pubmed.ncbi.nlm.nih.gov/35463307/) | 2022 | Meta-analysis | Frontiers in Oncology | Chemotherapy-induced amenorrhoea and its prognostic significance in premenopausal breast cancer |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Frontiers in Endocrinology | Current understanding of aetiology, symptomatology and treatment options in premature ovarian insufficiency |
| [28257537](https://pubmed.ncbi.nlm.nih.gov/28257537/) | 2017 | Review | Southern Medical Journal | Primary ovarian insufficiency — current concepts, including hormone replacement management |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | Review | Gynecological Endocrinology | Neuroendocrine control of ovulation and the GnRH–gonadotrophin–ovarian steroid axis in anovulation/amenorrhoea |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | Review | Climacteric | Clinical management of vaginal bleeding in postmenopausal women, referencing oestrogen/progesterone withdrawal |
| [36653588](https://pubmed.ncbi.nlm.nih.gov/36653588/) | 2023 | Review | Reproductive Sciences | Methods for repairing and regenerating injured endometrium (intrauterine adhesions causing amenorrhoea) |
| [18756412](https://pubmed.ncbi.nlm.nih.gov/18756412/) | 2008 | Review | Seminars in Reproductive Medicine | Intrauterine adhesions (Asherman's syndrome), a structural cause of amenorrhoea |

## UK Market Information

No UK marketing authorisation records are present in this evidence pack (`total_licenses = 0`, `licenses` empty, `market_status = "Not marketed"`). This does not necessarily mean progesterone is unavailable in the UK market generally — it indicates the data source used to build this evidence pack currently holds no MHRA licence record for this DrugBank entry. This should be verified directly against the MHRA Products database before any clinical or commercial decision is made.

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is biologically well established (progesterone withdrawal bleeding underpins both diagnostic testing and cyclic treatment of amenorrhoea) and is supported by two Level-2 reviews plus 50 clinical trials, but the evidence level is capped at L3 because most trials test progesterone only as part of a background regimen (alongside oestrogen or other agents) rather than as the primary intervention, and no UK product/licence data could be confirmed.

**To proceed, the following is needed:**
- MHRA product/SmPC data confirming current UK licensing status of progesterone products (blocking gap, DG001)
- DrugBank/company mechanism-of-action documentation (DG002)
- Confirmation of which specific progesterone-only trials (vs. combination oestrogen/progesterone regimens) directly support the amenorrhoea indication
- A formal safety review (contraindications, DDI, thromboembolic and hormone-sensitive cancer risk) before any guardrail-based prescribing recommendation is finalised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

