---
layout: default
title: Estriol
parent: Model Prediction Only (L5)
nav_order: 242
evidence_level: L5
indication_count: 1
---

# Estriol
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

# Estriol: From Unspecified Indication to Amenorrhea

## One-Sentence Summary

Estriol (DrugBank DB04573) is a naturally occurring estrogen; the evidence pack does not document its originally licensed indication or mechanism of action, both of which are flagged as data gaps. The TxGNN model predicts potential efficacy for **Amenorrhea**, with a high raw prediction score, but the supporting clinical trial evidence in this pack actually relates to **Estetrol (E4)**, a related but distinct estrogen — not Estriol itself — so the clinical-trial evidence should not currently be counted as direct support for this candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.18% (rank 7,056 among model predictions — not a top-tier rank despite the high score) |
| Evidence Level | L3 (based on Estriol-specific observational evidence; see caveat below) |
| UK Market Status | Not marketed (Not marketed) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this candidate (data gap DG002), and no original licensed indication is recorded in the evidence pack (`original_indications` is empty). Based on general pharmacological knowledge, Estriol is a weak, naturally occurring estrogen. Estrogens are physiologically linked to the hypothalamic–pituitary–gonadal axis, so a mechanistic link to amenorrhea (particularly functional hypothalamic amenorrhea, FHA, which is characterised by hypoestrogenism) is biologically plausible.

This plausibility is supported by one directly relevant piece of literature: Genazzani et al. (2012, PMID 22137494) reported that Estriol administration modulated luteinizing hormone secretion in women with functional hypothalamic amenorrhea, suggesting a neuroendocrine-modulating effect consistent with the proposed indication.

**Important caveat:** the two completed Phase 3 trials returned in this evidence pack (NCT04090957, NCT04209543 — the "E4Comfort" studies) are trials of **Estetrol (E4)**, not Estriol (E3). These are distinct estrogen molecules, and despite the query having been run against "Estriol," they should not be treated as clinical evidence for this specific drug without independent confirmation. This substantially changes the evidence picture from what the raw trial count would suggest, and is the main reason the Evidence Level below is set lower than the trial phase/completion data alone would imply.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04090957](https://clinicaltrials.gov/study/NCT04090957) | Phase 3 | Completed | 1,015 | Evaluated **Estetrol (E4)** 15/20 mg vs placebo for vasomotor symptoms in postmenopausal women. **Drug identity caveat: this trial is for Estetrol, not Estriol.** |
| [NCT04209543](https://clinicaltrials.gov/study/NCT04209543) | Phase 3 | Completed | 1,570 | Evaluated **Estetrol (E4)** 15/20 mg vs placebo for vasomotor symptoms, plus endometrial/general safety. **Drug identity caveat: this trial is for Estetrol, not Estriol.** |
| [NCT04487392](https://clinicaltrials.gov/study/NCT04487392) | Phase 2 | Withdrawn (0 enrolled) | 0 | Photobiomodulation for vulvovaginal atrophy in postmenopausal women; amenorrhea appears only as background definition, not as a treated indication, and the study did not proceed. |

None of the three registered trials constitutes direct clinical evidence of Estriol for amenorrhea.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | Observational | Fertility and Sterility | Estriol administration modulated luteinizing hormone secretion in women with functional hypothalamic amenorrhea — the most directly relevant Estriol-specific evidence in this pack. |
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | Review | Biomedicines | Discusses low-dose estrogens (as a class) as neuroendocrine modulators in functional hypothalamic amenorrhea, supporting the mechanistic rationale but not Estriol-specific. |
| [16526238](https://pubmed.ncbi.nlm.nih.gov/16526238/) | 2005 | Observational | Medicinski pregled | Effects of estro-progestagens on lipid/hormonal profiles in premature primary ovarian failure (hypergonadotropic amenorrhea) — estrogen class relevance, not Estriol-specific; abstract available. |
| [4102186](https://pubmed.ncbi.nlm.nih.gov/4102186/) | 1971 | Case report | Lancet | Endocrinological findings in two patients with premature ovarian failure; no abstract available, historical case report. |
| [14194444](https://pubmed.ncbi.nlm.nih.gov/14194444/) | 1964 | Historical/trial report | J Obstet Gynaecol Br Commonw | Early gonadotrophin trial in idiopathic secondary amenorrhoea; no abstract, predates modern estrogen-specific therapy data. |
| [13931724](https://pubmed.ncbi.nlm.nih.gov/13931724/) | 1963 | Mechanism study | J Clin Endocrinol Metab | Mechanism of action of anti-ovulatory compounds; general mechanistic background, no abstract available. |

The remaining retrieved records (e.g. PMID 7026111, 4254759, 2949864, 5935707, 979592, 1239569, 4307531) are older publications with no abstract text and appear to be keyword-level matches (general amenorrhea, hormone assay methodology, or unrelated topics such as hormonal contraception and anorexia nervosa) rather than direct evidence for Estriol in amenorrhea; they have been excluded from the table above as low relevance.

---

## UK Market Information

No MHRA marketing authorisations are recorded for Estriol in this evidence pack (`total_licenses: 0`, market status: not marketed). Confirmation of UK availability, licensed brand names, and BNF classification should be sought directly from the MHRA product database before further evaluation.

---

## Safety Considerations

Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Note: TFDA label warnings/contraindications for Estriol are flagged as a **Blocking** data gap (DG001) in this pack — this must be resolved before any safety evaluation (S1 stage) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The candidate has no UK marketing authorisation on record, no documented original indication or mechanism of action, and a blocking safety data gap (DG001).
- The apparent Phase 3 clinical trial support is for a different molecule (Estetrol, not Estriol) and cannot currently be relied upon; the only directly relevant evidence is a single older observational study.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/MHRA product labelling (warnings, contraindications) before any safety review.
- Resolve DG002: confirm mechanism of action and original licensed indication via DrugBank/SmPC.
- Verify whether the Estetrol trials (NCT04090957, NCT04209543) have any legitimate bearing on Estriol (e.g. shared metabolite, class effect), or exclude them from the evidence base entirely.
- Seek Estriol-specific clinical trial data for amenorrhea/functional hypothalamic amenorrhea, if any exist, to substantiate the TxGNN prediction beyond the single 2012 observational study.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

