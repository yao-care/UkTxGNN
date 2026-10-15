---
layout: default
title: Flavoxate
parent: Model Prediction Only (L5)
nav_order: 290
evidence_level: L5
indication_count: 8
---

# Flavoxate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Flavoxate: From Urinary Tract Smooth Muscle Spasm to Attention Deficit Hyperactivity Disorder (Inattentive Type)

## One-Sentence Summary

Flavoxate is a urinary tract smooth muscle relaxant with antimuscarinic, phosphodiesterase-inhibiting and calcium-antagonist properties, marketed in the UK as a 200 mg tablet.
The TxGNN model predicts it may be effective for **attention deficit hyperactivity disorder, inattentive type**, but there are currently **no clinical trials** and **no publications** supporting this prediction. It rests on a graph-based model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data (flavoxate is generally used for urinary urgency, frequency and related bladder symptoms) |
| Predicted New Indication | Attention deficit hyperactivity disorder, inattentive type |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Based on known pharmacology, flavoxate relaxes urinary tract smooth muscle through antimuscarinic, phosphodiesterase-inhibiting and calcium-antagonist actions.

These properties have no established link to ADHD, which is characterised mainly by dopaminergic and noradrenergic dysregulation. The high TxGNN score is therefore best read as a graph-proximity signal rather than a pharmacologically grounded hypothesis. The model also ranks closely related entries highly, including "attention deficit-hyperactivity disorder" and "specific developmental disorder". These likely reflect the same underlying signal counted more than once, so they should not be treated as independent support.

Among the other predictions, **irritable bowel syndrome** (score 99.74%) has the most plausible rationale. Antimuscarinic and smooth muscle relaxant activity is conceptually similar to antispasmodics such as hyoscine and dicyclomine. This link is still unverified, as no trials or literature were available. Predictions for neurogenic bladder largely overlap with the drug's existing symptomatic urological use. Those for gastroduodenitis, peptic ulcer disease and cauda equina syndrome have weak or indirect rationales.

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0704020G0AAACAC | Flavoxate HCl tablets 200 mg | Tablet | Not stated in the data compiled |

The identifier shown is a drug classification code rather than a standard PL number. Indication text and dosage form were not available in the compiled data. Please check the current SmPC, the BNF and NICE guidance for the authorised indications.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from model relationships, not label text, and must be confirmed against the SmPC): angle-closure glaucoma, pyloric stenosis, paralytic ileus, intestinal obstruction, familial visceral myopathy, active peptic ulcer disease and urinary tract obstruction.
- **Drug Interactions**: 74 potential interactions were identified. The most notable are the two classed as **Major**:
  - Potassium citrate
  - Potassium chloride

  Many others are classed as **Moderate**, mostly additive anticholinergic or gut-motility effects, including:
  - Antimuscarinics: hyoscyamine, atropine, glycopyrronium, scopolamine, dicyclomine, propantheline, trospium
  - Opioids and antidiarrhoeals: morphine, loperamide, eluxadoline
  - Prokinetics and others: metoclopramide, prucalopride, pramlintide
  - Cannabinoids: dronabinol, nabilone

Please refer to the SmPC and BNF for full safety information. Report suspected adverse reactions via the Yellow Card Scheme.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no registered trials or publications and no plausible mechanistic link to ADHD. All predicted indications are at evidence level L5.

**To proceed, the following is needed:**
- Mechanism of action data for flavoxate, to allow proper mechanistic analysis
- SmPC-based indication, warning and contraindication data for the UK authorisation
- A literature and trial search specific to flavoxate in the predicted conditions
- If any indication is pursued, irritable bowel syndrome is the more biologically plausible candidate. Neurogenic bladder should first be mapped to current terminology (e.g. neurogenic detrusor overactivity) and treated as an extension of existing use
- A review of anticholinergic burden and the contraindications listed above before any new population is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

