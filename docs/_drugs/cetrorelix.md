---
layout: default
title: Cetrorelix
parent: Model Prediction Only (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cetrorelix: predicted new indication hypertrichosis (disease) (evidence level L5). Approved use: Inhibition of premature LH surges in women undergoing controlled ovar…"
monitor_inn: "Cetrorelix"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "persistent fetal circulation syndrome", "familial isolated trichomegaly", "familial male-limited precocious puberty", "aromatase excess syndrome", "centra precocious puberty 1"]
---

# Cetrorelix
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

## Cetrorelix: From Controlled Ovarian Stimulation (Fertility Treatment) to hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Cetrorelix is a GnRH receptor antagonist used to inhibit premature LH surges in women undergoing controlled ovarian stimulation as part of fertility treatment.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **no clinical trials** and **no publications** in the data compiled for this report, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inhibition of premature LH surges in women undergoing controlled ovarian stimulation (the UK licence record contains no indication text; this is taken from the pharmacology data) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| UK Market Status | Marketed (valid licences: 1 of 1) |
| Number of Marketing Authorisations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cetrorelix is a peptide antagonist of the GnRH receptor (GnRH1 receptor, encoded by *GNRHR*). By blocking this receptor it suppresses LH and FSH release and, downstream, sex steroid production. Detailed mechanism of action data are not otherwise available in the data compiled for this report.

The link to the predicted indication is weak. Hypertrichosis is not a classic androgen-driven condition (unlike hirsutism), so suppressing sex steroids has no clear reason to help. The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. There is no supporting clinical or literature data, so it should be read as a hypothesis-generating signal rather than evidence of benefit.

**Other predictions reviewed.** The model produced ten predictions in total. Most are even less plausible, including Ambras syndrome, malformation syndromes, Dandy-Walker malformation, hair shaft abnormalities, persistent fetal circulation syndrome, familial trichomegaly and aromatase excess syndrome. These are genetic, structural or developmental conditions, or involve non-gonadal pathways, and no mechanism for GnRH antagonism has been identified. Two predictions are flagged as research questions because they involve the hypothalamic-pituitary-gonadal axis:

- **Central precocious puberty:** GnRH receptor blockade is mechanistically well aligned, and this is the strongest candidate. However, the standard of care is GnRH agonists, and no trial or literature data were available for cetrorelix in this population. Its short-acting dosing and the lack of a depot formulation limit practicality.
- **Familial male-limited precocious puberty:** This is caused by activating *LHCGR* mutations, which drive testosterone secretion independently of gonadotropins. A GnRH antagonist acts upstream and would not block this, so efficacy is doubtful, apart from a theoretical role in secondary central puberty activation.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0607020D0AAAAAA | Cetrorelix injection 250 micrograms vial with diluent | Not recorded | Not recorded |

The identifier above is the BNF-style product code from the data compiled for this report, not a PL number. The record has no dosage form or indication text, so the licensed indication should be confirmed against the current SmPC.

---

## Safety Considerations

- **Drug Interactions:** The interaction search completed, but returned only a pharmacology record (target: GnRH1 receptor), not a drug-drug interaction. No clinically graded interactions were identified.

Warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC and BNF for safety information. Report suspected adverse reactions via the Yellow Card Scheme.

Use in neonates (relevant to the persistent fetal circulation prediction) would raise additional safety concerns, and there are no data to support it.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has a high model score but no trials, no literature and only a speculative mechanistic link, so the evidence level is L5. Safety data are also incomplete.

**To proceed, the following is needed:**
- Mechanism of action data confirmed from a primary source (e.g. DrugBank)
- Warnings and contraindications from the current SmPC and BNF
- The full UK licence details (PL number, dosage form, indication text)
- A systematic literature and trial search for hypertrichosis, and separately for central precocious puberty, which is the most plausible of the ten predictions and could be reviewed as a research question
- Comparison with existing standard-of-care options in any indication that is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

