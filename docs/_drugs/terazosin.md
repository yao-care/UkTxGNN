---
layout: default
title: Terazosin
parent: Model Prediction Only (L5)
nav_order: 606
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Terazosin: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Hypertension"
monitor_inn: "Terazosin"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine disorder", "migraine with brainstem aura", "Raynaud disease", "Ambras type hypertrichosis universalis congenita", "manic bipolar affective disorder", "kyphoscoliotic heart disease"]
---

# Terazosin
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

# Terazosin: From Hypertension and Benign Prostatic Hyperplasia to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Terazosin is an alpha-1 adrenergic blocker, originally used to treat hypertension and benign prostatic hyperplasia.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but there are **no clinical trials and no publications** supporting this top-ranked prediction. It is a graph-based prediction only.
Among the other predicted indications, **Raynaud disease** and **migraine** have the most (though still limited and dated) supporting literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension; benign prostatic hyperplasia (from the knowledge graph, as no approved indication text is available for the UK authorisation) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, terazosin is a selective alpha-1 adrenergic antagonist. Its efficacy in hypertension and benign prostatic hyperplasia is established, and it acts by relaxing vascular and prostatic smooth muscle.

For the top-ranked prediction, the only plausible link is that alpha-1 blockade causes vasodilation, which may change scalp microcirculation around hair follicles. However, hypotrichosis simplex is a genetic disorder of hair follicle development, so a vascular mechanism is unlikely to be disease-modifying. The high score is therefore best read as a graph-proximity signal rather than a mechanistic one.

The other hair-related predictions (congenital hypotrichosis milia, diffuse alopecia areata, Ambras-type hypertrichosis) have the same weakness: they are genetic or autoimmune conditions with no established link to alpha-1 antagonism. Predictions with a more credible rationale are Raynaud disease (excess alpha-adrenergic vasoconstriction in digital vessels) and migraine (vascular tone and sympathetic activity). These are summarised below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, or for any of the other nine predicted indications.

---

## Literature Evidence

There is no literature for the top-ranked prediction (hypotrichosis simplex of the scalp). The publications below relate to lower-ranked predictions and are shown for context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9273472](https://pubmed.ncbi.nlm.nih.gov/9273472/) | 1997 | Clinical study (design unverified) | Minerva Cardioangiol | Raynaud disease: terazosin reduced the number, intensity and duration of vasospastic attacks in idiopathic and secondary Raynaud's phenomenon, with improved thermographic and ultrasonographic findings |
| [7911406](https://pubmed.ncbi.nlm.nih.gov/7911406/) | 1994 | Clinical study (design unverified) | Clin Ter | Migraine: open trial in 46 patients with migraine without aura, comparing terazosin, buflomedil and both for prophylaxis |
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Review | Headache | Migraine: 10 patients given terazosin or doxazosin; most had fewer or milder migraines, but 5 stopped because of side effects |
| [34779371](https://pubmed.ncbi.nlm.nih.gov/34779371/) | 2022 | Review | Curr Cardiol Rev | Alopecia: general review of extracardiac effects of cardiovascular drugs; indirect only, and terazosin has no demonstrated hair-growth effect |

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0205040V0AAABAB | Terazosin HCl Tab 2mg | Not stated | Not stated |

One single-ingredient authorisation is recorded as valid. Indication text and dosage form are not available in the data compiled for this report.

---

## Safety Considerations

- **Contraindications and risk conditions (from the knowledge graph, not label text):** multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, priapism, and intraoperative floppy iris syndrome.
- **Drug Interactions:** 100 interactions were identified. The main moderate-level ones include:
  - corticosteroids (hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - opioids (morphine, liposomal morphine, opium)
  - cannabinoids (dronabinol, nabilone)
  - bupropion

  Several others (calcitriol, pantoprazole, glimepiride) are of unknown severity.
- For Raynaud disease in particular, hypotension and orthostasis remain concerns.

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is supported only by a graph-based score, with no trials or publications and a weak mechanistic rationale for a genetic hair-follicle disorder. The hair-related predictions as a group lack plausibility. The more credible directions are Raynaud disease and migraine, but their evidence is small, dated and of unverified design, so they are better treated as research questions.

**To proceed, the following is needed:**
- Mechanism of action data and UK label warnings and contraindications (currently missing, and they block formal safety screening)
- Approved indication text and dosage form for the UK authorisation
- For Raynaud disease or migraine: appraisal of the original studies' design and size, followed by a controlled trial with blood pressure and orthostasis monitoring
- For hair disorders: preclinical or mechanistic evidence before any clinical work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

