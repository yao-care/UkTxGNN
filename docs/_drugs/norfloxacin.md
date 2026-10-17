---
layout: default
title: Norfloxacin
parent: Model Prediction Only (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Norfloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Urinary tract infection, typhoid fever, salmonellosis, bronchitis…"
monitor_inn: "Norfloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Norfloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Norfloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Norfloxacin is a fluoroquinolone antibacterial, originally used for infections such as urinary tract infection, typhoid fever, bronchitis and dysentery.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but there are **no clinical trials** and **no publications** supporting this prediction. It is a graph-based prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, typhoid fever, salmonellosis, bronchitis, dysentery and other bacterial infections (the UK authorisation record has no indication text) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| UK Market Status | Marketed |
| Number of Marketing Authorisations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Norfloxacin is a fluoroquinolone antibacterial. Fluoroquinolones act by inhibiting bacterial DNA gyrase and topoisomerase IV, and its efficacy in bacterial infections is established.

This mechanism has no recognised link to hyperamylasemia. Norfloxacin has no known action on amylase regulation or pancreatic enzyme clearance. The high TxGNN score reflects graph-based inference only, and it should not be read as evidence of benefit.

**Other predictions reviewed.** Of the ten highest-ranked predictions, most also had no supporting evidence (for example polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, diffuse scleroderma). Two are worth noting as research questions:

- **Septicemic plague**: biologically plausible, since *Yersinia pestis* is a Gram-negative bacterium within the fluoroquinolone spectrum and other fluoroquinolones are used for plague. However, the retrieved papers are preclinical, and norfloxacin's limited systemic exposure makes it a poor choice for septicaemia.
- **Punctate epithelial keratoconjunctivitis**: the retrieved case series concern microsporidial keratoconjunctivitis, which often resolves with swabbing or spontaneously. Any drug effect is therefore confounded, and a role may be limited to preventing bacterial superinfection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for hyperamylasemia.

---

## UK Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 0501120Q0AAAAAA | Norfloxacin Tab 400mg | Tablet (400 mg) | Not stated in the compiled record |

Only one valid single-ingredient authorisation is recorded. The identifier shown is not in the usual MHRA "PL" format, so please verify it against the MHRA register. Please refer to the BNF (antibacterial drugs, quinolones) and current SmPC for licensed indications.

---

## Safety Considerations

**Contraindications and conditions of concern** (from the knowledge graph, not from label text; verify against the SmPC):

- Cardiac: long QT syndrome (including familial), torsades de pointes
- Neurological and psychiatric: epilepsy, peripheral neuropathy and other peripheral nervous system disease, anxiety disorder, psychotic and schizoaffective disorders
- Hepatic and renal: liver failure, liver disease, cirrhosis, gallbladder disease, kidney disease
- Musculoskeletal: tendinitis, periarthritis, rhabdomyolysis
- Metabolic: diabetes mellitus, diabetic ketoacidosis, potassium deficiency
- Haematological: thrombocytopenia, anaemia

**Drug interactions** (100 recorded; the main examples are below):

- **Major**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone; the combination raises tendon-injury risk), bupropion, chlorpropamide
- **Moderate**: antidiabetic drugs (metformin, pioglitazone, acarbose, alogliptin, albiglutide, canagliflozin; the risk is altered blood glucose), famotidine, loperamide, aspirin, balsalazide, bisacodyl, calcium and potassium salts

Please refer to the SmPC and BNF for full warnings. Report suspected adverse reactions via the Yellow Card Scheme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hyperamylasemia prediction has no mechanistic rationale, no trials and no literature (L5). Norfloxacin also carries a substantial safety burden, so there is no basis to proceed.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis for hyperamylasemia, with supporting preclinical data
- Mechanism of action data for norfloxacin
- Verified UK licensing details (MHRA PL number, dosage form and approved indications)
- Label warnings and contraindications from the SmPC and BNF
- If a repurposing direction is wanted, prioritise the research-question candidates (septicemic plague, punctate epithelial keratoconjunctivitis), noting that a better-absorbed fluoroquinolone may suit plague
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

